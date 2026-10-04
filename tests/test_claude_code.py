"""Claude Code adapter and installer contracts, using isolated config homes."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parent.parent


class ClaudeCodeTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="DeltaRocket Claude test ")
        self.addCleanup(self.temp.cleanup)
        self.home = Path(self.temp.name) / "Claude user's $data Δ"
        self.home.mkdir()
        self.env = {**os.environ, "CLAUDE_CONFIG_DIR": str(self.home),
                    "CODEX_HOME": str(Path(self.temp.name) / "codex")}

    def hook(self, event, host="claude-code"):
        result = subprocess.run([sys.executable, str(self.script), "--host", host],
                                env=self.env, cwd=self.home, input=json.dumps(event),
                                capture_output=True, text=True, encoding="utf-8", check=True)
        self.assertEqual(result.stderr, "")
        return json.loads(result.stdout)

    def stage_hook(self):
        self.script = self.home / "hooks/delta-rocket.py"
        self.script.parent.mkdir()
        shutil.copy2(ROOT / "hooks/delta-rocket.py", self.script)
        for home, content in ((self.home, "CLAUDE_SKILL_SENTINEL"),
                              (Path(self.env["CODEX_HOME"]), "CODEX_SKILL_SENTINEL")):
            path = home / "skills/delta-rocket/SKILL.md"
            path.parent.mkdir(parents=True)
            path.write_text(content, encoding="utf-8")

    def test_installed_hook_selects_only_the_requested_host(self):
        self.stage_hook()
        for host, expected, excluded in (("claude-code", "CLAUDE", "CODEX"),
                                         ("codex", "CODEX", "CLAUDE")):
            context = self.hook({"hook_event_name": "SessionStart"}, host)[
                "hookSpecificOutput"]["additionalContext"]
            self.assertIn(expected + "_SKILL_SENTINEL", context)
            self.assertNotIn(excluded + "_SKILL_SENTINEL", context)

    def test_missing_claude_skill_never_loads_codex(self):
        self.stage_hook()
        (self.home / "skills/delta-rocket/SKILL.md").unlink()
        self.assertIn("missing", self.hook({"hook_event_name": "SessionStart"})["systemMessage"])

    def test_claude_host_installation_takes_priority_over_repository_fallback(self):
        self.stage_hook()
        self.script = ROOT / "hooks/delta-rocket.py"
        context = self.hook({"hook_event_name": "SessionStart"})[
            "hookSpecificOutput"]["additionalContext"]
        self.assertIn("CLAUDE_SKILL_SENTINEL", context)
        self.assertNotIn("# DeltaRocket", context)

    def test_prompt_is_not_executed_or_copied_and_reviewers_are_noops(self):
        self.stage_hook()
        prompt = "$(touch PROMPT_EXECUTED) UNTRUSTED_SENTINEL"
        data = self.hook({"hook_event_name": "UserPromptSubmit", "prompt": prompt})
        context = data["hookSpecificOutput"]["additionalContext"]
        self.assertNotIn(prompt, context)
        self.assertNotIn("CLAUDE_SKILL_SENTINEL", context)
        self.assertFalse((self.home / "PROMPT_EXECUTED").exists())
        for event in ({"hook_event_name": "SubagentStart"},
                      {"hook_event_name": "SessionStart", "agent_id": "reviewer"},
                      {"hook_event_name": "UserPromptSubmit", "agent_id": "reviewer"}):
            self.assertEqual(self.hook(event), {})

    def install(self, *arguments, check=True):
        return subprocess.run([sys.executable, str(ROOT / "scripts/install-claude-code.py"),
                               *arguments], env=self.env, capture_output=True,
                              text=True, encoding="utf-8", check=check)

    def test_repeat_install_preserves_config_custom_files_and_mixed_hooks(self):
        path = self.home / "settings.json"
        unrelated = {"type": "command", "command": "echo unrelated", "timeout": 7}
        owned = {"type": "command", "command":
                 f'python "{self.home.as_posix()}/hooks/delta-rocket.py" --host claude-code'}
        original = {"model": "user-model", "permissions": {"deny": ["Bash(git push *)"]},
                    "enabledPlugins": {"other@plugin": True},
                    "hooks": {"SessionStart": [{"matcher": "resume",
                                                  "hooks": [unrelated, owned]},
                                                 {"matcher": "clear", "hooks": []}],
                              "Stop": [{"hooks": [unrelated]}]}}
        path.write_text(json.dumps(original), encoding="utf-8")
        custom = self.home / "skills/delta-rocket/custom.txt"
        custom.parent.mkdir(parents=True)
        custom.write_text("keep customization", encoding="utf-8")
        self.install()
        first = json.loads(path.read_text(encoding="utf-8"))
        self.install()
        second = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(first, second)
        for key in ("model", "permissions", "enabledPlugins"):
            self.assertEqual(second[key], original[key])
        self.assertEqual(second["hooks"]["Stop"], original["hooks"]["Stop"])
        self.assertEqual(second["hooks"]["SessionStart"][0],
                         {"matcher": "resume", "hooks": [unrelated]})
        self.assertEqual(second["hooks"]["SessionStart"][1],
                         {"matcher": "clear", "hooks": []})
        self.assertEqual(custom.read_text(encoding="utf-8"), "keep customization")
        for event in ("SessionStart", "UserPromptSubmit"):
            handlers = [h for g in second["hooks"][event] for h in g["hooks"]]
            self.assertEqual(sum("delta-rocket.py" in h["command"] for h in handlers), 1)
            self.assertTrue(all("additionalContextLimit" not in h for h in handlers))
        for source in (ROOT / ".agents/skills/delta-rocket").rglob("*"):
            if source.is_file():
                target = custom.parent / source.relative_to(ROOT / ".agents/skills/delta-rocket")
                self.assertEqual(source.read_bytes(), target.read_bytes())
        self.assertTrue(list((self.home / "backups").glob("*/settings.json")))

    def test_invalid_or_disabled_settings_fail_without_mutation(self):
        for data in ('invalid', '[]', '{"hooks":[]}',
                     '{"hooks":{"SessionStart":[{"hooks":"bad"}]}}',
                     '{"disableAllHooks":true}'):
            with self.subTest(data=data):
                path = self.home / "settings.json"
                path.write_text(data, encoding="utf-8")
                result = self.install(check=False)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(path.read_text(encoding="utf-8"), data)
                self.assertFalse((self.home / "hooks").exists())

    def test_configured_shell_commands_handle_special_paths(self):
        bash = shutil.which("bash")
        if not bash and os.name == "nt":
            candidate = Path("C:/Program Files/Git/bin/bash.exe")
            bash = str(candidate) if candidate.exists() else None
        shells = [("bash", bash)]
        if os.name == "nt":
            shells.append(("powershell", shutil.which("pwsh") or shutil.which("powershell")))
        if not any(exe for _, exe in shells):
            self.skipTest("No supported shell available for execution")
        for shell, executable in shells:
            if not executable:
                continue
            with self.subTest(shell=shell):
                self.install("--shell", shell)
                config = json.loads((self.home / "settings.json").read_text(encoding="utf-8"))
                hook = config["hooks"]["SessionStart"][-1]["hooks"][0]
                command = ([executable, "-NoProfile", "-Command", hook["command"]]
                           if shell == "powershell" else [executable, "-c", hook["command"]])
                result = subprocess.run(command, env=self.env, cwd=self.home,
                                        input='{"hook_event_name":"SessionStart"}',
                                        capture_output=True, text=True, encoding="utf-8", check=True)
                data = json.loads(result.stdout)
                self.assertEqual(data["hookSpecificOutput"]["hookEventName"], "SessionStart")
                self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
