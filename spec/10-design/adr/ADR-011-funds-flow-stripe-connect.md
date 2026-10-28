---
id: ADR-011
type: adr
title: If money flows through Amperlane, it flows through Stripe Connect (conditional)
status: approved
owner: Mykola Marchuk
version: 1
kyiv: null
parents: []
sources: [SRC-C2@00:45:33, SRC-C2@00:45:58, SRC-C2@00:46:21, SRC-C2@00:47:10, SRC-C2@00:56:15, SRC-C2@00:56:43, CTX-106, CTX-128]
decided_by: Proposed by Andriy Bondar (Intellias); confirmed by Ravi Menon (Amperlane CTO) in the Call 2 recap
---
# ADR-011 · If money flows through Amperlane, it flows through Stripe Connect (conditional)

## Context
Amperlane runs on Stripe Billing today, with no Connect (SRC-C2@00:03:28). In options B and C of the business model,
fleets pay Amperlane and Amperlane pays stations (CF-008). The CTO does not want Amperlane to need a money-transmitter
licence (SRC-C2@00:45:17).

## Decision (conditional)
**Applies only if** the business model puts Amperlane in the money flow (Q-001), **and** Amperlane's counsel confirms
the structure (Q-019):
- Stations are connected accounts on Stripe Connect; Stripe holds and moves the funds, and Amperlane takes its margin as
  the platform. Money never sits in Amperlane's own bank account (SRC-C2@00:45:33).
- The charge type is separate charges and transfers, because one fleet invoice covers sessions at many stations
  (SRC-C2@00:45:58).
- Fleets get net-30 invoices through Stripe Invoicing, and stations get weekly transfers (SRC-C2@00:46:21).
- The payment provider sits behind an interface (ADR-003); Adyen for Platforms remains an alternative "only for pricing
  at scale" (SRC-C2@00:47:10).

## Status in the sources
The closing recap included "Stripe Connect with weekly payouts and net-30 invoicing", and the CTO confirmed: "Yep,
that's it." (SRC-C2@00:56:15, SRC-C2@00:56:43). The CTO named the weekly cadence (SRC-C2@00:46:21).

## Consequences
- If the business model leaves energy money between drivers and stations, as in the pilot, this ADR does not apply,
  and Stripe stays limited to invoicing.
- If it applies, there is a cash gap (CF-024, Q-021).
