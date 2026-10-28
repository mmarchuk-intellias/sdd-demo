---
id: ADR-012
type: adr
title: Build SOC 2-ready from day one; the audit itself comes later
status: approved
owner: Mykola Marchuk
version: 1
kyiv: null
parents: []
sources: [SRC-C2@00:43:30, SRC-C2@00:43:54, SRC-C2@00:44:04, SRC-C2@00:44:25, CTX-078, CTX-107]
decided_by: Proposed by Olena Marchuk (Intellias); agreed by Ravi Menon (Amperlane CTO)
---
# ADR-012 · Build SOC 2-ready from day one; the audit itself comes later

## Context
A large rideshare platform's EV team wants SOC 2 Type I within 12 months of its pilot start, plus a pen test
(SRC-C2@00:43:30, SRC-C2@00:43:54). The target date is open (CF-016).

## Decision
Design and build the platform so that a SOC 2 Type I audit is a process exercise, not a rebuild: access control, audit
logging, change management, encryption, and a separate production account from day one. The audit, the auditor and
any compliance tool are on Amperlane's side.

## Status in the sources
Proposed by Intellias (SRC-C2@00:44:04). The CTO: "That's what I want. I don't want to find out in a year we need to
rewrite auth." (SRC-C2@00:44:25).

## Open points
- The target date, the auditor, and whether the rideshare pilot falls in Phase 1: Q-018.
