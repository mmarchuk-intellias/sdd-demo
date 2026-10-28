---
id: ADR-001
type: adr
title: TypeScript, PostgreSQL and AWS, in Amperlane-owned repositories and accounts
status: approved
owner: Mykola Marchuk
version: 1
kyiv: null
parents: []
sources: [SRC-C2@00:06:05, SRC-C2@00:06:41, SRC-C2@00:06:50, CTX-005, CTX-085]
decided_by: Ravi Menon (Amperlane CTO); ownership wording by Olena Marchuk (Intellias), accepted by the CTO
---
# ADR-001 · TypeScript, PostgreSQL and AWS, in Amperlane-owned repositories and accounts

## Context
Amperlane has two engineers and wants to own its platform outright. The CTO has seen startups "where the agency owns the
platform and the startup rents its own product" (SRC-C2@00:06:05). Amperlane holds $100k in AWS Activate credits.

## Decision
- Language: TypeScript end to end, "if we can".
- Database: PostgreSQL. Cloud: AWS.
- Code lives in Amperlane's repositories. Infrastructure is Amperlane's AWS accounts, defined in Amperlane's Terraform.
- Open source is used only where it is mature, never as "the first production user of somebody's weekend project".

## Status in the sources
The client's CTO stated the stack and the IP requirement (SRC-C2@00:06:05). The "code in your repos, your AWS accounts,
your Terraform" wording is Intellias' (SRC-C2@00:06:41), and the CTO accepted it: "Good." (SRC-C2@00:06:50).

## Consequences
- The data store must support the database-enforced invariants in ADR-006.
- The specific AWS services (ECS Fargate, RDS, ElastiCache/Valkey, EventBridge/SQS) are Intellias' proposals in SRC-D2#10
  and are not covered by this ADR.

## Open points
- PostGIS, and the managed-service choices: see design.md §2.5.
