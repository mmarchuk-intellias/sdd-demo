---
id: EPICS
type: epics
title: Amperlane Platform v1 epics and feature blocks
status: approved
owner: Mykola Marchuk
version: 2
kyiv: null
parents: [REQUIREMENTS]
sources: [SRC-D1, SRC-C1, SRC-C2, SRC-D2, SRC-R1]
---
# Epics and feature blocks

Step 3.0 (playbook §5, prompt P3.0), 2026-10-28. This file groups the 330 active requirements of the approved
[requirements list](../20-requirements/requirements.md) (Gate 2) into 14 epics (`EP-##`) and 60 feature
blocks (`FT-##.#`). Epics are named in Amperlane's business vocabulary ([glossary](../01-context/glossary.md)).
They are containers for stories (Step 3.1), not a delivery order, and may be regrouped at Step 4.2 (playbook §10.4).

- **Each active requirement is in exactly one feature.** The REQ ids in an `FT` row are its members
  (`tools/trace.py` checks this). The five deprecated rows (REQ-068, REQ-098, REQ-099, REQ-157, REQ-261) are in no
  feature.
- **Parked (V) rows are placed** in the feature they would join if the client chose them, so a change request lands
  in the right container. FT-03.6 and FT-10.5 – FT-10.8 hold only V rows: they are the options of undecided client
  decisions (Q-001, Q-002, Q-003) and out-of-scope pricing ideas.
- **Stated and unstated rows mix** within a feature. A non-functional row sits in the feature it constrains; only
  cross-cutting ones go to the enabling epics EP-13 and EP-14.
- **KYIV** in the summary is the provisional value from requirements.md; a feature has no KYIV of its own, and
  stories inherit it from their requirements.

## Epics

| EP | Title | Grouping logic |
|---|---|---|
| EP-01 | Booking a slot | Everything that decides whether a booker gets a slot: the slot calendar and capacity rules, holds, confirmation and cancellation, connector compatibility, booking for another driver, the shift-change burst, and the site, time-zone and vehicle data the calendar is computed from. |
| EP-02 | Allocation and station hold | What happens between confirmation and arrival to secure one EVSE: late allocation from the pool, the station hold by charger reservation (pattern A) or by site staff (patterns B and C), occupied EVSEs and walk-ups, and the attendant view site staff use for it. |
| EP-03 | Arrival, grace and no-shows | How arrival is evidenced and what follows when it is missing: grace, auto-release, late arrival, the no-show fee and its exclusions, and disputes, together with the parked fee-payer and grace-extension options that would change these rules. |
| EP-04 | Charger faults and rebooking | The charger-fault path end to end: detecting a fault from any source, rebooking the affected bookings automatically, and the ops work for bookings the platform could not place. |
| EP-05 | CSMS connections and live EVSE status | The adapters to each station operator's CSMS and the EVSE status and price data they deliver (pilot sites now, OCPI and further networks parked), kept apart because every booking epic depends on them and none owns them. |
| EP-06 | Driver channel | Everything the driver touches: the driver PWA, SMS and WhatsApp, identity by registered mobile number and signed links, booking messages, languages and consent, and the deep links to navigation and the Uber or Lyft driver app. |
| EP-07 | Ops console | The tools Amperlane ops use instead of the Amperlane Concierge tools: one exception queue and live site board, booking on behalf and overrides, and manual holds. |
| EP-08 | Fleet portal | What a fleet manager sets up and sees: drivers, vehicles and fleet policies (parked booking limits included), and the fleet's bookings, no-shows and usage. |
| EP-09 | Station portal | What a station operator controls and sees for its sites: bookable hours, capacity rules and tariffs, upcoming bookings, the impact of charger faults and the off-peak sessions Amperlane brings. |
| EP-10 | Money, ledger and invoicing | Money that holds under every business model (ledger, monthly fleet invoice, payment provider, reconciliation and collections) first, then the parked revenue-model and pricing options (Q-001) as V-only features, so a client decision lands in one container. |
| EP-11 | Reporting and metrics | The north-star metric and every report computed from booking evidence: completed bookings and the Series A data room, then site, fleet, ops-workload and unit-cost reports. |
| EP-12 | Pilot migration and cut-over | Moving from the Amperlane Concierge to Amperlane Platform v1: loading and cleaning the pilot history, protecting the pilot data, and switching live bookings over at launch. |
| EP-13 | Security, privacy and compliance | Controls that apply across modules rather than to one feature: access, audit trail, encryption and secrets, breach readiness, retention and the data register, and SOC 2 readiness; privacy rules that constrain one feature (location, dispute evidence) stay with that feature. |
| EP-14 | Platform reliability and operations | Enabling qualities with no single user-facing home: availability and outage fallback, durable booking timers, idempotent commands and webhooks, architecture and test environments, and Amperlane's ownership of code and knowledge. |

## Feature blocks

### EP-01 · Booking a slot

| FT | Title | Requirements |
|---|---|---|
| FT-01.1 | Slot calendar and capacity rules | REQ-001, REQ-004, REQ-005, REQ-006, REQ-152, REQ-327, REQ-330 |
| FT-01.2 | Holds, confirmation and cancellation | REQ-002, REQ-008, REQ-039, REQ-041, REQ-145, REQ-147, REQ-150 |
| FT-01.3 | Vehicle and connector compatibility | REQ-012, REQ-013, REQ-014, REQ-015 |
| FT-01.4 | Booking for another driver or shift | REQ-009, REQ-010, REQ-011, REQ-201 |
| FT-01.5 | Shift-change burst without double booking | REQ-007, REQ-101, REQ-102, REQ-130, REQ-131 |
| FT-01.6 | Vehicle data and state of charge | REQ-017, REQ-018, REQ-075, REQ-257, REQ-311, REQ-312 |
| FT-01.7 | Site set-up, time zones and new metros | REQ-138, REQ-146, REQ-151, REQ-165, REQ-324, REQ-326 |

### EP-02 · Allocation and station hold

| FT | Title | Requirements |
|---|---|---|
| FT-02.1 | Allocation, occupied EVSEs and walk-ups | REQ-003, REQ-016, REQ-020, REQ-021, REQ-022, REQ-046, REQ-148, REQ-149, REQ-200, REQ-336 |
| FT-02.2 | Charger reservation at pattern A sites | REQ-023, REQ-024, REQ-025, REQ-153, REQ-155, REQ-167, REQ-323 |
| FT-02.3 | Station hold by site staff (patterns B and C) | REQ-026, REQ-027, REQ-035, REQ-114, REQ-154, REQ-156, REQ-170 |
| FT-02.4 | Attendant view | REQ-081, REQ-158, REQ-159, REQ-176 |

### EP-03 · Arrival, grace and no-shows

| FT | Title | Requirements |
|---|---|---|
| FT-03.1 | Arrival by QR scan and CSMS session start | REQ-043, REQ-044, REQ-174, REQ-178, REQ-204 |
| FT-03.2 | Location-based arrival and grace extension | REQ-173, REQ-175, REQ-255, REQ-256, REQ-306, REQ-307 |
| FT-03.3 | Grace, auto-release and late arrival | REQ-033, REQ-034, REQ-037, REQ-038, REQ-040, REQ-042, REQ-177, REQ-305, REQ-334 |
| FT-03.4 | No-show fee rules | REQ-036, REQ-171, REQ-172, REQ-180, REQ-181, REQ-183 |
| FT-03.5 | No-show disputes and evidence | REQ-045, REQ-179, REQ-182, REQ-259 |
| FT-03.6 | No-show fee payer options (Q-002, Q-003) | REQ-298, REQ-299, REQ-300, REQ-301, REQ-302, REQ-303, REQ-304 |

### EP-04 · Charger faults and rebooking

| FT | Title | Requirements |
|---|---|---|
| FT-04.1 | Fault detection and return to service | REQ-047, REQ-191, REQ-192, REQ-193, REQ-194 |
| FT-04.2 | Automatic fault rebooking | REQ-048, REQ-049, REQ-052, REQ-141, REQ-239 |
| FT-04.3 | Ops handling of unplaced bookings | REQ-050, REQ-054, REQ-187, REQ-188 |

### EP-05 · CSMS connections and live EVSE status

| FT | Title | Requirements |
|---|---|---|
| FT-05.1 | Pilot site connections (AMPECO, ChargeLab, LIC CSV) | REQ-028, REQ-031, REQ-032, REQ-105, REQ-162, REQ-332 |
| FT-05.2 | Live EVSE status and staleness | REQ-029, REQ-104, REQ-107, REQ-160, REQ-164, REQ-168, REQ-169 |
| FT-05.3 | OCPI and further CSMS networks | REQ-108, REQ-166, REQ-308, REQ-309, REQ-310, REQ-313, REQ-325, REQ-328 |
| FT-05.4 | Public charging map and prices | REQ-030, REQ-163, REQ-238, REQ-333 |

### EP-06 · Driver channel

| FT | Title | Requirements |
|---|---|---|
| FT-06.1 | Driver PWA and two-tap booking | REQ-019, REQ-059, REQ-063, REQ-100, REQ-321 |
| FT-06.2 | Booking by SMS and WhatsApp | REQ-061, REQ-062, REQ-090, REQ-222, REQ-249 |
| FT-06.3 | Driver identity and secure links | REQ-060, REQ-198, REQ-202, REQ-240, REQ-241, REQ-242 |
| FT-06.4 | Confirmations, reminders and delivery | REQ-067, REQ-088, REQ-089, REQ-203, REQ-219, REQ-221 |
| FT-06.5 | Languages and messaging consent | REQ-112, REQ-199, REQ-220, REQ-248, REQ-250 |
| FT-06.6 | Directions and deep links to Uber and Lyft | REQ-064, REQ-065, REQ-066, REQ-322 |

### EP-07 · Ops console

| FT | Title | Requirements |
|---|---|---|
| FT-07.1 | Exception queue, live site board and driver look-up | REQ-189, REQ-190, REQ-195, REQ-196, REQ-197, REQ-316 |
| FT-07.2 | Ops booking actions and overrides | REQ-055, REQ-056, REQ-057, REQ-058 |
| FT-07.3 | Manual holds: maintenance and fleet priority | REQ-184, REQ-185, REQ-335 |

### EP-08 · Fleet portal

| FT | Title | Requirements |
|---|---|---|
| FT-08.1 | Fleet set-up: drivers, vehicles and policies | REQ-070, REQ-072, REQ-205, REQ-206, REQ-207, REQ-294, REQ-295, REQ-331 |
| FT-08.2 | Fleet bookings, no-shows and usage | REQ-069, REQ-071, REQ-073, REQ-074, REQ-208, REQ-243 |

### EP-09 · Station portal

| FT | Title | Requirements |
|---|---|---|
| FT-09.1 | Bookable hours, capacity rules and tariffs | REQ-076, REQ-077, REQ-078, REQ-082, REQ-186 |
| FT-09.2 | Bookings, fault impact and off-peak value | REQ-051, REQ-079, REQ-080, REQ-094, REQ-209 |

### EP-10 · Money, ledger and invoicing

| FT | Title | Requirements |
|---|---|---|
| FT-10.1 | Double-entry ledger | REQ-085, REQ-086, REQ-210, REQ-211, REQ-212, REQ-247 |
| FT-10.2 | Monthly fleet invoice | REQ-083, REQ-084, REQ-109, REQ-213, REQ-217, REQ-218 |
| FT-10.3 | Payment provider (Stripe) | REQ-087, REQ-110, REQ-111, REQ-244, REQ-245, REQ-246 |
| FT-10.4 | Reconciliation, collections and finance views | REQ-161, REQ-214, REQ-215, REQ-216, REQ-280, REQ-281, REQ-282, REQ-292 |
| FT-10.5 | Fleet pricing and energy resale options (Q-001) | REQ-270, REQ-271, REQ-274, REQ-285, REQ-286, REQ-293, REQ-296 |
| FT-10.6 | Station fees, tariffs and pricing options | REQ-273, REQ-275, REQ-276, REQ-284, REQ-329 |
| FT-10.7 | Station payouts (Q-001) | REQ-272, REQ-277, REQ-287, REQ-288, REQ-289 |
| FT-10.8 | Payout rails and money-transmission compliance (Q-001) | REQ-278, REQ-279, REQ-283, REQ-290, REQ-291, REQ-297 |

### EP-11 · Reporting and metrics

| FT | Title | Requirements |
|---|---|---|
| FT-11.1 | Completed bookings and the Series A data room | REQ-091, REQ-095, REQ-224, REQ-225 |
| FT-11.2 | Performance, ops workload and unit-cost reports | REQ-092, REQ-093, REQ-113, REQ-226, REQ-227, REQ-251 |

### EP-12 · Pilot migration and cut-over

| FT | Title | Requirements |
|---|---|---|
| FT-12.1 | Pilot history migration | REQ-096, REQ-115, REQ-116, REQ-117, REQ-314 |
| FT-12.2 | Pilot data clean-up and protection | REQ-118, REQ-228, REQ-229, REQ-230, REQ-252 |
| FT-12.3 | Cut-over and go-live | REQ-097, REQ-142, REQ-231, REQ-232, REQ-269 |

### EP-13 · Security, privacy and compliance

| FT | Title | Requirements |
|---|---|---|
| FT-13.1 | Roles and organisation-scoped access | REQ-120, REQ-235, REQ-258 |
| FT-13.2 | Audit trail | REQ-053, REQ-121, REQ-126, REQ-262, REQ-263 |
| FT-13.3 | Encryption, secrets and breach readiness | REQ-123, REQ-124, REQ-253, REQ-254, REQ-260 |
| FT-13.4 | Retention, anonymisation and data register | REQ-125, REQ-233, REQ-234, REQ-264, REQ-265 |
| FT-13.5 | SOC 2 Type I readiness | REQ-122, REQ-318, REQ-319, REQ-320 |

### EP-14 · Platform reliability and operations

| FT | Title | Requirements |
|---|---|---|
| FT-14.1 | Availability, maintenance window and outage fallback | REQ-128, REQ-129, REQ-132, REQ-223, REQ-266, REQ-268, REQ-317 |
| FT-14.2 | Durable booking timers | REQ-133, REQ-134, REQ-315 |
| FT-14.3 | Idempotent commands and webhooks | REQ-103, REQ-106, REQ-236 |
| FT-14.4 | Architecture, stack and test environments | REQ-127, REQ-135, REQ-136, REQ-137, REQ-139, REQ-140, REQ-237 |
| FT-14.5 | Amperlane ownership and handover | REQ-119, REQ-143, REQ-144, REQ-267 |

## Did not fit

Every active requirement is placed. These rows fit no single feature well; each is placed in the feature named,
for the reason given. The reviewer may move them at Gate 3 without changing the requirement.

| REQ | Placed in | Why |
|---|---|---|
| REQ-028 | FT-05.1 | It is a rule for the whole booking lifecycle (allocation, grace, no-show, fault rebooking) at all three supply patterns, not a capability of one feature. It sits with the pilot site connections because it is shown by running the same scenario at a site of each supply pattern, each through its own adapter. |
| REQ-058 | FT-07.2 | It is an umbrella over many features: the exception queue, overrides, station holds, fault rebooking and driver messaging. It sits with the ops booking actions as the acceptance check that no pilot tool is still needed; stories for it will mostly link to the other features. |
| REQ-113 | FT-11.2 | It is an outcome across arrival, auto-release and fault rebooking rather than one capability. It sits with the ops-workload reports because it is measured from the audit trail as manual ops actions per booking (REQ-227). |
| REQ-117 | FT-12.1 | It constrains the codebase, not the migration. It sits with the pilot history migration because both come from one decision (ADR-010: discard the prototype, migrate the history). |
| REQ-118 | FT-12.2 | It covers platform data used outside production as well as pilot data. It sits with pilot data protection, next to the rule for the raw pilot export (REQ-252), where requirements.md lists it; FT-13.4 is the alternative home if the reviewer prefers it with the platform-wide privacy rules. |
| REQ-330 | FT-01.1 | Demand response is a grid programme with no feature of its own in v1. It sits with the capacity rules because taking part would mean reducing or shifting bookable capacity at a site for a time window. |
| REQ-331 | FT-08.1 | Autonomous-vehicle fleets and depots are a new kind of fleet and site rather than a capability. It sits with fleet set-up because onboarding such a fleet, whose vehicles have no driver, is where the change would start. |

## Summary for the reviewer

Counts computed from requirements.md (active rows only, provisional KYIV).

| EP | Features | REQs | K | Y | I | V |
|---|---|---|---|---|---|---|
| EP-01 | 7 | 39 | 17 | 13 | 3 | 6 |
| EP-02 | 4 | 27 | 15 | 11 | 0 | 1 |
| EP-03 | 6 | 37 | 9 | 15 | 3 | 10 |
| EP-04 | 3 | 14 | 3 | 10 | 1 | 0 |
| EP-05 | 4 | 25 | 4 | 9 | 6 | 6 |
| EP-06 | 6 | 31 | 15 | 12 | 2 | 2 |
| EP-07 | 3 | 13 | 3 | 8 | 1 | 1 |
| EP-08 | 2 | 14 | 2 | 8 | 1 | 3 |
| EP-09 | 2 | 10 | 0 | 7 | 3 | 0 |
| EP-10 | 8 | 49 | 9 | 13 | 0 | 27 |
| EP-11 | 2 | 10 | 1 | 5 | 4 | 0 |
| EP-12 | 3 | 15 | 4 | 10 | 0 | 1 |
| EP-13 | 5 | 22 | 8 | 8 | 3 | 3 |
| EP-14 | 5 | 24 | 10 | 11 | 1 | 2 |
| **Total** | **60** | **330** | **100** | **140** | **28** | **62** |
