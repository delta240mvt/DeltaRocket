"""Install the DeltaRocket skill and user hooks without changing hook trust."""

import json
import os
from pathlib import Path
import shutil
from datetime import datetime, timezone


def install():
    root = Path(__file__).resolve().parent.parent
    home = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex").resolve()
    target = home / "hooks.json"
    config = json.loads(target.read_text(encoding="utf-8-sig")) if target.exists() else {}
    events = config.setdefault("hooks", {})
    script = home / "hooks/delta-rocket.py"
    # The documented installation requires Python 3 available as `python`.
    command = f'python "{script.as_posix()}"'

    for event in ("SessionStart", "UserPromptSubmit"):
        groups = events.setdefault(event, [])
        kept = []
        for group in groups:
            handlers = [handler for handler in group["hooks"]
                        if script.as_posix() not in handler.get("command", "").replace("\\", "/")]
            if handlers:
                kept.append({**group, "hooks": handlers})
        group = {"hooks": [{"type": "command", "command": command,
                            "timeout": 5, "additionalContextLimit": 2500}]}
        if event == "SessionStart":
            group["matcher"] = "startup|resume|clear|compact"
        # Preserve unrelated handlers and their configuration.
        events[event] = kept + [group]

    if target.exists():
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        backup = home / "backups" / f"deltarocket-{stamp}"
        backup.mkdir(parents=True)
        shutil.copy2(target, backup / "hooks.json")
    shutil.copytree(root / ".agents/skills/delta-rocket", home / "skills/delta-rocket",
                    dirs_exist_ok=True)
    script.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(root / "hooks/delta-rocket.py", script)
    temporary = target.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
    temporary.replace(target)
    print(f"Installed DeltaRocket skill and hooks in {home}")
    print("Restart Codex, then review and trust the two DeltaRocket hooks in /hooks.")


if __name__ == "__main__":
    install()
