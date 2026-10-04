# Codex and Claude Code

Use the same workflow and records in either host. Keep the main conversation as
the implementer. Consult this reference when installation, invocation, a model
change or reviewer tools differ from the host you normally use.

| Host | Explicit invocation | Personal skill | Project skill |
|---|---|---|---|
| Codex | `$delta-rocket` | `$CODEX_HOME/skills/delta-rocket` (default `~/.codex`) | `.agents/skills/delta-rocket` |
| Claude Code | `/delta-rocket` | `$CLAUDE_CONFIG_DIR/skills/delta-rocket` (default `~/.claude`) | `.claude/skills/delta-rocket` |

Resolve relative references against the loaded skill directory. The same complete
package is installed in both hosts; OpenAI UI metadata is optional and is not a
Claude Code dependency. Do not set a skill-level `model`, `context: fork`, or
permissions override merely to make the workflow portable.

## Implementation checkpoint

After plan and specification reviews and corrections, pause and show those
artifacts. Remind the user that they can change the implementation model now,
then ask whether to implement the whole plan. Use the user's language and models
actually available in that host; keep the current model unless they change it.

In Codex the user can use its model selector (for example, their chosen Astra to
Luna workflow). In Claude Code they can use `/model` to choose an available Claude
model. Do not offer Astra or Luna as native Claude model names. A model switch
alone is not approval. Keep approval, state and review counters on resume.

## Reviews and permissions

Use the host's available delegation tools for the bounded read-only reviews.
Claude Code exposes Agent (Task in older versions); request a general-purpose
reviewer with the required artifacts, no edits or further delegation. Preserve
the user's model settings and inspect the actual model if the host reports it;
do not silently choose a different reviewer model. If delegation is unavailable
or forbidden, use the disclosed inline assessment defined by review policy.
Permission prompts and host plan modes still apply; workflow approval does not
grant tool permissions or automatically exit a read-only host mode.

## Automatic routing

From the repository, `python scripts/install-codex.py` installs Codex user hooks.
`python scripts/install-claude-code.py` installs Claude Code personal hooks.
Both use SessionStart and UserPromptSubmit, never SubagentStart or Stop. They add
context and do not technically block implementation or enforce completion.
SessionStart reloads the entrypoint on startup, resume, clear and compaction;
UserPromptSubmit adds a small reminder. Explicit workflow choices take priority.

Codex requires enabled, trusted user hooks. In Claude Code inspect `/hooks` after
restarting. Disabled or managed-only hook policies can prevent user hooks from
running; do not bypass those policies. Review other workflow hooks if their
instructions compete. Installing DeltaRocket preserves other skills and plugins.
