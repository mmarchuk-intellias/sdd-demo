---
id: ADR-004
type: adr
title: Amperlane owns the slot calendar; a charger reservation is only a short-lead station hold
status: approved
owner: Mykola Marchuk
version: 1
kyiv: null
parents: []
sources: [SRC-C2@00:07:35, SRC-C2@00:08:09, SRC-C2@00:08:48, SRC-C2@00:13:32, SRC-C2@00:26:27, SRC-C2@00:26:34, SRC-C2@00:56:15, SRC-C2@00:56:43, CTX-088]
decided_by: Proposed by Olena Marchuk (Intellias); agreed by Ravi Menon (Amperlane CTO)
---
# ADR-004 · Amperlane owns the slot calendar; a charger reservation is only a short-lead station hold

## Context
The brief assumed "real-time reservation on every charger via OCPP" (SRC-D1#9). In OCPP, reservations are optional and
can be rejected, and ReserveNow means "hold from now until expiry", not a future slot (SRC-C2@00:07:35,
SRC-C2@00:08:09). OCPI 2.2.1 RESERVE_NOW has the same semantics (SRC-C2@00:26:05). Only 10 of 16 chargers at one
of three sites accept reservations (CF-002).

## Decision
- The slot calendar (bookable capacity per site and time) lives in Amperlane's platform and is the system of record
  for bookings.
- Chargers receive at most a "hold now" (ReserveNow), about 15 minutes before the slot, where the EVSE supports it
  (A-002). Elsewhere the platform keeps a soft hold, with signage, the attendant or ops as fallback.
- The slot and booking model is designed so it can map onto the OCPI 2.3 Booking module later.

## Status in the sources
Proposed by Intellias (SRC-C2@00:08:48). The CTO: "Our own model, designed so it maps onto 2.3 Booking later"
(SRC-C2@00:13:32); "So whatever happens, the calendar is ours… That's the IP." (SRC-C2@00:26:27). The closing recap,
"Amperlane owns the calendar; ReserveNow only as a hold about fifteen minutes before", was confirmed by the CTO: "Yep,
that's it." (SRC-C2@00:56:15, SRC-C2@00:56:43). The exact lead time stays an assumption (A-002).

## Consequences
- The engine needs a "station hold failed" path (SRC-C2@00:09:34).
- The guarantee differs by supply pattern (design.md §3).
