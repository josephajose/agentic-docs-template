---
name: agent-flow
description: Maintain the lean agent workflow (lanes, NOW / optional board + slice cards, phase docs, decisions log, usage log). Modes - open (claim a slice or start ops, log start) | close (after the slice PR merges - tick, record, log end, offer plan) | plan (write the next NOW or Ready cards) | optimize (rotate DECISIONS, shrink docs) | audit (broken links, size drift). Use when the user types /agent-flow, starts a slice or ops fix, closes or plans a slice, or says docs/context are growing.
---

# agent-flow

Lanes live in [AGENTS.md](../../../AGENTS.md). Process files: [docs/3-engineering/process/](../../../docs/3-engineering/process/). Keep preloaded files (AGENTS.md, NOW, a card) short; everything else is on demand.

## NOW modes

- **Sequential** (default): [NOW.md](../../../docs/3-engineering/process/NOW.md) holds one slice inline (scope, **Facts**, **Done when**).
- **Parallel** (opt-in, for cloud agents or concurrent IDE chats): NOW becomes a board (`## Active`, `## Ready`, `## Last closed`), one line per slice: `- <id> | <source: phase N / ops / backlog> | <owner ide|bc-…> | feature/<id> | slices/<file>.md | <in progress / PR open / in UAT / accepted>`. Each slice has a card in [process/slices/](../../../docs/3-engineering/process/slices/README.md); a slice agent reads only its card and edits only its own board line. Cards are deleted at close, when the PR merges.
- **Only one slice with a DB migration in flight at a time.**
- **Usage-log line** ([usage-log.md](../../../docs/3-engineering/process/usage-log.md)): `- <id> | <slice|ops|uat> | <owner ide|bc-…> | open <YYYY-MM-DD HH:MM TZ> | close <… or —> | model <name or auto>`.

## open

`/agent-flow open <slice|ops|uat> <id>` at the start of a new chat.

1. **Claim (parallel, slice only):** move the card's line from Ready to Active with owner (`ide` or your `bc-…` id), branch `feature/<id>`, status `in progress`. For cloud agents the Architect adds the line at launch. Already claimed → stop and say so.
2. **Log:** append the usage-log line with `close —` (local clock: `date '+%Y-%m-%d %H:%M %Z'`). It rides with the session's first commit.
3. Load the lane (slice → NOW or your card; ops → AGENTS.md only), confirm lane and id in one line, start.

## close

Run when the slice PR **merges** (as the last commit on that PR). Same chat that did the work if possible.

1. Confirm **Done when** is fully checked; if not, list what is left and stop.
2. Summarize what shipped (3–6 bullets; Planning: decisions, not code).
3. **Record:** phase slice → tick the phase doc and add a `Closed log` line with the PR link; ops/backlog work → a dated line at the top of DECISIONS with the PR link. Leftovers → BACKLOG rows. Phase exit criteria done → flush unfinished items to BACKLOG; don't auto-start the next phase.
4. **Release:** sequential → replace the inline slice with a one-line Last closed note. Parallel → move the board line to Last closed (keep ~3) and delete the card. Abandoned slice → back to Ready, or a BACKLOG row.
5. Run **optimize** if DECISIONS is over its cap, then **audit**.
6. **Log last:** replace `close —` on this session's line with the close time (no open line → add one marked `open ?`).
7. Offer **plan next**. Close never writes the next NOW.

**Ops sessions:** do only step 6, committed with the fix.

## plan

Architect or a planning session. Read ROADMAP, the open phase's slices table and the relevant BACKLOG section only.

- **Sequential:** write the next inline NOW (product slice with Facts + Done when, a Planning NOW, or an ops-only note).
- **Parallel:** write Ready cards from the [card template](../../../docs/3-engineering/process/slices/README.md), one Ready line each with ordering notes; mark parallel-safe slices; respect the one-migration rule.
- **Phase slices tables:** include a `Parallel-safe` column (yes / no + why, e.g. "no: migration", "after N.A"). Don't rewrite closed phase docs.

## optimize

- DECISIONS over **15** entries → move the oldest to DECISIONS-archive. First copy any fact the active slice needs into NOW / its card / the phase doc.
- Trim history out of NOW (it belongs in phase Closed logs).

## audit

- `python scripts/check_doc_links.py`; fix broken links.
- Flag NOW or a card that has grown past roughly a page, or a NOW/card without **Done when**.
