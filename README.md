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

**One workflow to plan, build and check your software.**

[![Codex Skill](https://img.shields.io/badge/Codex-Skill-111111?style=flat-square)](.agents/skills/delta-rocket/SKILL.md) [![Version](https://img.shields.io/badge/Version-0.2-4a8d83?style=flat-square)](docs/design/2026-09-13-delta-rocket-v0.2.md)

[Why DeltaRocket](#why-deltarocket) · [How it works](#how-it-works) · [Install](#install) · [Documentation](#documentation)

</div>

## Why DeltaRocket

DeltaRocket is a Codex skill for building software. It combines three useful ideas:
**plan before building** from Superpowers, **keep the solution simple** from
Ponytail, and **keep updates short** from Caveman.

Using three separate skills can leave the agent with overlapping instructions
about what to do next. DeltaRocket brings those ideas into one set of rules:
when to plan, who writes the code, what to review, and when the work is done.
You do not need to install the three original skills.

**Why this can work better for a whole feature or project:**

- **One builder keeps the context.** The main agent writes and fixes the code.
  Reviewers check the work at clear checkpoints.
- **Small changes stay small.** A safe text correction gets an edit and a check,
  without a planning document or a formal review.
- **Reviews cover useful pieces of the product.** Each large module gets one
  review. Small checklist steps do not each trigger another review cycle.
- **Simple still means complete.** Reuse existing code and avoid unnecessary
  complexity while preserving agreed behavior, validation and relevant tests.
- **Less to load and repeat.** The agent reads detailed instructions when needed
  and saves decisions so it can resume work without starting the process again.

The benefit is a more consistent process with less coordination to manage.
It is not yet proven to be faster, cheaper or better at finding bugs than the
three skills used separately. An individual skill may be enough when you only
want its specific behavior.

## How it works

DeltaRocket chooses the amount of process the task needs:

| Request | What happens |
| --- | --- |
| Small, reversible change with a clear outcome and low risk | Edit, check, report. No required planning documents or formal reviews. |
| A feature, project, or consequential change | Agree on behavior, plan modules, write the specification, build, review and verify. |
| A question or standalone review | Handle the request directly. No implementation workflow. |

Changes to permissions, data integrity or public contracts use the full workflow,
regardless of size. Work already in progress keeps its saved decisions and review counts.

For the full workflow, the review budget is **one plan review, one specification
review, one review per large module, and two final reviews of the whole change**.
The main agent fixes findings and runs the relevant checks.

If the second final review fails technically, the agent records the failure and
known notes in the shared project file `docs/delta-rocket/issues.md`, then continues.
Completion still requires the other reviews to be finished, checks to pass, and
no unresolved material bugs. The final report discloses the missing review.
A review that finds a real bug still requires a fix.

## Recent improvements

- Added the quick path for small changes.
- Reduced module reviews to exactly one per module.
- Added the shared issue log and continuation rule for a technical failure of final review 2.
- Added optional Codex hooks for automatic workflow selection.
- Standardized the display name as **DeltaRocket**. The technical identifier remains `$delta-rocket`.

## Install

### Use in this repository

```bash
git clone https://github.com/delta240mvt/DeltaRocket.git
cd DeltaRocket
```

Open the directory in Codex, then ask:

```text
$delta-rocket Build a CSV import dashboard with a preview and error handling.
```

To use it in another project, copy the entire
[delta-rocket folder](.agents/skills/delta-rocket) into that project's `.agents/skills/`.
Restart Codex if the skill does not appear.

### Install for all projects, with automatic routing

With Python 3 available as `python`, run from this repository:

```bash
python scripts/install-codex.py
```

The installer copies the skill and hook into `CODEX_HOME` (default: `~/.codex`).
It backs up existing hook settings, preserves other hooks, and can be run again
without adding duplicate DeltaRocket entries.

Restart Codex, open `/hooks`, and review and trust the two DeltaRocket entries.
[Untrusted hooks do not run](https://learn.chatgpt.com/docs/hooks).

The session hook loads the workflow rules; the message hook adds a short reminder
to choose the right path. An explicit request to use another workflow takes priority.
These hooks guide the agent; they do not enforce its decisions. The installer
does not disable other workflow hooks, so review those separately if they conflict.

## Validation

The v0.2 small-change trial used one skill file and zero formal reviews, compared
with nine files and five inline reviews in the earlier trial. Recovery scenarios
and an independent package review also passed. See the
[v0.2 results](docs/testing/2026-09-13-v0.2-results.md) for the evidence and limitations.

Hook and installer tests cover repeated installation, preservation of other hooks,
and context output. Run them with `python -m unittest discover -s tests -v`.
These checks are not a benchmark of delivery speed, token savings or code quality.

## Documentation

- [Skill instructions](.agents/skills/delta-rocket/SKILL.md)
- [Full review policy](.agents/skills/delta-rocket/references/review-policy.md)
- [Current specification — Polish](docs/design/2026-09-13-delta-rocket-v0.2.md)
- [Research and design rationale — Polish](docs/research/2026-09-13-delta-rocket-deep-research.md)

## Credits

Inspired by [Superpowers](https://github.com/obra/superpowers),
[Ponytail](https://github.com/dietrichgebert/ponytail) and
[Caveman](https://github.com/juliusbrussee/caveman).
Selected ideas and methods are adapted into one workflow.
See [sources and exact versions](.agents/skills/delta-rocket/SOURCES.md) and
[license notices](.agents/skills/delta-rocket/THIRD_PARTY_NOTICES.md).

Historical documents use the current DeltaRocket spelling; renaming them did not rerun the trials.

---

<div align="center"><strong>DeltaRocket · BY DELTA240MVT</strong><br><em>Think. Build. Verify.</em></div>
