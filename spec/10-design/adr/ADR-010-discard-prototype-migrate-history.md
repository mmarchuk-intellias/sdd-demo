---
id: ADR-010
type: adr
title: Discard the Supabase prototype; migrate the pilot history
status: approved
owner: Mykola Marchuk
version: 1
kyiv: null
parents: []
sources: [SRC-C2@00:04:20, SRC-C2@00:04:37, SRC-C2@00:04:43, SRC-C1@00:48:20, CTX-052, CTX-053]
decided_by: Ravi Menon (Amperlane CTO)
---
# ADR-010 · Discard the Supabase prototype; migrate the pilot history

## Context
A Next.js 14 + Supabase driver app is about 35% done, has no tests and never went to production. Its data model has no
EVSE or connector, and "a slot is a timestamp string" (SRC-C2@00:03:52, SRC-C2@00:04:20). A year of pilot history in
Airtable and Sheets is the only real dataset on fleet driver behaviour, and it will be in the Series A data room
(SRC-C2@00:04:43).

## Decision
- Start clean; do not build on the prototype. Keep its schema only for reference.
- Migrate the pilot history into the new platform properly, as mapped and cleaned records with provenance, "not a CSV
  dump in an S3 bucket".

## Status in the sources
The CTO: "I'd bin it. I'm not attached." (SRC-C2@00:04:20); "pilot history has to be migrated into whatever we build"
(SRC-C2@00:04:43). Also on Call 1: "I don't want to lose a year of bookings when we move." (SRC-C1@00:48:20).

## Open points
- Scope (how far back, which systems, cleansing level, what the data room needs): Q-020.
- Data quality: status values changed twice, moved bookings recorded as no-shows (CTX-054, CF-018).
