---
id: DATA-MODEL
type: design
title: Core data model (v0 hypothesis)
status: approved
owner: Mykola Marchuk
version: 0
kyiv: null
parents: [BUSINESS-CONTEXT, DESIGN]
sources: [SRC-C1, SRC-C2, SRC-D2]
---
# Core data model, v0 (hypothesis)

> **v0 hypothesis** (playbook §10.1): the core entities, key attributes, relationships and invariants. It is revised
> after Step 3. Names follow the [glossary](../01-context/glossary.md). The slot and booking entities should map onto
> the OCPI 2.3 Booking module later (SRC-C2@00:13:32, SRC-C2@00:13:40).

## 1. Entities

### Supply

| Entity | Key attributes | Notes | Sources |
|---|---|---|---|
| StationOperator | name, kind (CPO \| site host), payout account (if B/C), contacts | Kinship and Jamaica Bay are CPOs; Hunters Point Garages is a site host. | CTX-060, CTX-062 |
| Site | operator, address, geo point, time zone (A-013), supply pattern (A/B/C), CSMS kind, NEVI-funded flag, partner terms (grace, default 10 minutes per A-003; maximum ops grace extension per A-020; payout cadence) | One OCPI Location. | CTX-017, CTX-063, Q-004 |
| EVSE | site, external id per CSMS, reservable flag, status, status observed-at, status source | The reservable flag is set per EVSE, not per site: ops flips it when firmware is fixed. | CTX-060, A-004, Q-013 |
| Connector | EVSE, type (CCS1, NACS), max kW | One EVSE can have more than one connector (Q-013). | CTX-100 |
| CapacityRule | site, days of week, time window, max bookable (count or %), overbooking allowed (default false), valid from/to, set by | The station edits it itself; it also enforces NEVI public access. | CTX-064, CTX-065, CTX-132 |
| StatusEvent | EVSE, status (available, occupied, charging, faulted, unknown…), observed-at, received-at, source (webhook, poll, CSV, attendant), raw payload reference | Time series; dispute evidence. | CTX-091, CTX-112, CTX-127 |
| AttendantReport | site, EVSE, reported status or "driver arrived", reporter, time | A status source at pattern C. | CTX-033, CTX-062 |
| DiscoveryStation | external source (AFDC, OCM), location, connectors, power, attribution | Static layer; never used for availability. | CTX-089 |

### Demand

| Entity | Key attributes | Notes | Sources |
|---|---|---|---|
| Fleet | name, kind (lessor, cab operator), billing contact, invoice terms (net-30) | | CTX-073, CTX-074, CTX-032 |
| FleetPolicy | fleet, no-show payer (fleet, driver, fleet pays and deducts), fee after re-offer, adapter policy, spend limits (allowed sites, max bookings per day) | The values are undecided (Q-002, Q-003, Q-032). | CTX-031, CTX-100, CTX-134 |
| Driver | fleet(s), mobile number, preferred language (EN, ES, BN), preferred channel (SMS, WhatsApp), consent records | No password account (A-006). | CTX-026 – CTX-028 |
| Vehicle | fleet, plate, make/model, native connector, allowed adapters (overrides the fleet policy), max DC kW, telematics link | | CTX-100 |
| TelematicsLink | vehicle, provider (Geotab, Tesla, Smartcar, manual), authorisation reference | Authorisation from the account owner for battery level and vehicle state; vehicle location also needs the driver's consent (A-024). | CTX-099, CTX-109 |
| VehicleReading | vehicle, SoC %, location (only with consent), observed-at, source | A location reading is deleted once its arrival event is derived; location is never kept as a trace (A-025, Q-022). | CTX-101, CTX-108 |
| Consent | driver, purpose (location from the phone or the vehicle), granted-at, revoked-at | Opt-in, off by default, scoped to the booking window (A-024). | CTX-109, Q-016 |

### Booking

| Entity | Key attributes | Notes | Sources |
|---|---|---|---|
| Hold | site, window, vehicle, booker, expires-at, status | A row in Postgres per A-005; TTL from A-001. | CTX-093, CF-017 |
| Booking | site, window (start, end), vehicle, charging driver, booker (driver, a fleet's booker-only number per A-023, fleet manager or ops), channel, status, grace deadline (extendable by an ops override), running-late flag and ETA, idempotency key, created-at | Made against a pool, not an EVSE. Extending grace beyond the station's terms is open (CF-021). | CTX-029, CTX-035, CTX-092, CTX-093, CTX-135 |
| CapacityUnit | site, 15-minute slot start, capacity class (connector type in SRC-D2#12), bookable, committed | The pre-allocation capacity check (A-014). It is Intellias' design, not agreed with the client (ADR-006). It must also account for adapters, power and buffers. | SRC-D2#12, CTX-064, CTX-100 |
| Allocation | booking, EVSE, time range (incl. buffer), active flag, allocated-at | The exclusion constraint lives here (ADR-006). | CTX-092, CTX-093 |
| StationHoldAttempt | booking, EVSE, method (ReserveNow, signage, attendant, ops), sent-at, result, response | Dispute evidence. | CTX-088, CTX-127 |
| BookingEvent | booking, from-state, to-state, reason code, actor (system or user), time | Append-only; feeds the audit log. | CTX-036, CTX-110 |
| ArrivalEvidence | booking, kind (session start, QR scan, geofence, attendant), time | | CTX-102 |
| ManualHold | site or EVSE, window, reason (maintenance, fleet priority), set by | An ops action. A maintenance hold reassigns affected bookings as on a fault; a fleet-priority hold leaves confirmed bookings standing (A-018). | CTX-035 |
| Offer | booking (lost), proposed site/window/EVSE, expires-at, accepted | A re-offer after a no-show, a lost slot or a fault. | CTX-133, CTX-136 |

### Money (structure only; amounts and flows wait for Q-001)

| Entity | Key attributes | Notes | Sources |
|---|---|---|---|
| Tariff | operator or site, kind (station B2B, fleet bundled, fee), price per kWh or per event, valid from/to | The shape depends on the business model. | CTX-116, CTX-121 |
| SessionRecord | site, EVSE, source (OCPI CDR, AMPECO, ChargeLab, CSV), external id, energy kWh, start, end, cost, received-at | The unit of truth for consumption. | CTX-127 |
| BookingSessionMatch | booking, session record, match method, confidence | | CTX-127 |
| Charge | subject (a booking, or a vehicle-month for a subscription), kind (energy, booking fee, no-show fee, subscription), amount, payer, status | The no-show fee is its own line. A subscription is per vehicle per month, not per booking. | CTX-116, CTX-127 |
| LedgerAccount | owner (fleet, operator, Amperlane, payment-provider clearing), kind | | CTX-095 |
| LedgerEntry | transaction id, account, debit/credit, amount, currency, posted-at, reference | Double-entry, append-only. | CTX-095 |
| FleetInvoice | fleet, period (month), due date (net-30), lines, external invoice id, status | | CTX-032 |
| Payout | operator, period (week), amount, external transfer id, status | Only if options B/C. | CTX-068, CTX-128 |
| Dispute | charge, raised by, reason, evidence references, outcome, decided by | | CTX-035, CTX-127 |

### Cross-cutting

| Entity | Key attributes | Notes | Sources |
|---|---|---|---|
| User / Role | person, organisation, role (fleet manager, station operator, attendant, ops, finance) | | CTX-024, CTX-025 |
| AuditEvent | actor, action, target, reason, time, request id | Append-only; covers every state change, override, manual action and payout. | CTX-110 |
| InboundMessage | provider message id (dedupe key), from number, body, received-at, processed-at | Fixes today's duplicate-confirmation bug. | CTX-044, CTX-093 |
| Notification | recipient, channel, template, language, status, provider id | | CTX-097 |
| MigrationRecord | source system (Airtable, Sheets, Stripe, Twilio), source id, original status value, mapped entity, cleansing notes | Provenance for the Series A data room. | CTX-053, CTX-054 |

## 2. Relationships

| From | To | Cardinality | Note |
|---|---|---|---|
| StationOperator | Site | 1 : n | |
| Site | EVSE | 1 : n | |
| EVSE | Connector | 1 : n | |
| Site | CapacityRule | 1 : n | Windows must not overlap for the same days (INV-2). |
| EVSE | StatusEvent | 1 : n | |
| Fleet | Vehicle | 1 : n | |
| Fleet | Driver | n : m | A driver may drive for more than one fleet (A-016). |
| Fleet | FleetPolicy | 1 : 1 (versioned) | |
| Booking | Vehicle | n : 1 | |
| Booking | Driver (charging), booker | n : 1 each | The booker may differ from the charging driver. |
| Booking | Allocation | 1 : 0..n | Only one active allocation at a time; re-allocations keep history. |
| Booking | BookingEvent | 1 : n | |
| Booking | SessionRecord | 1 : 0..1 (via match) | A session record may also exist without a booking (walk-up). |
| Booking | Charge | 1 : n | Subscription charges hang off a vehicle-month instead. |
| Charge | LedgerEntry | 1 : n | |
| Fleet | FleetInvoice | 1 : n | |
| StationOperator | Payout | 1 : n | |
| Charge | Dispute | 1 : 0..n | |

## 3. Booking lifecycle

The happy path is from SRC-D2#7 and SRC-C2@00:27:21; side paths are from SRC-C2@00:27:57, SRC-C2@00:24:04,
SRC-C2@00:21:33 and SRC-C2@00:47:53. Timings (T-15, T-10, grace) are assumptions A-001 – A-003. Every state that
can fail has an exit; none waits for a capability that is unconfirmed (U-6, U-7, U-14).

| State | Entered when | Leaves to |
|---|---|---|
| Held | A hold is created against the site pool | Confirmed; Expired (TTL) |
| Confirmed | The booker confirms | Allocated; AllocationFailed; Cancelled; Moved |
| AllocationFailed | No compatible EVSE is free at T-15 (e.g. the site is full of walk-ups) | Allocated (an EVSE frees up, or ops intervenes); Moved (re-offer accepted); Cancelled. Ops is alerted (SRC-C2@00:24:04). |
| Allocated | An EVSE is assigned at T-15 | StationHeld; StationHoldUnacknowledged; StationHoldFailed; Cancelled |
| StationHeld | The charger accepted the reservation (pattern A), or site staff acknowledged the signage request (B/C) | Arrived; NoShow; StationHoldFailed (the EVSE is still in a session at T-10); Moved (fault); Cancelled |
| StationHoldUnacknowledged | The signage or attendant request was not acknowledged ("sometimes the cone doesn't happen", SRC-C2@00:21:33) | Arrived; NoShow; StationHoldFailed. Ops sees an exception, but the booking stays valid. |
| StationHoldFailed | The charger rejected the hold, or reports the EVSE occupied or overrunning | Allocated (reassigned to another EVSE); Moved; AllocationFailed |
| Arrived | An arrival signal is received (session start, QR, geofence, attendant) | Charging; ChargeFailed |
| ChargeFailed | The driver arrived but the charger didn't start (SRC-C2@00:47:53) | Allocated (another EVSE); Moved; a dispute or fault case (no no-show fee) |
| Charging | The session is live, from CSMS status or as reported by the attendant | Completed |
| Completed | The session ended, **and** either a session record is matched or ops/the attendant confirmed it (fallback while session records are unconfirmed, flagged for reconciliation) | Settled (only where settlement applies, Q-001) |
| Settled | Invoiced and, if options B/C, paid out | — |
| NoShow | No arrival within grace | — (a fee line per policy Q-002; a re-offer may create a new booking) |
| Cancelled | The driver (one tap, at any point before arrival), the fleet or ops cancels | — |
| Moved | Rebooked after a fault, a failed hold or a failed allocation, with a reason code | — (the new booking continues) |
| Expired | The hold TTL passed without confirmation | — |

## 4. Invariants

| # | Invariant | Basis |
|---|---|---|
| INV-1 | No two active allocations on the same EVSE overlap in time, buffer included. The database enforces this, not only the application. | CTX-093, ADR-006 |
| INV-2 | A new hold or booking is accepted only if the committed capacity for every slot it covers stays within the bookable capacity of the capacity rule in force. Overbooking is off unless the rule allows it. Existing bookings are never dropped silently. When a station lowers its cap or ops adds a fleet-priority hold, confirmed bookings stand and the new limit applies to new bookings only; the bookings above it are shown to the station or ops for explicit action (A-018, Q-035). When physical capacity drops (an EVSE faults or is held for maintenance), each affected booking is re-checked and, if it no longer fits, reassigned automatically with a reason code (A-017, A-018); whether a move may exceed the bookable cap is open (Q-038). | CTX-064, CTX-065, CTX-132, CTX-136 |
| INV-3 | An allocation's EVSE has a connector the vehicle can use natively or with an adapter allowed for that vehicle. | CTX-100 |
| INV-4 | Two requests with the same idempotency key give one booking; an inbound message with an already-seen provider message id is processed once. | CTX-093 |
| INV-5 | A hold not confirmed before expiry no longer counts against capacity. | CTX-093, A-001 |
| INV-6 | Every booking state change has an actor and a reason code; BookingEvent and AuditEvent are append-only. | CTX-036, CTX-110 |
| INV-7 | Ledger entries are append-only, and each transaction balances: debits equal credits. | CTX-095 |
| INV-8 | A no-show fee is a separate Charge from energy and can be reversed without changing energy charges. | CTX-127 |
| INV-9 | Every status shown to a user carries its observed-at time. For connected sites, status older than 60 seconds is shown as stale. | CTX-112 |
| INV-10 | Location, from the phone or the vehicle, is stored only with an active consent, and only for the retention period of its data type (A-025). | CTX-108, CTX-109, Q-022 |
| INV-11 | Every migrated record keeps its source system, source id and original status value. | CTX-053, CTX-054 |
| INV-12 | A walk-up is never displaced: allocation chooses only EVSEs that are free, or expected to be free, at the slot start. | CTX-066 |
