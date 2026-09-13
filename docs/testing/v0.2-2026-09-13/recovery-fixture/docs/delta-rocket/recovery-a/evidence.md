# Trial evidence — assumptions, not executed checks

This disposable fixture simulates the supplied scenario. No application, build,
tests or actual reviewer was run. No real implementation or release is claimed.

Scope: recovery-a; input/code snapshot: fixture-snapshot-a-v1.
Assumed unchanged during recovery and resume.
- Approved plan and spec satisfy the assigned scenario.
- Plan review: 1 consumed attempt, 1 completed assessment, no open findings.
- Spec review: 1 consumed attempt, 1 completed assessment, no open findings.
- Module M1: 1 consumed attempt, 1 completed assessment, no open findings.
- Final 1 (recovery-a-final-1): 1 consumed attempt, 1 completed assessment.
- Final 2 (recovery-a-final-2): previously reserved, started, irreversibly failed,
  no usable report; 1 consumed attempt, 0 completed assessments.
- Current agreed checks pass and no material defect is unresolved: scenario
  assumptions only, not facts established by running checks here.

The first recovery and second resume only change workflow records.
