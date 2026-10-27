# Docs map

> **Agents: do not preload.** Open one doc when the change needs it. Open `3-engineering/process/` only in slice / close / inbox / planning lanes (see [AGENTS.md](../AGENTS.md)).

## Layers

Docs are split into three layers. Each layer drives the one below it.

1. [1-domain/](1-domain/README.md): how the work is done with no software at all. Vocabulary, rules, and decision records (DR-NN) in `1-domain/decisions/`. Cross-layer gaps: [alignment-register.md](1-domain/alignment-register.md).
2. [2-system/](2-system/README.md): how software is designed to automate the domain. Architecture, features, contracts, technical notes, and ADRs in `2-system/decisions/`.
3. [3-engineering/](3-engineering/README.md): how the software gets built. Process (NOW, BACKLOG, DECISIONS, ROADMAP, usage log, optional slice cards) and phases.

Code is the source of truth for behavior. These docs define intent, structure, and rules.

## Traceability rule

- Core system features cite their source: `Implements: 1-domain/...`.
- Phases cite what they deliver: `Delivers: 2-system/...`.
- Exempt (no upstream source needed): `2-system/technical/` and engineering work such as testing, ops, and refactoring.

## Ownership

Docs use roles, never personal names.

- **The owner:** confirms domain rules and product direction, gives final confirmation on docs changes, merges PRs.
- **The Architect (docs-owner agent):** owns the whole docs tree, structure and content, and pushes docs changes directly. Follow-ups land straight in the right doc (BACKLOG, phase, ADR).
- **Project agents (IDE and cloud):** work through the process docs ([AGENTS.md](../AGENTS.md) lanes, skill `agent-flow`) and update docs when their work changes them: `agent-flow close` for slices, alongside the fix for ops. They propose domain changes rather than editing domain rules directly.
