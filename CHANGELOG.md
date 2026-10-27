# Changelog

Template versions. Projects that applied an earlier version can use this to pull forward.

## 0.3.0 — 2026-10-27

- Roles: the Architect (docs-owner agent) owns the whole docs tree and pushes docs directly; the owner confirms; project agents update docs through the process docs. Removed `docs/3-engineering/architect/` (asks/replies channel) and its references.
- New `.cursor/skills/agent-flow/` skill: open (claim + log start), close (on PR merge; log end; offers plan next, no longer writes NOW), plan, optimize, audit. NOW modes: sequential default; opt-in parallel board with `process/slices/` cards (template only), one DB migration in flight, `Parallel-safe` column in the phase slices table.
- New `process/usage-log.md` (owner field; slice|ops|uat). AGENTS.md: lanes table, New chat line, check gate (code via `feature/<id>` PR; Architect docs pushes direct). Cloud agents: card is the brief; `bc-…` id on the board line.

## 0.2.0 — 2026-10-15

- Cloud-agents pattern validated on a real end-to-end slice. Adds roles (owner, coordinator, agent), one full PR per slice, a blocker policy (soft blockers become follow-ups), soft and hard tool-call budgets (example 500 / 2000), a context-economy rule, fresh-agent guidance for long fix rounds, a richer brief checklist, and a local usage rollup.

## 0.1.1 — 2026-10-15

- Cloud-agents pattern: keep budget project-chosen; document an example default of 100 tool calls in the budget bullet and brief checklist; add “Why tool calls (for now)” guidance.

## 0.1.0 — 2026-10-15

- Initial public seed: three-layer docs map, process stubs, ADR/DR/rule/feature/phase templates, AGENTS.md lane sketch, link checker, optional cloud-agent brief pattern.
