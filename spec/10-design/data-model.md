---
id: DATA-MODEL
type: design
title: Core data model (v2)
status: approved
owner: Mykola Marchuk
version: 2
kyiv: null
parents: [BUSINESS-CONTEXT, DESIGN]
sources: [SRC-C1, SRC-C2, SRC-D2]
---
# Core data model, v2

> **v1, revised after Steps 3 and 4** (playbook §10.1, CR-012). v0 was a hypothesis from the sources. v1 is the
> logical model that the approved system stories (SS) and tasks (T) require. Every entity cites the SS clauses or tasks
> that need it. Names follow the [glossary](../01-context/glossary.md); table names from the tasks are in `code`.
> Entities are grouped by the component that owns them (design.md §2.3, §2.6). Links between modules are ids without
> foreign keys (constitution, code conventions row 4), so cardinalities across modules are logical only. The booking
> entities should still map onto the OCPI 2.3 Booking module later (SRC-C2@00:13:32, SRC-C2@00:13:40). Gaps the revision
> found are in section 5. **v2** (CR-013, 2026-10-29) closes them: SS-046 enters Completed, the fleet has a billing
> contact (SS-040), the station operator is a minimal record, and the decisions on G-4 – G-6 are recorded.

## 1. Entities

### Inventory & site configuration

| Entity | Key attributes | Notes | Required by |
|---|---|---|---|
| StationOperator | id, name | A minimal record created with the first site that names it (SS-028.1, T-108; G-3). Contacts are OperatorNoticeContact. | SS-028.1, SS-323.1; T-108 |
| Site (`site`) | operator, name, unique site code, address, latitude and longitude, IANA time zone, supply pattern (A/B/C), CSMS kind (integrated kinds; `simulator` in CI and staging), exactly one live status source (CSMS, OCPI Locations peer, attendant view), live flag (default false), synthetic flag | Terms and parameters are versioned entities below. | SS-028.1 – SS-028.8, SS-206.1, SS-428.5; T-100, T-931 |
| EVSE (`evse`) | site, external id per CSMS, label, reservable flag (default false) | Live status is EvseCurrentStatus. The label is the stall name drivers are given (G-5). | SS-029.5, SS-100.3; T-100 |
| Connector (`connector`) | EVSE, type (CCS1, NACS), maximum kW (> 0) | At least one per EVSE. | SS-030.1 – SS-030.3 |
| CapacityRule (`capacity_rule`) | site, days of week, local window (may cross midnight), cap as a count of EVSEs (at most the EVSE count), valid from, actor | No percentage cap and no overbooking flag. | SS-023.1 – SS-023.4; T-103 |
| BookablePeriod (`bookable_period`) | site, days of week, local start and end | | SS-023.1, SS-023.4; T-103 |
| SiteParameterVersion (`site_parameter_version`) | site, version, the per-site values of design.md §8, site-staff channel and number, session-start arrival switch and evidence, valid from, actor | A booking keeps the version it was confirmed under. | SS-026.1, SS-026.5, SS-026.10, SS-026.11; T-101, T-102 |
| PlatformParameterVersion (`platform_parameter_version`) | version, the platform-wide values of design.md §8, valid from, actor | Includes the status poll interval per CSMS kind (SS-026.9). | SS-026.2; T-101 |
| PartnerTermsVersion (`partner_terms_version`) | site, version, no-show fee (minor units, ISO 4217 currency), station share, valid from, actor | "Never set" differs from 0. | SS-027.1, SS-027.2, SS-027.4; T-106 |
| QR code | derived from a signed (site, EVSE) pair; stable on reprint | Not stored. | SS-031.2, SS-031.3; T-110 |

### Booking & calendar

| Entity | Key attributes | Notes | Required by |
|---|---|---|---|
| Hold | site, start and end, booker kind and id, charging driver, vehicle, expires at, state (placed, confirmed, expired, released) | Its own entity, not a booking state (section 3). | SS-002, SS-016.1; T-120 |
| Booking | unique code, site, start and end, fleet (the vehicle's fleet), vehicle, charging driver, booker kind and id, site parameter version, partner terms version, cancellation cut-off, origin (platform, carried over, pilot migration), carried-over source id, state | Vehicle, booker and driver may be empty for bookings that did not start in the platform. End of grace is derived, not stored. | SS-003.6, SS-003.8, SS-003.9, SS-006.1, SS-011.3, SS-127.1; T-120, T-128, T-983 |
| BookingStateChange (`booking_state_change`) | booking, state before and after, actor kind and id, reason code, recorded at, occurred at (outage entries), corrects entry | Insert-only; replaces v0 BookingEvent. | SS-020.1, SS-020.6, SS-020.8, SS-020.9; T-122 |
| ReasonCode catalogue | stable UPPER_SNAKE id, label, group | Also codes for audited ops actions that change no state. | SS-020.2, SS-020.4; T-122 |
| ManualHold | kind (maintenance, fleet priority), site, EVSEs or units of capacity, fleet, window, reason, actor, ended at | | SS-017.1, SS-018.1; T-120, T-145 |
| Offer, OfferSlot | Offer: for a booking or a hold, reason code, answer, answered at. OfferSlot: slot, optional hold, option number, signed accept link | A re-offer after a no-show creates a new booking; other offers rebook the same one. | SS-011.3, SS-011.7 – SS-011.9, SS-316.1; T-120, T-138 |
| SiteRequest | site, sequence value, received at | The per-site queue that serialises attempts at the shift-change burst. | SS-007.1; T-134 |
| IdempotencyKey (`idempotency_key`, in every module schema) | key, principal, request hash, state, stored response, created at | Kept at least 7 days. | SS-014.2 – SS-014.5, SS-025.2; T-129, T-207 |
| OverLimitSlot | slot, bookings, excess, bookings marked above the limit, who made the cut | After a lowered cap or reduced hours. | SS-019.2, SS-019.5; T-147 |

### Allocation & rebooking, Station-hold dispatcher

| Entity | Key attributes | Notes | Required by |
|---|---|---|---|
| Allocation | booking, site, EVSE, half-open time range (buffer from the booking's parameter version), active, deactivated at, actor, reason | The exclusion constraint lives here (INV-1); the EVSE is referenced without a foreign key. | SS-102.1, SS-102.2, SS-103.1; T-300 |
| SiteFullMark | booking, marked at, cleared at | Replaces v0 AllocationFailed. | SS-105.1, SS-105.4; T-305 |
| RebookingProposal | booking, exception, proposed site, slot and EVSE, state | Holds no capacity. | SS-110.1 – SS-110.6; T-309, T-311 |
| FaultOutcome | trigger id and kind (fault, ops rebook-all, maintenance hold), booking, outcome, reason, final outcome | | SS-108.8, SS-108.10, SS-113.6; T-310 |
| StationHoldAttempt | booking, allocation, EVSE, method (charger reservation, site staff, ops), request code, state | At most one per active allocation. | SS-121.1, SS-121.4; T-304 |
| StationHoldAnswer | attempt, kind, time, detail | Insert-only; replaces the result fields of v0. | SS-121.1, SS-121.3; T-304 |
| SiteHoldMode | site, manual or automated, actor, time | Kept with its history. | SS-123.1, SS-123.2; T-322 |
| Manual station-hold list entry | booking, EVSE, mark and clear times, arranged by and at | Stored or derived: uncertain. | SS-123.3 – SS-123.5; T-322, T-323 |

### Arrival & no-show

| Entity | Key attributes | Notes | Required by |
|---|---|---|---|
| ArrivalEvidence | booking, kind (QR scan, CSMS session start, attendant), EVSE, source, actor, time, counts as arrival, late, unidentified | Geofence and location are no longer arrival kinds. | SS-124.2, SS-125.8, SS-128.1, SS-340.1; T-303 |
| QrScan | EVSE, booking (empty while pending), time, device cookie, applied at | | SS-124.3, SS-124.9; T-327, T-353 |
| GraceExtension | booking, minutes, ops user, reason, time | | SS-130.1; T-303, T-335 |
| RunningLateReport | booking, driver, time | Replaces the v0 running-late flag and ETA. | SS-129.1; T-334 |
| BlockedStallReport | booking, reporter, time, arrival evidence at that moment | | SS-133.1, SS-133.5; T-338 |
| FeeExclusion | booking, kind (rebooked, station hold failed, site full, site faulted, grace timer late, late cancellation), source, time | | SS-127.4, SS-131.2; T-303 |
| FeeDecision | booking, outcome, ops user, reason, time | One per booking. | SS-131.1, SS-131.3, SS-131.5; T-336 |
| NoShowDispute | no-show booking, raised by, opened at, state, decision (reverse or keep), reason, decided by and at | Hangs off the booking, not the charge; replaces v0 Dispute. | SS-134.1 – SS-134.6; T-341, T-354 |

### EVSE status service, CSMS integrations

| Entity | Key attributes | Notes | Required by |
|---|---|---|---|
| EvseCurrentStatus | EVSE, status (available, occupied, charging, faulted, unknown), observed at, source, last heard, exclusion reason (fault or silence) and its source | One row per EVSE. | SS-200.1, SS-200.6, SS-202.6, SS-208.7; T-501 |
| StatusObservation, StatusReceipt | observation: EVSE, status, observed at, source; receipt: EVSE, received at | Insert-only partitions; status age is measured from the last receipt. Replace v0 StatusEvent; no raw payload is kept. | SS-200.6, SS-205.1; T-516 |
| AppliedStatusEvent | dedupe key | Kept at least 7 days. | SS-200.4; T-501 |
| FreshnessMinute (`freshness_minute`) | EVSE, minute, maximum age, API reachable | | SS-201.5, SS-201.6; T-504 |
| SiteFeedState (`site_feed_state`) | site, unavailable since, last received at | | SS-203.1, SS-203.5; T-506 |
| Fault episode | EVSE, start, end or ongoing | A table or events only: uncertain. | SS-208.2, SS-209.5, SS-234.1; T-512, T-553 |
| CsmsCapability, StatusMapping | declared capabilities per integration; versioned map from each vendor value to exactly one status | | SS-211.3, SS-214.3, SS-217.3; T-500, T-519 |
| CsmsRejection | integration, reason, received at, payload hash | | SS-211.4, SS-214.4; T-519, T-523 |
| ReservationRequest | station-hold attempt, typed result | | SS-212.2 – SS-212.6; T-520 |
| SessionRecordCursor, LicRow | the read resume point per integration; the LIC row keys already taken in | | SS-213.2, SS-213.3, SS-215.3; T-522, T-524 |
| SessionStartEvent | site, EVSE, start, event id, vehicle, token or account id, or "unidentified" | Whether it is stored: uncertain. | SS-216.1, SS-216.3; T-525 |

### Fleet & vehicles

| Entity | Key attributes | Notes | Required by |
|---|---|---|---|
| Fleet (`fleet`) | name (unique, case-insensitive), kind, adapter policy, billing contact (name, e-mail address) | The billing contact feeds the fleet's Stripe customer (G-2). | SS-039.1, SS-040.5 – SS-040.7; T-180, T-184, T-1007 |
| Vehicle (`vehicle`) | fleet, plate (unique among the fleet's active vehicles), native connector, allowed adapters, adapter override, maximum DC kW, retired at | | SS-038.1 – SS-038.5; T-183 |
| Driver | internal id, E.164 number, first name | A driver can exist with no registration and so no right to book; anonymised under a pseudonym that keeps the id. Language, channel and consent live in Messaging and Audit. | SS-318.1, SS-323.4, SS-337.2, SS-337.5; T-208, T-1009 |
| DriverRegistration (`driver_registration`) | fleet, E.164 number, registered by and at, removed at | | SS-037.1, SS-037.3, SS-037.5; T-181 |
| BookerRegistration (`booker_registration`) | fleet, E.164 number, registered by and at | A number is a driver or booker-only in a fleet, never both. | SS-042.1 – SS-042.3; T-182 |
| DriverVehicleLimit (`driver_vehicle_limit`) | driver registration, vehicles | | SS-045.2, SS-045.4; T-185 |
| VehicleDataAuthorisation (`vehicle_data_authorisation`) | fleet, agreement date, scope (battery level, charging state), recorded and revoked by and at | Replaces v0 TelematicsLink. | SS-043.1, SS-043.3, SS-043.5; T-189 |
| VehicleReading (`vehicle_reading`) | vehicle, booking, SoC (integer 0 – 100), observed at, source (manual) | No location. | SS-044.1, SS-044.4; T-190 |
| BookingNeedingAction (`booking_needing_action`) | booking, fleet, reason (no compatible EVSE, vehicle not allowed) | | SS-038.6, SS-045.6; T-186 |

### Identity & access

| Entity | Key attributes | Notes | Required by |
|---|---|---|---|
| PartnerUser | user, exactly one organisation (fleet, station operator or site), one role | Staff roles are separate; finance is read-only. | SS-323.1, SS-440; T-740 |
| SiteStaffLogin | person, site, revoked | | SS-324.1, SS-324.3, SS-324.5; T-751 |
| DriverRemoval | number, fleet, actor, time | Stored once, as DriverRegistration.removed at in Fleet & vehicles; Identity reads it (G-6). | SS-319.1, SS-319.6; T-745 |
| DriverLink, DriverSession | link: signed token bound to number and booking, expiry, first device; session: full or limited | | SS-320.1, SS-320.2, SS-320.4, SS-320.8; T-746, T-747 |
| VerifiedDevice, OneTimeCode, CodeBlock | device and number with valid-until; hashed code with expiry and wrong-code count; block end | | SS-321.4 – SS-321.8; T-749 |

### Notifications (messaging)

| Entity | Key attributes | Notes | Required by |
|---|---|---|---|
| OutboundMessage (`message`) | type, booking, recipient, channel, template, language, trigger and accepted times, delivery status (never regresses), not-sent outcome | Replaces v0 Notification; sent through the outbox. | SS-304.10, SS-307.1, SS-307.2; T-700 |
| InboundMessage (`inbound_message`) | provider message id, channel, from number, edge stamp, processed at | "Processed" means its effect committed; no body is kept. | SS-309.1 – SS-309.5; T-706 |
| MessagingAgreement (`agreement`) | number, channel, recorded at, how it was given, recorded by, ended at (STOP) | At most one in force per number and channel. | SS-304.1, SS-304.2, SS-304.9; T-703 |
| DriverLanguage (`driver_language`), ChannelPreference | per E.164 number: EN, ES or BN; SMS or WhatsApp | | SS-303.1, SS-308.2; T-701, T-709 |
| ConsentText, ConsentAcceptance | versioned EN/ES/BN texts with a published flag; insert-only acceptance (driver, version, language, time) | | SS-305.1 – SS-305.7; T-732 |
| OpsMessage (`ops_message`) | booking, ops user, template or free text, recipient, channel, delivery status | | SS-314.3; T-729 |
| OperatorNoticeContact | station operator, one E.164 number | | SS-313.1, SS-313.5; T-728 |

### Ops console, Partner portals, Reporting

| Entity | Key attributes | Notes | Required by |
|---|---|---|---|
| OpsException (`ops_exception`) | type, site, EVSE, booking, level key, details, state (open, closed, resolved), repeat count, closure | One open exception per type and key. | SS-219.1, SS-219.2, SS-219.5; T-507, T-510 |
| ExceptionType (`exception_type`) | code, name, dedupe level | 18 seeded. | SS-219.11; T-507 |
| Portal read models | fleet bookings, booking evidence, station upcoming bookings, station fault outcomes, attendant's due drivers | Plate and first name only. | SS-223.1, SS-225.1, SS-227.1, SS-228.1; T-536 – T-544 |
| ReportingBookingEvidence | per booking: state changes and reasons, arrival, session-record match and energy, rebooks, final slot, the no-show it followed | | SS-229.1; T-546 |
| CompletedDefinition (`completed_definition`) | version, rule over the evidence fields only, actor, time | Default "state is Completed" (SS-046). | SS-229.2 – SS-229.4, SS-229.10; T-547, T-548 |
| FaultCost | per fault: counts by final outcome | | SS-234.1, SS-234.2; T-553 |

### Settlement & ledger, Payments (Stripe)

Structure in every business-model option; option-specific flows (payouts, subscriptions, energy resale) are parked (Q-001).

| Entity | Key attributes | Notes | Required by |
|---|---|---|---|
| LedgerAccount | owner, kind, currency | A new kind is a row, not a schema change. | SS-400.1, SS-400.6; T-947 |
| LedgerTransaction | kind, posted at, reference, reason, actor | | SS-400.1, SS-400.2; T-947 |
| LedgerEntry | transaction, account, side, amount in minor units, currency, corrects entry | Append-only. | SS-400.1, SS-400.3; T-947 |
| Charge | booking, kind (baseline: NO_SHOW_FEE only), payer (the fleet) | Unique per booking; its status is the net of its entries. | SS-401.1 – SS-401.4, SS-402.11; T-949 |
| SessionRecord | source, external id (unique per source), EVSE, start, end, kWh, received at | | SS-407.1, SS-407.4; T-965 |
| BookingSessionMatch | booking, session record | Only for an arrived booking allocated to that EVSE; an ambiguous match becomes a ReconciliationCase. | SS-407.2 – SS-407.5; T-966 |
| ReconciliationCase | kind, booking, charge, session record, outcome, reason, closed by and at | One open per booking or charge; nothing in an open case is invoiced. | SS-408.1 – SS-408.12; T-962 |
| FleetInvoice | fleet, month, issue and due dates, total (sum of lines), payment status, overdue flag, Stripe id and hosted page, submission state | Unique per fleet and month; insert-only once issued. | SS-404.2, SS-404.3, SS-409.1 – SS-409.6; T-950, T-964 |
| InvoiceLine | invoice, kind (charge, adjustment, credit, carried credit), booking, final-slot date, entries, amount | | SS-405.1, SS-405.2, SS-406.1; T-950 |
| PaymentAttempt | invoice, failed attempts | Uncertain. | SS-409.3; T-964 |
| InvoiceSubmission, StripeCustomerMapping, ProcessedProviderEvent | submission key from the invoice id, with its state; fleet to Stripe customer; provider event ids (kept at least 7 days) | | SS-412.1 – SS-412.9, SS-413.3; T-958, T-1007 |
| Pilot invoicing export | one-off CSV of bookings invoiced by the pilot process | | SS-410.4, SS-410.5; T-971 |

### Audit & privacy

| Entity | Key attributes | Notes | Required by |
|---|---|---|---|
| AuditEntry | actor kind and id with role, action, target, mandatory reason, time, correlation id, correction of | Immutable for every role; ids only. Kinds include security events and configuration changes with before and after values. Replaces v0 AuditEvent. | SS-235.2, SS-332.1 – SS-332.7, SS-333, SS-334; T-780, T-782 |
| PersonalDataAccessEntry | user, organisation, driver, data elements, view or export, time | | SS-335.1, SS-335.3, SS-335.5; T-785 |
| DataRegisterEntry | field, class, sensitive flag, purpose, reader roles, vendors, retention or "not set", finance rule | | SS-336.1, SS-342.1; T-786, T-788 |
| DriverLatestActivity | driver, instant | Retention counts from it. | SS-336.6; T-788 |
| DeletionJournal | ids, data type, time | Append-only, no personal data; re-applied after a restore. | SS-336.7; T-790 |
| LocationOptIn | driver, on, withdrawn, consent version | Replaces the location part of v0 Consent. | SS-341.4, SS-341.6; T-798, T-799 |
| RawLocationReading | driver, booking, encrypted location, time | Kept only until arrival is derived or grace ends. | SS-340.2 – SS-340.4; T-797 |
| BreachProcedureRecord | document, counsel review, owner | | SS-338.8; T-794 |

### Migration & cut-over

| Entity | Key attributes | Notes | Required by |
|---|---|---|---|
| MigrationRun | export id, rule versions, status | | SS-417.5, SS-417.6; T-977 |
| MigrationRecord | run, file, row, site, month, outcome (loaded, merged, rejected), reason | | SS-417.1 – SS-417.4; T-977 |
| MigratedBooking | booking, source system and id (unique), recorded EVSE, arrival time, outcome; insert-only: original status, rule and version, evidence, pre-February-2026 flag | No state machine, ledger entry, workflow or message. | SS-416.1 – SS-416.3, SS-416.11, SS-418.1 – SS-418.6; T-981, T-983 |
| ConflictListEntry | run, booking, both source values, value kept, rule version | | SS-419.6, SS-419.9; T-980 |
| Migration rule sets | versioned files: status map, re-classification, precedence, site map, column-to-EVSE map | | SS-416.5, SS-418.2, SS-419.1; T-978 |
| RawPilotExport | access list, retention end ("not set"), deletion record | Stored read-only. | SS-420.1 – SS-420.8; T-985 |
| Cut-over records | instant (versioned), cut-over record with steps and confirmations, vehicle assignment per pilot source id, result list with reasons | | SS-421.1, SS-421.4, SS-421.7, SS-422.1, SS-422.3, SS-422.7; T-987, T-988, T-994 |
| GoLiveRecord | criteria, period, staff list, per-site proof, evidence, switch-off approval | | SS-423.1 – SS-423.7; T-991 |

### Platform

| Entity | Key attributes | Notes | Required by |
|---|---|---|---|
| Outbox, ProcessedEvent (in each schema) | domain events written in the same transaction; consumed event ids | Kept at least 7 days. Replaces the v0 event bus (design.md §2.5). | SS-427; T-1001 |
| OutageCopy | per site: next bookings, driver contact, window, EVSE, last complete refresh | Outside the primary system. | SS-436.1 – SS-436.8; T-943, T-944 |

Operational records outside the domain model: change records (SS-426.2, T-1010), the deployment log (SS-429.4, T-927),
the production access log (SS-433.2, T-917), the runbook register (SS-437.2, T-939), the handover checklist (SS-438.5,
T-941) and the export manifest (SS-434.5, T-935).

## 2. Relationships

| From | To | Cardinality | Note |
|---|---|---|---|
| StationOperator | Site | 1 : n | |
| Site | EVSE · Connector | 1 : n · EVSE 1 : n | At least one connector per EVSE. |
| Site | CapacityRule, BookablePeriod, SiteParameterVersion, PartnerTermsVersion, SiteHoldMode | 1 : n each | Exactly one capacity rule per bookable slot (INV-2). |
| Site | SiteFeedState | 1 : 0..1 | |
| EVSE | EvseCurrentStatus · StatusObservation, StatusReceipt, FreshnessMinute | 1 : 1 · 1 : n | |
| Fleet | Driver | n : m through DriverRegistration | A driver may drive for more than one fleet (A-016). |
| Fleet | BookerRegistration, Vehicle, VehicleDataAuthorisation | 1 : n each | At most one authorisation in force. |
| DriverRegistration | DriverVehicleLimit | 1 : 0..1 | The limit names vehicles (n : m). |
| Hold | Booking | 1 : 0..1 | |
| Booking | Fleet · Vehicle | n : 1 · n : 0..1 | Vehicle, booker and driver are empty for some non-platform origins. |
| Booking | SiteParameterVersion, PartnerTermsVersion | n : 1 each | Fixed at confirmation; replaced only by a rebook to another site. |
| Booking | BookingStateChange | 1 : n | |
| Booking | Allocation | 1 : 0..n | Exactly one active at a time; history kept. |
| Allocation | StationHoldAttempt | 1 : 0..1 | An attempt has 1 : n StationHoldAnswer and 1 : 0..1 ReservationRequest. |
| Booking | ArrivalEvidence, QrScan, GraceExtension, RunningLateReport, BlockedStallReport, FeeExclusion, OpsException, OutboundMessage, OpsMessage | 1 : 0..n each | |
| Booking | FeeDecision, RebookingProposal, SiteFullMark, MigratedBooking, Charge | 1 : 0..1 each | One NO_SHOW_FEE charge at most. |
| Booking (no-show) | NoShowDispute | 1 : 0..n | At most one open. |
| Booking (re-offer) | Booking (the no-show it followed) | n : 1 | |
| Offer | Booking or Hold · OfferSlot | n : 1 · 1 : n | |
| Booking | SessionRecord | 0..1 : 0..1 through BookingSessionMatch | Only if the booking arrived and was allocated to that EVSE; a session record may exist without a booking (walk-up). |
| SessionRecord | EVSE | n : 1 | v0: Site. |
| ReconciliationCase | Booking, Charge, SessionRecord | n : 0..1 each | |
| LedgerTransaction | LedgerEntry | 1 : 2..n | An entry may correct another entry. |
| FleetInvoice | InvoiceLine | 1 : n | A line has n : m ledger entries and n : 1 booking. |
| Fleet | FleetInvoice · StripeCustomerMapping | 1 : n · 1 : 0..1 | |
| MigrationRun | MigrationRecord, ConflictListEntry | 1 : n each | A pilot record has 0..1 carried-over booking. |
| ConsentText (version) | ConsentAcceptance | 1 : n | An acceptance is n : 1 Driver; a LocationOptIn is n : 1 acceptance. |
| PartnerUser | Fleet, StationOperator or Site | n : 1, exactly one | |
| DriverLink | (number, booking) · device | n : 1 · 0..1 | |

## 3. Lifecycles

### Hold

| State | Entered when | Leaves to |
|---|---|---|
| Placed | A slot is picked (SS-002) | Confirmed (becomes a booking); Expired (HOLD_EXPIRED); Released |
| Expired | The hold time passed without confirmation | — (ops can force-confirm it, FORCE_CONFIRMED, SS-016.1) |
| Released | A check failed at confirmation (SS-003.4, SS-003.5), an offer was declined (SS-011.6, SS-011.7), or a synthetic check ended (SYNTHETIC_CHECK_RELEASED, SS-428) | — |

### Booking

Every change is a BookingStateChange with an actor and a catalogue reason code (SS-020). Station-hold outcomes, site-full
marks, grace extensions and running-late reports change no state (SS-117.4, SS-119.2, SS-105.1, SS-130, SS-129.1).

| State | Entered when | Leaves to |
|---|---|---|
| Confirmed | The booker confirms a hold (SS-003.7), or a pilot booking is carried over at cut-over (CARRIED_OVER_AT_CUTOVER, SS-003.9, SS-421.1) | Allocated at the allocation offset (SS-100); Cancelled; stays Confirmed with a site-full mark when no compatible EVSE is free (SS-105.1), then Allocated at the pre-arrival check (SS-105.6) or rebooked (MOVED_SITE_FULL, SS-105.3) |
| Allocated | An EVSE is assigned at the allocation offset | Allocated again on reallocation (REALLOCATED_EVSE_OCCUPIED SS-104.1, REALLOCATED_STALL_BLOCKED SS-106.1, REBOOKING_UNDONE SS-111.2); Arrived; NoShow; Cancelled |
| Arrived | The first arrival evidence within the arrival window: ARRIVED_QR_SCAN, ARRIVED_SESSION_START or ARRIVED_ATTENDANT (SS-124.1, SS-124.7, SS-125.1, SS-126.1) | Rebooked with MOVED_SESSION_NOT_STARTED when the session does not start, or the "charge not started" exception (SS-107.1 – SS-107.3); Completed (SS-046). Never released after arrival (SS-127.3) and no reallocation (SS-104.7, SS-111.5). |
| NoShow | Grace ended with no arrival: auto-release, RELEASED_NO_ARRIVAL, the system as actor (SS-127.2) | — A late arrival keeps NoShow and sets the late flag (SS-128.1), and its re-offer creates a new booking (SS-011.2, SS-128.3); cancelling is refused (SS-132.4) |
| Cancelled | The driver, the booker or the fleet cancels before arrival (CANCELLED_BY_DRIVER, CANCELLED_BY_BOOKER, CANCELLED_BY_FLEET, SS-013.1, SS-013.6), or ops release it (RELEASED_BY_OPS, with the effect of a cancellation and never a no-show, SS-016.3, SS-016.5) | — A late cancellation carries a mark (SS-132.2) |
| Completed | A session record is matched (COMPLETED_SESSION_MATCHED, SS-046.1), or ops close the booking's reconciliation case with a manual match or "accepted without a session record" (SS-046.2). An Arrived booking with neither stays Arrived after its window (SS-046.5). The default completed definition counts this state (SS-229.2). | — Final: commands on it are refused (SS-046.4) |

**Rebook.** A rebook keeps the booking id and changes its slot, site or EVSE (SS-011.3, SS-108.6, SS-114.1) with
MOVED_CHARGER_FAULT, MOVED_MAINTENANCE, MOVED_SITE_FULL, MOVED_SESSION_NOT_STARTED or REBOOKED_BY_OPS. Its allocation is
deactivated at once (SS-102.5). A booking rebooked to a later slot is Confirmed again and is allocated at its new
allocation offset (G-4).

**v0 states removed:** Held and Expired (now the hold's lifecycle), AllocationFailed (a site-full mark), StationHeld,
StationHoldUnacknowledged and StationHoldFailed (station-hold answers), ChargeFailed (a rebook or an exception),
Charging ("charging started" is evidence only, SS-225, SS-315), Moved (a rebook keeps the id; "move" is an avoided term
in the glossary) and Settled (in no SS or task).

### Other lifecycles

OpsException: open, closed, resolved (SS-219). NoShowDispute: open, then decided to reverse or keep the fee (SS-134).
FleetInvoice: issued once, then a payment status and an overdue flag (SS-404, SS-409). ReconciliationCase: open, then
closed with one of five outcomes (SS-408). MigrationRun: per SS-417.

## 4. Invariants

| # | Invariant | Basis |
|---|---|---|
| INV-1 | No two active allocations on the same EVSE overlap in time, on half-open ranges with the buffer of the booking's parameter version. The database enforces it for every writer, the database role included; a violation maps to EVSE_TAKEN, never to a server error. | SS-102.1, SS-102.2, SS-103.2, SS-103.3, SS-103.5; ADR-006 |
| INV-2 | Every bookable slot falls under exactly one capacity rule, whose cap is at most the site's EVSE count. A new hold or booking is accepted only if unexpired holds and confirmed bookings, with the buffer and manual-hold units, stay within the cap for every slot it covers. A fault keeps the cap and removes the EVSE from the pool, and the bookings confirmed last yield. A lowered cap or reduced hours keep existing bookings and mark those above the limit. Fleet-priority units go only to that fleet. Carried-over bookings may exceed the cap. No overbooking option. | SS-001.2, SS-003.2, SS-018.2, SS-019.1, SS-023.2, SS-023.3, SS-108.2, SS-108.3, SS-421.6, SS-421.7; A-050 |
| INV-3 | An allocation's EVSE has a connector the vehicle can use natively or with an adapter allowed by the vehicle's override, else the fleet's policy, at check time. A booking without a vehicle has no compatible EVSE. | SS-004.2, SS-101.5 |
| INV-4 | One idempotency key gives one result: the key is looked up first, a different request with the same key gets 409, and keys are kept at least 7 days; a form resend reuses its key. An inbound message id counts as processed only once its effect has committed, after the signature check. Status events apply once, in observed-at order. At most one outbound message per booking, recipient and kind, and delivery status never goes back. | SS-014.2 – SS-014.5, SS-200.3 – SS-200.5, SS-236.2, SS-237.2, SS-300.6, SS-302.9, SS-307.2, SS-309.3, SS-317.4 |
| INV-5 | A hold stops counting at its expiry instant, whatever its timer does; a cancellation frees capacity at once. | SS-002.6, SS-013.2 |
| INV-6 | Every booking state change, and every ops action that changes no state, has an actor, the actor's role and a catalogue reason code; codes are never renamed or reused. Corrections are new entries; outage entries keep both times. A failed audit write rolls the change back; no role can update or delete audit entries, which hold ids only. | SS-020.2 – SS-020.4, SS-020.6, SS-020.9, SS-130.3, SS-131.4, SS-235.2, SS-332.2, SS-332.3, SS-332.7 |
| INV-7 | A ledger transaction has at least two entries, balances per currency and posts atomically; an entry's currency is its account's; no balance is stored. | SS-400.2 – SS-400.5 |
| INV-8 | A booking has at most one no-show fee line, posted only on an Arrival & no-show request, with at most one reversal or waiver and no waiver once invoiced; any fee exclusion means no automatic fee; a rebook or an ops release is never a no-show. The fee line is separate from energy and is reversed without changing energy lines. | SS-016.5, SS-108.5, SS-131.2, SS-401.2, SS-401.4, SS-402.6, SS-402.8; REQ-211, REQ-212 |
| INV-9 | Status age is the time since the last receipt; for connected sites a status older than 60 seconds is shown as stale, attendant-view status never is, and no status is guessed. Each site has one live status source; the CSV, discovery data and driver reports never change status. | SS-200.6, SS-202.3, SS-202.4, SS-206.1, SS-206.2 |
| INV-10 | Raw location is admitted only with the driver's opt-in, inside the window from reminder to end of grace, and deleted once arrival is derived or at end of grace at the latest; a fleet's authorisation is not an opt-in. Vehicle data is read only under an authorisation in force and in scope. Location is shown only in an open dispute, and every view is logged. | SS-043.4 – SS-043.6, SS-135.4, SS-135.5, SS-340.2 – SS-340.4, SS-341.2, SS-341.3, SS-341.5 |
| INV-11 | Every source record has one migration outcome and at most one platform copy per (system, id); provenance is immutable; a migrated booking gets no ledger entry, workflow or message; the merge does not depend on source order. | SS-410.2, SS-416.11, SS-417.1, SS-417.7, SS-418.5, SS-419.8 |
| INV-12 | A walk-up is never displaced: allocation chooses only an EVSE whose status is available, with no maintenance hold and no overlapping allocation; no station hold or stop command goes to an EVSE in use, and no walk-up is asked to leave. | SS-101.2, SS-104.4 |
| INV-13 | A booking's site parameter and partner terms versions are fixed at confirmation and replaced only by a rebook to another site. | SS-003.6, SS-011.3, SS-026.5, SS-027.3 |
| INV-14 | End of grace is the slot start plus the site's grace plus extensions, and the extensions total at most the site's maximum. | SS-127.1, SS-130.2 |
| INV-15 | Booking codes are unique; a booking's fleet is its vehicle's fleet, and a retired vehicle cannot be booked. | SS-003.8, SS-006.1, SS-006.4 |
| INV-16 | A number is a driver or booker-only in a fleet, never both, and its right to book for the fleet ends at removal. | SS-042.2, SS-042.3, SS-319.1, SS-319.4 |
| INV-17 | One open exception per type and key; at most one open dispute per no-show, opened within the dispute window. | SS-134.3, SS-134.5, SS-219.2 |
| INV-18 | One invoice per fleet and month; a charge's month is its final slot's month in the site's time zone; issued lines never change; credits never exceed charges; nothing in an open reconciliation case is invoiced; a session record is unique per source and external id. | SS-404.3, SS-404.4, SS-406.2, SS-406.5, SS-407.4, SS-408.3 |
| INV-19 | Retention never deletes booking, audit or ledger rows, and deletions are re-applied after a restore; no link is kept from a number to its pseudonym; listed identifiers are encrypted and every read is audited, and unlisted ones are not stored. | SS-336.3, SS-336.7, SS-337.5, SS-342.2, SS-342.5 |
| INV-20 | The hidden test site and its holds are kept out of every capacity view, report, invoice and message. | SS-428.5 |

## 5. Gaps found in the revision

Gaps the v1 revision found in the approved system stories and tasks, and how CR-013 (2026-10-29) settled them.

| # | Gap | Settled by |
|---|---|---|
| G-1 | No clause moved a booking to Completed, yet the default completed definition counts that state (SS-229.2, T-547), so the north-star count would have stayed at zero (K: REQ-224, REQ-091, REQ-132). | SS-046 (new) and T-209 (new); the reason codes join SS-020 (v3). |
| G-2 | T-1007 creates a fleet's Stripe customer "from the fleet's billing contact (SS-040)", but no clause or task recorded one (K: REQ-083, REQ-084, REQ-087). | SS-040 v2 clauses 6 and 7, T-180 v2. For the pilot fleets, Q-067 may reuse their Stripe customers. |
| G-3 | No clause or task created the station operator record that sites and station-portal users refer to (SS-028.1, SS-323.1). | A minimal record created with the site, T-108 v2. No new behaviour. |
| G-4 | No clause named the state of a booking rebooked to a later slot. | Section 3: Confirmed again, allocated at its new allocation offset. T-122 implements it. |
| G-5 | No clause said whether the stall in the allocation message (REQ-200) is the EVSE label. | The EVSE label is the stall name; site staff confirm the labels at onboarding in Phase 0. |
| G-6 | DriverRemoval (SS-319) and DriverRegistration.removed at (SS-037) recorded the same fact. | One record in Fleet & vehicles; Identity reads it (T-181, T-745). |

The SS-020 notes no longer refer to a station-hold booking state (SS-020 v3).

## 6. Changes from v0

- **New:** the configuration versions, idempotency keys, ops exceptions, station-hold answers and modes, the arrival
  and fee entities, EVSE status freshness and feed state, CSMS records, fleet registrations, identity, messaging
  agreements and consent texts, reconciliation cases, invoice lines, the audit and privacy records, migration and
  cut-over records, the outbox and the outage copy.
- **Replaced:** BookingEvent → BookingStateChange; StatusEvent → StatusObservation and StatusReceipt; AttendantReport →
  observations with the attendant view as source and attendant arrival evidence; Dispute → NoShowDispute; Notification →
  OutboundMessage; Consent → MessagingAgreement, ConsentAcceptance and LocationOptIn; TelematicsLink →
  VehicleDataAuthorisation; FleetPolicy → the fleet's adapter policy and DriverVehicleLimit (payer, fee after re-offer and
  spend limits are parked with Q-002, Q-003); User/Role → PartnerUser and staff roles.
- **Dropped:** CapacityUnit (the cap and pool are computed at query time, T-124, T-126); Tariff (the fee comes from
  PartnerTermsVersion, SS-401.1); DiscoveryStation (REQ-030 is I); Payout and subscription charges (parked, Q-001).
- **Lifecycle:** see section 3.
