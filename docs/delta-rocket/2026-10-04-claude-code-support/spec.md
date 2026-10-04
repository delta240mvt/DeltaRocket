# Claude Code support — specification

## Accepted behavior
DeltaRocket runs as the same portable skill in Codex and Claude Code. Codex
invocation is $delta-rocket; Claude Code invocation is /delta-rocket. No automatic
model override or expanded permissions. Preserve quick/full routing, exactly one
review per module, two final rounds and the existing final-2 recovery rule, dated
scope documents and one project history. The usual implementation checkpoint
still requires user confirmation, with model choices appropriate to the host.
For this scope only the user explicitly requested autonomous implementation and
authorized commit/push main and local deployment.

## M1 — Host adaptation
Add references/hosts.md with host locations, invocation, user-driven model changes
(Claude /model; Codex model selector) and use of actual available reviewer tools.
The hook keeps Codex default behavior and supports --host claude-code explicitly.
Select CODEX_HOME/~/.codex or CLAUDE_CONFIG_DIR/~/.claude independently. A hook
installed in one host must not load another host's personal skill. Source-repo
execution may use the canonical repository skill when no host installation is
present. Installed missing-skill events produce a visible diagnostic, not wrong
host fallback. SessionStart sends the current entrypoint plus host guidance;
UserPromptSubmit only sends the brief routing reminder. Reject unsupported events,
malformed/non-object input and subagent agent_id events without prompt execution,
network, file mutation, model selection or hidden reviewer restarts.

## M2 — Install, test and deploy
python scripts/install-claude-code.py installs an ordinary personal skill folder
and hook, honors CLAUDE_CONFIG_DIR, backs up settings.json before replacement,
merges only owned SessionStart/UserPromptSubmit handlers, and retains all unrelated
settings, groups, hooks and skill resources. Default commands use the installing
Python interpreter with Bash-safe absolute-path quoting, including paths with
spaces, apostrophes, dollar signs and Unicode. Windows supports Git Bash and an
explicit PowerShell shell option with its own quoting; macOS/Linux use shell form.
Use fields verified with installed Claude Code 2.1.132, without relying on new
exec-form args. Hooks emit the host's documented hookSpecificOutput JSON.
No duplicate hook after repeated installs; invalid settings fail before writes.
An existing disableAllHooks policy is preserved and reported as a blocker for
automatic activation. No overwriting model, permissions or enabledPlugins.

README uses simple English for both hosts, personal and project skill locations,
commands, model-switch checkpoint and automatic hooks, update instructions and
host/behavior-test limitations. No unmeasured performance claims or cloud-server
hosting implied. Canonical source remains .agents/skills/delta-rocket; project
Claude usage may copy it into .claude/skills/delta-rocket (no new required clone).
Local deployment installs both host copies and hooks; compare all task-owned files.

## Verification evidence
Run Python unit tests for Codex regression and Claude hook routing, installer
repetition, mixed hook groups, unrelated custom files, config shape failure,
disableAllHooks preservation and command quoting. Run configured commands using
actual Bash and PowerShell on Windows. Attempt a bounded installed-CLI smoke test
with no tools and isolated settings/cwd, retaining account/model selection and
without changing production app files. Record actual hook lifecycle plus any
authentication/service limitation separately from schema or model compliance.
Validate skills, local Markdown links and git diff. Independent reviewers assess
M1, M2 and both final rounds within existing budgets. Final completion records
verification and links; then authorized commit, push and local install.
