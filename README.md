<h1 align="center">DeltaRocket</h1>

<div align="center">

<pre align="center">
                                                 ▄▄▀&#32;
                                           ▄▄▄████▀ &#32;
                                      ▄▄▄█████████  &#32;
                                    ▄████████████   &#32;
                                  ▄█████████████▀   &#32;
                                ▄███▓▓▓████████▀    &#32;
                              ▄██▓▓     ▓██████     &#32;
                          ▄▄▄████▓▄     ▓▓███▀      &#32;
                   ▄▄▄▓▓▓▓▓██████▓▓▄▄ ▄▄▓██▀        &#32;
           ▄▄▄▄▓▓▓▓▓▓▓▓▓▓██████████▓▓▓▓▓█▀          &#32;
            ▀▓▓▓▓▓▓▓▓▓▓████████████████▀            &#32;
              ▓▓▓▓▓▓▓████████████████▀              &#32;
               ▀▓▓▓█▓▓▓█████████████▓               &#32;
                ▄█████▓▓▓█████████▓▓                &#32;
                ▒███████▓▓▓█████▓▓▓▓                &#32;
               ▒▒▒▒███████▓▓▓█▓▓▓▓▓                 &#32;
                ▒▒▒▒▒███████▓▓▓▓▓▓▀                 &#32;
            ▒▒▒▒  ▒▒▒▒▒▀█▀▓▓▓▓▓▓▓▓                  &#32;
          ▒▒▒▒▒▒▒▒  ▒▒     ▀▓▓▓▓▓▀                  &#32;
       ▒▒▒▒▒▒▒▒▒▒▒            ▀▓▓                   &#32;
    ░░░░▒▒▒▒▒▒▒▒                ▀                   &#32;
 ░ ░ ░░░░░▒▒▒▒▒                                     &#32;
    ░░░░░░░░▒▒                                      &#32;
   ░░░░░░  ░░                                       &#32;
  ░░░░     ░                                        &#32;
░░                                                  &#32;

      ██████╗ ███████╗██╗  ████████╗ █████╗         &#32;
      ██╔══██╗██╔════╝██║  ╚══██╔══╝██╔══██╗        &#32;
      ██║  ██║█████╗  ██║     ██║   ███████║        &#32;
      ██║  ██║██╔══╝  ██║     ██║   ██╔══██║        &#32;
      ██████╔╝███████╗███████╗ ██║   ██║  ██║       &#32;
      ╚═════╝ ╚══════╝╚══════╝ ╚═╝   ╚═╝  ╚═╝       &#32;

 ██████╗  ██████╗  ██████╗██╗  ██╗███████╗████████╗ &#32;
 ██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝██╔════╝╚══██╔══╝ &#32;
 ██████╔╝██║   ██║██║     █████╔╝ █████╗     ██║    &#32;
 ██╔══██╗██║   ██║██║     ██╔═██╗ ██╔══╝     ██║    &#32;
 ██║  ██║╚██████╔╝╚██████╗██║  ██╗███████╗   ██║    &#32;
 ╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝    &#32;

                   BY DELTA240MVT                   &#32;
</pre>

**From an idea to working software. Clear decisions. Coherent modules. Focused reviews.**

[![Codex Skill](https://img.shields.io/badge/Codex-Skill-111111?style=flat-square)](.agents/skills/delta-rocket/SKILL.md) [![Version](https://img.shields.io/badge/Version-0.2-4a8d83?style=flat-square)](docs/design/2026-09-13-delta-rocket-v0.2.md) [![Module reviews](https://img.shields.io/badge/Module_reviews-1-f4c542?style=flat-square)](.agents/skills/delta-rocket/references/review-policy.md) [![Final reviews](https://img.shields.io/badge/Final_reviews-2-9b7bdb?style=flat-square)](.agents/skills/delta-rocket/references/review-policy.md)

**One main builder · Simple, readable code · Concise communication**

[Quick start](#quick-start) · [Why DeltaRocket](#why-deltarocket) · [Workflow](#workflow) · [Review policy](#review-policy) · [Documentation](#documentation)

</div>

---

DeltaRocket is a software development skill for Codex. It brings together
Superpowers' development discipline, Ponytail's preference for simple solutions,
and Caveman's concise communication in one coordinated workflow.

The main agent carries a project from design decisions through implementation.
It builds complete functional modules, brings in reviewers at defined checkpoints,
and records decisions and review counts so work can resume coherently.

## Why DeltaRocket

**Choose DeltaRocket when you want a capable main agent to build substantial
features with a clear process and predictable review boundaries.** Its advantage
is how the methods work together: requirements guide simplification, module
boundaries guide reviews, and concise updates report verified progress.

| Compared with | DeltaRocket's advantage for this workflow | Practical result |
| --- | --- | --- |
| Superpowers | Main-agent implementation, stable module boundaries and a tighter review budget. | Fewer implementation handoffs and less opportunity for repeated task-level review cycles. |
| Ponytail | A complete design-to-verification process around the simplicity principles. | Minimal code remains tied to agreed behavior, integration contracts and acceptance criteria. |
| Caveman | Control over work structure as well as communication. | The agent addresses review and context overhead alongside verbose narration. |

These are differences in workflow design. DeltaRocket has not demonstrated
lower total token use, faster delivery or higher code quality in a comparative
benchmark. The comparisons below refer to the specific upstream snapshots in
[SOURCES.md](.agents/skills/delta-rocket/SOURCES.md), reviewed on September 13, 2026.
They compare the relevant skills, not every feature in those projects.

### Compared with Superpowers: continuity and tighter review boundaries

Superpowers provides the foundation: clarify the goal, agree on a design, plan,
implement, review and verify. DeltaRocket retains adapted methods for debugging,
TDD, evaluating feedback and checking completion.

Its main changes are in execution:

| Decision | Referenced Superpowers workflow | DeltaRocket |
| --- | --- | --- |
| Implementation owner | Subagent-driven development assigns a fresh implementer to each plan task. | The main agent implements and fixes all modules. |
| Review unit | A plan task, whose size depends on decomposition. | A large functional module with a stable ID; internal checklist steps do not trigger reviews. |
| Correction cycles | The referenced SDD skill permits up to five fix-and-scoped-re-review rounds per task after its initial assessment. | Exactly one review per module; the main agent fixes and verifies its findings. |
| Planning detail | The planning skill asks for short execution steps and implementation code in the plan. | A module plan defines boundaries and dependencies; the following spec defines behavior and contracts. |
| Final assessment | A broad final review, with a scoped re-review if its findings require fixes. | Two whole-implementation rounds, including when the first is clean; a technical failure of round 2 is logged and does not by itself block delivery. |

Sources: [SDD execution and review rules](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/subagent-driven-development/SKILL.md)
and [planning instructions](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/writing-plans/SKILL.md).

**Why this can be better:** the same builder maintains implementation context
across related changes. Reviewers assess a complete capability rather than being
scheduled around each small piece of work. A correction does not repeatedly
bounce between fresh implementers and reviewers. The intended benefit is lower
coordination overhead while retaining explicit quality checkpoints.

For example, catalog, checkout and receipts can be three modules containing
18 small steps. DeltaRocket schedules **three module reviews plus two
final reviews**. The steps do not become 18 review units. Plan and spec reviews
add two separate document assessments. Superpowers can also group work into
three tasks; its current task-sizing guidance does not require reviewing every
checklist step. The difference is DeltaRocket's explicit module contract and
smaller correction budget.

**Tradeoff:** fresh implementers can isolate context and bring a different
perspective. Superpowers is a better fit when that execution model is desired.
DeltaRocket's main agent carries more context, and its mandatory second final
review can mean more reviews on an otherwise clean run. Neither workflow is
universally cheaper.

### Compared with Ponytail: simplicity with a delivery contract

Ponytail teaches valuable implementation judgment: reuse existing code, prefer
the standard library and native capabilities, avoid speculative abstractions,
and write only what is needed. It also explicitly protects required validation,
security, accessibility and user requirements, and calls for runnable checks
of non-trivial logic. [Ponytail skill](https://github.com/dietrichgebert/ponytail/blob/356918eba965ee1eac64bd3a7f0dd02108350de5/skills/ponytail/SKILL.md).

DeltaRocket adds the structure needed to carry that judgment through a project:

- **Decisions before dependent code.** Socratic gates resolve material questions
  about scope and behavior. The agent reuses existing answers and handles routine
  implementation choices autonomously.
- **A shared contract for simplicity.** The spec determines which behavior must
  survive a simplification. Module interfaces and acceptance criteria make that
  decision checkable across the application.
- **Scheduled quality checks.** Module reviews, two integration reviews and
  completion evidence are part of the same workflow as implementation.
- **Continuity across sessions.** A work record preserves decisions, progress,
  findings and consumed review rounds.
- **Readable implementation without a persona.** DeltaRocket keeps the reuse
  principles while omitting intensity modes and one-line code targets.

**Why this can be better:** on a feature spanning import, validation and storage,
reducing each component independently is not enough. Their contracts must agree.
DeltaRocket makes that integration an explicit responsibility and checks the
finished behavior against the original goal.

The advantage is the surrounding delivery process; it is not a claim that
Ponytail lacks safeguards or produces bad code. For a focused refactor or a small
change inside an established workflow, Ponytail alone may require less ceremony.

### Compared with Caveman: efficiency beyond the wording of replies

Caveman focuses on compressed communication. Its skill already preserves technical
meaning, keeps code blocks intact and calls for normal prose in saved artifacts.
Its lighter mode also preserves ordinary grammar. Those protections are shared
principles, not inventions of DeltaRocket.
[Caveman skill](https://github.com/juliusbrussee/caveman/blob/15581d14007fd01fb3f132016741962f34936ca2/skills/caveman/SKILL.md).

DeltaRocket extends the efficiency goal to the work itself:

- **Review scheduling:** stable module boundaries and finite rounds constrain
  how often another assessment is requested.
- **Context loading:** a small entrypoint routes to phase and method references
  as needed; research reports are not part of the default execution context.
- **Implementation continuity:** the main agent builds and fixes the code,
  avoiding routine transfers of each task to a new implementer.
- **Useful updates:** short findings, decisions and blockers keep the user
  informed while respecting progress requirements imposed by the host.
- **Clear output boundaries:** narration stays concise; questions remain
  intelligible; code, comments and documentation remain complete.

**Why this can be better:** a short final answer does not remove the work and
context involved in repeated agent dispatches. DeltaRocket addresses those
sources of overhead alongside the amount of text shown in chat.

This comparison concerns the Caveman communication skill, not its separate
engine or proxy components. If all you need is shorter replies in an existing
workflow, Caveman is the more focused tool. DeltaRocket does not claim to
compress replies more aggressively, control Codex's tool cards or achieve
Caveman's advertised token savings.

## What DeltaRocket includes

| Capability | What it does |
| --- | --- |
| Socratic brainstorming | Resolves consequential questions about purpose, scope, behavior and tradeoffs. |
| Module planning | Defines coherent capabilities, dependencies and completion evidence. |
| Detailed specification | Captures interfaces, edge cases and testable requirements before implementation. |
| Main-agent execution | Keeps implementation and corrections with one builder; a subagent may review. |
| Bounded review rounds | One review per module, followed by two final rounds with a documented technical-failure fallback. |
| Quality methods | Bundles adapted code review, feedback evaluation, systematic debugging, TDD and verification. |
| Durable work state | Records decisions, progress, findings, checks and review counters for resumption. |
| Concise communication | Summarizes meaningful progress while preserving complete project artifacts. |

## Workflow

For small, reversible changes with a clear outcome and low risk, the agent edits
and checks directly, without plan/spec/state documents or formal reviews. Changes
to permissions, data integrity or public contracts use the full workflow below,
regardless of diff size. Existing full-workflow scopes retain their recorded history.

```text
IDEA
  |
  v
Brainstorming + Socratic gates
  |
  v
Module plan -> Plan review -> Corrections
  |
  v
Detailed spec -> Spec review -> Corrections -> Align plan
  |
  v
For each large module:
  Build -> Test -> Review -> Fix and verify
  |
  v
Whole-implementation review: round 1
  |
  v
Fixes + tests
  |
  v
Whole-implementation review: round 2
  |
  v
Final corrections + verification
```

The plan owns decomposition and order. The spec owns required behavior.
The agent reuses previous answers and approvals, returning to the user when
new evidence requires a material change to the agreed design.

## Review policy

| Scope | Budget |
| --- | --- |
| Module plan | One review, followed by corrections. |
| Specification | One review, followed by corrections. |
| Each large module | Exactly one review, followed by fixes and direct verification. |
| Whole implementation | Two rounds after all modules; technical failure of final 2 follows the ledger-and-continue rule. |

Review counters survive resumed sessions, new commits and renamed or split
modules. A new reviewer assessment of a single correction still consumes a round.
Tests, diagnosis and direct verification by the implementer do not consume one.

The second final review happens even when the first finds no issues. After the
last round, the main agent applies justified corrections and runs affected checks.
Unresolved material requirements prevent a ready verdict; reaching the review
limit is not evidence that the software works.

If the second final round fails technically, record the incident and known notes
in the shared project ledger `docs/delta-rocket/issues.md`, then continue to
verification and authorized delivery. Preserve existing entries and update the
same incident on resume. Completion remains conditional on final 1 and other
required assessments being complete, passing checks and no unresolved material
defects. Report the missing review and ledger link; do not claim two successful
reviews. A review reporting a defect is not a technical failure.

Without available subagents, the main agent performs explicitly recorded inline
assessments under the same budgets and discloses the lack of independent review.
See the [complete review policy](.agents/skills/delta-rocket/references/review-policy.md).

## Quick start

### Use in this repository

```bash
git clone https://github.com/delta240mvt/DeltaRocket.git
cd DeltaRocket
```

Open the directory in Codex and invoke:

```text
$delta-rocket Build a CSV import dashboard with a data preview and error handling.
```

The skill lives in `.agents/skills/delta-rocket`, the project skill location
recognized by Codex. If it does not appear in the skill list, restart Codex.

### Use in another project

Copy the entire [`delta-rocket`](.agents/skills/delta-rocket) directory into that
project's `.agents/skills/` folder. Keep the references, methods and notices.
Invoke it the same way. Installing Superpowers, Ponytail or Caveman is not required.

### Install globally with automatic routing

With Python 3 available as `python`, run from this repository:

```bash
python scripts/install-codex.py
```

The installer copies the skill and the [DeltaRocket hook](hooks/delta-rocket.py)
to `CODEX_HOME` (default: `~/.codex`) and merges two entries into `hooks.json`.
It backs up an existing hook configuration and preserves other hooks. Running
it again updates DeltaRocket without adding duplicate entries. It does not
disable other workflows or modify hook trust.

Restart Codex, open `/hooks`, and review and trust the two DeltaRocket entries.
[Codex requires explicit trust for user hooks](https://learn.chatgpt.com/docs/hooks).
An enabled entry awaiting trust will not run.

- `SessionStart` loads the entrypoint on startup, resume, clear and compaction.
- `UserPromptSubmit` adds a short routing reminder for each user message.
- The model chooses a quick change, the full workflow, or a direct response for
  questions and standalone reviews. An explicit choice of another workflow wins.
- Subagents receive no automatic hook, so reviewers do not restart the workflow.

The hook only emits context; it does not execute the prompt, call a model, or
enforce the model's decision. Supporting references are loaded on demand.

The display name is **DeltaRocket**. The compatible technical skill identifier,
directory name and explicit invocation remain `delta-rocket` / `$delta-rocket`.

## Project layout

```text
.agents/skills/delta-rocket/
  SKILL.md                  Entry point and workflow routing
  agents/openai.yaml        Codex interface metadata
  references/               Phase instructions and review policy
  methods/                  Quality methods loaded when needed
  SOURCES.md                Provenance and adaptation boundaries
  THIRD_PARTY_NOTICES.md     Upstream license notices
docs/
  design/                   Skill plan and specification
  research/                 Source analysis
  testing/                  Scenarios and validation results
hooks/delta-rocket.py        Session and prompt routing context
scripts/install-codex.py     Global skill and hook installation
```

## Validation and scope

Version 0.2 passed a repeated real JSON correction trial, recovery bookkeeping
scenarios and one independent package review. The small correction used one skill
file and zero formal reviews, compared with nine files and five inline reviews
in the earlier trial. See the [v0.2 results](docs/testing/2026-09-13-v0.2-results.md)
for evidence and the distinction between real edits and scenario assumptions.

Version 0.1 passed structural validation and underwent two final package reviews.
A separate agent evaluated eight simulated workflow scenarios and produced a
recovered-state artifact. These were process decisions, not eight complete
application builds. See the [validation report](docs/testing/2026-09-13-results.md)
for the observations and limitations.

**What remains unproven:** comparative token savings, delivery speed, defect
rates and reliability across real projects. A fair benchmark would hold the
model, task, repository and verification criteria constant, then measure the
whole run, including subagents and rework. Shorter visible replies alone are
not evidence of lower total cost.

DeltaRocket supplies behavioral instructions, not a runtime that technically
enforces limits. It uses the model and tools available in the host. Existing
skills remain unchanged; the optional installer adds user hooks as described
above. Host instructions still apply. Historical documents and trial artifacts
use the current DeltaRocket spelling; this naming update does not rerun those trials.

## Documentation

The skill instructions and this README are in English. The original design,
research and validation summary are in Polish; the behavioral trial artifacts
are in English.

- [Module plan — Polish](docs/design/2026-09-13-delta-rocket-plan.md)
- [Current specification v0.2 — Polish](docs/design/2026-09-13-delta-rocket-v0.2.md)
- [Historical specification v0.1 — Polish](docs/design/2026-09-13-delta-rocket-spec.md)
- [Deep research — Polish](docs/research/2026-09-13-delta-rocket-deep-research.md)
- [Behavior scenarios — Polish](docs/testing/scenarios.md)
- [Validation summary — Polish](docs/testing/2026-09-13-results.md)
- [Behavioral trial report — English](docs/testing/behavior-report.md)

## Credits and provenance

DeltaRocket builds on [Superpowers](https://github.com/obra/superpowers),
[Ponytail](https://github.com/dietrichgebert/ponytail) and
[Caveman](https://github.com/juliusbrussee/caveman). Their ideas and methods
are adapted to one main builder, functional modules and bounded reviews.

Exact snapshots and adaptation boundaries are documented in
[SOURCES.md](.agents/skills/delta-rocket/SOURCES.md).
Upstream license notices are preserved in
[THIRD_PARTY_NOTICES.md](.agents/skills/delta-rocket/THIRD_PARTY_NOTICES.md).

---

<div align="center"><strong>DeltaRocket · BY DELTA240MVT</strong><br><em>Think. Build. Verify.</em></div>
