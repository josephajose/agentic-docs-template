# Agentic docs template

Stack-agnostic documentation and development-workflow layout for projects that use coding agents.

Copy this into a new or existing repo, then fill in project-specific content. Nothing here assumes a language, framework, cloud, or product domain.

## Layers

Docs live under `docs/` in three layers. Each layer drives the one below it.

1. **`docs/1-domain/`** — how the work is done with no app at all: vocabulary, rules, and decision records (DR-NN).
2. **`docs/2-system/`** — how software automates the domain: architecture, features, contracts, technical notes, and architecture decision records (ADRs).
3. **`docs/3-engineering/`** — how the software gets built: process files (NOW, BACKLOG, DECISIONS, usage log), phases, and an optional slice-card board for concurrent work.

## Traceability

- Core system features cite their source: `Implements: 1-domain/...`.
- Phase docs cite what they deliver: `Delivers: 2-system/...`.
- Exempt (no upstream source needed): `2-system/technical/` and pure engineering work such as testing, ops, and refactoring.

## What's included

| Path | Purpose |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Lane model and always-load rules for coding agents |
| [docs/README.md](docs/README.md) | Docs map |
| `docs/1-domain/` | Domain stubs, glossary, alignment register, rule + DR templates |
| `docs/2-system/` | System stubs, feature + ADR templates |
| `docs/3-engineering/process/` | NOW, BACKLOG, DECISIONS, ROADMAP, inbox, usage log; `slices/` card template (parallel mode) |
| `docs/3-engineering/phases/` | Phase doc template |
| [.cursor/skills/agent-flow/](.cursor/skills/agent-flow/SKILL.md) | Workflow skill: open / close / plan / optimize / audit |
| [scripts/check_doc_links.py](scripts/check_doc_links.py) | Broken relative-link checker |
| [CHANGELOG.md](CHANGELOG.md) | Template version history (pull changes into applying projects) |
| [docs/3-engineering/cloud-agents.md](docs/3-engineering/cloud-agents.md) | Optional pattern for branch+PR cloud coding agents |

## Apply to a project

1. Copy `docs/`, `AGENTS.md`, `.cursor/skills/agent-flow/`, and `scripts/check_doc_links.py` into the target repo (merge carefully if those paths already exist).
2. Rewrite stubs with project vocabulary. Keep mocked examples only in checked-in docs.
3. Point agents at [docs/README.md](docs/README.md) and [AGENTS.md](AGENTS.md).
4. Run `python scripts/check_doc_links.py` after doc edits.

## Changelog

- 2026-10-27 (0.3.0): the Architect owns the docs tree (asks channel removed); opt-in concurrent slices (NOW board + `slices/` cards); `agent-flow` plan mode; usage log. Full history: [CHANGELOG.md](CHANGELOG.md).

## License

MIT. See [LICENSE](LICENSE).
