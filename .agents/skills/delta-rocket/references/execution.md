# Main-agent execution

Read the approved contract, module plan, work state and [review policy](review-policy.md).
Recover review history before dispatching any reviewer. Keep the main agent as
the implementer and integrator; do not redirect to subagent-driven-development
or delegate each checklist step.

Before implementation, confirm that the specification phase's implementation
checkpoint has explicit approval for this scope. If it is pending, present that
checkpoint and wait. A model change preserves the approved plan, specification,
work state and review counters; it does not start a new workflow.

Once approved, keep working until every planned module, required review,
justified correction and final check is complete. Do not end a turn merely
because one module or batch is done, or offer to do the remaining plan later.
Send brief progress updates and proceed to the next action without routine
continuation questions. Stop for a user pause, a necessary new scope/permission
decision, or a genuine blocker only when no useful authorized work can continue.
Record any remaining work and precise blocker; do not report partial work as
full completion. Context compaction or a resumed session continues the same plan.

Before the first edit, record the scope's starting revision when available,
file inventory and relevant staged, unstaged and untracked state. Preserve
the relevant pre-existing dirty/untracked contents in a recoverable local
snapshot, without modifying user work or committing snapshot copies. Record
its location in the work state. An empty repository has an explicit empty
baseline, not an assumed HEAD. Retain this starting baseline for final review;
also record each module's boundary and affected starting state before editing it.

For each planned module:

1. Inspect the relevant existing flow. Build the smallest readable implementation
   that satisfies the contract. Use [TDD](../methods/test-driven-development.md)
   for behavior changes; keep checks proportional to the actual risk.
2. Run the module's checks and inspect their results. For a failure, use
   [systematic debugging](../methods/systematic-debugging.md), then resume this
   module. Debugging does not restart design or grant review rounds.
3. Once the whole module is ready, run its single combined contract/quality review.
   Process feedback using [receiving review](../methods/receiving-code-review.md).
   Fix justified findings as the main agent and verify the corrections.
4. Verify corrections directly; do not dispatch a second module assessment.
   Record the module's outcome, open findings and evidence. Continue to the next
   module when its acceptance criteria and required checks are met. Independent
   work may proceed while a genuine dependency remains blocked.

Keep interfaces aligned across modules as you build. Finish all modules, then
handle the two final whole-implementation rounds under review policy, including
its continuation rule if final 2 fails technically. After
the last corrections, use [verification](../methods/verification-before-completion.md).

## Durable work state

Update the scope-local `state.md` at phase/module boundaries and before each review dispatch.
Record scope ID and accepted decisions; implementation checkpoint status and
approval evidence; phase and next action; module statuses;
plan/spec/module/final review attempts and completed assessments separately;
reviewed revision or file snapshot;
review report references; finding dispositions; verification commands/results.
Reference artifacts instead of copying plans, code, logs or conversation history.
Link any project-wide issue entries created under review policy. On resume,
reuse those entries and handle relevant unresolved items without restarting
unrelated work from the project's backlog.

On resume, compare the state with the working tree and recorded reviews. Recover
missing information from evidence. A missing or compacted history is not zero
reviews; if the remaining budget cannot be established, do not start a new
review until it is resolved. Continue useful implementation or diagnosis.

## Project completion history

Keep one chronological project history at `docs/delta-rocket/state.md`, separate
from `<dated-scope>/state.md`. The local file tracks active work; the shared file
briefly records delivered outcomes across all scopes. If an existing shared
`state.md` has other content, preserve it and use a dedicated completion-history
section. Follow an explicitly established alternative documentation root
consistently; do not create a second competing history.

Append one entry after the whole scope has completed final review 2, all justified
corrections and final verification. Do not append completion entries after each
module or while final review is still running. If final 2 fails technically and
review policy permits completion, use an explicit "Completed with final-2 review
gap" status and link the incident in the project-wide issues ledger; never claim
the missing assessment passed. Blocked work stays in the scope's working state.

Each entry contains the completion date in the user's local timezone, stable
scope ID, a short description of what was delivered (mention modules where useful),
and relative links to the scope's plan, specification and working state. Keep it
to a few lines; reference detailed review/test evidence instead of copying logs.
Use the completion date here, even if it differs from the directory's start date.
For example (illustrative only):

```markdown
### 2026-09-19 — CSV import
Scope: 2026-09-17-csv-import. Completed.
Added CSV preview, row validation and confirmed import. Both final reviews and checks completed.
[Plan](2026-09-17-csv-import/plan.md) · [Spec](2026-09-17-csv-import/spec.md) · [State](2026-09-17-csv-import/state.md)
```

Preserve earlier entries and append at the end. On resume, look up the stable
scope ID and reconcile its existing entry rather than appending a duplicate.
Correct inaccurate or reopened completion status in that entry; a genuinely new
scope gets a new entry. Do not backfill old work without evidence. A quick change
still requires no workflow documents or completion-history entry.
