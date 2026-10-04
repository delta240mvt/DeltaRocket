"""Supply DeltaRocket routing context; never execute the user's prompt."""

import argparse
import json
import os
from pathlib import Path
import sys


def hook_output(event, host="codex"):
    name = event.get("hook_event_name")
    if name not in ("SessionStart", "UserPromptSubmit") or event.get("agent_id"):
        return {}

    root = Path(__file__).resolve().parent.parent
    skill = root / ".agents/skills/delta-rocket/SKILL.md"
    variable, directory = ("CLAUDE_CONFIG_DIR", ".claude") if host == "claude-code" else ("CODEX_HOME", ".codex")
    host_home = Path(os.environ.get(variable) or Path.home() / directory)
    host_skill = host_home / "skills/delta-rocket/SKILL.md"
    if (host == "claude-code" and host_skill.is_file()) or not skill.is_file():
        skill = host_skill
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
        host_context = (
            "Host: Claude Code. Invoke /delta-rocket. At the implementation checkpoint, "
            "the user may choose an available model with /model, then explicitly approve "
            "implementation. Use the selected Claude model; Codex model names are not "
            "Claude model choices. "
            if host == "claude-code" else
            "Host: Codex. Invoke $delta-rocket. At the implementation checkpoint, "
            "the user may use the host model selector, then explicitly approve implementation. "
        )
        routing += (
            f"\n{host_context}\nInstalled skill: {skill.as_posix()}. Resolve its relative references "
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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", choices=("codex", "claude-code"), default="codex")
    args = parser.parse_args()
    try:
        event = json.load(sys.stdin)
        result = hook_output(event, args.host) if isinstance(event, dict) else {}
    except (ValueError, OSError):
        result = {}
    print(json.dumps(result, ensure_ascii=True))
