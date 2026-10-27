# Slice cards (parallel mode only)

Used only when NOW is a board (skill `agent-flow`, NOW modes). One card per Active or Ready slice, named `<id>-<slug>.md`. A slice agent reads only its own card; a cloud-agent brief references the card path instead of copying it. `plan` writes cards, `open` claims them, `close` deletes the card in the slice PR when it merges.

Keep cards short: facts the slice needs, not history. Only one slice with a DB migration in flight at a time.

## Template

```markdown
# <id> — <title>

- **Source:** phase N (slices table row) / ops / BACKLOG <section>
- **Owner:** ide | bc-… (set by `open`, or by the Architect at cloud launch)
- **Branch:** feature/<id>
- **Touches:** main modules / docs; **migration:** yes / no
- **Depends on:** <slice ids or "none">; parallel-safe: yes / no

## Scope

<2–4 lines; Out of scope if it helps>

**Facts:** <decisions and constraints the slice needs>

### Done when

- [ ] …
```
