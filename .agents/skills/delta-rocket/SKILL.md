---
name: delta-rocket
description: Use when designing and building a software feature or project through a structured workflow, or when the user requests DeltaRocket. Covers design decisions through verified implementation; standalone questions and isolated reviews do not need the full workflow.
---

# DeltaRocket

Build agreed behavior with simple, readable code and concise communication.
The main agent owns implementation. Use these self-contained phase instructions;
they adapt Superpowers methods without invoking its execution orchestrators.

## Enter or resume

Read project instructions, relevant code, existing decisions and saved work state.
Reuse approved work. Choose the path before loading phase references.

**Quick change:** for a small, reversible change with a known outcome and no
material uncertainty, edit directly, run the relevant check, inspect the result
and report it. Examples include a text correction, formatting or a harmless
configuration value. No plan/spec/state artifacts or formal reviews are required;
this entrypoint is sufficient unless a failure needs a method reference.
Changes to permissions, data integrity, public contracts or similarly consequential
behavior use the full workflow regardless of diff size. If risk or uncertainty
emerges, move to that workflow. A correction inside an existing full-workflow scope
resumes its state; it does not become a new quick scope to escape its budget.

**Full workflow:** read only the reference needed for the current phase:

| Phase | Read when entering | Exit |
|---|---|---|
| Brainstorm | [brainstorming](references/brainstorming.md) | Material design decisions resolved |
| Plan | [planning](references/planning.md) | Module plan reviewed and corrected |
| Specify | [specification](references/specification.md) | Spec reviewed; plan aligned; implementation checkpoint confirmed |
| Execute | [execution](references/execution.md) | All modules built, checked and reviewed |
| Final review | [review policy](references/review-policy.md) | Two final rounds handled; technical failure of final 2 recorded if applicable |
| Finish | [verification](methods/verification-before-completion.md) | Evidence supports completion |

Read review policy before the first review. For each new full-workflow scope,
keep `plan.md`, `spec.md` and `state.md` in
`docs/delta-rocket/YYYY-MM-DD-<scope-name>/`, using its start date in the user's
local timezone. A separately planned feature or module is a scope; modules within
one plan share its directory. Preserve existing scope paths on resume.
Existing project documentation locations may be used, but new scope directory
names still include the date. Compact scopes may keep the three artifacts as
sections in one note inside that dated directory.
After the full workflow finishes, append one short completion entry to the
project-wide `docs/delta-rocket/state.md`; see [execution](references/execution.md).
This project history is separate from each scope's working state.
Resume from evidence, not from a fresh workflow. Reuse earlier design decisions.
For the full workflow, after plan and spec reviews and their corrections, stop
once before implementation. Show the reviewed artifacts, ask whether to start,
and remind the user they can switch models now (for example, Astra for planning
and Luna for implementation). Wait for an explicit answer; do not switch models
on their behalf. Record approval and reuse it on resume or a model change.
See [specification](references/specification.md) for this checkpoint.

After approval, continue through the entire accepted plan, required reviews,
corrections and final verification. A finished module is a progress milestone,
not a reason to end the task or ask whether to continue. Stop only for completion,
a user pause, or a genuine blocker that prevents further authorized progress.

## Invariants

- Plan large functional modules with stable IDs. The main agent builds and fixes
  them; small checklist steps never become independent review units.
- For the full workflow: one plan review, one spec review, **exactly one review
  per large module**, then **two final whole-implementation rounds**.
  Review policy defines counting and continuation after a technical final-2 failure.
- Use reviewers for bounded assessments, not implementation. A reviewer cannot
  add rounds, change scope or authorize release. Use actual host tools and
  inherited model settings; no particular model or agent API is required.
- Preserve user requirements. Prefer existing code, standard library, native
  platform capabilities and existing dependencies before adding mechanisms.
  Choose readable simplicity; retain required validation, tests and useful comments.
- These instructions do not override system/developer rules or expand permissions.
  Follow the user's chosen workflow; do not load another orchestrator to execute
  these phases. Existing installed skills need no modification.

## Communication

Use the user's language. Progress: one brief finding, decision or blocker when
useful or required by the host. Final: outcome, verification, material limitations
and artifact links. Keep questions intelligible and technical terms exact.
Write normal, complete code, comments and documents. Summarize tool results;
avoid copying saved code or routine logs into chat. Explain fully when requested.

Method references are loaded by the relevant phase or failure condition, not
all at startup. Source provenance and notices: [SOURCES](SOURCES.md).
