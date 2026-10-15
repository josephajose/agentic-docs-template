# Agents

Stack-agnostic agent rules for this repository. Prefer finishing the active slice over expanding scope.

Docs map: [docs/README.md](docs/README.md) — layers `1-domain` → `2-system` → `3-engineering`.

## Lanes (pick one first; minimize context)

- **Planning:** doc edits only unless NOW's Done-when checklist says otherwise. Read [docs/3-engineering/process/NOW.md](docs/3-engineering/process/NOW.md) and the cited domain/system docs.
- **Product (slice):** implement only the active NOW unit. Do not edit NOW, BACKLOG, DECISIONS, phase docs, this file, or `.cursor/` unless the brief explicitly lists them.
- **Ops:** skip NOW; follow ops runbooks if present.

## Always

- Open one doc when the change needs it. Do not preload the whole tree.
- Mocked examples only in checked-in docs. Never commit secrets or personal data.
- Relative links must resolve: `python scripts/check_doc_links.py`.
- Prefer branch + PR for product code. Workflow-doc updates (NOW / DECISIONS close-out) belong to whoever owns the docs process after merge.

## Traceability

- Features: `Implements: 1-domain/...`
- Phases: `Delivers: 2-system/...`
