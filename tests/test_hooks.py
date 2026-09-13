"""Run with: python -m unittest discover -s tests -v"""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parent.parent


class HooksTest(unittest.TestCase):
    def test_install_preserves_other_hooks_and_is_repeatable(self):
        with tempfile.TemporaryDirectory(prefix="DeltaRocket test ") as directory:
            home = Path(directory)
            env = {**os.environ, "CODEX_HOME": directory}
            other = {"hooks": [{"type": "command", "command": "echo unrelated"}]}
            original = {"description": "Keep me", "hooks": {"SessionStart": [other]}}
            config_path = home / "hooks.json"
            config_path.write_text(json.dumps(original), encoding="utf-8")
            for _ in range(2):
                subprocess.run([sys.executable, str(ROOT / "scripts/install-codex.py")],
                               env=env, check=True, capture_output=True)
            config = json.loads(config_path.read_text(encoding="utf-8"))
            self.assertEqual(config["description"], "Keep me")
            self.assertEqual(config["hooks"]["SessionStart"][0], other)
            self.assertEqual(len(config["hooks"]["SessionStart"]), 2)
            self.assertEqual(len(config["hooks"]["UserPromptSubmit"]), 1)
            self.assertNotIn("SubagentStart", config["hooks"])
            self.assertTrue(list((home / "backups").glob("*/hooks.json")))
            self.assertFalse((home / "config.toml").exists())
            skill = home / "skills/delta-rocket/SKILL.md"
            self.assertEqual(skill.read_bytes(),
                             (ROOT / ".agents/skills/delta-rocket/SKILL.md").read_bytes())

            script = home / "hooks/delta-rocket.py"
            for event in ("SessionStart", "UserPromptSubmit"):
                result = subprocess.run([sys.executable, str(script)], env=env, cwd=home,
                                        input=json.dumps({"hook_event_name": event,
                                                          "prompt": "UNTRUSTED_SENTINEL"}),
                                        text=True, capture_output=True, check=True)
                payload = json.loads(result.stdout)["hookSpecificOutput"]
                self.assertEqual(payload["hookEventName"], event)
                self.assertNotIn("UNTRUSTED_SENTINEL", payload["additionalContext"])
                self.assertEqual(skill.read_text(encoding="utf-8-sig") in
                                 payload["additionalContext"], event == "SessionStart")
                self.assertEqual(result.stderr, "")

    def test_unsupported_and_malformed_inputs_are_noops(self):
        for data in ('{"hook_event_name":"SubagentStart"}', "[]", "null", "invalid"):
            with self.subTest(data=data):
                result = subprocess.run([sys.executable, str(ROOT / "hooks/delta-rocket.py")],
                                        input=data, text=True, capture_output=True, check=True)
                self.assertEqual(json.loads(result.stdout), {})
                self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
