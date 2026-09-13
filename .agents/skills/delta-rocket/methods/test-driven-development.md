# Test-driven development

For new or changed behavior, use a focused red-green-refactor cycle:

1. Express an observable requirement in a small test. Identify what incorrect
   production behavior would make it fail.
2. Run it and verify the expected failure. An import error or broken fixture
   does not demonstrate the missing behavior.
3. Implement the simplest correct behavior. Run the test and affected checks.
4. Simplify while keeping the tests green.

Prefer real behavior over mocked implementation details. Use mocks where needed
for external boundaries, understanding what they replace. Test important error
paths and shared contracts, not a quota of functions or lines. Follow the
project's existing test tools; avoid introducing a framework for a trivial check.

For a bug, reproduce the original failure before correcting it. Preserve existing
user code when adding missing coverage; do not delete working changes to stage
an artificial test-first history. Report honestly when a test was added after
implementation. For configuration, prose or low-impact mechanical changes,
use appropriate validation rather than contrived unit tests.

Repeat checks when edits or failures justify it. A module's test cycles do not
dispatch reviewers. Test results feed its scheduled review and final verification.
