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

[![Codex + Claude Code](https://img.shields.io/badge/Codex_+_Claude_Code-Skill-111111?style=flat-square)](.agents/skills/delta-rocket/SKILL.md) [![Version](https://img.shields.io/badge/Version-0.3-4a8d83?style=flat-square)](docs/delta-rocket/2026-10-04-claude-code-support/spec.md)

[Why DeltaRocket](#why-deltarocket) · [How it works](#how-it-works) · [Install](#install) · [Documentation](#documentation)

</div>

## Why DeltaRocket

DeltaRocket is a skill for building software in **Codex and Claude Code**. It combines three useful ideas:
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
After the plan and specification have been reviewed and corrected, the agent
pauses once before implementation. It asks whether to start and reminds you that
you can switch models. In Codex, use its model selector (for example, Astra to
Luna). In Claude Code, use `/model` to choose an available Claude model.
You choose the model; the skill does not switch it automatically.

After your approval, the agent works through the entire plan, fixes findings,
completes the required reviews and runs the final checks. It does not stop after
each module to ask whether to continue. A genuine blocker or your request to
pause can still interrupt work. Resuming or changing models preserves progress
and the approval already given.

If the second final review fails technically, the agent records the failure and
known notes in the shared project file `docs/delta-rocket/issues.md`, then continues.
Completion still requires the other reviews to be finished, checks to pass, and
no unresolved material bugs. The final report discloses the missing review.
A review that finds a real bug still requires a fix.

## Project records

Each new feature with its own plan gets a folder with a start date and a clear
name. For example:

```text
docs/delta-rocket/
  2026-09-19-csv-import/
    plan.md     What to build and in what order
    spec.md     How it should work
    state.md    What is done and what to do next
  state.md      A short history of finished work across the project
  issues.md     Notes about missing final reviews, when needed
```

Modules that belong to the same plan share one folder. A separately planned
module gets its own dated folder. Continuing work tomorrow or changing models
keeps the same folder. Existing folders are not renamed.

After the whole plan, both final reviews, fixes and checks are done, the agent
adds a few lines to the shared `state.md`: the finish date, what was built, and
links to its documents. This lets you follow the project's progress in one place.
The finish date can differ from the folder's start date.

If the second final review has a technical failure and the completion rules above
are met, the history clearly notes the missing review and links to `issues.md`.
It never says that a failed review passed. Resuming the same work updates its
entry instead of adding a duplicate. Small changes still need no such documents.

## Recent improvements

- **A chance to change models.** After the plan and specification are reviewed,
  the agent asks before starting to build. You can plan with Astra, switch to
  Luna in Codex, or choose a different Claude model with `/model`, then give the go-ahead.
- **Finish the whole plan.** After your approval, the agent keeps going through
  all modules, reviews and checks, unless blocked or asked to pause.
- **Dated folders.** New planned work gets a date and a name, so it is easy to find later.
- **One project history.** Finished work gets a short note in the shared `state.md`.
- **Less process for small edits.** Simple changes get an edit and a check.
  Larger work gets one review per module and two final reviews.
- **Recovery and automatic startup.** A failed second final review has a clear
  logging rule. Optional hooks load the workflow rules in Codex and Claude Code.

- **Two supported hosts.** The same skill, project records and review rules work
  in Codex and Claude Code. Each has its own installer and hook settings.

The display name is **DeltaRocket**. Invoke it with `$delta-rocket` in Codex or
`/delta-rocket` in Claude Code.

## Install

Clone the repository and choose the installer for your host. Python 3 is required.

```bash
git clone https://github.com/delta240mvt/DeltaRocket.git
cd DeltaRocket
```

| Host | Install for all your projects | Invoke explicitly |
| --- | --- | --- |
| Codex | `python scripts/install-codex.py` | `$delta-rocket` |
| Claude Code | `python scripts/install-claude-code.py` | `/delta-rocket` |

Run both installers if you use both hosts. They copy the same complete skill
and add two hooks: one loads the rules at session start, the other adds a short
reminder with each user message. Both help the agent choose quick changes or the
full workflow. Questions and standalone reviews stay simple.

Existing settings are backed up. Other hooks, plugins, models and permissions
are preserved. Run the same installer again after `git pull` to update.

### Codex

The personal install uses `CODEX_HOME` (default `~/.codex`). Restart Codex,
open `/hooks`, and review and trust the two DeltaRocket entries.
[Untrusted hooks do not run](https://learn.chatgpt.com/docs/hooks).

```text
$delta-rocket Build a CSV import dashboard with a preview and error handling.
```

This repository already has the project skill in `.agents/skills/delta-rocket`.
You can copy that whole folder to another project's `.agents/skills/` if you
prefer project-only use without global hooks.

### Claude Code

The personal install uses `CLAUDE_CONFIG_DIR` (default `~/.claude`): the skill
lives in `skills/delta-rocket`, and hooks are added to `settings.json`.
Restart Claude Code and inspect `/hooks`.

```text
/delta-rocket Build a CSV import dashboard with a preview and error handling.
```

For project-only use, copy the whole `.agents/skills/delta-rocket` folder to
`.claude/skills/delta-rocket` in your project. The
[Claude Code skills documentation](https://code.claude.com/docs/en/skills)
explains personal and project skills. Global installation is local to your
computer; it does not upload the skill to Claude's cloud services.

On Windows, the default installer uses Git Bash. If you use PowerShell for
Claude hooks instead, run `python scripts/install-claude-code.py --shell powershell`.
The installed Python interpreter is used, so keep it available after installation.
Hook shell selection is described in the
[Claude Code hooks documentation](https://code.claude.com/docs/en/hooks).

### What the hooks do

Hooks add instructions; they do not technically block edits or enforce completion.
The agent still asks before implementation after plan and spec reviews, and you
can change the model then. An explicit choice of another workflow takes priority.
No hook is installed for reviewer subagents or to force the agent to keep talking.
Disabled hooks, managed settings or other competing workflow plugins can affect
activation. Inspect your host's hooks and policies rather than bypassing them.

## Validation

The v0.2 small-change trial used one skill file and zero formal reviews, compared
with nine files and five inline reviews in the earlier trial. Recovery scenarios
and an independent package review also passed. See the
[v0.2 results](docs/testing/2026-09-13-v0.2-results.md) for the evidence and limitations.

Hook and installer tests cover both hosts, repeated installation, preservation
of other settings and hooks, host isolation, context output and paths with spaces
or special characters. Run them with `python -m unittest discover -s tests -v`.
These checks are not a benchmark of delivery speed, token savings or code quality.

For v0.3, both hooks also ran successfully in installed Claude Code 2.1.132.
The model-response smoke test could not finish because the local Claude OAuth
token had expired. A complete Claude-driven build has not been verified. See the
[host support checks](docs/delta-rocket/2026-10-04-claude-code-support/verification.json).

## Documentation

- [Skill instructions](.agents/skills/delta-rocket/SKILL.md)
- [Full review policy](.agents/skills/delta-rocket/references/review-policy.md)
- [Codex and Claude Code guidance](.agents/skills/delta-rocket/references/hosts.md)
- [Claude Code support specification](docs/delta-rocket/2026-10-04-claude-code-support/spec.md)
- [Workflow specification v0.2 — Polish](docs/design/2026-09-13-delta-rocket-v0.2.md)
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
