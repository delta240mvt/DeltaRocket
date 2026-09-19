# Verification before completion

Before claiming a module or scope is ready, identify the evidence needed for
that claim, run the appropriate checks on the current changed state, inspect
results and exit status, and compare them with the acceptance criteria.

Tests passing supports those tests, not an unrun build or unexamined requirement.
A reviewer verdict is an assessment, not a test result. Check a subagent's
claims against actual artifacts. Record skipped or unavailable checks explicitly.
Reuse still-valid evidence; changes invalidate checks for affected behavior.

For final completion, confirm:

- Every item in the accepted plan is complete; approved behavior and module
  contracts are satisfied. Unfinished work is a blocker or an explicit user-approved
  scope change, not an implicit deferral.
- Required reviews occurred with preserved counters and scope coverage, or
  [review policy](../references/review-policy.md)'s documented final-2 technical
  failure exception applies. Quick changes require no formal reviews.
- Justified review corrections are implemented and their checks pass.
- No material unresolved findings are hidden by a consumed review budget.
- The final summary describes the actual scope and verification limitations.

After fixes from the second final review, run affected tests or concrete
validation; do not start an unbudgeted third assessment. After a technical final-2
failure, write the shared issue entry and finish with that limitation when the
policy's conditions hold. Other missing required evidence still needs to be
obtained or reported as a precise blocker. Do not claim success because a
deadline or review limit was reached.

Finishing does not itself authorize publishing, pushing, merging, deployment,
external messages or destructive cleanup. Perform the actions the user actually
requested and preserve existing authorization without adding routine approvals.
