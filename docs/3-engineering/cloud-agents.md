# Cloud coding agents (optional pattern)

Use when a hosted coding agent should implement a whole NOW slice with minimal real-time management. The owner is involved only at the end: one PR, pulled and tested locally, then merged.

## Roles

- **Owner** — merges, does the final local test, and approves anything hard to undo.
- **Coordinator** (docs owner or architect agent) — writes the brief, answers the agent's questions, reviews the PR, marks it ready, and closes out the docs after merge.
- **Cloud agent** — implements on a branch and opens one PR.

## Defaults

- Work on a **branch + PR** only. Never merge; never push to the default branch.
- **Mocked / synthetic data only** in the brief and in commits. No secrets or real account data.
- Do **not** edit NOW, BACKLOG, DECISIONS, phase docs, `AGENTS.md`, or `.cursor/` unless the brief lists them. The coordinator applies workflow close-out after merge.
- **One full PR per slice.** Aim to meet every Done-when item in one PR so the owner tests once.
- **Blockers:** the coordinator answers questions. A soft blocker becomes a follow-up listed in the PR body and moves to the next slice. Stop only for a major blocker that would be very hard to undo.
- **Budget (soft):** a project-chosen tool-call budget per run (example default **500**). Put it in the brief and require an honest count in the PR body. Near the soft cap, finish if Done-when is nearly met; otherwise stop and update the PR with what is done.
- **Budget (hard):** a ceiling (example **2000** tool calls) where the agent **stops and asks the coordinator to continue**. The coordinator checks with the owner before authorizing another run.
- **Context economy (keeps quality, cuts tokens):** search before reading (`rg`, then read only the needed line ranges; don't re-read a file you already read unless it changed). Run **targeted** tests for touched modules while iterating, and the full suite once before each push. Filter long command output or write it to a file and read the tail; never dump full logs. On follow-up runs, work from the PR diff plus the owner's comment instead of re-exploring the repo.
- **Fresh agent for big new rounds.** Every step re-reads the agent's whole conversation (cache reads), so a long fix session gets more expensive per step. Small fixes can go to the same agent; for a big new round of changes, start a fresh agent with a short brief.
- Open the PR as **draft**; the coordinator marks it ready after review.
- Prefer a PR-comment loop: the owner comments on the PR, the agent fixes, and chat pings happen only for merge-readiness, owner-only decisions, or budget overruns.

## Brief checklist

- Goal in user-visible terms, and links to the source-of-truth docs (NOW, phase, ADR)
- Architecture constraints the agent must keep
- Allowed paths and forbidden paths
- Done-when items copied from NOW
- Test commands to run
- Soft and hard tool-call budgets, plus the stop rules above
- The context-economy rule, pasted verbatim
- Out-of-scope list (next slices)
- Explicit “leave X for the owner” items (manual spot-checks), and a local test plan in the PR body

## After merge

1. Coordinator updates NOW, phase, and ADR checklists, and lists the soft follow-ups under Last closed.
2. Owner runs any local spot-checks the brief left unchecked.
3. Close the slice when Done-when is complete.
4. Coordinator appends one rollup line to a local usage log (below).

## Usage rollup (local, not in git)

Purpose: when the tool's usage % jumps, scan one file to see which agent run used it.

- Kept off-repo by the coordinator; cloud agents never touch it.
- One line per closed run, or one rollup line for a multi-run feature. No per-tool rows.
- Line shape: `date | agent id | PR | short name | calls (approx) | usage% before→after | Δpp | model | notes`
- Add a line only when the call count or usage % change is known; backfill later otherwise.

## Why tool calls (for now)

Usage % is what we can see after a run. Token or dollar totals usually aren't readable, and agents often misreport "steps." Tool calls are countable in the transcript and track usage well enough to set a budget. Recalibrate the soft and hard numbers whenever a run's call count and usage-% change are both known. Switch to a token or dollar cap if the tool ever exposes one that can be enforced.

## Reference calibration

One real run: an end-to-end feature slice used about 250 tool calls in its first run, and usage rose about 1 point. Owner-driven fix runs on the same PR added about 2 more points, with millions of tokens, mostly cache reads. That is why the context-economy and fresh-agent rules exist.
