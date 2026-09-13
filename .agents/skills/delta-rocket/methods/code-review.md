# Code review

Load for a scheduled review. [Review policy](../references/review-policy.md)
owns scheduling and budgets; this method owns assessment quality.

## Establish the actual scope

Read project conventions and the contract. Compare the entire specified change
against its recorded starting state. A last-commit diff alone can omit earlier
commits, staged/unstaged changes and new files. Inspect repository status and
the supplied manifest as well as diffs. Read relevant callers and interfaces.
If HEAD does not exist, inspect all in-scope files directly. In a dirty starting
tree, distinguish pre-existing user work from this scope using the saved baseline.
Do not create commits or stage files merely to make a review diff.

## Combined assessment

Check required behavior, important edge cases, interface consistency, regressions,
maintainability and appropriate security constraints. Inspect whether tests
would detect the likely failures; passing tests alone do not prove completeness.
Look for unnecessary abstractions or dependencies, while retaining behavior
the user requested. For document reviews, apply the phase's document rubric.

Report actionable findings with severity, file and line/section, triggering
condition, consequence and suggested direction. Distinguish confirmed defects
from questions. Do not manufacture findings, impose personal style or request
speculative features. Use critical/important/minor consistently; explain why
an issue blocks acceptance rather than relying only on the label.

Return: verdict; findings; evidence examined and verification gaps. A clean
review can be a few sentences. Remain read-only: do not edit files, index or
HEAD; do not delegate. Recommend corrections, not additional review rounds.
