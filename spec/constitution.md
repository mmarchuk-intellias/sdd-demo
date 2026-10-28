---
id: CONSTITUTION
type: constitution
title: Amperlane platform constitution
status: approved
owner: Mykola Marchuk
sources: [SRC-D1, SRC-C1, SRC-C2, SRC-D2, CTX-002, CTX-005, CTX-006, CTX-027, CTX-028, CTX-036, CTX-039, CTX-044, CTX-045, CTX-055, CTX-062, CTX-070, CTX-078, CTX-085, CTX-086, CTX-087, CTX-090, CTX-091, CTX-093, CTX-094, CTX-095, CTX-097, CTX-103, CTX-107, CTX-108, CTX-109, CTX-110, CTX-112, CTX-113, CTX-114, CTX-115, CTX-127, CTX-135, CTX-138, ADR-001, ADR-002, ADR-003, ADR-005, ADR-006, ADR-007, ADR-008, ADR-009, ADR-012]
parents: []
kyiv: null
version: 1
---
# Constitution

Step 2.2 (prompt P2.5). This file sets the rules that apply to every requirement, story, system story and task unless
an artefact states an override. Every rule says how it is checked: by a tool (CI, `tools/trace.py`, a test) or by a
named role at a gate.

- **Numbers** come from sources (`SRC-…`, `CTX-…`) only. Every other number or rule is an assumption (`A-###`).
  A-031 – A-045 are Intellias working assumptions proposed in Step 2 (2026-10-28), to be registered in
  [open-questions.md](01-context/open-questions.md); the earlier ones are as registered there.
- **"Intellias convention"** marks a rule Intellias proposes for the delivery team. It is not a client fact; the
  Amperlane CTO confirms or changes it in Phase 0.
- **Labels** N1…, R1…, D1…, SC1…, P1… are row labels inside this file, not artefact IDs. Cite them as "constitution N3".
- **Roles:** engagement lead, solution architect and tech lead are Intellias roles; "Amperlane CTO" is the client's
  technical decision maker ([stakeholders.md](01-context/stakeholders.md)).

## NFR baseline

Every story and system story inherits these targets. A story that needs a different target adds a section
"NFR overrides" listing the N label, the new target, the reason and its source or A-###. The solution architect
approves any relaxation at Gate 3. If a requirement in requirements.md and this table disagree, the difference is raised
at Gate 2; neither is changed silently.

| N | NFR | Baseline | Source or assumption | How it is checked |
|---|---|---|---|---|
| N1 | Station status freshness | For connected sites (a CSMS API or an OCPI peer), the status held for each EVSE is no older than 60 s. | CTX-112 (SRC-C2@00:49:22, SRC-C2@00:49:30), CTX-090. How age is measured, and CSMS outages: **A-031**. | Production metric "status age per EVSE" with an alert at 60 s (N21). A simulator test in CI changes an EVSE's status and asserts the platform holds it within 60 s. |
| N2 | Status age shown | Every view of EVSE or site status shows when it was observed. Status of a connected site older than 60 s is shown as stale. LIC shows "last updated by attendant at <time>". | CTX-112 (SRC-C2@00:49:30, SRC-C2@00:49:38), CTX-062; INV-9 in data-model.md. | End-to-end test per status view, including a stale case and the LIC case. |
| N3 | Booking API latency | p95 under 300 ms, including the shift-change burst and the database constraint check. | CTX-113 (SRC-C2@00:49:44, SRC-C2@00:49:48, SRC-C2@00:49:52). Which operations, measured where, over which window: **A-032**. | Load test (N6) per 10-minute window; production metric per hour with an alert (N21). |
| N4 | Availability | 99.9% between 05:00 and 01:00 Eastern time (America/New_York) for making bookings. Overnight bookings are allowed. No availability target between 01:00 and 05:00. | CTX-114 (SRC-C2@00:50:00, SRC-C2@00:50:06, SRC-C2@00:50:13); A-028 (CF-015 is needs-decision). Measurement: **A-033** (about 36 failed minutes allowed in a 30-day month). | Synthetic booking check every minute (A-033); monthly availability report to the Amperlane CTO. |
| N5 | Maintenance and timers | Planned downtime only between 01:00 and 05:00 ET; zero-downtime deployment is not required. During downtime, booking timers (hold expiry, reminder, T-15 hold, T-10 check, grace, auto-release) and notifications may fire late but are never lost; a late timer's effect is applied once. | A-028; CTX-094, ADR-007. | Deployment log: every change with downtime falls inside the window (tech lead, monthly). Staging test: stop the workflow engine and workers with timers pending, restart, assert each timer fired exactly once. |
| N6 | Burst and contention | Design load: about 400 booking attempts in 10 minutes around 4:30 PM ET (today's worst 10 minutes: 40–50 requests). Load test at 5×: 2,000 attempts in 10 minutes with heavy contention on a few sites. Contention, not throughput, is the risk. | CTX-115 (SRC-C2@00:15:32, SRC-C2@00:16:00, SRC-C2@00:34:07, SRC-C2@00:34:22), CTX-055, A-009. Contention profile, seeded volume and pass criteria: **A-034**. | Load test on staging before launch and before every release that changes booking, inventory or workflows (D6); report attached to the release. |
| N7 | No double booking | Zero overlapping active allocations on one EVSE, enforced by a PostgreSQL constraint and not only by code. Before allocation (about T-15), bookings are protected by a per-site capacity check (A-014, CF-023). | CTX-093, ADR-005, ADR-006 (SRC-C2@00:31:16, SRC-C2@00:31:45). | Integration test on real PostgreSQL: the constraint rejects an overlap. Load test (N6): zero overlaps. Daily production query: zero overlapping allocations, alert otherwise. |
| N8 | Idempotency | Every booking request carries an idempotency key: the same key gives the same result and one booking. Inbound SMS and WhatsApp messages are deduplicated by the provider's message id. | CTX-093 (SRC-C2@00:32:51, SRC-C2@00:33:15), CTX-044. How long keys are kept: **A-035**. | Contract tests replay every state-changing request and every inbound message. Production metric "duplicate confirmations" stays at zero (N21). |
| N9 | Webhooks and reconciliation | Every inbound webhook (CSMS, payments, messaging) may arrive twice or out of order. Consumers are idempotent, and a periodic poll reconciles: a webhook is never the only path. For station status, the poll interval keeps N1. | CTX-091 (SRC-C2@00:15:02, SRC-C2@00:15:14), ADR-003. | Contract tests per integration feed duplicated, reordered and dropped events and assert the final state. The solution architect checks at Gate 4 that each webhook-fed integration has a reconciliation task. |
| N10 | Durable timers | Booking timers and rebooking sagas run as durable Temporal workflows, never as cron jobs or in-process timers. | CTX-094, ADR-007 (SRC-C2@00:33:32, SRC-C2@00:33:51). | CI lint forbids schedulers outside the workflows code; workflow replay tests in CI. |
| N11 | Message dispatch | During the availability window, a driver message the platform originates is handed to Twilio within 10 s of its trigger at p95. Handset delivery is tracked, not targeted. | **A-036** (no source sets a number). Channels and provider: CTX-097. | Production metric trigger-to-provider-accepted with an alert (N21); Twilio delivery status stored per message. |
| N12 | Volume | Sized for at least 10,000 completed bookings a month in NYC by June 2027 (about 1,850 today), over the three pilot sites plus three or four new ones. Sizing does not depend on how "completed" is defined (Q-017). | CTX-138 (SRC-C1@00:29:22), CTX-039, CTX-070. Seeded test volume: A-034. | Load test (N6) on staging seeded per A-034. |
| N13 | SOC 2-ready | From day one: access control, audit logging, change management, encryption, and a separate production AWS account. The audit, the auditor and any compliance tool are Amperlane's. | CTX-107, ADR-012 (SRC-C2@00:44:04, SRC-C2@00:44:25). | Terraform defines a separate production account. The solution architect reviews N14 – N17 and the security checklist at Gate 4 and before launch. |
| N14 | Encryption | TLS 1.2 or later for all traffic, internal and external; encryption at rest with KMS keys in Amperlane's account for databases, backups, object storage, logs and the workflow store; secrets only in a managed secret store. | CTX-107, CTX-108; **A-037**. | AWS configuration rules and Terraform review in CI; secret scanning in CI (SC1). |
| N15 | Access control | Staff accounts use single sign-on with MFA; production access is role-based, least-privilege and logged; access is reviewed quarterly and removed within one business day of a person leaving. Fleet and station users may turn MFA on; drivers use signed links (A-006). | CTX-107; **A-038**. | Identity-provider configuration reviewed by the solution architect before launch; quarterly access-review record kept by the Amperlane CTO. |
| N16 | Vulnerabilities and pen test | No release with a known critical or high vulnerability unless an exception is approved. A pen test comes with SOC 2 Type I; its date follows the SOC 2 target, which is not assumed (CF-016, Q-018). | CTX-078 (SRC-C2@00:43:30); **A-039**. | Dependency and image scan gate in CI (SC2); pen-test report and retest record. |
| N17 | Audit trail | Every booking state change, override, manual ops action and payout is recorded append-only with actor (system or person), action, reason code and time. | CTX-036, CTX-110 (SRC-C2@00:50:39, SRC-C2@00:53:32, SRC-C2@00:53:46). | A test per state transition and per ops action asserts the audit event; a database test asserts the application role cannot update or delete audit rows. |
| N18 | Personal data | NY SHIELD safeguards and breach notification for credentials and licence or account numbers. Location is sensitive: used only with the driver's opt-in (A-024), kept only as arrival events, retained per data type (A-025; counsel sets periods, Q-022). Vehicle data needs the account owner's authorisation. | CTX-108, CTX-109 (SRC-C2@00:39:22, SRC-C2@00:50:18, SRC-C2@00:50:34); A-024, A-025. | Data register: every personal-data field has a class, a retention period and a tested purge job (SC4). Test: no location is stored without an active opt-in. Incident runbook naming Amperlane's breach-notification owner, reviewed before launch. |
| N19 | Ledger integrity | Money is recorded in a double-entry, append-only ledger; every transaction balances; a no-show fee is a separate line from energy. | CTX-095, CTX-127, ADR-008. | Database test: the application role cannot update or delete ledger entries. Daily check: no unbalanced transaction (alert, N21). Test: a no-show fee is reversed without changing energy lines. |
| N20 | Backup and recovery | Data loss at most 5 minutes (RPO). Service back within 30 minutes after losing an availability zone, and within 4 hours after a restore from backup. | **A-040** (no source sets a number). | Restore drill before launch and every quarter, recorded by the tech lead. |
| N21 | Observability | Metrics, structured logs and traces for every module; a dashboard and an alert for N1, N3, N4, N7, N8, N11 and N19; logs carry a correlation id and the booking id, and no secrets or personal data beyond ids. | **A-041**. Who is on call: Q-039. | The solution architect checks dashboards and alert rules before launch; log-scrubbing test in CI (SC5). |
| N22 | Languages | Driver messages (SMS and WhatsApp, via Twilio) and the driver PWA in English, Spanish and Bengali. Other interfaces and translation review: A-042. | CTX-097, CTX-028 (SRC-C2@00:50:56, SRC-C2@00:51:03); PWA languages SRC-D2#13 (Intellias); **A-042**. | CI fails when a message key lacks EN, ES or BN; native-speaker review per A-042 before release. |
| N23 | Driver effort | No app download and no account. Booking takes two taps from the open-slot view: pick a slot, confirm. Cancel and "running late" take one tap from the booking's message or page. | CTX-002 (SRC-D1#5, SRC-C1@00:03:57); CTX-135 (SRC-C1@00:12:26, SRC-C1@00:12:42); CTX-027, ADR-009. | End-to-end test counts the interactions in each flow. |
| N24 | Web baseline and accessibility | Driver PWA and attendant view: WCAG 2.2 AA; current and previous major versions of Safari on iOS and Chrome on Android; a page opened from a message link is usable within 3 s at p75 on a throttled 4G profile; the booking flow works on a 360 px wide screen. Fleet portal, station portal and ops console: current desktop Chrome, Edge, Safari and Firefox. | **A-043**. | Automated accessibility and performance checks in CI on the booking flow; device-matrix test before launch. |

## Definition of Ready

A story, system story or task can enter a sprint only when every row holds.

| R | Criterion | Checked by |
|---|---|---|
| R1 | It is approved, its front-matter is complete, and it is not stale (no parent changed after approval). | `trace.py`: no front-matter problem, dangling reference, stale or unstamped entry for the item. Approval: a human at Gate 3 or 4. |
| R2 | It has parents: a story links at least one REQ; a system story links at least one story (or `parents: []` as an enabler) and at least one REQ; a task implements at least one SS. | `trace.py` coverage report. |
| R3 | AC are testable. Stories: Gherkin with a happy path, at least two failure paths and one edge case. System stories: labelled EARS clauses, each testable alone, with at least one `[Unwanted]` clause where failure is possible. Tasks: each AC references an EARS clause number. | Product/BA (stories) and solution architect (system stories) at Gate 3; tech lead (tasks) at Gate 4. The P3.2, P3.4 or P4.2 critique output is attached to the review. |
| R4 | KYIV is set: inherited, or overridden with `kyiv_override_reason`. | `trace.py`: no missing KYIV, priority conflict or mismatch without a reason. |
| R5 | Dependencies are known: `depends_on` and `blocks` are filled (empty lists allowed), mirrored and acyclic; external dependencies (API access, credentials, a client action) are named. | `trace.py` (cycles, mirroring); tech lead at Gate 4 for external dependencies. |
| R6 | Every linked Q is answered or covered by an A-###. Nothing depends on a needs-decision conflict or an undecided client business decision, unless it is a parked V item (P5). | Engagement lead, against open-questions.md and conflicts.md. |
| R7 | It assumes no integration capability that integrations.md marks unconfirmed or unavailable, unless the gap is a linked Q or A. | Solution architect at Gate 3 (P3.2, check 4). |
| R8 | Tasks only: one PR, about two days of work or less, finishable by a developer or an agent without asking a question. | Tech lead at Gate 4 (P4.2). |
| R9 | NFR overrides, if any, list the N label, target, reason and source or A-###, and are approved. | Solution architect at Gate 3. |

## Definition of Done

A task (one PR) is done when every row holds. D1 – D5 and D7 come from the playbook (§5, 2.2); D6 and D8 are Intellias
conventions.

| D | Criterion | Checked by |
|---|---|---|
| D1 | Every AC of the task has at least one automated test, and all tests pass. | CI required check; the reviewer confirms the AC-to-test list in the PR body. |
| D2 | Each EARS clause of the implemented system stories maps to exactly one test case (it may be parameterised), named after the clause, e.g. "SS-034.3". | A CI script lists clauses with no test or more than one, and fails (to be built in Phase 0); tech lead. |
| D3 | The trace is updated: the PR and its commits carry T-###; the task's status is updated in tasks.yaml; `trace.py --check` passes in the spec repository with no K coverage gap. | CI (PR-title lint); `trace.py --check` in the spec repository's CI. |
| D4 | Docs are updated: the API contract for changed endpoints, the runbook for any new alert or job, an ADR for any new architecture decision. If the behaviour differs from the spec, the spec is changed first. | PR template checklist; reviewer. |
| D5 | The security checklist (SC1 – SC9) passes. | CI for SC1, SC2, SC5 and SC6; reviewer for the rest. |
| D6 | If the change touches booking, inventory or workflows, the load test (N6) and the simulator suite with the Gowanus fault replay pass on staging before release. | Release pipeline gate; tech lead. |
| D7 | A person other than the author approved the PR; an agent's review does not count. Changes to the booking core, the ledger, identity or database migrations also need the solution architect or a second reviewer. | Branch protection in the code repository. |
| D8 | Merged to main and deployed to staging by the pipeline, with migrations applied. | CI/CD record. |

**Security checklist.** Basis: N13 – N18 (CTX-107, CTX-108, ADR-012); the individual checks are Intellias conventions.

| SC | Check | Checked by |
|---|---|---|
| SC1 | No secrets in code, configuration or history. | Secret scanner in CI. |
| SC2 | No known critical or high vulnerability in dependencies or images, unless excepted per A-039. | Scanner gate in CI. |
| SC3 | Every new endpoint, message command and webhook checks authorisation; a test shows that a user of another fleet, site or role is refused. Webhook signatures are verified where the provider signs. | Tests in CI; reviewer. |
| SC4 | New personal-data fields are in the data register with a class and a retention period (A-025); location is stored only with consent (A-024); storage is encrypted (N14). | Reviewer, on the data-register diff in the PR. |
| SC5 | Logs, traces and error responses contain no secrets, tokens, message bodies, payment data or raw location. | Log-scrubbing test in CI; reviewer. |
| SC6 | Every new state change, override, manual ops action or payout writes an audit event (N17). | Test in CI. |
| SC7 | Every external input (API, message, webhook, CSV file) is validated against a schema at the edge. | Contract tests; reviewer. |
| SC8 | Infrastructure changes are made in Terraform only, with least-privilege IAM. | Terraform plan in CI; daily drift check. |
| SC9 | A new open-source dependency passes the maturity check (code conventions, row 3). | Reviewer. |

## Spec conventions

These restate or sharpen AGENTS.md; if the two ever differ, AGENTS.md wins and this file is corrected.

| # | Rule | Checked by |
|---|---|---|
| 1 | Layout and machine-readable formats follow AGENTS.md: the requirements table columns, epic and feature rows, `requirements:` on stories, `parents:` plus `requirements:` on system stories, `implements:` on tasks, `traces_to` filled only by `trace.py`. | `trace.py` (parse problems, dangling references). |
| 2 | IDs use the prefixes of playbook §4.1 (SRC, CTX, Q, A, CF, ADR, REQ, EP/FT, US/JS, SS, T, CR). They are permanent: never reused or renumbered. A withdrawn item keeps its ID with a note (e.g. A-027). | `trace.py` (duplicate IDs); reviewer. |
| 3 | Every artefact has front-matter with id, type, title, status, owner, sources, parents, kyiv and version. Status is draft, in-review, approved or deprecated. Agents create `draft` and never set `approved`. An approved artefact is deprecated (`superseded_by:`), never deleted. `version` goes up when meaning changes. A human approval of a story, system story or task adds `approved_with:`. | `trace.py` (front-matter problems, stale, unstamped); git history at each gate. |
| 4 | Citations: `SRC-D1#<slide>`, `SRC-D2#<slide>`, `SRC-C1@<hh:mm:ss>`, `SRC-C2@<hh:mm:ss>`, `SRC-R1#<anchor>`. Speaker notes cite their slide; transcripts cite the line that carries the claim. Read the extracts in `spec/00-inputs/_extracted/`; nothing in `spec/00-inputs/` is edited. | Reviewer spot-checks at least five citations at each gate (playbook §8). |
| 5 | Who said it decides the quadrant. S-F and S-NF need SRC-D1 or an Amperlane speaker in SRC-C1/C2. A claim supported only by SRC-D2, SRC-R1 or an Intellias speaker is U-F or U-NF, unless an Amperlane speaker agreed to it on the record (cite both). | Engagement lead at Gate 2, on every S-* row. |
| 6 | Requirements cite sources and context only: `SRC-` and `CTX-` in the sources column, `Q-`/`A-` in the links column. They never cite design.md, data-model.md, integrations.md or ADRs (playbook §10.1). | A search of the requirements sources column finds only SRC- and CTX- ids; reviewer at Gate 2. |
| 7 | A requirement is one sentence, one behaviour, testable and quadrant-tagged. Banned words: "fast", "easy", "etc." (playbook §5, 2.1), and "user-friendly", "as appropriate", "and/or" (Intellias convention). | Search for banned words; reviewer at Gate 2 (P2.4 critique). |
| 8 | Story formats and AC formats follow AGENTS.md. EARS clauses carry one label: `[Ubiquitous]`, `[Event]`, `[State]`, `[Unwanted]` or `[Optional]`. | Reviewer at Gate 3 (P3.4 critique). |
| 9 | Vocabulary: use the Term column of glossary.md. Words in its Avoid column do not appear in requirements, stories or system stories, except inside quotes from a source. | Search for Avoid words in spec/20-requirements and spec/30-stories; reviewer. |
| 10 | Every number in a spec artefact cites an SRC/CTX or an A-###. Unknowns become Q-### or A-### in open-questions.md. Conflicts between sources go to conflicts.md with the rule "later > earlier, specific > general, data > estimate", or `needs-decision`. | Reviewer at each gate. |
| 11 | Dates are written YYYY-MM-DD. Clock times are Eastern (America/New_York) unless a site's own time zone is meant (A-013). Durations carry units. Intellias convention. | Reviewer. |
| 12 | No implementation code in spec files; snippets only in design.md and ADRs. | Reviewer; search for code blocks outside spec/10-design. |
| 13 | After every change, run `trace.py` and include the coverage-report diff in the summary. Before a gate, `trace.py --check` passes. | `trace.py --check` in the spec repository's CI (exits 1 on a K gap). |
| 14 | An approved artefact changes only by a human edit or a change request (`CR-###` in CHANGELOG.md, playbook §7). After Gate 2, a new requirement enters only through a CR. | Engagement lead; CHANGELOG.md. |
| 15 | Commits in this repository use Conventional Commits with scope `spec` and name the step, gate or CR, e.g. "docs(spec): … approved at Gate 1". Intellias convention. | Reviewer. |

## Code conventions

The stack and its boundaries come from the sources and ADRs. Everything marked "Intellias convention" is our proposal;
the Amperlane CTO confirms it in Phase 0.

| # | Area | Convention | Basis | Checked by |
|---|---|---|---|---|
| 1 | Stack | TypeScript end to end, with strict compiler settings; PostgreSQL; AWS; Temporal for durable workflows; Terraform for infrastructure. Runtime, back-end and front-end frameworks: A-044. Test and build tools are chosen with A-044 in Phase 0. | CTX-085, ADR-001, ADR-007; **A-044**; strict settings: Intellias convention. | Type-check in CI; solution architect. |
| 2 | Ownership | Code in Amperlane's repositories; infrastructure in Amperlane's AWS accounts through Amperlane's Terraform; Amperlane engineers work in the same repositories from Phase 0. No cloud resource is created by hand. | CTX-005, CTX-006, ADR-001; "no hand-made resources": Intellias convention. | Daily Terraform drift check; repository access list reviewed by the Amperlane CTO at the end of Phase 0. |
| 3 | Open source | Open source only where it is mature. The check: a licence that allows proprietary use (no AGPL, SSPL or GPL in deployed code), a release in the last 12 months, and more than one active maintainer or a foundation behind it. Anything else needs an ADR approved by the Amperlane CTO. | CTX-085, ADR-001; the check: Intellias convention. | Licence scanner in CI; reviewer (SC9). |
| 4 | Module boundaries | One deployable modular monolith. Modules: inventory, booking and calendar, fleet and vehicles, pricing, settlement, notifications, identity, audit, plus workflows, reporting and migration. Each module owns its database schema. No module reads or writes another module's tables or imports its internals; cross-module calls go through the module's public interface or a domain event. | ADR-002, CTX-087; enforcement: Intellias convention. | Dependency-boundary lint in CI; reviewer checks SQL for foreign schemas. |
| 5 | Integrations | Every external system (CSMS, OCPI peers, telematics, payments, messaging, maps) is reached through an integration module at the edge. Vendor SDKs and vendor types never appear in core modules. Software adapters are named "integrations" (folder `integrations/<vendor>`), because the glossary's "adapter" is the physical connector adapter. | ADR-003, CTX-086; naming: Intellias convention. | Import lint in CI fails on a vendor package outside `integrations/`. |
| 6 | Naming | Domain names come from the glossary Term column (Site, EVSE, Connector, Booking, Hold, Allocation, Rebook, Reason code, …), never its Avoid words (no "reservation" for a booking, no "stall" for an EVSE). Files kebab-case; types PascalCase; functions and variables camelCase; database objects snake_case. Reason codes and error codes are stable UPPER_SNAKE strings in one catalogue per module; once released, they are never renamed or reused. | glossary.md; CTX-036; the rest: Intellias convention. | Naming lint and forbidden-identifier list in CI; reviewer. |
| 7 | Error model | Expected domain outcomes (slot taken, capacity exhausted, connector incompatible, hold expired, key reused) are typed results with stable codes, not exceptions. The HTTP API returns problem details (RFC 9457) with the code and a correlation id: 4xx for caller and domain errors, 409 for conflicts (with alternatives when a slot is taken), 5xx only for faults. A database constraint violation maps to its domain code and never surfaces as a 500. User-facing text comes from message keys (N22). | ADR-006 (alternatives for the losers, SRC-C2@00:32:16); the rest: Intellias convention. | Contract tests per endpoint; lint forbids literal user-facing strings. |
| 8 | Idempotency | Every state-changing API call requires an `Idempotency-Key` header. Messaging commands use the provider message id as the key; webhooks use the provider event id. The key is stored with a request hash and the response for at least 7 days (A-035). Same key and payload: the original response. Same key, different payload: 409 `IDEMPOTENCY_KEY_REUSED`. Workflow activities are idempotent, keyed by workflow id and step. | CTX-091, CTX-093, ADR-006; A-035; mechanics: Intellias convention. | Contract tests replay every state-changing call, message and webhook. |
| 9 | Workflows | One Temporal workflow per booking, with the booking id as workflow id. Timers live only in workflows (N10). Workflow code is deterministic: time, randomness and I/O only through Temporal APIs or activities. | ADR-007, CTX-094; the rest: Intellias convention. | Workflow replay tests in CI; lint. |
| 10 | Data | Invariants live in the database where possible (exclusion, check and foreign-key constraints), not only in code. Times are stored as instants (timestamp with time zone) and shown in the site's time zone. Schema changes are versioned, forward-only migrations applied by the pipeline. Business parameters (grid, slot lengths, buffers, hold TTL, T-15, T-10, grace) are per-site configuration, never literals in code. | ADR-006, A-013, A-001 – A-003; migrations: Intellias convention. | Integration tests on real PostgreSQL; lint flags time types without a zone; reviewer. |
| 11 | Money | The ledger follows N19. Amounts are integer minor units with an ISO 4217 currency; per-kWh prices are fixed-scale decimals; never floating point. Ledger and audit tables are insert-only for the application role. | ADR-008, CTX-095, CTX-110; number types: Intellias convention. | Database grant test; lint forbids floating-point money types. |
| 12 | Personal data | Phone numbers in E.164. Personal data appears in logs only as internal ids (SC5). Location is read and stored only through the consent check (A-024). | CTX-108, CTX-109, A-024; E.164: Intellias convention. | Tests; reviewer. |
| 13 | Test layout | Unit tests beside the code (`*.test.ts`). Module integration tests on real PostgreSQL in containers (constraints cannot be mocked). Contract tests per integration with recorded vendor payloads, including duplicated and out-of-order webhooks. Workflow tests with Temporal's time-skipping test environment. End-to-end tests for the PWA, portals, ops console and attendant view. Load tests per A-034. Simulator tests on EVerest, with the Gowanus fault replay ("1:50 PM, charger fault, nine bookings") as a permanent regression test. Test names start with what they cover: "US-012 S2 …", "SS-034.3 …". | CTX-103 (simulator and replay, SRC-C2@00:55:37, SRC-C2@00:55:51); the rest: Intellias convention. | CI runs every suite except load (release gate, D6); the D2 script checks clause-to-test mapping. |
| 14 | Commits and PRs | Branch `t-###-<slug>`. Conventional Commits: `type(module): summary`, footer `Refs: T-###`. One task is one PR; PR title "T-###: <task title>". The PR body lists the SS clauses implemented and their tests, KYIV, NFR impact (N labels), spec changes and the DoD checklist. Only automated dependency updates may omit T-###. | Playbook §5 Step 4 (one task, one PR); the format: Intellias convention. | Commit-message and PR-title lint in CI; PR template. |
| 15 | Releases | Trunk-based development with a protected main branch; deployment only through the pipeline; downtime only between 01:00 and 05:00 ET (N5). | A-028; the rest: Intellias convention. | Branch protection; deployment log. |

## KYIV rules

KYIV replaces MoSCoW (playbook §5, Step 5).

| | Meaning | MoSCoW | Rule of thumb |
|---|---|---|---|
| **K · Keep for sure** | Non-negotiable. Without it the release fails its goal or breaks a hard constraint (legal, contractual, safety, money). | Must | The sum of K fits the committed capacity with a buffer (P6). If it doesn't, the scope or the date is wrong. |
| **Y · Yes, if we possibly can** | High value, strongly committed. Dropped only under real pressure, and only after telling the client. | Should | Planned, but last in the sequence. |
| **I · If we have extra budget, we will** | **Not in the committed plan; enters only if capacity frees up.** | Could | Not in any sprint until a recorded decision admits it (P7). |
| **V · Very unlikely** | **Not this release, visible and agreed**, not "maybe later". | Won't (this time) | Keeps its ID and stays visible in the parking lot. This protects scope. |

| P | Rule | Checked by |
|---|---|---|
| P1 | Requirements get KYIV from humans: provisional at Gate 2 (column "K (provisional)"), final at Step 5 by the client's product owner and the engagement lead. | Gate records; `trace.py` (missing KYIV). |
| P2 | A story, system story or task inherits the highest KYIV among its parents. | `trace.py` computes the effective KYIV. |
| P3 | A different value needs `kyiv_override_reason:` in front-matter. A child ranked above all its parents is a priority conflict. | `trace.py` lists conflicts, mismatches without a reason, and every override. |
| P4 | Agents suggest KYIV only (P5.1): a proposal table, each value with a reason from context (dates, budget, regulation, contracts, success metrics, items the client deferred). Agents never choose or change a KYIV value: they only copy the value inherited under P2, and never write `kyiv_override_reason`. | Reviewer checks the git diff of `kyiv` fields at each gate. |
| P5 | A requirement that holds only under one option of an undecided client business decision goes to the parking lot as V, linked to the Q in its Q-/A- column, and is priced as an option in the proposal. If the client chooses it later, it enters through a change request (CR-###), which sets its KYIV. Requirements that hold in every option go into the baseline. The undecided decisions are those listed in open-questions.md: Q-001, Q-002, Q-003, Q-017, Q-021, Q-023, Q-025, the SOC 2 date in Q-018, the March integration scope in Q-036 and CF-025, the back-end operator question in Q-010, and questions that depend on them (e.g. Q-032). | Engagement lead at Gate 2; `trace.py` lists parked requirements. |
| P6 | The sum of K estimates is at most 80% of the committed capacity up to the date (a buffer of at least 20%, **A-045**). If not, the engagement lead raises scope or date with the client before the proposal. | Engagement lead at Gate 2 (provisional) and Gate 5 (final). |
| P7 | An I item enters a sprint only by a decision of the engagement lead with the client's product owner, recorded in the sprint plan. Dropping a Y item is recorded as a CR after the client is told. | Tech lead at sprint planning; CHANGELOG.md. |
| P8 | Export: K → Highest, Y → High, I → Low, V → Lowest in the task manager's priority field, plus the label `kyiv:<letter>`. Intellias convention for the mapping of Y and I. | Tech lead at Gate 4, on the export. |

## Changing this constitution

Any change bumps `version`. After Gate 2, changes go through a change request (CR-###) with an impact analysis (P7.1).
Artefacts approved against an earlier version are re-checked only where the CR says so.
