# Claude Code support — plan

Approved request: make DeltaRocket work in Codex and Claude Code, update README,
commit and push main, and deploy the skill locally. User explicitly requested
autonomous execution of this change, including implementation and delivery.

## M1 — Portable workflow and hook
Use one shared skill package. Add focused host guidance for invocation, model
selection and available reviewer tools. Keep existing workflow, review budgets,
dated records and implementation checkpoint. Make the existing Python hook
resolve the correct host installation without selecting the other host's skill.
Preserve the existing Codex command and output contract. Claude Code receives
SessionStart and UserPromptSubmit context only; reviewers do not restart the flow.
Validate host isolation, Unicode and space paths, malformed input, subagent no-ops,
checkpoint guidance and existing Codex behavior. No permission/model changes.

## M2 — Claude installer, documentation and deployment
Add a personal Claude Code installer for ~/.claude/skills/delta-rocket and its
hooks; honor CLAUDE_CONFIG_DIR, merge settings.json without altering other keys,
back up existing settings, and avoid duplicate entries on reinstall. Use Python
3 with shell quoting that works on the supported host; verify the real installed
Claude Code 2.1.132 hook lifecycle. Explain both hosts, installation, explicit
invocation, model checkpoint and limitations in simple English in README.
Test repeat install, unrelated settings/hooks preserved, invalid configuration,
actual shell command output and complete package resources. Deploy locally to
Codex and Claude Code after required reviews/checks, then commit/push main.

M2 depends on M1. Canonical source remains .agents/skills/delta-rocket; personal
Codex copy is updated file-by-file with unrelated differences preserved. Claude
uses an ordinary installed personal copy. No website/server deployment exists.
