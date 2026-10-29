---
id: TASKS
type: tasks-index
title: Task index
status: approved
owner: Mykola Marchuk
version: 3
kyiv: null
parents: [EPICS]
sources: []
---
# Task index

Human-readable index of [tasks.yaml](tasks.yaml), the machine-readable source. Generated; do not edit by hand.

## EP-01

| Task | Title | Type | KYIV | Implements | Depends on | Chain depth |
|---|---|---|---|---|---|---|
| T-100 | Create the inventory module with site, EVSE and connector records and the site's bookable status | data | K | SS-030, SS-028 | T-900, T-906, T-998, T-1001 | 4 |
| T-101 | Hold the per-site and platform-wide booking parameter catalogue as versions with defaults | backend | K | SS-026 | T-100 | 5 |
| T-102 | Change booking parameters through the ops API with validation, new versions and change events | backend | K | SS-026 | T-101, T-207, T-909, T-911 | 6 |
| T-103 | Store capacity rules and bookable hours and validate that each bookable slot has exactly one cap | backend | K | SS-023 | T-100 | 5 |
| T-104 | Save capacity rules and bookable hours in force at once, with walk-up figures and a reduced-hours event | backend | K | SS-023, SS-024 | T-103, T-207, T-742, T-909, T-911 | 7 |
| T-107 | Mark a site live only when its onboarding data and fee terms are complete | backend | K | SS-028, SS-027 | T-100, T-103, T-106, T-207, T-909, T-911 | 6 |
| T-108 | Onboard a site as data through the ops API with code, time zone and CSMS checks | backend | K | SS-028 | T-101, T-103, T-106, T-107, T-909, T-911 | 7 |
| T-120 | Create the booking module with hold, booking, offer and manual-hold tables and the booking code | data | K | SS-003, SS-005, SS-006 | T-100, T-900, T-906, T-998, T-1001 | 5 |
| T-121 | Lay out site time grids in the site's time zone and handle daylight-saving changes | backend | K | SS-021 | T-101, T-103, T-120 | 6 |
| T-124 | Place holds on the site's grid with the cap check, the hold time and typed refusals | backend | K | SS-002, SS-001 | T-100, T-101, T-103, T-120, T-121, T-909, T-911 | 7 |
| T-126 | Check pool feasibility of a booking against compatible EVSEs with the site's buffer | backend | K | SS-003 | T-120, T-130, T-505 | 11 |
| T-127 | Confirm a held booking with the cap re-check and the pool check, fixing its terms | backend | K | SS-003, SS-002, SS-014 | T-101, T-106, T-122, T-125, T-126, T-129, T-909, T-911 | 12 |
| T-128 | Record carried-over bookings requested by the cut-over | backend | K | SS-003 | T-127 | 13 |
| T-130 | Apply one connector-compatibility rule from the vehicle profile and adapter policy | backend | K | SS-004 | T-100, T-124, T-183, T-184 | 9 |
| T-131 | Record the booker and the charging driver from the fleet's registrations | backend | K | SS-005 | T-127, T-181, T-182, T-742 | 13 |
| T-132 | Check that the booking vehicle is registered, allowed for the driver and not retired | backend | K | SS-006 | T-124, T-183, T-185, T-909, T-911 | 9 |
| T-133 | Answer open-slot queries with exactly the start times a hold would accept | backend | K | SS-001 | T-124, T-130, T-909, T-911 | 10 |
| T-134 | Decide hold and confirmation requests per site in the order they reached the platform | backend | K | SS-007 | T-125, T-127 | 13 |
| T-135 | Measure booking-operation latency from the platform edge and check it at design load | backend | K | SS-008 | T-133, T-134, T-138, T-140, T-905, T-907, T-908, T-913, T-932 | 14 |
| T-136 | Run the five-times burst load test and record its result as the release gate | qa | K | SS-008 | T-135, T-300, T-302, T-932, T-933 | 17 |
| T-140 | Cancel an active booking in one request and return its capacity at once | backend | K | SS-013 | T-127, T-742, T-909, T-911 | 13 |
| T-141 | State the allocation and station hold on the booking-cancelled event | backend | K | SS-013 | T-140, T-300, T-304 | 15 |
| T-142 | Confirm an afternoon and an overnight slot together, each decided on its own | backend | Y | SS-012 | T-127, T-134, T-909, T-911 | 14 |
| T-149 | Prove one booking core across supply patterns, time zones and entry points | qa | K | SS-002, SS-004, SS-021 | T-121, T-127, T-133, T-137, T-139 | 15 |
| T-160 | Start one workflow per hold from the outbox and expire unconfirmed holds | backend | K | SS-032, SS-034 | T-127, T-900, T-906, T-998, T-1001 | 13 |
| T-161 | Schedule booking timers from the parameter version fixed at confirmation | backend | K | SS-032 | T-101, T-128, T-160 | 14 |
| T-162 | Move or cancel a booking's timers when it is rebooked, extended, cancelled or ends | backend | K | SS-032 | T-161, T-303 | 15 |
| T-182 | Register booker-only numbers apart from the fleet's drivers | backend | K | SS-042 | T-181, T-742, T-909, T-911 | 8 |
| T-189 | Record, show and revoke a fleet's vehicle-data authorisation and guard vehicle-data reads | backend | Y | SS-043 | T-183, T-742, T-798, T-909, T-911 | 15 |
| T-190 | Store an optional manual state of charge and keep booking free of vehicle data | backend | K | SS-044 | T-127, T-183 | 13 |
| T-200 | Build the ops console screens for site onboarding and going live | frontend | K | SS-028 | T-107, T-108, T-511 | 19 |
| T-201 | Build the ops console screens for booking parameters, partner terms, reservable flags and QR sheets | frontend | K | SS-026, SS-027, SS-029, SS-031 | T-102, T-106, T-109, T-110, T-511 | 19 |
| T-202 | Add bookable hours and walk-up figures to the capacity-rule screens of the station portal and ops console | frontend | K | SS-023, SS-024 | T-104, T-534, T-535 | 20 |
| T-300 | Create the allocation table with the database no-overlap constraint | data | K | SS-103, SS-102 | T-100, T-101, T-127, T-183, T-900, T-906, T-998, T-1001 | 13 |
| T-763 | Send one-tap cancel and accept actions at once, with one idempotency key per tap | frontend | K | SS-327 | T-129, T-138, T-139, T-140, T-748, T-760 | 16 |
| T-765 | Show booking times in the site's time zone with the abbreviation in force | frontend | Y | SS-329 | T-121, T-760 | 16 |
| T-768 | Add running-late, fault and blocked-stall actions and show each one-tap action's result | frontend | K | SS-327 | T-334, T-338, T-352, T-517, T-763 | 22 |

## EP-02

| Task | Title | Type | KYIV | Implements | Depends on | Chain depth |
|---|---|---|---|---|---|---|
| T-109 | Let ops set the reservable flag of each EVSE with effect at once | backend | K | SS-029 | T-100, T-207, T-909, T-911 | 5 |
| T-137 | Find cross-site alternatives ranked by distance from the booked site | backend | K | SS-010 | T-101, T-124, T-130 | 10 |
| T-301 | Choose the EVSE for an allocation - compatible, free, lowest sufficient power | backend | K | SS-101 | T-100, T-130, T-145, T-183, T-300, T-505 | 14 |
| T-302 | Allocate each confirmed booking at its allocation offset | backend | K | SS-100, SS-102 | T-101, T-122, T-139, T-141, T-161, T-300, T-301 | 16 |
| T-304 | Create the station-hold record and its time-ordered read | data | K | SS-121 | T-300, T-900 | 14 |
| T-305 | Handle site-full bookings with an ops exception and immediate alternatives | backend | K | SS-105 | T-102, T-122, T-125, T-137, T-139, T-302, T-303, T-507, T-510 | 17 |
| T-306 | Reallocate bookings whose EVSE is in use at the station-hold offset or the pre-arrival check | backend | K | SS-104, SS-105 | T-122, T-161, T-301, T-302, T-303, T-305, T-505 | 18 |
| T-316 | Run the station-hold step and send site-staff requests to the attendant view | backend | K | SS-118 | T-101, T-109, T-122, T-161, T-303, T-304, T-306 | 19 |
| T-317 | Request charger reservations at the station-hold offset | backend | K | SS-116 | T-101, T-109, T-303, T-304, T-306, T-316, T-500 | 20 |
| T-318 | Fall back to site staff when a charger reservation is rejected or unanswered | backend | K | SS-117, SS-121 | T-122, T-304, T-306, T-316, T-317, T-500, T-505, T-507, T-780 | 21 |
| T-319 | Send site-staff requests by SMS and take SMS replies as acknowledgements | backend | K | SS-118 | T-101, T-316, T-700, T-702, T-705, T-706 | 20 |
| T-320 | Raise an ops exception when a site-staff request is not delivered in time | backend | K | SS-118, SS-121 | T-101, T-160, T-161, T-164, T-304, T-316, T-507 | 20 |
| T-321 | Clear station holds on release, cancellation or rebooking | backend | K | SS-120 | T-101, T-139, T-141, T-144, T-303, T-304, T-317, T-319, T-320, T-500, T-507 | 21 |
| T-322 | Switch a site to manual mode and give ops the timed station-hold list | backend | K | SS-123 | T-122, T-124, T-127, T-129, T-316, T-317, T-321, T-741, T-780, T-911 | 22 |
| T-323 | Record station holds arranged by ops and fail unarranged ones at the end of grace | backend | K | SS-123 | T-122, T-129, T-141, T-303, T-304, T-322, T-510, T-741, T-911 | 23 |
| T-324 | Follow grace extensions in charger reservations and site-staff clear times | backend | K | SS-116, SS-118 | T-303, T-317, T-318, T-319, T-500 | 22 |
| T-325 | Raise 'contact the site' at the pre-arrival check for unacknowledged requests | backend | K | SS-119 | T-303, T-304, T-306, T-316, T-323, T-507, T-510 | 24 |
| T-326 | Run Gowanus station holds through site staff while AMPECO is down or stale | backend | Y | SS-122 | T-316, T-317, T-318, T-320, T-500, T-505, T-506 | 22 |
| T-330 | Record arrival confirmed by the site's attendant | backend | K | SS-126 | T-122, T-129, T-303, T-751, T-911 | 14 |
| T-331 | Add the 'driver arrived' action to the attendant view | frontend | K | SS-126 | T-330, T-544 | 20 |
| T-338 | Store blocked-stall reports and count them as failed station holds | backend | K | SS-133 | T-129, T-302, T-303, T-304, T-332, T-336, T-507, T-747, T-911 | 19 |
| T-339 | Reallocate a booking after a blocked-stall report | backend | K | SS-106 | T-301, T-306, T-338 | 20 |
| T-347 | Ops console - switch a site's station holds to manual mode and back | frontend | K | SS-123 | T-322, T-528 | 23 |
| T-520 | Send Gowanus charger reservations through AMPECO with typed results | integration | K | SS-212 | T-101, T-109, T-165, T-500 | 9 |
| T-521 | Cancel AMPECO charger reservations with retry until confirmed or expired | integration | K | SS-212 | T-101, T-102, T-165, T-520 | 10 |
| T-544 | Build the attendant view shell with today's due drivers by EVSE | frontend | K | SS-228 | T-101, T-141, T-302, T-306, T-312, T-332, T-742, T-743, T-751, T-786, T-911, T-912 | 19 |
| T-545 | Show station-hold requests and clear instructions in the attendant view with delivery and acknowledgement | frontend | K | SS-228 | T-129, T-316, T-321, T-511, T-544, T-751, T-911 | 22 |
| T-714 | Tell the charging driver the allocated EVSE and stall, and each reallocation | backend | K | SS-301 | T-302, T-306, T-329, T-702, T-704 | 19 |
| T-715 | Send the rebooking notice for ops and approved-proposal rebookings, and keep walk-up requests out of templates | backend | K | SS-301 | T-312, T-702, T-704 | 18 |
| T-726 | Send the re-offer and alternatives message with one-tap accept links and keywords | backend | K | SS-316 | T-138, T-702, T-704, T-746 | 14 |
| T-727 | Hand offer messages to the provider within their set times and reply to an accepted offer | backend | K | SS-316 | T-102, T-138, T-139, T-726 | 15 |
| T-751 | Create personal site-staff logins scoped to one site, revocable by ops at once | backend | K | SS-324 | T-129, T-742, T-909, T-916 | 9 |

## EP-03

| Task | Title | Type | KYIV | Implements | Depends on | Chain depth |
|---|---|---|---|---|---|---|
| T-106 | Hold versioned per-site no-show fee terms fixed at confirmation | backend | K | SS-027 | T-100, T-207, T-909, T-911 | 5 |
| T-110 | Produce a signed printable QR code per EVSE and verify scanned codes | backend | K | SS-031 | T-100, T-905, T-909, T-911 | 5 |
| T-303 | Build the arrival record, arrival window and end-of-grace rules | backend | K | SS-124, SS-127 | T-101, T-127, T-900 | 13 |
| T-327 | Record arrival from a QR scan within the arrival window | backend | K | SS-124 | T-110, T-122, T-129, T-303, T-747, T-911 | 14 |
| T-328 | Add the QR scan page to the driver PWA | frontend | K | SS-124 | T-327, T-353, T-747, T-760, T-767 | 17 |
| T-329 | Record arrival from a CSMS session start where the site has it switched on | backend | K | SS-125 | T-101, T-122, T-302, T-303, T-500, T-501, T-525 | 17 |
| T-332 | Release bookings at the end of grace without arrival and mark late grace timers | backend | K | SS-127 | T-102, T-122, T-124, T-161, T-302, T-303, T-304 | 17 |
| T-333 | Keep late arrivals as no-shows and trigger the same-site re-offer | backend | K | SS-128 | T-102, T-125, T-139, T-303, T-332 | 18 |
| T-334 | Record running-late reports for ops without changing grace or fee | backend | K | SS-129 | T-129, T-303, T-332, T-747, T-748, T-911 | 18 |
| T-335 | Let ops extend a booking's grace up to the site maximum | backend | K | SS-130 | T-101, T-122, T-129, T-303, T-327, T-332, T-741, T-911 | 18 |
| T-336 | Decide the no-show fee with one fee request or an ops fee decision | backend | K | SS-131 | T-106, T-122, T-129, T-303, T-332, T-507, T-510, T-700, T-741, T-911, T-949 | 18 |
| T-337 | Route late cancellations to an ops fee decision | backend | Y | SS-132 | T-140, T-141, T-303, T-336 | 19 |
| T-340 | Rebook or escalate when no charging session starts after arrival | backend | Y | SS-107 | T-102, T-122, T-160, T-161, T-164, T-301, T-303, T-306, T-329, T-332, T-507 | 19 |
| T-341 | Open no-show disputes from the fleet portal, the driver page and ops | backend | K | SS-134 | T-102, T-129, T-303, T-332, T-336, T-507, T-742, T-749, T-911 | 19 |
| T-342 | Serve the dispute evidence timeline, with location only while the dispute is open | backend | K | SS-135 | T-304, T-329, T-341, T-354, T-516, T-700, T-741, T-781, T-785, T-911, T-966 | 21 |
| T-348 | Ops console - fee decisions on excluded no-shows | frontend | K | SS-131 | T-336, T-507 | 19 |
| T-349 | Ops console - disputes, decisions and the evidence timeline | frontend | K | SS-134, SS-135 | T-341, T-342, T-354, T-507 | 22 |
| T-350 | Raise a no-show dispute from the fleet portal and the driver page | frontend | K | SS-134 | T-341, T-538, T-749, T-760 | 21 |
| T-352 | Ops console - grace extension and running-late reports on a booking | frontend | K | SS-130, SS-129 | T-334, T-335, T-557 | 21 |
| T-353 | Keep a QR scan made without a link session and apply it when the booking page opens on that device | backend | K | SS-124 | T-129, T-327, T-746, T-747, T-911 | 15 |
| T-354 | Decide no-show disputes by reversing or keeping the fee, and tell the raiser | backend | K | SS-134 | T-122, T-129, T-341, T-510, T-729, T-741, T-911, T-952 | 20 |
| T-525 | Deliver CSMS session-start events where a site's integration declares them | integration | K | SS-216 | T-100, T-108, T-500 | 9 |
| T-797 | Keep location only as derived arrival events and delete raw readings by the end of grace | backend | Y | SS-340 | T-164, T-303, T-786, T-798 | 16 |
| T-798 | Pass every location reading through the driver's opt-in and the booking window before it is stored | backend | K | SS-341 | T-101, T-303, T-780 | 14 |
| T-799 | Keep each location opt-in off by default and record the consent text version accepted with it | backend | K | SS-341 | T-732, T-798 | 15 |
| T-949 | Post exactly one no-show fee line per requested no-show, at the booking's fixed terms and apart from energy | backend | K | SS-401, SS-404 | T-106, T-120, T-947, T-998 | 6 |
| T-952 | Reverse a no-show fee on a dispute decision by a new entry | backend | K | SS-402 | T-122, T-949, T-951 | 10 |
| T-953 | Let ops waive an uninvoiced no-show fee with a reason code | backend | K | SS-402 | T-122, T-129, T-780, T-909, T-911, T-952 | 11 |
| T-975 | Add the fee waiver action to the ops console | frontend | K | SS-402 | T-912, T-953 | 12 |

## EP-04

| Task | Title | Type | KYIV | Implements | Depends on | Chain depth |
|---|---|---|---|---|---|---|
| T-167 | Run the fault-rebooking saga per EVSE and trigger over the affected bookings | backend | K | SS-036 | T-160, T-307, T-308, T-310, T-512 | 22 |
| T-168 | Resume interrupted rebooking sagas and raise and resolve 'fault rebooking incomplete' exceptions | backend | K | SS-036 | T-167, T-507, T-510 | 23 |
| T-307 | Rebook the bookings of a faulted EVSE to other compatible EVSEs at the site | backend | K | SS-108 | T-122, T-301, T-303, T-306, T-512 | 19 |
| T-308 | Re-check the site's unallocated bookings after a fault | backend | K | SS-108 | T-126, T-307 | 20 |
| T-309 | Offer alternatives, raise the ops exception and attach a proposal for unplaced bookings | backend | K | SS-109, SS-110 | T-102, T-125, T-137, T-138, T-139, T-303, T-307, T-507, T-510, T-511 | 20 |
| T-310 | Record and emit per-booking outcomes of faults and maintenance holds | backend | K | SS-108 | T-139, T-144, T-307, T-308, T-309 | 21 |
| T-311 | Apply ops bulk approval and rejection of rebooking proposals | backend | K | SS-110 | T-125, T-126, T-129, T-139, T-301, T-302, T-309, T-510, T-511, T-715, T-741, T-911 | 21 |
| T-313 | Serve the fault summary and undo a single automatic fault rebooking | backend | Y | SS-111 | T-122, T-129, T-303, T-307, T-310, T-505, T-741, T-911 | 22 |
| T-314 | Let ops rebook all bookings of an EVSE in one action, marking it faulted | backend | Y | SS-112 | T-122, T-129, T-167, T-307, T-308, T-310, T-512, T-514, T-741, T-911 | 23 |
| T-343 | Automate the Gowanus fault replay on the simulator | qa | Y | SS-115 | T-125, T-137, T-167, T-307, T-308, T-309, T-310, T-313, T-512, T-921, T-923 | 23 |
| T-344 | Gate releases that change booking, inventory or workflows on the Gowanus replay | infra | Y | SS-115 | T-343, T-923, T-934 | 24 |
| T-345 | Ops console - approve or reject rebooking proposals in bulk | frontend | K | SS-110 | T-311, T-507, T-511 | 22 |
| T-346 | Ops console - fault summary and undo of a single rebooking | frontend | Y | SS-111 | T-313, T-528 | 23 |
| T-351 | Ops console - rebook all bookings of an EVSE and mark it faulted | frontend | Y | SS-112 | T-314, T-528 | 24 |
| T-512 | Take faulted EVSEs out of allocation and emit one fault event | backend | K | SS-208 | T-102, T-501, T-505, T-507, T-780 | 11 |
| T-513 | Apply the attendant's free, occupied and faulted settings as live status | backend | K | SS-207 | T-129, T-501, T-512, T-544, T-751, T-911 | 20 |
| T-514 | Return faulted EVSEs to service after a stable available period or an ops return | backend | K | SS-209 | T-102, T-122, T-129, T-506, T-512, T-513, T-740, T-780, T-909, T-911, T-916 | 21 |
| T-517 | Turn driver fault reports into ops exceptions without changing status | backend | K | SS-210 | T-129, T-302, T-505, T-507, T-747, T-748 | 17 |

## EP-05

| Task | Title | Type | KYIV | Implements | Depends on | Chain depth |
|---|---|---|---|---|---|---|
| T-500 | Define the vendor-neutral CSMS interface, capability registry and fake integration | integration | K | SS-217 | T-108, T-900, T-906, T-998, T-1001 | 8 |
| T-501 | Create the EVSE status service module and apply status events idempotently in observed-at order | backend | K | SS-200 | T-108, T-129, T-500, T-900, T-906, T-998, T-1001 | 9 |
| T-502 | Accept live status only from each site's configured status source | backend | Y | SS-206 | T-501 | 10 |
| T-503 | Run the per-site status poll reconciliation workflow | backend | K | SS-201 | T-102, T-165, T-500, T-501 | 10 |
| T-504 | Record per-minute status age and CSMS reachability for the A-031 freshness figure | backend | K | SS-201 | T-503 | 11 |
| T-505 | Serve EVSE status reads with observed-at, source, stale flag and exclusion | backend | K | SS-202 | T-108, T-501 | 10 |
| T-506 | Publish stale flags and mark site status feeds unavailable and recovered | backend | K | SS-202, SS-203 | T-165, T-503, T-505 | 11 |
| T-508 | Raise the status-feed-down exception and keep bookings untouched during a feed outage | backend | K | SS-203 | T-506, T-507 | 12 |
| T-515 | Mark silent EVSEs unknown and out of allocation, and bring them back | backend | Y | SS-204 | T-101, T-506, T-507, T-512, T-514 | 22 |
| T-516 | Keep append-only status history and answer the status at a past moment | backend | K | SS-205 | T-501, T-505 | 11 |
| T-518 | Prove the same status rules at sites of each supply pattern | qa | Y | SS-206 | T-502, T-505, T-506, T-512, T-513, T-514, T-515 | 23 |
| T-519 | Integrate AMPECO status webhooks and polls for Gowanus | integration | K | SS-211 | T-100, T-108, T-500, T-501, T-503 | 11 |
| T-522 | Read AMPECO session records once each, resuming after outages | integration | Y | SS-213 | T-100, T-102, T-108, T-165, T-500, T-519, T-520, T-965 | 19 |
| T-523 | Integrate ChargeLab status for JFK by webhook or poll | integration | K | SS-214 | T-100, T-108, T-500, T-501, T-503 | 11 |
| T-524 | Ingest LIC ChargePoint exports uploaded by ops for reconciliation | integration | K | SS-215 | T-129, T-500, T-511, T-740, T-780, T-909, T-911, T-916, T-965 | 19 |
| T-527 | Prove that switching a site's CSMS integration needs no core change | qa | K | SS-217 | T-108, T-317, T-503, T-512, T-519, T-520, T-555, T-921, T-1004, T-1005 | 21 |
| T-555 | Serve the simulated site through a simulator CSMS integration for the integration-switch proof | integration | K | SS-217 | T-100, T-108, T-500, T-526, T-921, T-1004, T-1005 | 19 |

## EP-06

| Task | Title | Type | KYIV | Implements | Depends on | Chain depth |
|---|---|---|---|---|---|---|
| T-125 | Find the same-site next free slot and hold it as an offer when a slot is full | backend | K | SS-009, SS-002 | T-124 | 8 |
| T-129 | Require idempotency keys on every state-changing booking command | backend | K | SS-014 | T-124, T-207 | 8 |
| T-138 | Accept, decline or let lapse a same-site offer by tap or keyword | backend | K | SS-011 | T-125, T-127, T-909, T-911 | 13 |
| T-139 | Turn an accepted re-offer or alternative into a new booking or a rebooking | backend | K | SS-011 | T-137, T-138 | 14 |
| T-148 | Preset the site, vehicle and duration and read texted times in the site's time zone | backend | K | SS-022 | T-132, T-133 | 11 |
| T-163 | Request one reminder per booking at the site's lead time to the charging driver | backend | K | SS-033 | T-161, T-162 | 16 |
| T-185 | Limit a registered driver to named vehicles of the fleet | backend | K | SS-045 | T-181, T-183, T-742, T-909, T-911 | 8 |
| T-207 | Build the shared idempotency library with per-module key tables and a request guard | backend | K | SS-014 | T-900, T-906, T-998, T-1001 | 4 |
| T-700 | Create the notifications module and the Twilio SMS integration with a delivery record per message | integration | K | SS-307 | T-900, T-905, T-906, T-998, T-1001 | 4 |
| T-701 | Store one language per driver number with latest-setting-wins, validation and English fallback | backend | K | SS-303 | T-129, T-700, T-740, T-900 | 9 |
| T-702 | Build the driver message catalogue in English, Spanish and Bengali with the booking link, code and site time | backend | K | SS-302 | T-120, T-121, T-700, T-701, T-746 | 11 |
| T-703 | Record each number's agreement to booking messages per channel, with STOP and START | backend | K | SS-304 | T-129, T-700, T-701, T-740, T-900 | 10 |
| T-704 | Withhold every message on a channel without an agreement in force | backend | K | SS-304 | T-700, T-703 | 11 |
| T-705 | Receive Twilio webhooks with signature verification and apply delivery reports once and in order | integration | K | SS-307, SS-317 | T-164, T-700, T-905 | 16 |
| T-706 | Process each inbound message once by provider message id, marked processed with its effect | backend | K | SS-309, SS-317, SS-007 | T-129, T-134, T-164, T-705 | 17 |
| T-707 | Watch time-critical messages for delivery and raise the undelivered-message ops exception | backend | K | SS-307 | T-102, T-164, T-507, T-704, T-705 | 17 |
| T-708 | Resend a time-critical message once on the driver's other channel | backend | K | SS-307 | T-707 | 18 |
| T-709 | Carry booking requests, replies and booking messages on WhatsApp behind the channel switch | integration | Y | SS-308 | T-702, T-704, T-706, T-708, T-722 | 20 |
| T-710 | Treat a WhatsApp message with no approved template as undelivered and resend it by SMS | backend | Y | SS-307 | T-708, T-709 | 21 |
| T-711 | Send each booking's confirmation to the charging driver and a registered booker, with its terms | backend | K | SS-300 | T-101, T-106, T-127, T-128, T-702, T-704 | 14 |
| T-712 | Send exactly one confirmation per booking and recipient, across retries, multi-booking steps and downtime | backend | K | SS-300 | T-711 | 15 |
| T-713 | Send one cancellation message per recipient when a booking is cancelled or released by ops | backend | K | SS-300 | T-141, T-702, T-704, T-720 | 20 |
| T-716 | Send the booking reminder on the driver's channel once per booking and slot | backend | K | SS-302 | T-121, T-140, T-161, T-702, T-704 | 15 |
| T-717 | Welcome newly registered numbers once their agreement is recorded | backend | K | SS-306 | T-181, T-702, T-703, T-704 | 12 |
| T-718 | Send cut-over messages for carried-over pilot bookings and report drivers not told | backend | K | SS-306 | T-717 | 13 |
| T-719 | Recognise keywords in English, Spanish and Bengali and resolve the booking they apply to | backend | K | SS-310, SS-303 | T-120, T-701, T-702, T-706, T-744, T-750 | 18 |
| T-720 | Apply cancel, accept and decline keywords and reply with the outcome | backend | K | SS-310 | T-138, T-140, T-719 | 19 |
| T-721 | Answer help and link keywords and pass STOP and START to the agreement records | backend | K | SS-310 | T-703, T-719, T-746 | 19 |
| T-722 | Hand messages the platform cannot act on to ops and acknowledge them, unregistered numbers included | backend | K | SS-312, SS-310 | T-120, T-507, T-704, T-719 | 19 |
| T-723 | Turn a texted site code and time into a confirmed booking or an offer of the next free slot | backend | K | SS-311 | T-125, T-127, T-148, T-712, T-719 | 19 |
| T-724 | Handle late accepts, unknown site codes, missing vehicle presets and booker-only senders in text booking | backend | K | SS-311 | T-131, T-148, T-722, T-723, T-746 | 20 |
| T-725 | Take over the pilot's SMS number on request so the platform answers it | integration | K | SS-311 | T-705, T-723 | 20 |
| T-732 | Hold consent texts and fee notices as three-language versions and store each driver's acceptance | backend | K | SS-305 | T-129, T-701, T-747 | 12 |
| T-733 | Record each change of a driver's language in the configuration audit | backend | K | SS-303 | T-701, T-782 | 10 |
| T-734 | Apply running-late and fault keywords and reply | backend | K | SS-310 | T-334, T-352, T-517, T-719 | 22 |
| T-735 | Send no message about a booking to a number removed from the booking's fleet | backend | K | SS-302 | T-120, T-704, T-745 | 12 |
| T-744 | Identify a driver by the registered mobile number and give the booking engine the driver's bookable vehicles | backend | K | SS-318 | T-181, T-182, T-185, T-740 | 9 |
| T-745 | Withdraw a removed number's entitlement for that fleet at once, on every channel | backend | K | SS-319 | T-129, T-181, T-742, T-744, T-751, T-780 | 10 |
| T-746 | Issue and verify signed driver links, and renew a driver-page link by text | backend | K | SS-320 | T-102, T-744, T-905 | 10 |
| T-747 | Bind each driver link to the first device that opens it and scope driver sessions to the driver's own bookings | backend | K | SS-320 | T-745, T-746 | 11 |
| T-748 | Give unverified devices the limited view with one-tap actions only | backend | K | SS-321 | T-102, T-747 | 12 |
| T-749 | Verify devices with one-time codes sent by SMS, with a lockout after wrong codes | backend | K | SS-321 | T-102, T-702, T-704, T-748 | 13 |
| T-750 | Authorise booking commands by text only from the booking's booker or charging driver | backend | K | SS-322 | T-120, T-745, T-780 | 11 |
| T-752 | Show messaging agreements and code blocks per number in the ops console | frontend | K | SS-304, SS-321 | T-511, T-703, T-749, T-912 | 19 |
| T-753 | Expire booking links a set time after the booking's grace ends, extensions included | backend | K | SS-320 | T-102, T-303, T-746 | 14 |
| T-760 | Create the driver PWA and open a booking from a message link with nothing to install | frontend | K | SS-325 | T-747, T-753, T-912 | 15 |
| T-761 | Book in two taps from the open-slot view with changeable presets | frontend | K | SS-326 | T-124, T-127, T-129, T-133, T-148, T-749, T-760 | 16 |
| T-762 | Handle taken slots, expired holds and held offers in the booking flow, with an optional SoC | frontend | K | SS-326 | T-125, T-127, T-190, T-761 | 17 |
| T-764 | Render every driver PWA screen in the driver's stored language | frontend | K | SS-328 | T-701, T-749, T-760 | 16 |
| T-766 | Open directions in the phone's navigation app and return to the Uber Driver or Lyft Driver app by deep link | frontend | Y | SS-330 | T-108, T-760 | 16 |
| T-767 | Never read or ask for the phone's location without an active opt-in | frontend | K | SS-331 | T-760, T-798 | 16 |

## EP-07

| Task | Title | Type | KYIV | Implements | Depends on | Chain depth |
|---|---|---|---|---|---|---|
| T-143 | Book on behalf of a registered driver from the ops API under the driver's rules | backend | K | SS-015 | T-123, T-127, T-131, T-132, T-909, T-911 | 14 |
| T-144 | Let ops force-confirm a hold within capacity and force-release a booking as a cancellation | backend | K | SS-016 | T-123, T-127, T-140, T-141, T-909, T-911 | 16 |
| T-145 | Place maintenance holds on named EVSEs or units of capacity for a window | backend | K | SS-017 | T-123, T-126, T-129, T-133, T-909, T-911 | 12 |
| T-146 | Keep fleet-priority holds of capacity for one named fleet within the caps | backend | K | SS-018 | T-123, T-125, T-126, T-129, T-909, T-911 | 12 |
| T-203 | Build the manual-hold screens and the over-limit booking lists | frontend | K | SS-017, SS-018, SS-019 | T-145, T-146, T-147, T-511, T-535 | 19 |
| T-312 | Let ops rebook a single booking under the booking rules | backend | K | SS-114 | T-122, T-125, T-126, T-129, T-130, T-139, T-300, T-301, T-302, T-741, T-911 | 17 |
| T-315 | Rebook bookings taken off their EVSE by a maintenance hold | backend | K | SS-113 | T-145, T-167, T-301, T-307, T-308, T-309, T-310 | 23 |
| T-507 | Create the ops exception store, type catalogue and raise interface | backend | K | SS-219 | T-900, T-906, T-998, T-1001 | 4 |
| T-509 | Order the exception queue grace-critical first | backend | K | SS-219 | T-121, T-302, T-303, T-507, T-911 | 17 |
| T-510 | Close and resolve exceptions with reason codes, for the ops role only | backend | K | SS-219 | T-122, T-129, T-507, T-740, T-780, T-909, T-911, T-916 | 9 |
| T-511 | Build the ops console shell and the live exception queue screen | frontend | K | SS-219 | T-509, T-510, T-740, T-909, T-911, T-912, T-916 | 18 |
| T-528 | Build the ops console site board with today's bookings, EVSE status and open exceptions in site time | frontend | K | SS-220 | T-121, T-129, T-505, T-506, T-508, T-509, T-511, T-514, T-740, T-909, T-911, T-916 | 22 |
| T-529 | Search drivers by mobile number in the ops console | backend | K | SS-221 | T-120, T-181, T-511, T-700, T-740, T-785, T-909, T-911, T-916, T-949 | 19 |
| T-530 | Arrange station holds from the ops console with the manual-mode list and 'contact the site' | frontend | K | SS-222 | T-322, T-323, T-325, T-511, T-911 | 25 |
| T-531 | Answer a driver's unclear message from the ops console | frontend | K | SS-222 | T-511, T-722, T-729, T-911 | 20 |
| T-532 | Add the booking screen with ops actions and their recorded results | frontend | K | SS-222 | T-143, T-144, T-312, T-511, T-530, T-531, T-781, T-911 | 26 |
| T-533 | Run the pilot-shift acceptance suite and guard against pilot tools | qa | K | SS-222 | T-530, T-531, T-532, T-946 | 27 |
| T-556 | Keep the ops site board live and show when it is not | frontend | K | SS-220 | T-129, T-506, T-510, T-511, T-528 | 23 |
| T-557 | Search by plate and booking code in the ops console and label every match | backend | K | SS-221 | T-120, T-183, T-529 | 20 |
| T-729 | Send ops messages to drivers on their channel, record them on the booking, and send dispute decisions | backend | K | SS-314 | T-120, T-129, T-702, T-704, T-705, T-708, T-740 | 19 |

## EP-08

| Task | Title | Type | KYIV | Implements | Depends on | Chain depth |
|---|---|---|---|---|---|---|
| T-180 | Create the fleet module and let ops create fleets with no portal user | backend | K | SS-040 | T-207, T-900, T-906, T-909, T-911, T-998, T-1001 | 5 |
| T-181 | Register driver numbers to fleets in E.164 and answer registration lookups | backend | K | SS-037 | T-180, T-742, T-909, T-911 | 7 |
| T-183 | Add, edit and retire vehicle profiles with connector, adapters and power | backend | K | SS-038 | T-180, T-742, T-909, T-911 | 7 |
| T-184 | Hold the fleet adapter policy with per-vehicle overrides | backend | K | SS-039 | T-101, T-183, T-742, T-909, T-911 | 8 |
| T-186 | List confirmed bookings that a vehicle or policy change leaves without a compatible EVSE or allowed vehicle | backend | K | SS-038, SS-045 | T-127, T-130, T-183, T-184, T-185, T-742, T-909, T-911 | 13 |
| T-187 | Hand a fleet's registrations over to a new fleet manager unchanged | backend | K | SS-040 | T-181, T-182, T-183, T-742 | 9 |
| T-188 | Import vehicles and driver numbers from a CSV file with per-row errors | backend | Y | SS-041 | T-181, T-183, T-742, T-909, T-911 | 8 |
| T-204 | Build the fleet set-up screens for drivers and booker-only numbers | frontend | K | SS-037, SS-042, SS-040 | T-180, T-181, T-182, T-187, T-511, T-537 | 21 |
| T-205 | Build the fleet set-up screens for vehicles, adapter policy, driver limits and bookings needing action | frontend | K | SS-038, SS-039, SS-045 | T-183, T-184, T-185, T-186, T-511, T-537 | 21 |
| T-206 | Build the fleet import screen and the vehicle-data authorisation panel | frontend | Y | SS-041, SS-043 | T-188, T-189, T-511, T-537 | 21 |
| T-536 | Build the fleet bookings read model and API | backend | K | SS-223 | T-120, T-122, T-129, T-139, T-302, T-306, T-312, T-742, T-745, T-786, T-906, T-911, T-998, T-1001 | 19 |
| T-537 | Build the fleet portal shell and bookings screen in site time | frontend | K | SS-223 | T-121, T-536, T-742, T-912 | 20 |
| T-538 | Serve the fleet's no-shows by driver, excluding rebooks and cancellations | backend | K | SS-224 | T-122, T-141, T-332, T-333, T-536 | 20 |
| T-539 | Show fleet no-shows and dispute decisions in the fleet portal | frontend | K | SS-224 | T-354, T-537, T-538 | 21 |
| T-540 | Build the arrival and charging evidence read model for today's bookings | backend | Y | SS-225 | T-139, T-306, T-312, T-327, T-328, T-329, T-330, T-331, T-332, T-340, T-501, T-513, T-525, T-536 | 21 |
| T-541 | Show today's arrival and charging per vehicle live in the fleet portal | frontend | Y | SS-225 | T-511, T-537, T-540, T-742 | 22 |
| T-552 | Give fleets a per-vehicle monthly report with matched energy | backend | Y | SS-233 | T-183, T-537, T-547, T-550, T-742, T-911 | 23 |
| T-730 | Send booker-only numbers status messages for arrival, charging start and release | backend | Y | SS-315 | T-327, T-328, T-329, T-330, T-331, T-332, T-513, T-525, T-702, T-704 | 21 |
| T-731 | Send booker-only numbers status messages for a charge that did not start, its outcome and rebookings | backend | Y | SS-315 | T-139, T-306, T-312, T-340, T-730 | 22 |
| T-740 | Bind portal users to one organisation and one role, and check that scope on every request | backend | K | SS-323 | T-906, T-909, T-916, T-998, T-1001 | 4 |
| T-741 | Refuse out-of-scope requests as if the item did not exist, and record each refusal | backend | K | SS-323 | T-740, T-780 | 5 |
| T-742 | Apply fleet, station-operator and site-staff scope rules, with the site-staff day following the site's midnight | backend | K | SS-323 | T-741 | 6 |
| T-743 | Keep driver phone numbers from station staff, and a shared driver's other fleets from fleet users | backend | K | SS-323 | T-742 | 7 |

## EP-09

| Task | Title | Type | KYIV | Implements | Depends on | Chain depth |
|---|---|---|---|---|---|---|
| T-147 | List confirmed bookings above a lowered limit for the person who lowered it | backend | K | SS-019 | T-104, T-140, T-146, T-742, T-909, T-911 | 14 |
| T-542 | Show a station operator's upcoming bookings with their allocated EVSE | backend | K | SS-226 | T-129, T-139, T-141, T-302, T-306, T-312, T-332, T-535, T-742, T-743, T-786, T-911 | 19 |
| T-543 | Show fault and maintenance outcomes per affected booking in the station portal | backend | K | SS-227 | T-310, T-315, T-535, T-742, T-743, T-786, T-911 | 24 |
| T-553 | Show the cost of each charger fault to the station operator | backend | Y | SS-234 | T-309, T-310, T-512, T-514, T-535, T-742, T-911 | 22 |
| T-728 | Text the station operator within the set time when a fault or maintenance hold changes bookings | backend | K | SS-313 | T-102, T-129, T-310, T-315, T-507, T-543, T-702, T-705, T-740 | 25 |

## EP-10

| Task | Title | Type | KYIV | Implements | Depends on | Chain depth |
|---|---|---|---|---|---|---|
| T-947 | Create the ledger: accounts, balanced transactions and append-only entries | backend | K | SS-400, SS-402 | T-906 | 3 |
| T-948 | Compute balances as of any time and prove the ledger holds every business-model option | backend | K | SS-400 | T-914, T-947 | 6 |
| T-950 | Create fleet invoices with itemised lines traceable to ledger entries and bookings | backend | K | SS-405 | T-120, T-121, T-181, T-183, T-949 | 8 |
| T-951 | Build each fleet's monthly invoice: net-30, final-slot month, one per fleet and month, zero invoices | backend | K | SS-404 | T-950 | 9 |
| T-954 | Show a fleet's owed, paid and outstanding amounts at any past date | backend | Y | SS-403 | T-909, T-911, T-948, T-952 | 11 |
| T-955 | Define the payment-provider interface and the Stripe client with error translation | integration | K | SS-415 | T-900, T-905 | 4 |
| T-956 | Prove the payment provider is replaceable: the Stripe import rule and the contract suite on a second implementation | integration | K | SS-415 | T-955, T-958, T-998, T-1007 | 11 |
| T-957 | Keep invoice submissions pending while Stripe is down and retry them durably | integration | K | SS-412 | T-102, T-1007 | 10 |
| T-958 | Receive Stripe payment webhooks with signature check, deduplication and order independence | integration | K | SS-413 | T-911, T-955, T-1007 | 10 |
| T-959 | Reconcile open invoices with Stripe on the payment check interval | integration | K | SS-413 | T-102, T-958 | 11 |
| T-960 | Collect fleet payments only on Stripe-hosted pages and keep card data out of the platform | integration | K | SS-414 | T-912, T-913, T-958, T-1007 | 11 |
| T-961 | Run month close at the configured invoice close offset and request submission | backend | K | SS-404, SS-410 | T-102, T-180, T-945, T-951, T-955 | 10 |
| T-962 | Hold untraceable charges in a reconciliation case and keep held charges off invoices | backend | K | SS-405, SS-408 | T-961 | 11 |
| T-963 | Put late entries and newly linked charges on the next invoice as adjustment lines | backend | K | SS-404, SS-405, SS-408 | T-122, T-129, T-909, T-911, T-962 | 12 |
| T-964 | Track invoice payment status and flag overdue invoices | backend | Y | SS-409 | T-951, T-958 | 11 |
| T-965 | Store CSMS session records and keep the allocation and arrival read model for matching | backend | K | SS-407 | T-302, T-327, T-328, T-947 | 18 |
| T-966 | Match session records to arrived bookings within the session match time | backend | K | SS-407 | T-101, T-102, T-965 | 19 |
| T-967 | Open, hold and close reconciliation cases for unmatched bookings and session records | backend | K | SS-408 | T-962, T-963, T-966 | 20 |
| T-968 | Let ops record outcomes, accept in bulk and list open reconciliation cases | backend | K | SS-408 | T-122, T-129, T-780, T-909, T-911, T-963, T-967 | 21 |
| T-969 | Put reversed invoiced fees on the next invoice as credit lines and keep issued invoices unchanged | backend | K | SS-406 | T-951, T-952, T-953 | 12 |
| T-970 | Cap credits at an invoice's charges and carry the rest forward | backend | K | SS-406 | T-961, T-969 | 13 |
| T-972 | Serve the finance views of invoices, reconciliation and disputes across every fleet and site | backend | Y | SS-411 | T-349, T-354, T-741, T-785, T-909, T-911, T-957, T-964, T-968, T-969 | 23 |
| T-973 | Refuse finance users on booking, capacity-rule and fleet-policy commands | backend | Y | SS-440 | T-104, T-127, T-140, T-144, T-184, T-909, T-911 | 17 |
| T-974 | Build the finance screens in the ops console | frontend | Y | SS-411, SS-403 | T-912, T-954, T-972 | 24 |
| T-976 | Add the reconciliation case actions to the ops console | frontend | K | SS-408 | T-912, T-963, T-968 | 22 |
| T-1007 | Submit issued invoices to Stripe with a stable idempotency key and record the hosted invoice page | integration | K | SS-412, SS-414 | T-180, T-950, T-955 | 9 |

## EP-11

| Task | Title | Type | KYIV | Implements | Depends on | Chain depth |
|---|---|---|---|---|---|---|
| T-209 | Record arrived bookings as Completed on a matched session record or an ops reconciliation outcome | backend | K | SS-046 | T-122, T-966, T-968 | 22 |
| T-546 | Build the reporting evidence store per booking | data | K | SS-229 | T-122, T-129, T-138, T-139, T-312, T-327, T-328, T-329, T-330, T-331, T-333, T-906, T-966, T-998, T-1001 | 21 |
| T-547 | Count completed bookings under a configurable rule over the stored evidence | backend | K | SS-229 | T-546 | 22 |
| T-548 | Let ops change the completed definition without a deployment | backend | K | SS-229 | T-129, T-511, T-547, T-740, T-782, T-909, T-911, T-916 | 23 |
| T-549 | Report monthly completed bookings for NYC with pilot data separable | backend | K | SS-230 | T-108, T-121, T-547, T-740, T-909, T-911, T-916, T-981, T-983 | 23 |
| T-550 | Report no-show and late-arrival rates per month, fleet and site | backend | K | SS-232 | T-141, T-332, T-333, T-335, T-546, T-740, T-909, T-911, T-916 | 22 |
| T-551 | Produce the Series A data-room report traceable to booking ids | backend | K | SS-231 | T-549, T-550, T-740, T-909, T-911, T-916 | 24 |
| T-554 | Measure ops-free Five Boroughs bookings from the audit trail | backend | Y | SS-235 | T-305, T-309, T-507, T-546, T-740, T-780, T-781, T-909, T-911, T-916 | 22 |

## EP-12

| Task | Title | Type | KYIV | Implements | Depends on | Chain depth |
|---|---|---|---|---|---|---|
| T-795 | De-identify every dataset that leaves production with random driver surrogates | backend | K | SS-339 | T-780 | 5 |
| T-796 | Scan every outgoing dataset for phone numbers and known driver names and block its release on a match | backend | K | SS-339 | T-181, T-795, T-1009 | 9 |
| T-938 | Keep prototype code out of the codebase with a provenance check | infra | Y | SS-439 | T-901 | 3 |
| T-945 | Hold the one configured cut-over instant in the migration module | backend | K | SS-422 | T-1001 | 4 |
| T-946 | Keep pilot tools out of production: no Airtable, Google Sheets or Retool credential, export files only | infra | K | SS-422 | T-902, T-905, T-945 | 5 |
| T-971 | Invoice by slot start against the cut-over instant and hand earlier bookings to the pilot process | backend | K | SS-410 | T-128, T-945, T-952, T-953, T-961 | 14 |
| T-977 | Run migrations with one outcome per source record and count reconciliation against the export files | backend | K | SS-417 | T-945, T-985 | 5 |
| T-978 | Read the Airtable and Sheets exports through documented, versioned site and column-to-EVSE mappings | backend | K | SS-416, SS-417 | T-100, T-977 | 6 |
| T-979 | Pair Sheet cells with Airtable rows and settle disagreements by the precedence rule | backend | K | SS-419 | T-977 | 6 |
| T-980 | Keep the conflict list and re-settle conflicts under a changed rule | backend | K | SS-419 | T-979 | 7 |
| T-981 | Map pilot statuses to outcomes and keep the original status unchangeable | backend | K | SS-417, SS-418 | T-977 | 6 |
| T-982 | Re-classify rebooked and early no-show records with rule and evidence, and flag pre-2026-02-01 data | backend | K | SS-418 | T-979, T-981 | 7 |
| T-983 | Add the migrated-booking command and the booking query that returns pilot and platform bookings together | backend | K | SS-416 | T-120, T-300 | 14 |
| T-984 | Load the merged pilot history into the booking model, linked to sites, EVSEs, drivers and fleets | backend | K | SS-416 | T-100, T-180, T-978, T-980, T-982, T-983, T-1009 | 15 |
| T-985 | Store the raw pilot export read-only, readable only by the named people | infra | K | SS-420 | T-904, T-905, T-916 | 4 |
| T-986 | Delete the raw export when its retention ends and list it in the data register | backend | K | SS-420 | T-780, T-788, T-945, T-985 | 14 |
| T-987 | Carry open pilot bookings over at cut-over as confirmed platform bookings | backend | K | SS-421 | T-128, T-129, T-161, T-185, T-909, T-911, T-945, T-979 | 15 |
| T-988 | List carried-over bookings that need ops: unregistered driver, above the cap, no vehicle | backend | K | SS-421 | T-103, T-181, T-987 | 16 |
| T-989 | Report carried-over bookings to Messaging, publish the cut-over result and make the carry-over re-runnable | backend | K | SS-421 | T-718, T-988 | 17 |
| T-990 | Make migration re-runs replace, never duplicate, and keep carried-over bookings once | backend | K | SS-417, SS-421 | T-984, T-987 | 16 |
| T-991 | Keep the go-live record with criteria, real bookings and evidence per pilot site | backend | K | SS-423 | T-122, T-181, T-302, T-317, T-909, T-911, T-945 | 21 |
| T-992 | Accept the switch-off approval only when every criterion is met | backend | K | SS-423 | T-129, T-991 | 22 |
| T-993 | Verify the SMS number takeover with a help keyword from a registered test number | integration | K | SS-422 | T-703, T-721, T-945 | 20 |
| T-994 | Run the cut-over: preconditions, ordered steps, the cut-over record and resume | backend | K | SS-422 | T-107, T-181, T-725, T-989, T-992, T-993 | 23 |
| T-995 | Mark the cut-over complete only with a fresh outage copy and a named confirmation | backend | K | SS-422 | T-129, T-944, T-994 | 24 |
| T-996 | Add the cut-over screens to the ops console | frontend | K | SS-421, SS-422 | T-912, T-989, T-995 | 25 |
| T-997 | Add the go-live record screen to the ops console | frontend | K | SS-423 | T-912, T-992 | 23 |
| T-1009 | Create driver records for unregistered pilot numbers and attach them on a later registration | backend | K | SS-416 | T-181 | 8 |

## EP-13

| Task | Title | Type | KYIV | Implements | Depends on | Chain depth |
|---|---|---|---|---|---|---|
| T-122 | Keep the reason-code catalogue and an append-only booking state-change history | backend | K | SS-020 | T-120 | 6 |
| T-123 | Send every booking state change to the audit trail | backend | K | SS-020 | T-122, T-780 | 7 |
| T-208 | Anonymise and purge the driver data the fleet module holds | backend | K | SS-337, SS-336 | T-181, T-182, T-789, T-1009 | 23 |
| T-355 | Anonymise and purge the driver data of arrival, station-hold and dispute records | backend | K | SS-337, SS-336 | T-303, T-316, T-334, T-338, T-341, T-353, T-354, T-789 | 23 |
| T-526 | Verify CSMS webhook signatures or shared secrets before parsing | integration | K | SS-218 | T-519, T-523, T-784, T-905 | 18 |
| T-558 | Anonymise and purge the driver data of the partner-portal read models | backend | K | SS-337, SS-336 | T-536, T-542, T-543, T-544, T-789 | 25 |
| T-559 | Anonymise and purge the driver data held in ops exceptions | backend | K | SS-337, SS-336 | T-507, T-722, T-789 | 23 |
| T-780 | Create the append-only audit trail and security-event log with actor, reason code and correlation id | backend | K | SS-332 | T-900, T-906, T-998, T-1001 | 4 |
| T-781 | Return a booking's full history to ops in time order | backend | K | SS-332 | T-740, T-780 | 5 |
| T-782 | Record configuration changes with before and after values and answer the value in force at a past instant | backend | K | SS-333 | T-741, T-780 | 6 |
| T-783 | Record sign-ins, failed sign-ins, role changes and configuration changes as security events | backend | Y | SS-334 | T-747, T-749, T-751, T-782, T-909, T-916 | 14 |
| T-784 | Record refused requests, refused text commands and rejected webhooks as immutable security events | backend | K | SS-334, SS-317 | T-705, T-741, T-750, T-780 | 17 |
| T-785 | Log every view and export of a driver's personal data at the API | backend | K | SS-335 | T-743, T-780 | 8 |
| T-786 | Create the data register and list every credential, licence number and account number with purpose and readers | backend | K | SS-342 | T-780 | 5 |
| T-787 | Encrypt listed identifier fields, audit every read, and refuse unnamed readers and unapproved storage | backend | K | SS-342 | T-786, T-905, T-907, T-908, T-913 | 7 |
| T-788 | Extend the data register with retention periods and finance holds, counted from the driver's latest activity | backend | K | SS-336 | T-127, T-786 | 13 |
| T-789 | Run the daily retention purge with dispute and finance holds and record its counts | backend | K | SS-336 | T-102, T-164, T-341, T-350, T-780, T-788 | 22 |
| T-790 | Re-apply deletions and anonymisations after a backup restore before the data is used | backend | K | SS-336 | T-789 | 23 |
| T-791 | Anonymise one driver on ops request under a pseudonym in every fleet's records | backend | K | SS-337, SS-335 | T-129, T-741, T-785, T-789, T-790, T-794 | 24 |
| T-792 | List the drivers and data elements exposed through one account, with vendors and NY SHIELD marking | backend | K | SS-338 | T-741, T-785, T-786, T-791, T-909, T-916 | 25 |
| T-793 | List the individuals whose data an exposed copy of a data store held at a stated time | backend | K | SS-338 | T-790, T-792 | 26 |
| T-794 | Report a missing breach-notification procedure to the go-live record | backend | K | SS-338 | T-129, T-780, T-991 | 22 |
| T-800 | Record production data access as security events and check security-event recording in every release | backend | Y | SS-334 | T-780, T-783, T-917, T-919, T-1003 | 15 |
| T-902 | Add secret scanning of code, configuration, images and repository history to CI | infra | K | SS-424 | T-901 | 3 |
| T-904 | Bootstrap Terraform: AWS organisation, one account per environment, remote state and the plan and apply jobs | infra | K | SS-425, SS-431, SS-434 | T-900 | 2 |
| T-905 | Set up KMS keys per data class, the managed secret store and the encryption policy per environment | infra | K | SS-424 | T-904 | 3 |
| T-907 | Provision PostgreSQL on RDS with TLS-only connections, encryption at rest and point-in-time recovery | infra | K | SS-424 | T-905, T-1000 | 5 |
| T-908 | Provision the self-hosted Temporal deployment with TLS and an encrypted persistence store | infra | K | SS-424 | T-905, T-907, T-1000 | 6 |
| T-909 | Configure the identity realm and the deny-by-default permission guard with the staff roles | backend | K | SS-433, SS-440 | T-900 | 2 |
| T-910 | Run the identity service in each environment with TLS-only endpoints | infra | K | SS-424 | T-905, T-907, T-909, T-1000 | 6 |
| T-913 | Instrument the back end with OpenTelemetry and ship encrypted logs, metrics and traces | infra | K | SS-424 | T-900, T-905 | 4 |
| T-915 | Isolate production from the non-production accounts | infra | K | SS-425 | T-904, T-905, T-907, T-1000 | 6 |
| T-916 | Grant production access through IAM Identity Center roles assigned to named people | infra | K | SS-433 | T-904 | 3 |
| T-917 | Log every AWS access and refused attempt in production into the log-archive account | infra | K | SS-433 | T-904, T-916 | 4 |
| T-919 | Build the deployment pipeline under its own machine identity, gated on approval and on the access log | infra | K | SS-426, SS-433 | T-904, T-906, T-917, T-918, T-1008 | 8 |
| T-925 | Run the daily encryption configuration check with an alert to on-call | infra | K | SS-424 | T-904, T-914 | 6 |
| T-999 | Guard Terraform plans with policy as code: account targeting, organisation parent and AWS-only providers | infra | K | SS-425, SS-427, SS-431 | T-904 | 3 |
| T-1000 | Set up the network and TLS-only endpoints per environment: VPC, load balancers, certificates and CloudFront | infra | K | SS-424 | T-904, T-905 | 4 |
| T-1003 | Log database-console access to production data and refuse direct queries outside the database roles | infra | K | SS-433 | T-907, T-916, T-917 | 6 |
| T-1008 | Run the platform image on ECS Fargate: the api and worker services per environment | infra | K | SS-424 | T-905, T-907, T-908, T-913, T-1000 | 7 |
| T-1010 | Write a change record for every production apply to tamper-proof storage in the log-archive account | infra | Y | SS-426 | T-904, T-919 | 9 |
| T-1011 | Anonymise and purge the driver data in the migration module's run records | backend | K | SS-337, SS-336 | T-789, T-980, T-982 | 23 |

## EP-14

| Task | Title | Type | KYIV | Implements | Depends on | Chain depth |
|---|---|---|---|---|---|---|
| T-105 | Make capacity-rule changes idempotent with one change and one history entry per key | backend | K | SS-025 | T-104, T-207, T-782 | 8 |
| T-164 | Make booking timers durable, keyed per step and late-aware, and prove no timer runs elsewhere | backend | K | SS-034 | T-161, T-906, T-998, T-1001 | 15 |
| T-165 | Prove the workflow engine and its stores run only in Amperlane's AWS accounts | qa | K | SS-035 | T-904, T-905, T-907, T-908, T-913 | 7 |
| T-166 | Show booking timers keep firing with no service outside Amperlane's AWS accounts reachable | qa | K | SS-035 | T-161, T-165, T-905 | 15 |
| T-534 | Send one idempotency key per capacity-rule form from the ops console | frontend | K | SS-237 | T-104, T-105, T-511, T-911 | 19 |
| T-535 | Build the station portal shell and capacity-rule form with idempotent saves | frontend | K | SS-236 | T-104, T-105, T-742, T-911, T-912 | 9 |
| T-900 | Scaffold the platform monorepo and the modular-monolith back end with API and worker roles | backend | K | SS-427 | — | 1 |
| T-901 | Set up the CI pipeline: build and test suites, the D2 clause-to-test script, commit and PR lint, and the language and system-of-record gates | infra | K | SS-427 | T-900 | 2 |
| T-903 | Add the open-source maturity and licence gate to CI | infra | K | SS-427 | T-901 | 3 |
| T-906 | Build the database layer: per-module schemas and roles, forward-only migrations, insert-only tables and the PostgreSQL test harness | data | K | SS-427 | T-900 | 2 |
| T-911 | Serve the versioned API and generate its OpenAPI description per version | backend | K | SS-432 | T-900 | 2 |
| T-912 | Set up the front-end workspace: five React apps, a shared UI kit and the generated API client | frontend | K | SS-432 | T-909, T-911 | 3 |
| T-914 | Define dashboards and alert rules as code with runbook links and on-call routing, including the availability alert | infra | K | SS-437, SS-428 | T-904, T-913, T-916 | 5 |
| T-918 | Manage the code repositories in Terraform: protected main, the review rule and equal roles for Amperlane engineers | infra | K | SS-426, SS-434, SS-438 | T-904 | 3 |
| T-920 | Build the simulated site: EVerest chargers, the site registry and the engineer command API | integration | K | SS-435 | T-900 | 2 |
| T-921 | Add the fault scenario to the simulated site, delivered through the AMPECO webhook path | integration | K | SS-435 | T-920, T-1004 | 4 |
| T-922 | Add overrun and late-driver scenarios to the simulated site | integration | K | SS-435 | T-334, T-352, T-921, T-1004 | 22 |
| T-923 | Add the Gowanus fault replay scenario to the simulated site | integration | K | SS-435 | T-143, T-180, T-181, T-183, T-910, T-919, T-921, T-1005 | 15 |
| T-924 | Guard staging integrations against production endpoints, live credentials and real phone numbers | integration | K | SS-435 | T-519, T-700, T-920, T-955 | 12 |
| T-926 | Run the daily drift and unmanaged-resource checks | infra | K | SS-426, SS-434 | T-904, T-914, T-1000 | 6 |
| T-927 | Enforce the 01:00 - 05:00 ET window for interrupting deployments and keep the deployment log | infra | K | SS-429 | T-914, T-919 | 9 |
| T-928 | Run the synthetic booking check every minute from outside the production network | infra | K | SS-428 | T-107, T-122, T-124, T-180, T-183, T-904, T-909, T-914, T-919 | 9 |
| T-929 | Compute monthly availability from the synthetic check and send the report to the Amperlane CTO | infra | K | SS-428 | T-928 | 10 |
| T-930 | Roll back a non-interrupting deployment when the synthetic check fails | infra | K | SS-429 | T-927, T-928 | 10 |
| T-931 | Keep the hidden test site and its holds out of every capacity view, report, invoice and message | backend | K | SS-428 | T-100, T-133, T-528, T-546, T-549, T-711, T-928, T-951 | 24 |
| T-932 | Size staging as production for load tests from one shared sizing definition | infra | K | SS-430 | T-904, T-907, T-908, T-1008 | 8 |
| T-933 | Seed the load-test environment with the migrated pilot history and twelve months of bookings | data | K | SS-430 | T-127, T-795, T-932, T-983, T-1009 | 15 |
| T-934 | Gate releases on the seeded load test and attach its report | infra | K | SS-430 | T-136, T-919, T-933 | 18 |
| T-935 | Build the full data export to open formats in the production account | data | K | SS-434 | T-906, T-907, T-908, T-916, T-1008 | 8 |
| T-936 | Rehearse building, testing, deploying and exporting with no Intellias access | qa | K | SS-434 | T-916, T-918, T-919, T-935 | 9 |
| T-937 | Report hosting cost and AWS Activate credits to the Amperlane CTO every month | infra | Y | SS-431 | T-904, T-1000 | 5 |
| T-939 | Build the runbook register, the usage records and the hypercare handover report | infra | Y | SS-437 | T-914 | 6 |
| T-940 | Write the outage runbooks for every external system and register them | docs | Y | SS-437 | T-939, T-943, T-1006 | 10 |
| T-941 | Generate the integration handover checklist from production and record Priya Nair's sign-offs | infra | Y | SS-438 | T-900, T-918 | 4 |
| T-942 | Refuse a task's done status in the spec repository without a merged change in an Amperlane repository | infra | Y | SS-438 | T-918 | 4 |
| T-943 | Host the outage copy outside the platform with ops-only sign-in | infra | K | SS-436 | T-904, T-905, T-910, T-917, T-1008 | 8 |
| T-944 | Refresh the outage copy at the configured interval and show its age | backend | K | SS-436 | T-102, T-127, T-181, T-302, T-909, T-911, T-943 | 17 |
| T-998 | Add the architecture gates to CI: deployables register, module-boundary and vendor-import lint, SQL schema lint and scheduler lint | infra | K | SS-427 | T-901 | 3 |
| T-1001 | Add the transactional outbox and the after-commit event dispatcher with consumer deduplication | backend | K | SS-427 | T-906 | 3 |
| T-1002 | Gate API changes in CI: complete endpoint descriptions and no breaking change to a published version | backend | K | SS-432 | T-901, T-911 | 3 |
| T-1004 | Expose the simulated site through an AMPECO API stand-in | integration | K | SS-435 | T-920 | 3 |
| T-1005 | Deploy the simulated site to staging and point staging's AMPECO integration at it | infra | K | SS-435 | T-107, T-108, T-519, T-904, T-998, T-1000, T-1004 | 12 |
| T-1006 | Give named ops people break-glass access to the outage copy while single sign-on is down | infra | K | SS-436 | T-943 | 9 |

## Not Ready: tasks waiting for an answer or a decision

These tasks stay draft at Gate 4 (partial approval, playbook §10.8) until the label is cleared: a client answer (blocked-by), a conflict decision (needs-decision) or an Intellias tech-lead decision in Phase 0 (phase0-decision, design.md §9).

| Task | KYIV | Title | Labels |
|---|---|---|---|
| T-121 | K | Lay out site time grids in the site's time zone and handle daylight-saving changes | needs-decision:CF-015 |
| T-126 | K | Check pool feasibility of a booking against compatible EVSEs with the site's buffer | phase0-decision |
| T-133 | K | Answer open-slot queries with exactly the start times a hold would accept | needs-decision:CF-015 |
| T-136 | K | Run the five-times burst load test and record its result as the release gate | phase0-decision |
| T-142 | Y | Confirm an afternoon and an overnight slot together, each decided on its own | needs-decision:CF-015 |
| T-355 | K | Anonymise and purge the driver data of arrival, station-hold and dispute records | blocked-by:Q-058 |
| T-501 | K | Create the EVSE status service module and apply status events idempotently in observed-at order | phase0-decision |
| T-507 | K | Create the ops exception store, type catalogue and raise interface | phase0-decision |
| T-519 | K | Integrate AMPECO status webhooks and polls for Gowanus | blocked-by:Q-009, blocked-by:Q-061 |
| T-520 | K | Send Gowanus charger reservations through AMPECO with typed results | blocked-by:Q-009 |
| T-521 | K | Cancel AMPECO charger reservations with retry until confirmed or expired | blocked-by:Q-009 |
| T-522 | Y | Read AMPECO session records once each, resuming after outages | blocked-by:Q-009 |
| T-523 | K | Integrate ChargeLab status for JFK by webhook or poll | blocked-by:Q-012, blocked-by:Q-061 |
| T-524 | K | Ingest LIC ChargePoint exports uploaded by ops for reconciliation | blocked-by:Q-011 |
| T-525 | K | Deliver CSMS session-start events where a site's integration declares them | blocked-by:Q-051 |
| T-526 | K | Verify CSMS webhook signatures or shared secrets before parsing | blocked-by:Q-061 |
| T-536 | K | Build the fleet bookings read model and API | phase0-decision |
| T-549 | K | Report monthly completed bookings for NYC with pilot data separable | phase0-decision |
| T-551 | K | Produce the Series A data-room report traceable to booking ids | blocked-by:Q-020 |
| T-703 | K | Record each number's agreement to booking messages per channel, with STOP and START | blocked-by:Q-056 |
| T-709 | Y | Carry booking requests, replies and booking messages on WhatsApp behind the channel switch | blocked-by:Q-034 |
| T-728 | K | Text the station operator within the set time when a fault or maintenance hold changes bookings | blocked-by:Q-069 |
| T-749 | K | Verify devices with one-time codes sent by SMS, with a lockout after wrong codes | blocked-by:Q-071 |
| T-788 | K | Extend the data register with retention periods and finance holds, counted from the driver's latest activity | blocked-by:Q-070 |
| T-789 | K | Run the daily retention purge with dispute and finance holds and record its counts | blocked-by:Q-070 |
| T-791 | K | Anonymise one driver on ops request under a pseudonym in every fleet's records | blocked-by:Q-058 |
| T-901 | K | Set up the CI pipeline: build and test suites, the D2 clause-to-test script, commit and PR lint, and the language and system-of-record gates | blocked-by:Q-065 |
| T-904 | K | Bootstrap Terraform: AWS organisation, one account per environment, remote state and the plan and apply jobs | blocked-by:Q-065, blocked-by:Q-066 |
| T-918 | K | Manage the code repositories in Terraform: protected main, the review rule and equal roles for Amperlane engineers | blocked-by:Q-065 |
| T-919 | K | Build the deployment pipeline under its own machine identity, gated on approval and on the access log | blocked-by:Q-065 |
| T-922 | K | Add overrun and late-driver scenarios to the simulated site | phase0-decision |
| T-926 | K | Run the daily drift and unmanaged-resource checks | blocked-by:Q-068 |
| T-929 | K | Compute monthly availability from the synthetic check and send the report to the Amperlane CTO | blocked-by:Q-068 |
| T-934 | K | Gate releases on the seeded load test and attach its report | phase0-decision |
| T-936 | K | Rehearse building, testing, deploying and exporting with no Intellias access | blocked-by:Q-065 |
| T-937 | Y | Report hosting cost and AWS Activate credits to the Amperlane CTO every month | blocked-by:Q-066, blocked-by:Q-068 |
| T-938 | Y | Keep prototype code out of the codebase with a provenance check | blocked-by:Q-020 |
| T-941 | Y | Generate the integration handover checklist from production and record Priya Nair's sign-offs | blocked-by:Q-065 |
| T-942 | Y | Refuse a task's done status in the spec repository without a merged change in an Amperlane repository | blocked-by:Q-065 |
| T-943 | K | Host the outage copy outside the platform with ops-only sign-in | blocked-by:Q-063 |
| T-978 | K | Read the Airtable and Sheets exports through documented, versioned site and column-to-EVSE mappings | blocked-by:Q-020 |
| T-1000 | K | Set up the network and TLS-only endpoints per environment: VPC, load balancers, certificates and CloudFront | blocked-by:Q-068 |
| T-1006 | K | Give named ops people break-glass access to the outage copy while single sign-on is down | blocked-by:Q-063 |
| T-1007 | K | Submit issued invoices to Stripe with a stable idempotency key and record the hosted invoice page | blocked-by:Q-067 |

## Step 5 agenda: Y work that K work depends on

Resolved at Step 5 (CR-011, 2026-10-29): the requirements behind the 49 Y prerequisites, and those their inheritance pulled in, were raised to K (provisional), so no K task depends on a Y task. The one exception is T-710, which depends on the WhatsApp channel (T-709, Y); a human override sets it to Y (P3, P4). The reasons are in [kyiv-proposal.md](../20-requirements/kyiv-proposal.md), section 2.
