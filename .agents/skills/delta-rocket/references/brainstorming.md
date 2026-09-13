# Brainstorming with Socratic gates

Inspect the request, relevant existing behavior and previous decisions first.
Scale depth to uncertainty and consequence. A gate is a resolved decision,
not a required number of questions or a new approval ceremony.

| Gate | Establish |
|---|---|
| Purpose | User, concrete problem, observable success |
| Scope | Required outcome, exclusions, constraints |
| Behavior | Main journey, consequential failures and edge cases |
| Approach | Boundaries, dependencies, meaningful tradeoffs |

Ask one question at a time only where the answer materially changes the design
and cannot be recovered from available evidence. State the decision, practical
alternatives and your recommendation. Keep a decision pending until answered;
continue independent exploration. Do not silently choose an answer to a material
product question. Routine implementation choices belong to the agent.

For example: "When an imported row repeats an existing ID, should it replace
the record or be rejected? I recommend rejection to preserve existing data."

Where there are genuine architectural alternatives, compare two or three
briefly; do not manufacture options. Capture decisions and unresolved questions
in the work record. Present the proposed design at a useful level of detail.
Reuse explicit acceptance already given in the conversation. Get acceptance
before implementation when the resulting design is not already covered.

Proceed to the module plan when material decisions are settled. Detailed
contracts are written in the specification phase. If later evidence changes
the agreed scope or behavior, reopen only that decision and affected artifacts.
