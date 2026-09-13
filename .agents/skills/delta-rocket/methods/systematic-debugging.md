# Systematic debugging

Use when a test, build, integration or expected behavior fails. Establish a root
cause before attempting a fix; time pressure does not make guessing evidence.

1. **Investigate.** Read the error and trace, reproduce the failure and inspect
   recent changes and environmental differences. For a multi-component flow,
   gather evidence at boundaries to locate where valid input becomes invalid.
   Inspect configuration presence without printing secrets. Trace a bad value
   backward through callers to its source. If reproduction is inconsistent,
   gather discriminating evidence instead of stacking patches.
2. **Compare.** Find a working analogous path and identify meaningful differences
   in data, assumptions, dependencies and state. Read the relevant reference
   completely enough to understand the behavior being used.
3. **Test a hypothesis.** State the suspected cause and supporting evidence.
   Change one variable in the smallest useful experiment. A failed experiment
   updates the hypothesis; it does not justify accumulating unverified fixes.
4. **Correct and verify.** Capture the reproduction as a regression check where
   practical. Fix the confirmed cause, then rerun the original scenario and
   affected checks using [verification](verification-before-completion.md).

After three unsuccessful fixes for the same issue, stop patching and reconsider
the architecture and assumptions. Continue evidence gathering. If the resulting
solution changes the agreed contract, return that decision to the user before
implementing it. A confirmed external limitation should be recorded with the
evidence and appropriate handling, not mislabeled as a solved internal bug.

Resume the current module after resolution. Debugging does not create a new
scope, reset review counters or authorize another reviewer.
