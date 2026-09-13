# Receiving code review

Read all findings before changing code. Understand each claim, verify it against
the actual code and approved contract, and evaluate its consequences. The
reviewer's confidence is not evidence and does not amend user requirements.

Investigate unclear feedback using the relevant code, callers and tests. If it
still needs a decision, ask a focused question; continue only independent work
whose correctness does not depend on that answer.

Fix confirmed blocking issues first. Apply coherent corrections with targeted
checks so failures remain attributable. Reject incorrect or out-of-scope advice
with concrete code, contract or test evidence. For proposed abstractions, look
for an actual caller or requirement before adding a mechanism.

Record each finding as fixed with evidence, rejected with reasoning, deferred
with its non-blocking consequence, or unresolved. A material unresolved issue
prevents readiness. If your initial rejection was wrong, correct it directly.
Give the user the relevant outcome, not a transcript of the review discussion.

Only [review policy](../references/review-policy.md) permits another assessment.
A request to "check this one fix again" still consumes a reviewer round.
