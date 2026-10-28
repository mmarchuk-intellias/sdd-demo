---
id: ADR-005
type: adr
title: Book against a pool of compatible EVSEs; assign the EVSE late
status: approved
owner: Mykola Marchuk
version: 1
kyiv: null
parents: []
sources: [SRC-C2@00:24:04, SRC-C2@00:24:36, SRC-C2@00:24:52, SRC-C2@00:24:59, CTX-066, CTX-092]
decided_by: Proposed by Olena Marchuk (Intellias); agreed by Luis Ortega (Amperlane COO)
---
# ADR-005 · Book against a pool of compatible EVSEs; assign the EVSE late

## Context
Stations never bump a walk-up. If the intended stall is taken, the booking must move to another free stall at the site
(SRC-C2@00:24:04). Drivers "don't care about stall 4. They care about plugging in." (SRC-C2@00:24:52).

## Decision
A booking reserves capacity in the pool of compatible EVSEs at a site for a time window. A specific EVSE is assigned
late, "around T-minus-fifteen", and can be reassigned before arrival. The exact timings, including a check at T-10 for
an EVSE still in a session, are Intellias' starting values and not part of this decision (A-002).

## Status in the sources
Proposed by Intellias (SRC-C2@00:24:36), agreed by the client's COO (SRC-C2@00:24:52). Intellias notes that it also
reduces contention: "fewer hot rows" (SRC-C2@00:24:59).

## Consequences
- Accepting a booking needs a capacity check that knows connector and adapter compatibility and power, not just counts
  (A-014, design.md §6 item 1).
- The EVSE-level exclusion constraint (ADR-006) applies at allocation.
- Drivers see a site and a time, not a stall number, until allocation.
