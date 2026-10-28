---
id: ADR-006
type: adr
title: No double booking, enforced by the database; per-site serialisation and idempotency keys
status: approved
owner: Mykola Marchuk
version: 1
kyiv: null
parents: []
sources: [SRC-C2@00:31:16, SRC-C2@00:31:45, SRC-C2@00:31:51, SRC-C2@00:32:16, SRC-C2@00:32:46, SRC-C2@00:32:51, SRC-C2@00:33:05, SRC-C2@00:33:15, SRC-C2@00:56:15, SRC-C2@00:56:43, CTX-093, CTX-115]
decided_by: Proposed by Olena Marchuk and Andriy Bondar (Intellias); agreed by Ravi Menon (Amperlane CTO)
---
# ADR-006 · No double booking, enforced by the database; per-site serialisation and idempotency keys

## Context
At the 4–5 PM shift change, about 400 booking attempts in 10 minutes compete for a few stalls. The problem is
contention, not throughput (CTX-115). Drivers retry on bad mobile connections, and today the SMS bot sometimes
processes a message twice (CTX-044).

## Decision
1. **Correctness in the database.** An allocation row holds the EVSE id and the time range. A PostgreSQL exclusion
   constraint rejects overlapping active allocations on the same EVSE, "and it doesn't depend on our code being
   correct" (SRC-C2@00:31:16).
2. **Fairness at burst time.** A single-writer queue per site processes competing requests in order, so the requests
   that lose get an instant alternative instead of an error (SRC-C2@00:32:16).
3. **Idempotency.** Every booking request carries an idempotency key; inbound SMS/WhatsApp messages are deduplicated by
   the provider's message id (SRC-C2@00:32:51, SRC-C2@00:33:15).

Illustration of the constraint (an example, not the final schema):

```sql
ALTER TABLE evse_allocation ADD CONSTRAINT one_car_per_evse
  EXCLUDE USING gist (evse_id WITH =, slot WITH &&) WHERE (active);
```

## Status in the sources
The CTO: "Yes. That's what I want." (SRC-C2@00:31:45); "Belt and braces. I can live with that." (SRC-C2@00:32:46);
"I'd have fired someone for not doing that." (SRC-C2@00:33:05).

The closing recap, "No double booking, enforced in Postgres", was confirmed by the CTO (SRC-C2@00:56:15,
SRC-C2@00:56:43).

## Scope of what was agreed
The CTO agreed to an EVSE-level exclusion constraint over held and confirmed bookings (SRC-C2@00:31:51). Under
ADR-005, held and confirmed bookings have no EVSE until allocation (around T-15), so the constraint can only bite at
allocation. **Before allocation, the only protection is a capacity check per site and time slot** (the "capacity
bucket" in SRC-D2#12, assumption A-014). That check is Intellias' design and has **not** been agreed with the client.
Per the Gate 1 decision, it is prototyped and simulated in Phase 0 and shown to the CTO there, not before (CF-023).

## Open points
- Whether holds are rows under the same constraint or short-lived cache entries: CF-017, A-005.
- How capacity is counted before allocation, including adapters, power and buffers: A-014, CF-023.
