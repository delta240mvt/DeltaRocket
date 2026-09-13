"""Supply DeltaRocket routing context; never execute the user's prompt."""

import json
import os
from pathlib import Path
import sys


def hook_output(event):
    name = event.get("hook_event_name")
    if name not in ("SessionStart", "UserPromptSubmit"):
        return {}

    root = Path(__file__).resolve().parent.parent
    skill = root / ".agents/skills/delta-rocket/SKILL.md"
    if not skill.is_file():
        codex_home = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex")
        skill = codex_home / "skills/delta-rocket/SKILL.md"
    if not skill.is_file():
        return {"systemMessage": "DeltaRocket hook: installed SKILL.md is missing."}

    routing = (
        "DeltaRocket is the user's default software workflow. Before acting, "
        "classify the current request using its quick-change/full-workflow rules. "
        "For questions, standalone reviews and tasks outside software implementation, "
        "answer or perform that task directly without the implementation phases. "
        "Respect an explicit user choice of another workflow or an instruction to skip "
        "DeltaRocket. Resume an existing scope from its state and review counters. "
        "Do not start another orchestrator merely because its skill is installed. "
        "This routing does not override higher-priority rules or expand permissions. "
        "Classify internally; announce the chosen path only when useful. "
    )
    if name == "SessionStart":
        routing += (
            f"\nInstalled skill: {skill.as_posix()}. Resolve its relative references "
            "against this skill directory. The entrypoint follows; supporting files "
            "are loaded only for the selected phase.\n\n"
            + skill.read_text(encoding="utf-8-sig")
        )
    else:
        routing += (
            f"If the entrypoint is not already available in context, read "
            f"{skill.as_posix()} before software implementation."
        )
    return {"hookSpecificOutput": {"hookEventName": name, "additionalContext": routing}}


if __name__ == "__main__":
    try:
        event = json.load(sys.stdin)
        result = hook_output(event) if isinstance(event, dict) else {}
    except (ValueError, OSError):
        result = {}
    print(json.dumps(result, ensure_ascii=True))
