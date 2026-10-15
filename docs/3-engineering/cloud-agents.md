# Cloud coding agents (optional pattern)

Use when a hosted coding agent should implement a NOW slice with minimal real-time management.

## Defaults

- Work on a **branch + PR** only. Never merge; never push to the default branch.
- **Mocked / synthetic data only** in the brief and in commits.
- Do **not** edit NOW, BACKLOG, DECISIONS, phase docs, `AGENTS.md`, or `.cursor/` unless the brief lists them. The docs owner applies workflow close-out after merge.
- Cap work with a **tool-call budget** (project-chosen; example default **100 tool calls**). Put the number in the brief and require an honest count in the PR body. Near the cap, stop and open/update the PR with what is done. Treat this as a soft stop until Cursor exposes a hard kill; steer if the agent overruns. Ask the agent to report the actual count; treat brief step hints as soft.
- Open the PR as **draft**; the docs owner marks it ready after review.
- Prefer a PR-comment loop: the owner comments on the PR; a watcher forwards comments to the agent and only pings chat when ready to merge or blocked.

## Brief checklist

- Allowed paths
- Forbidden paths
- Done-when items copied from NOW
- Test commands to run
- Tool-call budget (project-chosen; example default 100) and “stop and PR what you have” rule
- Explicit “leave X for the owner” items (manual spot-checks)

## After merge

1. Docs owner updates NOW / DECISIONS.
2. Owner runs any local spot-checks the brief left unchecked.
3. Close the slice when Done-when is complete.

## Why tool calls (for now)

Cursor’s usage % is what we can see after a run. We cannot read token or dollar totals from here, and the agent often misreports “steps.” Tool calls are countable in the transcript and correlated enough to set a budget. Recalibrate the default whenever a run’s call count and your usage-% delta are both known. Prefer a token or $ cap if Cursor later exposes one we can enforce.
