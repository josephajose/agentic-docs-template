# Cloud coding agents (optional pattern)

Use when a hosted coding agent should implement a NOW slice with minimal real-time management.

## Defaults

- Work on a **branch + PR** only. Never merge; never push to the default branch.
- **Mocked / synthetic data only** in the brief and in commits.
- Do **not** edit NOW, BACKLOG, DECISIONS, phase docs, `AGENTS.md`, or `.cursor/` unless the brief lists them. The docs owner applies workflow close-out after merge.
- Cap work with a **tool-call budget** (project-chosen). Ask the agent to report the actual count; treat brief step hints as soft.
- Open the PR as **draft**; the docs owner marks it ready after review.
- Prefer a PR-comment loop: the owner comments on the PR; a watcher forwards comments to the agent and only pings chat when ready to merge or blocked.

## Brief checklist

- Allowed paths
- Forbidden paths
- Done-when items copied from NOW
- Test commands to run
- Tool-call budget and “stop and PR what you have” rule
- Explicit “leave X for the owner” items (manual spot-checks)

## After merge

1. Docs owner updates NOW / DECISIONS.
2. Owner runs any local spot-checks the brief left unchecked.
3. Close the slice when Done-when is complete.
