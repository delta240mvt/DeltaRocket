# Specify the contract

Turn the agreed design and module plan into an executable contract, not a copy
of the plan. Record:

- Observable behavior and acceptance criteria, linked to module IDs.
- Exact shared interfaces, data formats and important invariants.
- Relevant error cases, validation, recovery and compatibility requirements.
- Required performance, security or accessibility constraints for this scope.
- Explicit exclusions and the checks that demonstrate completion.

Cover consequential cases; avoid speculative features and prescribing incidental
implementation details. Resolve contradictions rather than leaving placeholders.
If required information cannot be discovered, ask one focused question and
continue work that does not depend on the answer.

Use the one spec review under [review policy](review-policy.md). Check ambiguity,
contradictions, missing acceptance cases and consistency with the module plan.
Apply justified corrections, then directly check the updated contract and align
the plan. This alignment is not another independent review.

The spec owns required behavior; the plan owns decomposition and order. If they
disagree, reconcile them against user decisions before dependent implementation.
Confirm the resulting design is covered by user acceptance. Do not ask again
for decisions already accepted. Material changes need a focused new decision.
