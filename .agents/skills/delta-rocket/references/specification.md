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

## Implementation checkpoint

After both document reviews, corrections and plan alignment, pause before any
implementation. This is one checkpoint after both reviews, not one after each.
Present a short summary with links to the reviewed plan and specification, and
ask in the user's language: "The plan and specification are reviewed. You can
switch the implementation model now, for example from Astra to Luna. Shall I
start implementing the full plan?"

This checkpoint gives the user the requested chance to change models. Earlier
brainstorming or design acceptance alone does not satisfy it. Wait for an
explicit answer; elapsed time and a model change alone are not approval.
Use the model selected by the user in the host; never switch automatically or
claim a switch happened without evidence. They may also keep the current model.

Save the phase as awaiting implementation approval, with artifact references,
review counters and the next action. After the user authorizes implementation,
record that approval for the reviewed scope and proceed through the whole plan.
On resume or a model change, reuse recorded approval rather than asking again.
If the user requests revisions at the checkpoint, resolve them before starting;
follow the existing review budgets instead of resetting the workflow.
