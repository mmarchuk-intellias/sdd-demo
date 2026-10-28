---
id: ADR-013
type: adr
title: Uber and Lyft are integrated through deep links only in the MVP
status: approved
owner: Mykola Marchuk
version: 1
kyiv: null
parents: []
sources: [SRC-C2@00:42:43, SRC-C2@00:43:07, SRC-C2@00:43:30, SRC-C2@00:56:15, SRC-C2@00:56:43, CTX-023, CTX-098]
decided_by: Proposed by Andriy Bondar (Intellias); accepted by Ravi Menon (Amperlane CTO)
---
# ADR-013 · Uber and Lyft are integrated through deep links only in the MVP

## Context
The brief wanted "Uber / Lyft driver apps: deep link + data" (SRC-D1#10), so that a slot could be offered when a trip
ends. The Uber Driver API is limited-access and has no vehicle or EV data, and Lyft has no public driver or fleet API
(SRC-C2@00:42:43).

## Decision
In the MVP, the platform exchanges no data with Uber or Lyft. SMS opens Amperlane; Amperlane opens navigation or returns
the driver to the ride-hail app. Context such as "trip ended" comes from the driver.

## Status in the sources
The CTO: "Okay." (SRC-C2@00:43:30). The closing recap, "Deep links only for Uber and Lyft", was confirmed: "Yep, that's
it." (SRC-C2@00:56:15, SRC-C2@00:56:43).

## Consequences
- Driver-side signals (battery, arrival) come from telematics, the driver, QR codes or the CSMS, never from the
  ride-hail apps.
