---
id: ADR-008
type: adr
title: Money is recorded in a double-entry, append-only ledger
status: approved
owner: Mykola Marchuk
version: 1
kyiv: null
parents: []
sources: [SRC-C2@00:46:23, SRC-C2@00:46:41, SRC-C2@00:46:46, SRC-C2@00:48:32, CTX-095, CTX-126, CTX-129]
decided_by: Ravi Menon (Amperlane CTO) for double-entry; "append-only" proposed by Andriy Bondar (Intellias), the CTO did not object; accepted at Gate 1 (Mykola Marchuk, 2026-10-28)
---
# ADR-008 · Money is recorded in a double-entry, append-only ledger

## Context
Every candidate business model has money owed, paid and outstanding per fleet, with stations potentially paid weekly
while fleets pay net-30 (SRC-C2@00:46:23). The CTO has "scars" from reconciliation on payouts (SRC-C2@00:01:07).

## Decision
Record all monetary facts in a double-entry, append-only ledger, not in "balance" columns. Corrections are new
entries; nothing is updated in place.

## Status in the sources
The CTO decided "double-entry": "We'll need a real ledger. Double-entry, not 'balance' columns." (SRC-C2@00:46:41).
"Append-only" was added by Intellias, "Agreed — double-entry, append-only." (SRC-C2@00:46:46), and the CTO did not
respond to that part.

Gate 1 decision (Mykola Marchuk, 2026-10-28): append-only is treated as part of the decision. The CTO did not object,
and recording corrections as new entries follows from a double-entry ledger.

## Consequences
- The ledger is designed generically now; the accounts, charges and flows that depend on the business model wait for
  Q-001 (SRC-C2@00:48:32).
- No-show fees are separate lines from energy, so they can be reversed alone (CTX-127).
