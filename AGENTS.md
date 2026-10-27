# Agents

Stack-agnostic agent rules for this repository. Prefer finishing the active slice over expanding scope.

Docs: [docs/README.md](docs/README.md) — layers `1-domain` → `2-system` → `3-engineering`. The Architect (docs-owner agent) owns the docs tree and pushes docs directly; you update docs when your work changes them (`agent-flow close` for slices, with the fix for ops). The owner confirms.

## Lanes (pick one first)

| Lane | When | Load |
|---|---|---|
| **Ops** (default) | Bug/tweak on shipped work, questions, not the active slice, or "ops" | This file + files you touch. No NOW or phase docs. |
| **Slice** | "continue / NOW / the slice" | `docs/3-engineering/process/NOW.md` only (parallel mode: your card only). Product: implement. Planning: docs only unless **Done when** says otherwise. Phase doc only if NOW names an open phase. |
| **Close / plan next** | Slice PR merged, or "close / plan next" | skill `agent-flow` → `close`, then `plan`. |

- Ops that becomes a feature (new screen, schema, service, multi-slice) → switch to Slice or add a BACKLOG row.
- **Workflow:** skill [`agent-flow`](.cursor/skills/agent-flow/SKILL.md).
- **New chat:** `/agent-flow open <slice|ops> <id>` logs the start in [usage-log.md](docs/3-engineering/process/usage-log.md); `/agent-flow close` logs the end (ops too).
- **Check gate:** code and product changes: branch `feature/<id>` + PR (no direct `main`); Architect docs pushes go direct. `python scripts/check_doc_links.py` after doc edits.

## Always

- Open one doc when the change needs it. Do not preload the whole tree.
- Mocked examples only in checked-in docs. Never commit secrets or personal data.

## Traceability

- Features: `Implements: 1-domain/...`
- Phases: `Delivers: 2-system/...`
