# Alignment register

- **Status:** Active | Idle
- **Scope:** gaps between a domain rule (`1-domain/`), its system feature (`2-system/features/`), and the code.

## Purpose

The domain drives the system, and the system drives the code. This register lists every place where the three disagree, or where a domain value is still undecided, so each gap can be settled one at a time, domain first.

## Workflow

1. Confirm or adjust the domain rule.
2. Update the domain doc.
3. Update the system feature to match.
4. Add a [BACKLOG](../3-engineering/process/BACKLOG.md) row (or a slice) for the code change.
5. Close the entry when domain, system, and code agree.

**Statuses:** Open, Domain confirmed, Domain adjusted, Trickled down, Closed.

**Gap types:** value mismatch; rule missing in code; code without domain rule; undefined domain input; doc-only conflict.

## Entries

### AL-001 *(title)*

- **Gap type:**
- **Domain says:**
- **System doc says:**
- **Code does:**
- **Risk:** High | Medium | Low
- **Proposed question:**
- **Status:** Open
