# Main-agent execution

Read the approved contract, module plan, work state and [review policy](review-policy.md).
Recover review history before dispatching any reviewer. Keep the main agent as
the implementer and integrator; do not redirect to subagent-driven-development
or delegate each checklist step.

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

Update `state.md` at phase/module boundaries and before each review dispatch.
Record scope ID and accepted decisions; phase and next action; module statuses;
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
