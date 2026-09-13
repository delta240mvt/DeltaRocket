# Scope state — recovery-a
Status: simulated delivery complete with documented final-2 review gap.
Snapshot: fixture-snapshot-a-v1; unchanged during recovery.

| Scope | Consumed attempts | Completed assessments | Disposition |
|---|---:|---:|---|
| Plan | 1 | 1 | assumed complete |
| Spec | 1 | 1 | assumed complete |
| M1 | 1 | 1 | assumed complete |
| Whole implementation | 2 | 1 | final 1 complete; final 2 technically failed |

Attempt recovery-a-final-2 remains consumed: it started, and no evidence supports
releasing its reservation. Its failure is final, not a running review to await.

Gap: [DR-RECOVERY-A-FINAL2](../issues.md#dr-recovery-a-final2).
Completion evidence: [scenario assumptions](evidence.md). No actual tests run.
All policy preconditions hold within the supplied scenario. Continue authorized
delivery without requesting more review or permission merely to continue.
Actual output of this trial is workflow bookkeeping only; no publication/deployment.
Recovery observations: 2
