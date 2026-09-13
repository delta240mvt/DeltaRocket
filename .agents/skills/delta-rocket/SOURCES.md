# Sources and adaptation boundaries

Delta Rocket v0.2, revised 2026-09-13. This file documents provenance; it is
not a runtime phase and need not be loaded for ordinary execution.

The user's approved workflow is the source for sequencing, Socratic decisions,
main-agent implementation, one review per large module and two final
whole-implementation rounds. The v0.2 user revision adds a quick-change path and
continuation after a technical final-2 failure recorded in a shared project ledger.
Research reports are supporting analysis, not
instructions that supersede those decisions.

## Upstream snapshots

- [Superpowers](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797):
  brainstorming, planning, execution, review, receiving feedback, systematic
  debugging, TDD and verification. The bundled methods are concise adaptations,
  not verbatim replacements for every upstream example or supporting technique.
- [Ponytail](https://github.com/dietrichgebert/ponytail/tree/356918eba965ee1eac64bd3a7f0dd02108350de5):
  reuse and minimal necessary mechanisms, with readable code and required checks.
- [Caveman](https://github.com/juliusbrussee/caveman/tree/15581d14007fd01fb3f132016741962f34936ca2):
  communication compression and preservation of technical meaning. No engine,
  proxy, hooks or other Caveman runtime code is included.

MIT notices for adapted upstream material travel with this folder in
[THIRD_PARTY_NOTICES](THIRD_PARTY_NOTICES.md).

## Documentation used

- [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills):
  SKILL.md, progressive disclosure, project discovery and UI metadata.
- [OpenAI: Rethinking skills and prompts for GPT-6 Astra](https://learn.chatgpt.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra):
  concise routing, proportional process and avoiding redundant instruction layers.

Consult the current host for model availability and tool contracts. These
instructions intentionally do not pin a model, reasoning level, agent API,
concurrency configuration or operating system command.

## Deliberate changes

Superpowers orchestration is replaced: plan before detailed spec, no automatic
SDD handoff, main-agent implementation, module review units and finite budgets.
Review quality and debugging methods are retained with local links. TDD is
proportional to behavior and risk; user changes are not deleted to reconstruct
test-first history. Review reception preserves technical skepticism and permits
independent work while a separate question is pending.

Ponytail's persona, code-first chat output, intensity modes and one-line targets
are omitted. Caveman's persona and blanket suppression of required progress are
omitted. Output compression applies to narration, not to code or saved documents.

Installed upstream skills are untouched. Delta Rocket does not change the host's
instruction hierarchy; conflicting higher-priority instructions still apply.
It provides behavioral guidance, not a technical enforcement engine. No measured
token savings or universal agent compliance are claimed.
