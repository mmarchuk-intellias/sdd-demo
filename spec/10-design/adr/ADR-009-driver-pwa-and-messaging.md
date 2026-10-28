---
id: ADR-009
type: adr
title: Drivers use a mobile web app (PWA) and SMS/WhatsApp; no native app in the MVP
status: approved
owner: Mykola Marchuk
version: 1
kyiv: null
parents: []
sources: [SRC-C1@00:05:47, SRC-C1@00:06:33, SRC-C2@00:51:10, SRC-C2@00:51:22, SRC-C2@00:51:29, CTX-027, CTX-096, CTX-097]
decided_by: Dana Whitfield (Amperlane CEO) on Call 1; confirmed on Call 2 (Ravi Menon reporting the CEO's agreement)
---
# ADR-009 · Drivers use a mobile web app (PWA) and SMS/WhatsApp; no native app in the MVP

## Context
The brief planned native iOS and Android apps (SRC-D1#9, SRC-D1#11). The drivers have Uber and Lyft open all day and
will not download an app, create an account and add a card. They will text, or tap a link to a light browser page
(SRC-C1@00:05:47).

## Decision
For the MVP, the driver channel is a light mobile web app (PWA), reached through SMS and WhatsApp messages and links,
in English, Spanish and Bengali. Native apps move to Phase 2.

## Status in the sources
The CEO: "Honest answer is light mobile web plus messaging." (SRC-C1@00:06:33). Intellias restated it on Call 2
(SRC-C2@00:51:10), and the CTO confirmed: "Dana was a bit sad about the native app, but she agreed."
(SRC-C2@00:51:22). Native app in Phase 2 (SRC-C2@00:51:29).

## Open points
- How a driver is identified without an account: A-006, Q-028.
- The WhatsApp setup with Twilio: Q-034.
