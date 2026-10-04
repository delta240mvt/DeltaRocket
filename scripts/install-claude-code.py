"""Install DeltaRocket for Claude Code, preserving other settings and resources."""

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import shlex
import shutil
import sys
import tempfile


def command_for(script, shell):
    paths = (Path(sys.executable).as_posix(), script.as_posix())
    if shell == "powershell":
        quoted = ["'" + path.replace("'", "''") + "'" for path in paths]
        return "& " + " ".join(quoted) + " --host claude-code"
    return " ".join(shlex.quote(path) for path in paths) + " --host claude-code"


def validate(config):
    if not isinstance(config, dict) or not isinstance(config.get("hooks", {}), dict):
        raise ValueError("settings.json and its hooks field must be JSON objects")
    if config.get("disableAllHooks") is True:
        raise ValueError("disableAllHooks is enabled; review that policy before installing automatic hooks")
    for event in ("SessionStart", "UserPromptSubmit"):
        groups = config.get("hooks", {}).get(event, [])
        if not isinstance(groups, list):
            raise ValueError(f"{event} must contain a list of hook groups")
        for group in groups:
            if not isinstance(group, dict) or not isinstance(group.get("hooks"), list):
                raise ValueError(f"{event} has an invalid hook group")
            if any(not isinstance(h, dict) or not isinstance(h.get("command", ""), str)
                   for h in group["hooks"]):
                raise ValueError(f"{event} has an invalid handler")


def install(shell):
    root = Path(__file__).resolve().parent.parent
    home = Path(os.environ.get("CLAUDE_CONFIG_DIR") or Path.home() / ".claude").resolve()
    target = home / "settings.json"
    original = target.read_bytes() if target.exists() else None
    config = json.loads(original.decode("utf-8-sig")) if original is not None else {}
    validate(config)  # Validate before creating or changing installed files.
    script = home / "hooks/delta-rocket.py"
    script_path = script.as_posix()
    spellings = (shlex.quote(script_path), "'" + script_path.replace("'", "''") + "'",
                 '"' + script_path + '"')
    events = config.setdefault("hooks", {})
    for event in ("SessionStart", "UserPromptSubmit"):
        kept = []
        for group in events.get(event, []):
            handlers = []
            for handler in group["hooks"]:
                previous = handler.get("command", "").replace("\\", "/")
                owned = "--host claude-code" in previous and any(s in previous for s in spellings)
                if not owned:
                    handlers.append(handler)
            if handlers or not group["hooks"]:
                kept.append({**group, "hooks": handlers})
        group = {"hooks": [{"type": "command", "command": command_for(script, shell),
                            "shell": shell, "timeout": 5,
                            "statusMessage": "DeltaRocket routing"}]}
        if event == "SessionStart":
            group["matcher"] = "startup|resume|clear|compact|fork"
        events[event] = kept + [group]

    # Preserve concurrent user edits instead of overwriting a newer configuration.
    current = target.read_bytes() if target.exists() else None
    if current != original:
        raise ValueError("settings.json changed during preparation; retry installation")
    if original is not None:
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        backup = home / "backups" / f"deltarocket-{stamp}"
        backup.mkdir(parents=True)
        (backup / "settings.json").write_bytes(original)
    shutil.copytree(root / ".agents/skills/delta-rocket", home / "skills/delta-rocket",
                    dirs_exist_ok=True)
    script.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(root / "hooks/delta-rocket.py", script)
    # Atomic replacement in the same directory; keep existing config permissions.
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=home,
                                     prefix="deltarocket-", suffix=".tmp", delete=False) as tmp:
        temporary = Path(tmp.name)
        json.dump(config, tmp, indent=2, ensure_ascii=True)
        tmp.write("\n")
    try:
        if target.exists():
            shutil.copymode(target, temporary)
        current = target.read_bytes() if target.exists() else None
        if current != original:
            raise ValueError("settings.json changed during installation; configuration was not replaced")
        temporary.replace(target)
    finally:
        temporary.unlink(missing_ok=True)
    print(f"Installed DeltaRocket skill and hooks in {home}")
    print("Restart Claude Code and inspect /hooks. Invoke the skill with /delta-rocket.")


if __name__ == "__main__":
    # Redirected Windows streams may use a legacy encoding that loses path names.
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--shell", choices=("bash", "powershell"), default="bash",
                        help="Hook shell (Windows default requires Git Bash; PowerShell is optional)")
    args = parser.parse_args()
    try:
        install(args.shell)
    except (ValueError, OSError) as error:
        parser.exit(1, f"DeltaRocket installation failed: {error}\n")
