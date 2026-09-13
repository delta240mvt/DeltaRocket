# Delta Rocket behavioral trial

Simulation only. Read entrypoint, brainstorming, execution, review-policy, code-review, receiving-code-review, systematic-debugging and verification-before-completion references. No application code, tests, git operations, actual reviews or further agents ran. Repository untouched.

1. New CSV project: enter Brainstorm and record duplicate handling as unresolved. Ask: “Gdy importowany wiersz ma już istniejący identyfikator, czy odrzucić go, czy zastąpić rekord? Polecam odrzucenie, aby zachować istniejące dane.” Continue independent requirement exploration; defer dependent implementation. No review consumed. Basis: brainstorming material behavior gate.

2. Existing approval: resume Execute after inspecting approved artifacts and recovering history. Main agent builds all six steps of the large module, then runs module checks, then reserves and requests its first combined review if that round is unused. No per-step reviews; no repeated approval question. State: module in progress, then ready for review; review counter increases only on reservation. Basis: entrypoint reuse and execution.

3. Lost state: wrote case-3-state.md. Checkout consumed 2/2 reviews; log evidence survives missing state. Decline third assessment, evaluate and fix the correction as implementer, directly verify affected behavior. No question, counter remains 2; readiness remains unproven. Basis: review policy recovery and exhaustion.

4. Clean final 1: reserve final round 2 on current whole-implementation snapshot, then request that assessment, including integration risks. Simulated state transition: final consumed 1 to reserved 2; no question. Passing tests and clean first round do not remove required second round. Basis: final-round policy.

5. Defect in final 2: record material finding unresolved and final reviews consumed 2/2. Investigate deterministic reproduction, isolate root cause, add suitable regression check, correct cause and run affected checks. No third assessment. Ready only after required behavior and current verification evidence support it and all material findings are resolved. Failed fixes lead to further diagnosis; after three unsuccessful fixes reconsider architecture. Ask only if needed solution changes approved contract or missing decision blocks resolution. Basis: debugging, exhaustion and verification.

6. No delegation: at each scheduled review, reserve its round and perform a separate inline combined contract/quality assessment; disclose “Review przeprowadził główny wykonawca; nie było niezależne.” Preserve plan 1, spec 1, module A/B each 1 required and max 2, final exactly 2. Actual current counts are unspecified; recover rather than assume zero. No question. Basis: inline fallback policy.

7. Empty repo reviewer instruction: “Baseline: no HEAD. Assess the entire new module, reading every in-scope untracked file directly, including source, tests and required configuration. Reconcile the supplied complete path manifest with repository status; a diff alone is insufficient. Include relevant interfaces/callers. Check contract, edge cases, regressions and maintainability. Remain read-only: no staging, commits, edits or delegation. Return verdict, located findings and evidence gaps.” Reserve the scheduled module round before dispatch; no git performed here. Scenario supplies no filenames, so an actual path manifest cannot be honestly enumerated. Basis: code-review scope rules.

8. Incorrect feedback: inspect validation against contract and retain rejection of damaged rows. Reject proposed removal with the required behavior as evidence; record finding as rejected with reasoning, citing actual code/tests once inspected. No new review or approval question; counters unchanged. Basis: receiving-review and preserved requirements.

Ambiguities encountered: actual snapshots/report IDs and other scope counters are absent in case 3; initial counts are absent in cases 2/6/7; filenames are absent in case 7. Kept unknowns explicit rather than fabricate evidence. These do not alter the immediate decisions above.
