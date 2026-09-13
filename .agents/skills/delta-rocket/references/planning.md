# Plan the modules

Describe how to deliver the agreed outcome before writing the detailed spec.
A large module delivers a coherent capability that can be checked and reviewed
as a whole. Group setup, storage, UI and tests when they serve that capability.
Size by responsibility and coupling, not minutes, file count or token count.

For each module record:

- Stable ID and deliverable, including what lies outside its boundary.
- Dependencies and proposed interfaces with other modules.
- Relevant existing code and expected file areas.
- Verification approach and completion evidence.

Mark proposed interfaces as provisional until the spec makes them precise.
Avoid complete implementation code and minute-by-minute instructions. Small
checklists inside a module support execution, not separate reviewer dispatches.

Read [review policy](review-policy.md). Perform the one plan review against
the agreed design: coverage, feasibility, dependency order, module boundaries
and unnecessary complexity. Resolve findings together and verify corrections
directly. Missing product decisions return to their Socratic gate.

Then write the detailed spec. After spec review, align the plan to its contracts
without automatically launching another plan review. Preserve module IDs when
renaming, correcting or splitting work; review history follows the original
scope. Only genuinely new user-approved scope gets a new budget.
