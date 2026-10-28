---
id: ADR-007
type: adr
title: Booking timers and sagas run as durable workflows on Temporal
status: approved
owner: Mykola Marchuk
version: 1
kyiv: null
parents: []
sources: [SRC-C2@00:33:32, SRC-C2@00:33:51, SRC-C2@00:34:04, CTX-094]
decided_by: Proposed by Olena Marchuk (Intellias); agreed by Ravi Menon (Amperlane CTO)
---
# ADR-007 · Booking timers and sagas run as durable workflows on Temporal

## Context
Every booking has timers: hold expiry, reminder, the T-15 station hold, the T-10 check, grace and auto-release.
Faults trigger multi-step rebooking with compensation. Releases are done by hand today (CTX-046).

## Decision
Model each booking as a small long-running workflow with timers and compensations on Temporal, not cron jobs.

## Status in the sources
Proposed by Intellias (SRC-C2@00:33:32). The CTO: "We used Temporal for payouts at my last job. Fine. Self-host,
though — no extra vendor contract in year one if we can avoid it." (SRC-C2@00:33:51).

## Open points
- Self-hosted or Temporal Cloud: Intellias costs both (SRC-C2@00:34:04, Q-026). Working assumption A-029: self-hosted.
