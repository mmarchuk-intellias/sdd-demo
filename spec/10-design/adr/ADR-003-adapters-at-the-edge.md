---
id: ADR-003
type: adr
title: External vendors behind adapters; no vendor SDK in the booking core
status: approved
owner: Mykola Marchuk
version: 1
kyiv: null
parents: []
sources: [SRC-C2@00:06:50, SRC-C2@00:07:08, SRC-C2@00:47:10, CTX-086]
decided_by: Ravi Menon (Amperlane CTO)
---
# ADR-003 · External vendors behind adapters; no vendor SDK in the booking core

## Context
Stations use different CSMS products (AMPECO, ChargeLab, a legacy ChargePoint contract) and may switch. The CTO
does not want vendor lock-in: "If a station switches CSMS tomorrow, I want to swap an adapter, not rewrite the engine."
(SRC-C2@00:06:50).

## Decision
Every external system (CSMS APIs, OCPI peers, telematics, payments, messaging, maps) is reached through an adapter at
the edge. Adapters translate to and from the platform's own domain model. The booking core never imports a vendor SDK
or uses vendor data types.

## Status in the sources
Stated by the client's CTO (SRC-C2@00:06:50); Intellias confirmed: "adapters at the edge" (SRC-C2@00:07:08). The same
applies to the payment provider ("the provider sits behind an interface anyway", SRC-C2@00:47:10).

## Consequences
- The three supply patterns (A/B/C) differ only inside adapters and the station-hold step (design.md §3).
- Adapters handle duplicate and out-of-order webhooks idempotently, with polling for reconciliation (CTX-091).
