---
id: ADR-002
type: adr
title: A modular monolith, not microservices
status: approved
owner: Mykola Marchuk
version: 1
kyiv: null
parents: []
sources: [SRC-C2@00:54:21, SRC-C2@00:54:45, SRC-C2@00:54:57, CTX-007, CTX-087]
decided_by: Proposed by Olena Marchuk (Intellias); agreed by Ravi Menon (Amperlane CTO)
---
# ADR-002 · A modular monolith, not microservices

## Context
The platform will be run by a small team: Amperlane has two engineers. "With two engineers, twelve services is twelve
pagers" (SRC-C2@00:54:57).

## Decision
Build the core as one deployable modular monolith, with clear module seams (inventory, booking and calendar, fleet and
vehicles, pricing, settlement, notifications, identity, audit), so modules can be split out later if needed.

## Status in the sources
Proposed by Intellias (SRC-C2@00:54:21). The CTO said: "Modular monolith — thank you. I was afraid of twelve services."
(SRC-C2@00:54:45).

## Consequences
- Module boundaries are enforced in code (no cross-module table access); the code conventions belong in the
  constitution (Step 2.2).
- The framework (NestJS in SRC-D2#10) is a proposal and not part of this decision.
