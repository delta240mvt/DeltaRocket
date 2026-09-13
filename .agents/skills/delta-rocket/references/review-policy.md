# Review policy — single source for budgets

This policy applies to the full workflow; quick changes have no formal reviews.

| Scope | Required rounds | Maximum |
|---|---|---|
| Module plan | 1 | 1 |
| Detailed spec | 1 | 1 |
| Each large planned module | 1 | 1 |
| Whole implementation, after all modules | 2 rounds; final-2 technical failure uses the continuation rule below | 2 |

Each round is one bounded assessment by one reviewer, combining contract and
quality. A new reviewer assessment of even one fix consumes another round.
An explicit inline review also consumes a round. Tests, diagnosis and the main
implementer's direct checks of corrections are verification, not extra reviews.
Renaming an audit "verification" does not change how it counts.

Reserve the round in durable state before dispatch. Record scope, round number,
input revision/snapshot and status; attach the result afterward. If the call
fails ambiguously, the reservation remains consumed. Release it only with
positive evidence that the reviewer never started. Resume an existing running
review rather than launching a duplicate.
Track consumed attempts separately from completed assessments. A failed attempt
is not a completed review. When resuming an older scope, preserve its historical
counts; a module already reviewed once or more receives no further module review.

Counts survive compaction, new commits, renamed/split modules and reopened fixes.
Final rounds cannot be borrowed for another module review, or vice versa.
Existing scope keeps its history. Only an explicit user decision changes limits
or introduces genuinely new scope; a reviewer request cannot do either.

## Dispatch and disposition

Use a review subagent when available and permitted. Give it the contract, exact
scope, baseline and current snapshot, relevant files, verification evidence and
previous unresolved findings. Use [code review](../methods/code-review.md).
The reviewer is read-only and does not delegate. Keep its input focused; do not
copy the whole parent conversation. Freeze that scope while it is being reviewed.

If delegation is unavailable, conduct a separate inline assessment using the
same rubric and counters; disclose that it was not independent. Never claim
that an unavailable subagent reviewed the work.

The main agent [evaluates findings](../methods/receiving-code-review.md), fixes
confirmed problems and directly verifies the corrections. Each finding is fixed
with evidence, rejected with reasoning, deferred as non-blocking, or unresolved.
Material requirements cannot be deferred into a "ready" verdict.

## Final rounds and exhaustion

Final 1 examines the whole approved implementation: cross-module contracts,
end-to-end behavior, requirements and regressions. Apply justified fixes and test.
Final 2 again assesses the whole implementation, emphasizing changes since final
1 and remaining integration risks. It happens even if final 1 found no issues.

After round 2, apply justified fixes and run affected verification. There is no
automatic third reviewer dispatch, including a scoped one. Continue root-cause
diagnosis while progress is possible. If a material issue cannot be resolved,
report the unmet criterion and needed decision/evidence; do not call it ready.
User authorization for more review must be explicit, not inferred from urgency.

## Technical failure of final 2: record and continue

If final 2 terminates without a usable assessment, or cannot run because of a
technical failure, record the failure and continue to final verification and
the authorized delivery. Do not launch a replacement reviewer or an inline third
assessment, and do not ask for permission merely to continue. A still-running
review is not a failure; resume or await it using the host's tools.

Create or update the project-wide `docs/delta-rocket/issues.md` (relative to the
project root), or the project's existing shared issue ledger. It is shared by
all scopes in that project, not a machine-wide file. Preserve existing entries.
Use a stable issue ID and record scope, round/attempt ID, code snapshot, failure
evidence, missing review coverage, known findings with their status, and the next
action for later repair or assessment. Label missing coverage as a review gap,
not an invented code defect. Link the entry from the scope state. On resume,
update the same entry rather than creating a duplicate; mark it resolved only
when later evidence actually closes the gap. A bookkeeping entry alone does not
schedule an automation or authorize an extra review.

The recorded final-2 gap is non-blocking for delivery when final 1 and all other
required assessments are complete, the agreed checks pass on the current state,
and no material defect remains unresolved. Report completion with the explicit
limitation and ledger link; never claim two successful final reviews. If the
ledger cannot be written, obtain a durable project-local record before using
this exception. Keep fixing confirmed material defects and progressing with
independent work; a failed test or a review that reports defects is not a technical
review failure and does not become acceptable merely by logging it for later.
