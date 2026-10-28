---
id: REQUIREMENTS
type: requirements
title: Amperlane Platform v1 requirements (closed list for Gate 2)
status: approved
owner: Mykola Marchuk
version: 2
kyiv: null
parents: [BUSINESS-CONTEXT, CONSTITUTION]
sources: [SRC-D1, SRC-C1, SRC-C2, SRC-D2, SRC-R1]
---
# Requirements

Step 2, closing pass (playbook §5, 2.1, prompt P2.3), 2026-10-28. This is the closed, numbered list for Gate 2. It
was built from 580 candidates (P2.1 exhaustive pass, P2.2 unstated requirements); [candidates.md](candidates.md) maps
every candidate to its result. After Gate 2 the list is baselined as v1, and a new requirement enters only through a
change request (constitution, spec conventions row 14).

**How to read a row.** `| REQ | Q | Requirement | Sources | KYIV | Q/A |`

- **Q** is the quadrant. S-F and S-NF only when the client said or wrote it: SRC-D1, or an Amperlane speaker (Dana
  Whitfield, Luis Ortega, Ravi Menon, Priya Nair) in SRC-C1/C2, including an Intellias proposal an Amperlane speaker
  agreed to on the record (both cited). Anything supported only by SRC-D2, SRC-R1, an Intellias speaker or inference
  is U-F or U-NF (constitution, spec conventions row 5).
- **Sources** cite `SRC-…` and `CTX-…` only, never the design files (playbook §10.1).
- **Q/A** lists the working assumptions (A-###), open questions (Q-###) and conflicts (CF-###) the row depends on, or
  "—". Q-039 – Q-050 and A-031 – A-047 are proposed in Step 2 (2026-10-28) and are registered in
  [open-questions.md](../01-context/open-questions.md) with this list.
- "A set time" or "a set period" in a requirement is a configured value whose default is chosen in Step 3; the
  requirement is tested against the configured value.
- The [constitution](../constitution.md) NFR baseline (N1 – N24) applies to every row. The NFRs the client stated
  appear here as requirements with their source; numbers set only by the constitution's assumptions are not repeated.

**KYIV column.** Provisional KYIV was set at Gate 2 by Mykola Marchuk (2026-10-28): the agent's suggestions in
[KYIV suggestions for Gate 2](#kyiv-suggestions-for-gate-2) were accepted, except 22 rows moved from K to Y (marked
there). The final KYIV is set at Step 5 with the client (constitution P1). Parking-lot rows carry V (playbook P2.3).

**Rule P5 (constitution, decided at Gate 1).** A requirement that holds only under one option of an undecided client
business decision is in the parking lot as V, linked to the question, and is priced as an option in the proposal.
Requirements that hold in every option are in the baseline. The undecided decisions are Q-001 (revenue model, CF-008),
Q-002 and Q-003 (no-show fee payer, fee after a rebook), Q-017 (completed booking), Q-021 (cash gap), Q-023 (ops
hours), Q-025 (budget), the SOC 2 date (Q-018, CF-016), the March integration scope (Q-036, CF-025), the back-end
operator role (Q-010), and questions that depend on them (Q-032). Examples of the split: the no-show fee line, its
reversal and its dispute are baseline, while who pays it is parked; the evidence for any "completed booking"
definition is baseline, while billing per completed booking is parked.

## S-F · Stated functional

### Booking and capacity

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-001 | S-F | Drivers and fleet users see, per site and time, only the slots in which a hold for the chosen vehicle and duration would be accepted under the site's capacity rules and connector compatibility. | SRC-D1#5, SRC-D1#6, SRC-C1@00:03:57, CTX-002 | K (provisional) | CF-002 |
| REQ-002 | S-F | A booker creates a booking by choosing a site, a start time on the site's time grid and one of the site's configured booking durations. | SRC-D1#6, SRC-C1@00:03:57, CTX-002 | K (provisional) | A-001 |
| REQ-003 | S-F | A booking claims capacity from the pool of compatible EVSEs at the site and gets a specific EVSE only at the site's configured allocation offset before the slot (A-002), never at booking time. | SRC-C2@00:24:36, SRC-C2@00:24:52, CTX-092 | K (provisional) | A-002, CF-023 |
| REQ-004 | S-F | A new hold or booking is accepted only if, for every slot it covers, the holds and bookings overlapping that slot stay within the cap of the capacity rule for that slot. | SRC-C1@00:26:10, SRC-C2@00:24:04, SRC-C2@00:29:24, SRC-C2@00:29:35, CTX-064, CTX-132 | K (provisional) | Q-005 |
| REQ-005 | S-F | A site's capacity rules each set days of the week, a time window and a cap on bookable EVSEs, and every slot within the site's bookable hours falls under exactly one rule. | SRC-C1@00:26:10, SRC-C1@00:26:44, SRC-C1@00:26:54, CTX-064, CTX-065 | K (provisional) | Q-005 |
| REQ-006 | S-F | For a site flagged as NEVI-funded, the platform rejects a capacity rule that exceeds the public-access limit recorded for that site. | SRC-C1@00:27:12, SRC-C1@00:27:37, CTX-017 | I (provisional) | Q-040 |
| REQ-007 | S-F | No two allocations on one EVSE overlap in time, the site's buffer included, among allocations whose booking has not been cancelled, released or rebooked to another EVSE. | SRC-C2@00:31:16, SRC-C2@00:31:45, CTX-093 | K (provisional) | CF-023, A-014 |
| REQ-008 | S-F | When a booking attempt fails because the requested slot is full, the response offers the next free compatible slot at the same site, held for the driver for the site's hold time. | SRC-C2@00:32:16, SRC-C2@00:32:46, CTX-093 | Y (provisional) | — |
| REQ-009 | S-F | A booking records its charging driver as a mobile number registered to the booking's fleet and its booker as either such a number or the fleet-portal or ops user who made the booking, and the booker and the charging driver may differ. | SRC-C1@00:07:40, SRC-C1@00:07:53, SRC-C1@00:11:16, SRC-C1@00:38:52, SRC-C1@00:39:22, CTX-029, CTX-035 | K (provisional) | A-023, Q-028 | v2 | approved |
| REQ-010 | S-F | A booker selects an afternoon slot and an overnight slot for the same vehicle and confirms both with one confirmation. | SRC-C1@00:07:40, CTX-029 | Y (provisional) | A-028, CF-015, Q-024 |
| REQ-011 | S-F | A fleet manager or fleet owner can book a slot for a named driver of the fleet. | SRC-D1#6, SRC-C1@00:11:16, CTX-002, CTX-029 | Y (provisional) | A-023 |
| REQ-012 | S-F | Every booking names one vehicle registered to the booking's fleet, and that vehicle's connector, adapter and power profile is the one used for matching and allocation. | SRC-C2@00:40:58, SRC-C2@00:42:11, CTX-100 | K (provisional) | A-023 |
| REQ-013 | S-F | A booking is accepted and allocated only for EVSEs with a connector that matches the vehicle's native connector or one of its allowed adapters. | SRC-C2@00:41:17, SRC-C2@00:41:28, SRC-C2@00:41:32, SRC-C2@00:42:11, CTX-049, CTX-100 | K (provisional) | Q-013 |
| REQ-014 | S-F | Each EVSE connector records its connector type (CCS1 or NACS) and its maximum power in kW. | SRC-C2@00:16:36, SRC-C2@00:41:32, SRC-C2@00:42:11, CTX-058, CTX-100 | K (provisional) | A-004, Q-013 |
| REQ-015 | S-F | Each vehicle records its native connector, its allowed adapters and its maximum DC charging power. | SRC-C2@00:41:32, SRC-C2@00:42:11, CTX-100 | K (provisional) | — |
| REQ-016 | S-F | At allocation, the platform gives each vehicle the lowest-power free compatible EVSE that meets the vehicle's maximum power, or the highest-power one if none meets it. | SRC-C2@00:42:00, SRC-C2@00:42:11, CTX-100 | Y (provisional) | A-002, Q-050 |
| REQ-017 | S-F | When the vehicle's SoC is known, the booking flow suggests a duration from the SoC and the maximum power of the compatible EVSEs at the chosen site. | SRC-C2@00:38:05, SRC-C2@00:41:32, SRC-C2@00:42:11, CTX-100, CTX-101 | I (provisional) | Q-014 |
| REQ-018 | S-F | A driver can optionally enter the vehicle's current SoC in the booking flow. | SRC-C1@00:06:52, SRC-C2@00:40:06, SRC-C2@00:40:39, CTX-059, CTX-099 | Y (provisional) | — |
| REQ-019 | S-F | A driver can book a vehicle with no telematics from their own phone through SMS or the driver PWA, with no SoC, location or other vehicle data required. | SRC-C1@00:07:09, SRC-C2@00:40:02, CTX-074 | K (provisional) | — |
| REQ-020 | S-F | The platform never sends a stop command for a walk-up's session, never sends site staff a station-hold request for an EVSE a walk-up is using, and never tells anyone to make a walk-up leave. | SRC-C2@00:24:04, CTX-066 | K (provisional) | — |
| REQ-021 | S-F | When the allocated EVSE is occupied at station-hold time or at the pre-arrival check, the platform reallocates the booking to another free compatible EVSE at the same site, places the station hold on it and tells the charging driver the new EVSE. | SRC-C2@00:24:04, SRC-C1@00:40:55, SRC-C2@00:28:42, CTX-050, CTX-066 | K (provisional) | A-002 |
| REQ-022 | S-F | When no compatible EVSE at the site is free for an allocated booking at station-hold time or at the pre-arrival check, the platform puts an exception for that booking in the ops queue within a set time. | SRC-C2@00:24:04, CTX-066 | K (provisional) | Q-033, A-019, Q-023 |

### Station integration and holds

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-023 | S-F | Whether a booking is accepted, kept or released is decided only by Amperlane's slot calendar, and a charger reservation that is rejected, expires or is cancelled at the CSMS never by itself changes a booking. | SRC-C2@00:08:48, SRC-C2@00:26:27, SRC-C2@00:56:15, SRC-C2@00:56:43, CTX-088 | K (provisional) | — |
| REQ-024 | S-F | For an allocated EVSE flagged as reservable, the platform sends a charger reservation through the CSMS at the site's configured station-hold offset (A-002), with an expiry no earlier than the end of the booking's grace period. | SRC-C2@00:08:48, SRC-C2@00:21:07, SRC-C2@00:56:15, SRC-C2@00:56:43, CTX-060, CTX-088 | K (provisional) | A-002, Q-009 |
| REQ-025 | S-F | Each EVSE carries a reservable flag that ops can change without a software release. | SRC-C2@00:19:19, SRC-C2@00:19:30, CTX-060 | K (provisional) | Q-009, Q-013 |
| REQ-026 | S-F | For an allocated EVSE that is not reservable, the platform sends site staff a station-hold request at the site's station-hold offset, and raises an ops exception within a set time when the request cannot be delivered. | SRC-C2@00:08:48, SRC-C2@00:21:07, SRC-C2@00:56:15, SRC-C2@00:56:43, CTX-088 | K (provisional) | A-012 |
| REQ-027 | S-F | For each booking at a site with a physical station hold, the platform sends site staff the stall to mark, when to mark it and when to clear it, replacing the ops phone call. | SRC-C2@00:21:07, SRC-C2@00:21:33, CTX-061, SRC-C1@00:37:27, SRC-C1@00:40:15, SRC-C1@00:40:25, CTX-034, CTX-043 | K (provisional) | A-012, A-046, Q-041, A-021 |
| REQ-028 | S-F | Booking, allocation, grace, auto-release, no-show and fault rebooking follow the same rules at sites of all three supply patterns, and only the station-hold step and the source of EVSE status differ by pattern. | SRC-C2@00:20:38, SRC-C2@00:20:55, SRC-C2@00:56:15, SRC-C2@00:56:43, CTX-063 | Y (provisional) | — |
| REQ-029 | S-F | Live EVSE status comes only from CSMS APIs, OCPI Locations or the attendant view, and every charging site that is not a partner site is shown only as a static map layer. | SRC-C2@00:11:03, SRC-C2@00:11:38, CTX-090 | Y (provisional) | — |
| REQ-030 | S-F | Public charging sites from NLR AFDC and Open Charge Map are shown on the driver map as not bookable and without live availability, and never change bookable capacity. | SRC-C2@00:11:03, SRC-C2@00:11:38, SRC-D1#10, CTX-089 | I (provisional) | — |
| REQ-031 | S-F | The platform reads Gowanus EVSE status and sends and cancels charger reservations through the AMPECO API. | SRC-D1#10, SRC-C2@00:14:11, SRC-C2@00:18:52, SRC-C2@00:37:15, CTX-060, CTX-142 | K (provisional) | A-022, Q-009 |
| REQ-332 | S-F | The platform reads Gowanus session records through the AMPECO API once Kinship makes them available (Q-009). | SRC-D1#10, SRC-C2@00:14:11, SRC-C2@00:18:52, SRC-C2@00:37:15, CTX-060, CTX-142 | Y (provisional) | A-022, Q-009 |
| REQ-032 | S-F | The platform reads JFK's EVSE status from the ChargeLab API by webhook or poll. | SRC-D1#10, SRC-C2@00:19:30, CTX-061, CTX-142 | K (provisional) | A-022, Q-012 |
| REQ-333 | S-F | The platform reads JFK's public price from the ChargeLab API for display before booking. | SRC-D1#10, SRC-C2@00:19:30, CTX-061, CTX-142 | I (provisional) | A-022, Q-012 |

### Arrival, grace and no-show

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-033 | S-F | If no arrival is recorded by the end of the grace period, the platform releases the booking automatically with no human action. | SRC-C1@00:09:55, SRC-C1@00:10:20, SRC-C1@00:10:26, CTX-046, CTX-131 | K (provisional) | Q-004, A-003 |
| REQ-034 | S-F | Each site has a grace period, 10 minutes unless configured otherwise, and the auto-release, no-show and fee decisions for a booking use the value of that booking's site. | SRC-C1@00:09:55, SRC-C2@00:27:57, CTX-067 | K (provisional) | A-003, Q-004 |
| REQ-035 | S-F | When a booking with a physical station hold is released after grace, cancelled or rebooked to another EVSE, the platform tells site staff within a set time to clear that stall for walk-ups. | SRC-C1@00:09:55, CTX-067 | K (provisional) | A-012 |
| REQ-036 | S-F | A booking released after grace with no arrival creates exactly one no-show fee line item, unless it falls under an exclusion of REQ-180, in which case it goes to ops review. | SRC-C1@00:09:27, SRC-C1@00:09:55, CTX-067 | K (provisional) | Q-002 |
| REQ-037 | S-F | A driver who arrives after the booking's grace period, including any ops extension, keeps the booking recorded as a no-show, and the arrival time is stored with it as a late arrival. | SRC-C2@00:29:56, CTX-133 | Y (provisional) | Q-003 |
| REQ-038 | S-F | When a driver records arrival after the booking was released as a no-show, the driver gets, within a set time, an offer of the earliest free compatible slot at that site, accepted with one tap. | SRC-C2@00:30:01, SRC-C2@00:30:11, CTX-133 | Y (provisional) | Q-003 |
| REQ-039 | S-F | A driver cancels a booking with one tap on the page opened from any message about that booking, or on the driver page, with no confirmation dialog or sign-in step. | SRC-C1@00:12:26, SRC-C1@00:12:42, SRC-C1@00:46:10, CTX-041, CTX-135 | K (provisional) | — |
| REQ-040 | S-F | A driver reports 'running late' with one tap on the page opened from any message about that booking, or on the driver page, and the report and its time appear on the booking in the ops console. | SRC-C1@00:12:26, SRC-C1@00:46:10, SRC-C1@00:46:28, CTX-041, CTX-135 | Y (provisional) | A-020, CF-021 |
| REQ-041 | S-F | A driver who replies with a cancel keyword to an SMS about a booking cancels that booking only, and gets a reply naming the booking cancelled. | SRC-C1@00:12:42, CTX-041 | Y (provisional) | — |
| REQ-042 | S-F | Ops can extend the grace period of a single booking with a reason code, up to a maximum set per site. | SRC-C1@00:38:52, SRC-C1@00:39:22, CTX-035 | Y (provisional) | A-020, CF-021, Q-004 |
| REQ-043 | S-F | A driver records arrival by scanning the QR code posted at an EVSE of the booking's site, and the scan is stored with the EVSE, booking and time and counts as arrival only from a set time before the slot to the end of grace. | SRC-C2@00:40:06, SRC-C2@00:40:24, CTX-102 | K (provisional) | A-024 |
| REQ-044 | S-F | The platform produces a printable QR code for each EVSE that site staff can put up. | SRC-C2@00:40:24, CTX-102 | K (provisional) | A-012 |
| REQ-045 | S-F | A fleet or a driver can raise a dispute on a no-show within the dispute window (A-047), and ops records a decision with a reason code that reverses or keeps the fee line and is sent to whoever raised it. | SRC-C1@00:38:52, SRC-C1@00:39:22, SRC-C1@00:39:31, CTX-035 | Y (provisional) | Q-043, A-047, Q-002 |
| REQ-046 | S-F | A driver can report that the allocated stall was blocked on arrival, and the report is stored with its time and the arrival evidence, raises an ops exception and makes the booking count as a failed station hold for fees (REQ-180). | SRC-C1@00:38:52, SRC-C1@00:39:22, SRC-C1@00:43:56, CTX-035, CTX-068 | Y (provisional) | Q-005 |
| REQ-336 | S-F | When the charging driver reports the allocated stall blocked on arrival (REQ-046), the platform reallocates the booking to another free compatible EVSE at the same site where one is free, places the station hold on it and tells the driver the new EVSE. | SRC-C2@00:24:04, SRC-C1@00:38:52, SRC-C1@00:39:22, CTX-066 | Y (suggested) | Q-005 | v1 | approved |

### Charger faults and ops console

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-047 | S-F | Within a set time of receiving an EVSE fault status from the CSMS by webhook or poll, the platform removes the EVSE from new allocations and starts fault rebooking of its bookings (REQ-048). | SRC-C2@00:34:36, SRC-C2@00:34:48, SRC-C2@00:35:14, CTX-048, CTX-136 | K (provisional) | — |
| REQ-048 | S-F | On a fault, the platform rebooks every booking allocated to the faulted EVSE and re-checks every later booking at the site that day against the remaining compatible EVSEs, so each booking that no longer fits is handled as unplaced (REQ-049, REQ-050) before its allocation time. | SRC-C2@00:24:04, SRC-C2@00:34:48, SRC-C2@00:35:14, CTX-136 | Y (provisional) | A-017, CF-022, Q-038 |
| REQ-049 | S-F | A driver whose booking cannot be placed at the same site after a fault gets, within a set time, a message offering the next free compatible slot at that site and the nearest free compatible slots at other sites, each accepted with one tap or keyword. | SRC-C2@00:34:48, SRC-C2@00:35:14, CTX-136 | Y (provisional) | A-017 |
| REQ-050 | S-F | Each fault-affected booking the platform could not place appears in the ops exception queue within a set time of the fault, with the alternatives offered to its driver and the driver's answer. | SRC-C2@00:34:48, SRC-C2@00:35:14, CTX-136 | K (provisional) | A-017, Q-023 |
| REQ-051 | S-F | When a fault or a maintenance hold changes bookings at a site, the station operator gets a notice within a set time and sees in the station portal each affected booking and its outcome. | SRC-C2@00:34:48, SRC-C2@00:35:14, SRC-C2@00:52:34, CTX-047, CTX-136 | Y (provisional) | — |
| REQ-052 | S-F | A booking rebooked because of a fault carries the reason code 'moved — charger fault', the rebooking itself never records a no-show, and arrival and grace are then judged against the new allocation. | SRC-C2@00:52:53, SRC-C2@00:53:32, CTX-036, CTX-047 | K (provisional) | — |
| REQ-053 | S-F | Every booking state change records its actor (the system or a named person) and a reason code from a fixed catalogue, and a system-initiated change never uses a generic code. | SRC-C2@00:53:32, SRC-C2@00:53:40, SRC-C2@00:53:46, CTX-036 | K (provisional) | — |
| REQ-054 | S-F | Ops can rebook all bookings of a faulted EVSE in one action. | SRC-C1@00:38:27, SRC-C1@00:38:52, SRC-C1@00:39:22, CTX-035 | Y (provisional) | A-017, CF-022 |
| REQ-055 | S-F | Ops can make a booking on behalf of a registered driver under the same capacity, compatibility and hold rules as the driver's own booking, with ops recorded as booker. | SRC-C1@00:38:52, SRC-C1@00:39:22, CTX-035 | K (provisional) | — |
| REQ-056 | S-F | Ops can confirm a held or unconfirmed booking with a reason code, under the same capacity and no-overlap rules as any booking. | SRC-C1@00:38:52, SRC-C1@00:39:22, SRC-C2@00:53:00, CTX-035 | Y (provisional) | — |
| REQ-057 | S-F | Ops can release a booking with a reason code, with the same effect on capacity, station hold and driver messages as a cancellation. | SRC-C1@00:38:52, SRC-C1@00:39:22, SRC-C2@00:53:00, CTX-035 | Y (provisional) | — |
| REQ-058 | S-F | Every booking task ops performs in the pilot (taking a request, confirming, arranging station holds, rebooking, releasing, answering a driver) is done in the ops console, and no booking data is read from or written to Airtable, Google Sheets or Retool. | SRC-C1@00:33:22, SRC-C1@00:37:27, SRC-C1@00:39:49, CTX-042, CTX-139 | K (provisional) | — |

### Driver channel and identity

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-059 | S-F | The driver interface is a progressive web app opened in the phone's browser, with no app-store install. | SRC-C1@00:05:47, SRC-C1@00:06:33, SRC-C2@00:51:10, SRC-C2@00:51:22, CTX-096 | K (provisional) | CF-001 |
| REQ-060 | S-F | A driver books with the registered mobile number as the only identity, with no sign-up form, password, email address or payment card. | SRC-C1@00:05:47, CTX-027 | K (provisional) | A-006, Q-028 |
| REQ-061 | S-F | A driver who texts a site code and a time, such as 'GOW 1645', to Amperlane's SMS number gets by reply, with no ops action, either a confirmed booking or the next free compatible slot to accept. | SRC-C1@00:05:34, SRC-C1@00:05:47, SRC-C2@00:02:58, CTX-043 | Y (provisional) | A-008 |
| REQ-062 | S-F | A driver can book and receive booking messages through WhatsApp. | SRC-C1@00:06:09, SRC-C2@00:50:56, SRC-C2@00:51:03, CTX-027, CTX-097 | Y (provisional) | Q-034, A-008 |
| REQ-063 | S-F | Every booking message carries a link that opens the driver page for that booking. | SRC-C1@00:05:47, CTX-027 | K (provisional) | A-006 |
| REQ-064 | S-F | From a booking, the driver can open directions to the site in the driver's own navigation app. | SRC-D1#9, SRC-C2@00:43:07, CTX-098 | Y (provisional) | A-030, CF-020 |
| REQ-065 | S-F | The driver page shows the driver's estimated arrival time at the site. | SRC-D1#9 | I (provisional) | A-030, Q-027 |
| REQ-066 | S-F | From the driver page, the driver can return to the Uber or Lyft driver app with one tap. | SRC-C2@00:43:07, SRC-C2@00:43:30, CTX-098 | Y (provisional) | — |
| REQ-067 | S-F | The charging driver receives a reminder on their channel at the site's configured reminder lead time before the slot (A-011). | SRC-D1#6, SRC-C1@00:03:57, CTX-002 | K (provisional) | A-011 |
| REQ-068 | S-F | Deprecated at P2.4 (2026-10-28): a vendor choice, not a requirement; the behaviour is REQ-064 and REQ-065, and the vendor is A-030 (CF-020). | SRC-D1#9 | — | A-030, CF-020, Q-027 | v1 | deprecated |

### Fleet portal and policy

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-069 | S-F | A fleet manager sees in the fleet portal every upcoming and past booking of the fleet with its driver, vehicle, site, time and current state. | SRC-D1#9, SRC-D1#11, CTX-004 | K (provisional) | — |
| REQ-070 | S-F | A fleet manager can add, edit and retire the fleet's vehicles in the fleet portal, including connector, allowed adapters and maximum power. | SRC-D1#9, SRC-D1#11, SRC-C2@00:41:32, SRC-C2@00:42:11, CTX-004, CTX-100 | Y (provisional) | A-023 |
| REQ-071 | S-F | The fleet portal reports per vehicle and per month the bookings, no-shows, completed bookings and the charging energy of matched session records. | SRC-D1#8, SRC-D1#9, SRC-D1#11, CTX-004 | Y (provisional) | — |
| REQ-072 | S-F | A fleet sets whether its vehicles may use adapters, and the setting can be overridden per vehicle. | SRC-C2@00:41:53, SRC-C2@00:42:00, SRC-C2@00:42:11, CTX-100 | Y (provisional) | — |
| REQ-073 | S-F | A fleet manager sees the no-shows of the fleet's drivers. | SRC-C1@00:12:58, CTX-140 | Y (provisional) | — |
| REQ-074 | S-F | A fleet owner sees for each vehicle booked today whether arrival was recorded and whether a charging session started, updated as the evidence arrives. | SRC-C1@00:12:58, CTX-140 | Y (provisional) | Q-017 |
| REQ-075 | S-F | The platform reads SoC, charging state and location of a fleet's vehicles from Geotab where the fleet grants access. | SRC-C2@00:38:24, SRC-C2@00:40:31, SRC-C2@00:40:39, CTX-073, CTX-099 | I (provisional) | Q-014, A-022, Q-016 |

### Station portal

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-076 | S-F | A station operator sets the days and hours in which each of its sites accepts bookings, in the station portal. | SRC-D1#6, SRC-D1#11 | Y (provisional) | Q-005 |
| REQ-077 | S-F | A station operator changes a site's capacity rule in the station portal, and the change applies to new bookings at once with no Amperlane approval. | SRC-C1@00:26:54, SRC-C1@00:27:07, CTX-065 | Y (provisional) | A-018, Q-035 |
| REQ-078 | S-F | A station operator can record the tariffs that apply at each site. | SRC-D1#6, SRC-D1#11 | I (provisional) | Q-001 |
| REQ-079 | S-F | A station operator sees the upcoming bookings at its sites and the EVSE each one is allocated to. | SRC-D1#11, SRC-C2@00:52:34, CTX-047 | Y (provisional) | — |
| REQ-080 | S-F | A station operator sees, for each fault, how many bookings it forced to be rebooked, offered alternatives or sent to ops. | SRC-C2@00:35:14, CTX-037 | Y (provisional) | — |
| REQ-081 | S-F | Site staff, such as the LIC attendant, sign in to the platform on a site device through a site-scoped login of their own that ops can revoke at any time. | SRC-C1@00:08:34, SRC-C1@00:08:44, CTX-024, CTX-033, SRC-C1@00:08:08, SRC-C1@00:25:00 | K (provisional) | A-021, A-012, Q-049 |
| REQ-082 | S-F | The station portal shows, for each time window, how many EVSEs stay unbookable for walk-ups. | SRC-C1@00:25:55, SRC-C1@00:26:10, CTX-064 | Y (provisional) | Q-005 |

### Money, ledger and settlement

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-083 | S-F | Each fleet receives one consolidated invoice per month with net-30 payment terms. | SRC-C1@00:19:12, SRC-C1@00:33:25, SRC-C2@00:35:57, CTX-032, CTX-139 | K (provisional) | Q-037 |
| REQ-084 | S-F | Each fleet invoice is generated from ledger entries and submitted to the payment provider at month close with no manual data entry or file handling. | SRC-D1#5, SRC-D1#6, CTX-002 | K (provisional) | Q-001 |
| REQ-085 | S-F | The ledger is double-entry, with no balance columns. | SRC-C2@00:46:41, CTX-095 | K (provisional) | — |
| REQ-086 | S-F | The ledger shows, for each fleet and any past date, what the fleet owed, had paid and had outstanding. | SRC-C2@00:46:23, SRC-C2@00:46:41, CTX-126 | Y (provisional) | Q-021 |
| REQ-087 | S-F | Fleet invoice payments are collected through Stripe. | SRC-D1#9, SRC-D1#10, SRC-C2@00:03:28, CTX-051 | K (provisional) | A-007, Q-001 |

### Notifications and language

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-088 | S-F | After a booking is confirmed, the booker and the charging driver each receive one confirmation message in their language with the site, date, start time, duration and vehicle. | SRC-C1@00:05:34, CTX-043 | K (provisional) | — |
| REQ-089 | S-F | A driver never receives more than one confirmation for one booking. | SRC-C2@00:33:20, CTX-044 | K (provisional) | — |
| REQ-090 | S-F | An inbound SMS or WhatsApp message whose provider message id was already processed is not processed again. | SRC-C2@00:33:05, SRC-C2@00:33:15, SRC-C2@00:33:20, CTX-044, CTX-093 | K (provisional) | — |

### Reporting and metrics

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-091 | S-F | The platform reports completed bookings per month for NYC sites, using the definition configured under REQ-224, with migrated pilot data shown separately (REQ-225). | SRC-C1@00:29:22, SRC-C1@00:30:26, CTX-138 | Y (provisional) | Q-017 |
| REQ-092 | S-F | The platform reports per month, per fleet and per site the no-shows and the late arrivals, each as a share of all bookings whose slot fell in that month, with fault, site-full and maintenance rebooks not counted as no-shows. | SRC-C1@00:08:56, SRC-C1@00:09:10, SRC-C1@00:12:58, CTX-039, CTX-140 | Y (provisional) | CF-018, Q-029, Q-044 |
| REQ-093 | S-F | The platform reports the median wait from arrival to session start per site, from measured events. | SRC-D1#3, SRC-D1#7, SRC-C1@00:45:14, CTX-040 | I (provisional) | Q-009, Q-012 |
| REQ-094 | S-F | The platform reports utilisation per site for its off-peak windows. | SRC-D1#7, CTX-040 | I (provisional) | Q-005 |
| REQ-095 | S-F | On demand, the platform produces the Series A data-room report for any range of months since October 2025, with each figure computed under REQ-224 and REQ-225 and traceable to its booking ids. | SRC-C1@00:48:20, SRC-C2@00:04:43, CTX-053 | Y (provisional) | A-026, Q-020, Q-017 |

### Migration and pilot data

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-096 | S-F | The pilot history since October 2025 (bookings, no-shows, arrival times, drivers and stalls) is migrated into the platform. | SRC-C1@00:48:20, SRC-C2@00:04:43, CTX-053 | Y (provisional) | A-026, Q-020 |

### Delivery constraints and scope

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-097 | S-F | From the launch date, every new booking at the three pilot sites for the two pilot fleets is made and run in the platform, and none is taken in the pilot tools. | SRC-D1#7, SRC-C1@00:29:06, CTX-038, CTX-079 | K (provisional) | Q-007 |
| REQ-098 | S-F | Deprecated at P2.4 (2026-10-28): a scope statement, not testable alone; each actor's capabilities are separate rows (REQ-058, REQ-059, REQ-069, REQ-079, REQ-081). | SRC-C1@00:08:34, SRC-C1@00:08:44, SRC-C1@00:46:07, CTX-024 | — | CF-011, Q-037 | v1 | deprecated |
| REQ-099 | S-F | Deprecated at P2.4 (2026-10-28): a scope list, not testable alone; its parts are separate rows (REQ-002, REQ-059, REQ-069, REQ-076). | SRC-D1#9, SRC-D1#11, CTX-004 | — | CF-010, CF-025 | v1 | deprecated |

## S-NF · Stated non-functional

### Booking and capacity

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-100 | S-NF | A registered driver who opens the driver page from a message link books from the open-slot view in at most two taps (pick a slot, confirm), with site, vehicle and duration preset and changeable. | SRC-D1#5, SRC-C1@00:03:57, CTX-002 | K (provisional) | — |
| REQ-101 | S-NF | A database constraint enforces that no two active allocations on one EVSE overlap, so the rule holds even when application code is wrong. | SRC-C2@00:31:07, SRC-C2@00:31:16, SRC-C2@00:31:45, CTX-093 | K (provisional) | CF-023 |
| REQ-102 | S-NF | During a burst, competing attempts for the same site and slot are decided in the order the platform received them, so an earlier attempt never loses to a later one. | SRC-C2@00:32:16, SRC-C2@00:32:46, CTX-093 | Y (provisional) | — |
| REQ-103 | S-NF | Repeating a booking request with the same idempotency key creates at most one booking and returns the original result. | SRC-C2@00:32:51, SRC-C2@00:33:05, CTX-093 | K (provisional) | A-035 |

### Station integration and holds

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-104 | S-NF | For connected sites, each EVSE's status age, measured and evaluated as A-031 defines, is at most 60 seconds. | SRC-C2@00:49:22, SRC-C2@00:49:30, CTX-112 | K (provisional) | A-031, Q-012 |
| REQ-105 | S-NF | No CSMS vendor SDK is used inside the booking core, so moving a site to another CSMS changes only its integration. | SRC-C2@00:06:50, SRC-C2@00:07:08, CTX-086 | Y (provisional) | — |
| REQ-106 | S-NF | A webhook from a CSMS, the payment provider or the messaging provider that arrives twice or out of order changes state at most once and leaves the same final state as in-order delivery. | SRC-C2@00:14:55, SRC-C2@00:15:02, SRC-C2@00:15:14, CTX-091 | K (provisional) | A-035 |
| REQ-107 | S-NF | A periodic poll reconciles each connected site's EVSE status, so a lost webhook cannot leave status older than 60 seconds. | SRC-C2@00:15:02, SRC-C2@00:15:14, SRC-C2@00:49:30, CTX-091 | K (provisional) | A-031 |
| REQ-108 | S-NF | The booking and slot data model has a documented mapping to the OCPI 2.3 Booking module. | SRC-C2@00:13:32, SRC-C2@00:13:40, CTX-022 | I (provisional) | — |

### Money, ledger and settlement

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-109 | S-NF | Every fleet invoice line traces to ledger entries and to its booking when the invoice is issued. | SRC-C2@00:01:07, SRC-C2@00:47:25, CTX-127 | Y (provisional) | — |
| REQ-110 | S-NF | A scheduled check reconciles the status of invoices, and of payouts where the business model has them (Q-001), with the payment provider, so a lost payment webhook never leaves a record in the wrong state longer than one check interval. | SRC-C2@00:15:14, CTX-091 | Y (provisional) | — |
| REQ-111 | S-NF | The payment provider sits behind an interface, so it can be replaced without changing the booking core. | SRC-C2@00:47:10, SRC-C2@00:47:25 | Y (provisional) | A-007 |

### Notifications and language

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-112 | S-NF | All driver messages and the driver PWA are available in English, Spanish and Bengali. | SRC-C1@00:06:13, SRC-C1@00:45:35, SRC-C1@00:46:07, SRC-C2@00:50:56, SRC-C2@00:51:03, CTX-028, CTX-097 | K (provisional) | A-042 |

### Reporting and metrics

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-113 | S-NF | Each Five Boroughs booking reaches arrival, auto-release or an automatic rebook with no manual ops action in its audit trail, unless its site was full or faulted with no free compatible EVSE. | SRC-C1@00:33:03, CTX-139 | Y (provisional) | Q-023 |
| REQ-114 | S-NF | At Gowanus, every physical station hold the platform requests is matched by a platform instruction to clear it when the booking is released, cancelled or rebooked, so no stall stays marked after its booking ends. | SRC-C1@00:33:16, CTX-139 | Y (provisional) | A-012 |

### Migration and pilot data

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-115 | S-NF | Migrated pilot history lives in the platform's own data model, linked to the same driver, fleet, site and EVSE records as new bookings, and can be queried with them. | SRC-C2@00:04:43, CTX-053 | Y (provisional) | A-026 |
| REQ-116 | S-NF | A re-runnable pilot migration loads every source booking record or lists it as rejected with a reason, and its counts by month, site and original status equal those of the source export. | SRC-C1@00:48:20, SRC-C2@00:04:43, CTX-053 | Y (provisional) | Q-020 |
| REQ-117 | S-NF | No code from the discarded prototype is reused; only its schema is consulted. | SRC-C2@00:04:20, SRC-C2@00:58:41, CTX-052 | Y (provisional) | — |
| REQ-118 | S-NF | Pilot or platform data shared outside Amperlane or used outside production has driver names and phone numbers removed from every field, free text included. | SRC-C1@00:44:59 | Y (provisional) | — |

### Security, privacy and compliance

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-119 | S-NF | All platform code lives in Amperlane's repositories, and all infrastructure and data run in Amperlane's AWS accounts under Amperlane's Terraform. | SRC-C2@00:06:05, SRC-C2@00:06:41, CTX-005 | K (provisional) | — |
| REQ-120 | S-NF | Access to production systems and data is role-based, limited to named people and logged from the first release. | SRC-C2@00:44:04, SRC-C2@00:44:25, CTX-107 | K (provisional) | A-038 |
| REQ-121 | S-NF | From the first release, sign-ins, failed sign-ins, role and permission changes, production data access and configuration changes are audit-logged with actor and time. | SRC-C2@00:44:04, SRC-C2@00:44:25, CTX-107 | Y (provisional) | — |
| REQ-122 | S-NF | Every production change goes through a recorded change-management process with review and approval. | SRC-C2@00:44:04, SRC-C2@00:44:25, CTX-107 | Y (provisional) | — |
| REQ-123 | S-NF | Data is encrypted in transit and at rest. | SRC-C2@00:44:04, SRC-C2@00:44:25, CTX-107 | K (provisional) | A-037 |
| REQ-124 | S-NF | Production runs in an AWS account separate from every non-production environment. | SRC-C2@00:44:04, SRC-C2@00:44:25, CTX-107 | K (provisional) | — |
| REQ-125 | S-NF | Personal data is kept only as long as disputes, finance and the retention period counsel sets for its data type require, and is then deleted or anonymised automatically. | SRC-C2@00:50:34, SRC-C2@00:50:39, CTX-108 | Y (provisional) | A-025, Q-022 |
| REQ-126 | S-NF | An append-only audit trail records who did what and when for every booking state change, override, manual ops action, station hold and, where the business model has them (Q-001), payout. | SRC-C2@00:50:39, SRC-C2@00:53:46, CTX-110 | K (provisional) | — |
| REQ-127 | S-NF | Open-source components are used only where they are mature. | SRC-D1#10, SRC-C2@00:06:05, CTX-085 | Y (provisional) | — |

### Availability, performance and operations

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-128 | S-NF | Making bookings is available 99.9% of the time between 05:00 and 01:00 Eastern time. | SRC-C2@00:50:00, SRC-C2@00:50:06, SRC-C2@00:50:13, CTX-114 | K (provisional) | A-028, A-033, CF-015, Q-024 |
| REQ-129 | S-NF | Planned maintenance, and any deployment that interrupts booking, happens only between 01:00 and 05:00 Eastern time. | SRC-C2@00:50:06, SRC-C2@00:50:13, CTX-114 | K (provisional) | A-028 |
| REQ-130 | S-NF | Booking API responses take under 300 ms at the 95th percentile, including during the shift-change burst and the constraint check. | SRC-C2@00:49:44, SRC-C2@00:49:48, SRC-C2@00:49:52, CTX-113 | K (provisional) | A-032 |
| REQ-131 | S-NF | A load test of 2,000 booking attempts in 10 minutes, five times the modelled launch burst of about 400, with heavy contention on a few sites, meets the latency target with zero overlapping allocations. | SRC-C2@00:15:32, SRC-C2@00:16:00, SRC-C2@00:34:07, SRC-C2@00:34:22, CTX-055, CTX-115 | K (provisional) | A-009, A-034 |
| REQ-132 | S-NF | The platform supports at least 10,000 completed bookings a month in NYC by June 2027. | SRC-C1@00:29:22, SRC-C1@00:30:00, CTX-138 | K (provisional) | Q-017, Q-007 |
| REQ-133 | S-NF | Booking timers (hold expiry, reminder, station hold, pre-arrival check, grace, auto-release) run as durable workflows that survive restarts and maintenance, and fire late if needed but are never lost and take effect once. | SRC-C2@00:33:32, SRC-C2@00:33:51, CTX-094 | K (provisional) | A-028 |
| REQ-134 | S-NF | The workflow engine is self-hosted in Amperlane's AWS account. | SRC-C2@00:33:51, CTX-094 | Y (provisional) | A-029, Q-026 |
| REQ-135 | S-NF | The platform is one modular monolith, not a set of microservices. | SRC-C2@00:54:21, SRC-C2@00:54:45, CTX-087 | K (provisional) | — |
| REQ-136 | S-NF | The platform is written in TypeScript end to end, on PostgreSQL, hosted on AWS. | SRC-C2@00:06:05, CTX-085 | K (provisional) | — |
| REQ-137 | S-NF | Hosting uses Amperlane's AWS Activate credits first. | SRC-C2@00:06:05, CTX-085 | Y (provisional) | Q-025 |
| REQ-138 | S-NF | A test site in a time zone other than Eastern is configured, booked, allocated and released end to end with no change to the booking core. | SRC-D1#9, SRC-C1@00:31:33, CTX-008 | Y (provisional) | A-013 |
| REQ-139 | S-NF | Every booking function that the driver PWA, portals and ops console use is available through a versioned, documented API that they themselves use. | SRC-D1#9 | Y (provisional) | — |
| REQ-140 | S-NF | A simulated site lets engineers make chargers fault, overrun and report late drivers on demand. | SRC-C2@00:23:23, SRC-C2@00:55:37, SRC-C2@00:55:51, CTX-103 | Y (provisional) | — |
| REQ-141 | S-NF | An automated test replays the Gowanus fault (1:50 PM, nine bookings, two needing NACS or an adapter, during the shift change) and passes only if each booking is rebooked at Gowanus or offered alternatives, ops gets the summary, the station operator sees the outcomes and no booking is recorded as a no-show. | SRC-C2@00:55:37, SRC-C2@00:55:51, SRC-C2@00:56:04, CTX-047, CTX-103 | Y (provisional) | A-017 |

### Delivery constraints and scope

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-142 | S-NF | The platform goes live in NYC production on 1 March 2027 with real sites and real fleets and no spreadsheets in the critical path. | SRC-C1@00:29:06, CTX-079 | K (provisional) | — |
| REQ-143 | S-NF | Amperlane engineers work in the same repositories and rituals as Intellias from Phase 0, with no black-box handover. | SRC-C2@00:55:02, SRC-C2@00:55:08, SRC-C2@00:55:26, CTX-006 | Y (provisional) | — |
| REQ-144 | S-NF | By handover, Priya Nair owns the knowledge of the integration layer, confirmed by a handover checklist she signs. | SRC-C2@00:55:26, SRC-C2@00:55:32, CTX-006 | Y (provisional) | — |

## U-F · Unstated functional

### Booking and capacity

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-145 | U-F | Picking a slot places a hold on one unit of capacity, which expires and returns the capacity if the booker does not confirm within the hold time. | SRC-C2@00:27:21, SRC-D2#7, SRC-D2#12 | K (provisional) | A-001, A-005 |
| REQ-146 | U-F | Per-site parameters (time grid, durations, buffer, hold time, allocation and pre-arrival offsets, reminder lead time, grace and its maximum extension) are changed by ops without a deployment, each change is audited, and it applies to bookings confirmed after it while earlier bookings keep their values. | SRC-C2@00:19:19, SRC-C2@00:28:55, SRC-C1@00:43:44, SRC-D2#7, CTX-069 | Y (provisional) | A-001, A-002, A-003, A-011, A-020 |
| REQ-147 | U-F | A booking is confirmed only if, for every slot it covers, all bookings overlapping that slot, with the site's buffer, can still be allocated to distinct compatible EVSEs. | SRC-D2#12, SRC-C2@00:24:36, SRC-C2@00:41:32, CTX-092, CTX-100 | K (provisional) | A-014, CF-023 |
| REQ-148 | U-F | When the site is full at station-hold time or at the pre-arrival check, the driver immediately gets the next compatible slot at the same site and the nearest compatible free slots at other sites. | SRC-C2@00:24:04, SRC-C2@00:51:58, SRC-C2@00:52:32 | Y (provisional) | A-019, Q-033 | v2 | approved |
| REQ-149 | U-F | A booking rebooked because its site was full carries the reason code 'moved — site full'. | SRC-C2@00:24:04, SRC-C2@00:53:32 | Y (provisional) | A-019, Q-033 |
| REQ-150 | U-F | Cancelling a booking returns its capacity to the slot calendar as soon as the cancellation is confirmed. | SRC-C1@00:12:26, CTX-135 | K (provisional) | — |
| REQ-151 | U-F | Times are stored as instants and shown in the site's time zone with the zone indicated, and a booking across a daylight-saving change keeps its absolute duration. | SRC-C1@00:31:33, SRC-C2@00:50:06 | Y (provisional) | A-013 |
| REQ-152 | U-F | Drivers can book slots that start between 01:00 and 05:00 Eastern time. | SRC-C1@00:07:40, SRC-C1@00:18:24, SRC-D1#7 | Y (provisional) | A-028, CF-015, Q-024 |

### Station integration and holds

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-153 | U-F | When a booking with a charger reservation is cancelled, released or rebooked, the platform cancels the charger reservation. | SRC-C2@00:07:35, CTX-088 | K (provisional) | Q-009 |
| REQ-154 | U-F | For every booking the platform records the station-hold method used, each request sent, the response from the charger or site staff, and its time. | SRC-C2@00:08:09, SRC-C2@00:47:59, SRC-D2#8, CTX-127 | Y (provisional) | Q-009 |
| REQ-155 | U-F | When a charger reservation is rejected, or not answered within a set time, the platform sends a signage request to site staff and raises an ops exception. | SRC-C2@00:07:35, SRC-C2@00:09:34, SRC-C2@00:14:11, CTX-060, CTX-088 | K (provisional) | — |
| REQ-156 | U-F | When site staff have not acknowledged a station-hold request by the pre-arrival check, ops gets an exception to contact the site, and the booking stays valid. | SRC-C1@00:08:08, SRC-C1@00:37:27, SRC-C2@00:21:33, CTX-061 | Y (provisional) | A-046, Q-041, A-012 |
| REQ-157 | U-F | Deprecated at P2.4 (2026-10-28): merged into REQ-027, which keeps the client's statement (SRC-C2@00:21:33). | SRC-C1@00:37:27, SRC-C1@00:40:15, SRC-C1@00:40:25, CTX-034, CTX-043 | — | A-012, A-021 | v1 | deprecated |
| REQ-158 | U-F | The attendant view lets the attendant set each EVSE at the site to free, occupied or faulted. | SRC-C2@00:21:55, SRC-D2#6, SRC-D2#14, CTX-062 | K (provisional) | A-021, Q-010, Q-049 |
| REQ-159 | U-F | The attendant view shows which driver is due at which EVSE and when. | SRC-C2@00:21:55, SRC-D2#6 | Y (provisional) | A-021, Q-048 |
| REQ-160 | U-F | Every view of EVSE status shows when the status was observed, marks connected-site status older than 60 seconds as stale, and shows LIC status as 'last updated by attendant at <time>'. | SRC-C2@00:49:30, SRC-C2@00:49:38, CTX-112 | Y (provisional) | A-021 |
| REQ-161 | U-F | Every booking for which the operator provides a session record is matched to it within a set time of the record arriving, with energy, start and end, and bookings left unmatched go to the reconciliation queue (REQ-214). | SRC-C2@00:13:48, SRC-C2@00:47:29, CTX-127 | Y (provisional) | Q-009, Q-011, Q-012, Q-017 |
| REQ-162 | U-F | The platform ingests the LIC ChargePoint portal CSV, uploaded by hand at irregular times, for reconciliation only, and skips rows it already ingested. | SRC-C2@00:19:59, SRC-C2@00:21:49, SRC-C2@00:21:55, CTX-062 | Y (provisional) | A-021, Q-011 |
| REQ-163 | U-F | Where a CSMS provides pricing, the driver sees the site's public price before booking. | SRC-C2@00:19:30, CTX-061 | I (provisional) | Q-001, Q-012 |
| REQ-164 | U-F | The platform keeps a time-stamped history of every EVSE status change, so the status at any past moment can be retrieved. | SRC-C2@00:47:59, SRC-D2#10, CTX-127 | Y (provisional) | A-025 |
| REQ-165 | U-F | Ops onboards a new site in the ops console (operator, address, time zone, supply pattern, EVSEs, connectors, capacity rules, terms) without a code change, and the site becomes bookable only once ops marks it live. | SRC-C1@00:42:37, SRC-C1@00:43:44, SRC-C2@00:20:55, CTX-063, CTX-070 | Y (provisional) | A-022, Q-007 |
| REQ-166 | U-F | The platform connects to CPOs over OCPI 2.2.1 as an eMSP (Locations, Tariffs, Sessions, CDRs, Tokens and the RESERVE_NOW command), tested against a simulated CPO. | SRC-C2@00:25:36, SRC-C2@00:26:05, SRC-D2#14, CTX-104 | I (provisional) | A-015, A-022, Q-008 |
| REQ-167 | U-F | When the AMPECO API is unreachable or its status is stale, the platform runs station holds at Gowanus as at a status-only site until the API recovers. | SRC-C2@00:21:07, CTX-060, CTX-063, CTX-112 | Y (provisional) | — |
| REQ-168 | U-F | When a site's status feed is unavailable, the platform keeps accepting bookings within the capacity rules, shows the status as stale with its age, and raises an ops exception before the next allocation at that site. | SRC-C2@00:24:04, SRC-C2@00:49:38, CTX-061, CTX-112 | Y (provisional) | Q-012 |
| REQ-169 | U-F | When an API-connected EVSE sends no status for a set time while other EVSEs at its site still report, the platform marks it unknown, excludes it from new allocations and alerts ops. | SRC-C2@00:34:36, SRC-C2@00:51:36, CTX-047, CTX-048 | Y (provisional) | — | v2 | approved |
| REQ-170 | U-F | Ops can switch a site to manual mode, in which the platform keeps the slot calendar and gives ops a timed list of station holds instead of automated ones. | SRC-C1@00:40:15, SRC-C2@00:53:49, CTX-034 | Y (provisional) | — |

### Arrival, grace and no-show

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-171 | U-F | A booking cancelled before the site's cancellation cut-off (Q-042) gets no no-show fee. | SRC-C1@00:12:26, CTX-135 | Y (provisional) | Q-042, Q-002 |
| REQ-334 | U-F | A 'running late' report by itself never waives the no-show fee of a driver who then does not arrive within grace. | SRC-C1@00:12:26, CTX-135 | Y (provisional) | Q-042, Q-002 |
| REQ-172 | U-F | The booking confirmation tells the driver the grace period and the no-show fee terms that apply to the booking. | SRC-C1@00:47:44, SRC-D2#18 | Y (provisional) | Q-002 |
| REQ-173 | U-F | The platform records arrival from the phone's location only when the driver has opted in. | SRC-C2@00:39:22, SRC-C2@00:40:06, CTX-102, CTX-109 | I (provisional) | A-024, Q-016 |
| REQ-174 | U-F | The platform records arrival from a CSMS session-start event on the booking's allocated EVSE between a set time before the slot and the end of grace, where the CSMS sends one. | SRC-C2@00:40:06, SRC-D2#7, CTX-102 | Y (provisional) | Q-009, Q-012 |
| REQ-175 | U-F | The platform records arrival when a vehicle's telematics location enters the site's geofence, where the fleet authorised it and the driver opted in. | SRC-C2@00:38:05, SRC-D2#7, CTX-101 | I (provisional) | Q-014, Q-016, A-024 |
| REQ-176 | U-F | The attendant can confirm a driver's arrival in the attendant view. | SRC-C2@00:21:55, SRC-D2#6 | Y (provisional) | A-021, Q-010, Q-049 |
| REQ-177 | U-F | Once arrival is recorded, the booking is not released at the end of grace, even when the grace timer fires late. | SRC-D2#7, CTX-131 | K (provisional) | A-028 |
| REQ-178 | U-F | While a session runs, the platform shows its live status from the CSMS where the CSMS provides it. | SRC-D2#7 | I (provisional) | Q-009, Q-012 |
| REQ-179 | U-F | For a disputed no-show, ops sees on one screen the booking's ordered history: states, actors, reason codes, station-hold attempts, EVSE status at the time, arrival evidence, messages and the session record. | SRC-C2@00:47:53, SRC-C2@00:47:59, CTX-110, CTX-127 | Y (provisional) | A-024, A-047 |
| REQ-180 | U-F | No no-show fee is created automatically for a booking that was rebooked, whose station hold failed, whose site was full or faulted, whose reminder was not delivered, or whose grace timer fired late, and each such booking goes to the ops exception queue, where ops creates or waives the fee with a reason code. | SRC-C2@00:24:04, SRC-C2@00:52:53, CTX-036 | K (provisional) | A-019, A-028, Q-002 |
| REQ-181 | U-F | When a booking has an arrival but no charging session starts within a set time, no no-show fee is created, and the booking is rebooked at the site or routed to ops as a fault case. | SRC-C2@00:47:53, SRC-C2@00:47:59 | Y (provisional) | — |
| REQ-182 | U-F | Ops can waive a no-show fee before it is invoiced, with a reason code, recorded as a separate ledger entry. | SRC-C1@00:38:52, SRC-C1@00:39:22, CTX-035 | Y (provisional) | Q-002 |
| REQ-183 | U-F | The no-show fee amount and the station operator's share of it are set per site. | SRC-C1@00:43:27, SRC-C1@00:43:44, CTX-069 | Y (provisional) | Q-002, Q-005 |

### Charger faults and ops console

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-184 | U-F | Ops can place a maintenance hold that removes EVSEs or capacity at a site from booking for a time window. | SRC-C2@00:53:00, CTX-035 | Y (provisional) | A-018, Q-035 |
| REQ-335 | U-F | Ops can place a fleet-priority hold that keeps capacity at a site for a time window for one named fleet's bookings only. | SRC-C2@00:53:00, CTX-035 | Y (provisional) | A-018, Q-035 |
| REQ-185 | U-F | When a maintenance hold removes an EVSE with allocated bookings, those bookings are rebooked as on a fault, with the reason code 'moved — maintenance'. | SRC-C2@00:53:00 | Y (provisional) | A-018, Q-035 |
| REQ-186 | U-F | When a station operator lowers a capacity rule, or ops adds a fleet-priority hold, below the confirmed bookings, those bookings stand and the station operator or ops sees each booking above the new limit to act on it. | SRC-C1@00:26:54, SRC-C2@00:53:00, CTX-065 | Y (provisional) | A-018, Q-035 |
| REQ-187 | U-F | Ops sees a summary of the automatic fault rebookings and can undo any of them. | SRC-C2@00:53:00 | Y (provisional) | A-017, CF-022 |
| REQ-188 | U-F | For fault-affected bookings the platform could not place, it proposes rebookings that ops approves in bulk. | SRC-C2@00:53:00, CTX-035 | Y (provisional) | A-017, CF-022, Q-038 |
| REQ-189 | U-F | The ops console lists every open exception (failed or unacknowledged station hold, site full, fault, unplaced booking, undelivered time-critical message, status feed down, fee decision, open dispute) in one queue, in which the exceptions ops must handle before a booking's grace ends come first, ordered by that booking's slot start or, for a site-level exception, by the next allocation it affects, followed by the other exceptions, such as disputes and fee decisions, oldest first. | SRC-C2@00:24:04, SRC-C2@00:53:49, CTX-035 | K (provisional) | Q-023 | v2 | approved |
| REQ-190 | U-F | The ops console shows one live board per site for the current day with bookings by state, EVSE status with its age, and open exceptions. | SRC-C2@00:02:34, CTX-042 | Y (provisional) | — |
| REQ-191 | U-F | A driver can report a faulted EVSE in one tap from the booking page or by message, which creates an ops alert linked to the site and EVSE. | SRC-C2@00:34:36, SRC-C2@00:51:36, CTX-048 | Y (provisional) | — |
| REQ-192 | U-F | At LIC, a faulted status set by the attendant triggers the same rebooking as a CSMS fault. | SRC-C2@00:21:55 | Y (provisional) | A-021, Q-010 |
| REQ-193 | U-F | A station operator can mark an EVSE out of service in the station portal, which triggers fault rebooking. | SRC-C2@00:34:36, CTX-048 | I (provisional) | — |
| REQ-194 | U-F | After a fault, an EVSE returns to the pool only after it has reported available for a set time or ops returns it, and bookings already rebooked are not moved back. | SRC-C2@00:51:36, CTX-047 | Y (provisional) | — |
| REQ-195 | U-F | Ops can find a driver's bookings, messages and fees by mobile number, plate or booking code in one search. | SRC-C1@00:38:15, CTX-045 | Y (provisional) | — |
| REQ-196 | U-F | The ops console shows the full message history per driver and booking, with language and delivery status. | SRC-C1@00:37:27, CTX-043 | I (provisional) | — |
| REQ-197 | U-F | Ops can send a templated or free-text message to a driver on the driver's channel from the ops console, recorded against the booking. | SRC-C2@00:51:58, CTX-047 | Y (provisional) | — |

### Driver channel and identity

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-198 | U-F | A driver is identified by a mobile number registered to one or more fleets and can book any vehicle those fleets' policies allow. | SRC-C1@00:04:48, SRC-C1@00:05:47, SRC-C1@00:07:40, CTX-026 | Y (provisional) | A-006, A-016, A-023, Q-028 |
| REQ-199 | U-F | Each driver has a preferred language, set by the fleet, by ops or by the driver, every message and PWA screen uses it, and English is used only for drivers with no language set. | SRC-C1@00:06:13, SRC-C2@00:50:56, SRC-C2@00:53:00, CTX-028 | K (provisional) | A-042 |
| REQ-200 | U-F | When the EVSE is allocated or reallocated, the charging driver gets a message on their channel naming the EVSE and the stall. | SRC-C1@00:05:34, SRC-C2@00:24:36, CTX-092 | K (provisional) | A-002 |
| REQ-201 | U-F | A fleet can register a booker-only number that books for the fleet and names the charging driver. | SRC-C1@00:07:40, SRC-C1@00:11:16, CTX-029 | Y (provisional) | A-023, Q-028 |
| REQ-202 | U-F | When a fleet removes a driver, that driver's number can no longer book for that fleet on any channel (PWA, SMS, WhatsApp or an earlier link) from the moment of removal. | SRC-C1@00:04:48, CTX-026 | K (provisional) | A-023, Q-028, Q-045 |
| REQ-203 | U-F | When a driver's number is registered, the driver gets a welcome message in their language explaining how to book, cancel and report running late. | SRC-C1@00:05:47, CTX-027, CTX-028 | Y (provisional) | A-023 |
| REQ-204 | U-F | A driver who has not opted in to location can complete every booking step, with arrival taken from a QR scan, the CSMS session start or the attendant. | SRC-C2@00:40:06, SRC-C2@00:40:24, CTX-102 | K (provisional) | A-024 |

### Fleet portal and policy

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-205 | U-F | A fleet registers its drivers' mobile numbers and its vehicles in the fleet portal. | SRC-C1@00:05:47, SRC-C1@00:25:00 | Y (provisional) | A-023, Q-028 |
| REQ-206 | U-F | Ops can onboard a fleet and register its drivers and vehicles on its behalf, and a fleet manager can later take this over in the fleet portal. | SRC-C1@00:25:00, CTX-030 | K (provisional) | A-023, Q-028 |
| REQ-207 | U-F | A fleet manager or ops can import a fleet's vehicles and driver numbers from one file, with validation errors listed per row. | SRC-C1@00:42:50, CTX-073, CTX-100 | Y (provisional) | — |
| REQ-208 | U-F | A fleet manager can see the charges accrued in the current month before the invoice is issued. | SRC-C1@00:33:25, CTX-032 | I (provisional) | Q-037 |

### Station portal

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-209 | U-F | A station operator sees the off-peak sessions that Amperlane bookings brought to each site. | SRC-C1@00:18:24, SRC-C1@00:18:56, SRC-D1#7, CTX-119 | I (provisional) | Q-001 |

### Money, ledger and settlement

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-210 | U-F | The ledger records, with no schema change, a sample month of each Q-001 option (booking fee, fleet subscription, energy resale at B2B cost, station fee, no-show fee with station share, payouts), and every sample transaction balances. | SRC-C2@00:48:32, CTX-129 | K (provisional) | Q-001 |
| REQ-211 | U-F | A no-show fee is a separate line item, never mixed into energy charges. | SRC-C2@00:47:59, CTX-127 | K (provisional) | Q-002 |
| REQ-212 | U-F | A disputed no-show fee line can be reversed without changing any energy line. | SRC-C2@00:47:59, SRC-C2@00:53:00, CTX-127 | K (provisional) | Q-002 |
| REQ-213 | U-F | Reversing a fee line after the invoice that carried it was issued creates a credit line on the next invoice and never changes the issued invoice. | SRC-C1@00:33:25, SRC-C2@00:47:59, CTX-127 | Y (provisional) | Q-002 |
| REQ-214 | U-F | A booking that ends without a matched session record, and a session record on a booked EVSE and window without a matched booking, go to a reconciliation queue and are neither billed nor marked no-show until resolved. | SRC-C2@00:47:29, SRC-C2@00:47:53, SRC-C2@00:47:59, CTX-127 | Y (provisional) | Q-009, Q-011, Q-012 |
| REQ-215 | U-F | Amperlane finance has views for fleet invoices, reconciliation against session records and disputes, and finance users cannot change bookings, capacity rules or fleet policies. | SRC-C2@00:47:08, SRC-D2#6, CTX-025 | Y (provisional) | A-010, Q-037, CF-011 |
| REQ-216 | U-F | The platform tracks the payment status of every fleet invoice and flags any invoice unpaid after its due date. | SRC-C1@00:21:44, SRC-C2@00:46:23 | Y (provisional) | Q-021 |
| REQ-217 | U-F | Each fleet invoice lists every charged item with booking id, site, date, vehicle and driver. | SRC-C1@00:19:12, SRC-C1@00:33:25, CTX-032 | Y (provisional) | Q-001 |
| REQ-218 | U-F | An invoice month closes at a set time after month end, with period boundaries in the site's local time, and records that arrive after close go to the next invoice as adjustments. | SRC-C2@00:21:49, CTX-062, CTX-127 | Y (provisional) | A-013 |

### Notifications and language

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-219 | U-F | When a confirmation, reminder, allocation notice, re-offer or fault notice is reported undelivered, or has no delivery status within a set time, the platform lists the driver among undelivered messages in the ops console and resends the message on the driver's other registered channel, a confirmation only if it was reported undelivered. | SRC-C2@00:51:03, CTX-041, CTX-097 | Y (provisional) | A-008, Q-034 | v2 | approved |
| REQ-220 | U-F | Keyword replies (cancel, running late, accept or decline an alternative, help) are understood in English, Spanish and Bengali. | SRC-C1@00:06:13, SRC-C1@00:12:42, CTX-028 | Y (provisional) | — |
| REQ-221 | U-F | Every message to a driver tells the driver, in their language, how to reach ops. | SRC-C1@00:06:13, SRC-C1@00:37:27, CTX-028 | I (provisional) | — |
| REQ-222 | U-F | An inbound driver message the platform cannot understand goes to ops with the driver's language shown, and the driver gets an acknowledgement in their language. | SRC-C1@00:06:13, SRC-C1@00:37:27, CTX-045 | Y (provisional) | — |
| REQ-223 | U-F | During a platform outage, a driver who texts the booking number gets an automatic reply in their language that booking is unavailable and how to reach ops. | SRC-C2@00:02:58, CTX-043, CTX-114 | I (provisional) | — |

### Reporting and metrics

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-224 | U-F | For each booking the platform stores arrival, session-record match with energy, rebooks and reason codes, and reports completed bookings by a definition over those fields that ops can change without a deployment. | SRC-C1@00:13:26, SRC-C1@00:29:22, SRC-C2@00:30:01 | K (provisional) | Q-017 |
| REQ-225 | U-F | Migrated pilot data is marked as pilot data in every report, reported under the same status definitions as platform data, and every metric can be shown with or without it. | SRC-C2@00:05:22, SRC-C2@00:52:53, CTX-054 | Y (provisional) | A-026, CF-018, Q-029 |
| REQ-226 | U-F | The platform reports per site and day: booking attempts, expired holds, confirmations, alternatives offered and accepted, cancellations, no-shows, late arrivals and completed bookings. | SRC-C1@00:08:56, SRC-C1@00:30:00, CTX-039, CTX-138 | I (provisional) | Q-044 |
| REQ-227 | U-F | The platform reports ops workload: exceptions per day by type, time to pick up, and manual ops actions per booking. | SRC-C1@00:33:03, SRC-C1@00:38:15, CTX-139 | I (provisional) | — |

### Migration and pilot data

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-228 | U-F | Migrated statuses are re-classified so that moved, no-show and cancelled are distinct outcomes, and each re-classified record keeps its original status and the rule and evidence used. | SRC-C2@00:05:22, SRC-C2@00:52:53, CTX-054 | Y (provisional) | A-026, CF-018, Q-029 |
| REQ-229 | U-F | Where a site's pilot Google Sheet and Airtable disagree, the migration applies one documented precedence rule and lists every conflict it resolved. | SRC-C2@00:02:34, SRC-C2@00:05:22, CTX-042, CTX-054 | Y (provisional) | Q-020, A-026 |
| REQ-230 | U-F | Migrated records from before February 2026 carry a data-quality flag. | SRC-C2@00:05:22, CTX-054 | Y (provisional) | Q-020 |
| REQ-231 | U-F | At cut-over, every pilot booking for a slot after the cut-over exists in the platform with its driver, site and window, and its driver is told in their language how to manage it. | SRC-C1@00:29:06, SRC-C1@00:33:22, CTX-079 | K (provisional) | A-026 |
| REQ-232 | U-F | Each booking is invoiced exactly once, by the pilot process if its slot started before the cut-over and by the platform otherwise. | SRC-C1@00:13:26, SRC-C2@00:03:28, CTX-051 | K (provisional) | Q-017 |

### Security, privacy and compliance

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-233 | U-F | Ops can anonymise one driver's personal data on request, keeping booking, audit and ledger records with the driver replaced by a pseudonym. | SRC-C2@00:50:34, CTX-095, CTX-108, CTX-110 | Y (provisional) | A-025, Q-022 |
| REQ-234 | U-F | When a fleet or station operator leaves the platform, its users are disabled, its future bookings are cancelled with a reason code, and its data is kept or deleted per the retention matrix. | SRC-C1@00:43:27 | I (provisional) | A-025 |
| REQ-235 | U-F | Fleet and station portal users can sign in with a one-time link or code sent to their email or phone, without a password. | SRC-C1@00:25:00, CTX-030 | I (provisional) | A-038 |

## U-NF · Unstated non-functional

### Booking and capacity

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-236 | U-NF | Every state-changing command from any channel (confirm, cancel, running late, accept an alternative, ops override, capacity-rule change) carries an idempotency key, and a repeat with the same key makes no second state change and returns the first result. | SRC-C2@00:32:51, SRC-C2@00:33:05, CTX-093, CTX-135 | K (provisional) | A-035 |

### Station integration and holds

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-237 | U-NF | Staging runs every integration against a sandbox or simulator and never against production chargers, real payments or real drivers. | SRC-C2@00:36:50, SRC-C2@00:37:15, CTX-072, CTX-107 | Y (provisional) | Q-009 |
| REQ-238 | U-NF | Open Charge Map data is shown with the attribution its CC BY 4.0 licence requires. | SRC-C2@00:11:03 | I (provisional) | — |

### Charger faults and ops console

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-239 | U-NF | If automatic fault rebooking stops partway, every affected booking ends rebooked, proposed to ops, or on its original EVSE with an ops exception, never in an intermediate state. | SRC-C2@00:51:58, CTX-047, CTX-136 | Y (provisional) | A-017 |

### Driver channel and identity

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-240 | U-NF | Links in driver messages are signed and single-use, open only that driver's bookings without a password, keep working on the device that first opened them until a set time after the booking's grace ends, and a driver can get a new link by texting from the registered number. | SRC-C1@00:05:47, CTX-027 | K (provisional) | A-006, Q-028 |
| REQ-241 | U-NF | On a device that has not completed a one-time code for that driver within a set period, a booking link shows only the booking's site and time and its one-tap actions (cancel, running late, accept an offered slot or alternative, report a faulted EVSE or a blocked stall), and any other personal data or change needs a one-time code sent to the registered number. | SRC-C1@00:07:40, SRC-C2@00:44:25, SRC-C1@00:12:42, CTX-135 | Y (provisional) | A-006, Q-028 | v2 | approved |
| REQ-242 | U-NF | A command received by SMS or WhatsApp that changes a booking is accepted only from the registered number of that booking's booker or charging driver. | SRC-C1@00:05:47, CTX-029 | K (provisional) | A-006, A-023 |

### Fleet portal and policy

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-243 | U-NF | A small fleet can book and see whether each booked charge took place through messaging and Amperlane ops, without logging into the fleet portal. | SRC-C1@00:12:58, SRC-C1@00:25:00, CTX-030, CTX-074 | Y (provisional) | A-023 |

### Money, ledger and settlement

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-244 | U-NF | Every invoice, and every payout where the business model has them (Q-001), submitted to the payment provider carries an idempotency key, so a retry never invoices a fleet or pays a station operator twice. | SRC-C2@00:01:07, CTX-095 | K (provisional) | A-035 |
| REQ-245 | U-NF | When the payment provider is unavailable, bookings, arrivals and fee lines are still recorded, and each pending invoice submission is retried at a set interval until the provider accepts it. | SRC-C1@00:13:26, CTX-051 | Y (provisional) | A-007 |
| REQ-246 | U-NF | Card details are entered only on payment-provider-hosted pages or fields, so card numbers never reach Amperlane's systems. | SRC-C2@00:03:28, CTX-051 | Y (provisional) | A-007 |
| REQ-247 | U-NF | Ledger entries are append-only, and every correction is made by a new entry. | SRC-C2@00:46:46, CTX-095 | K (provisional) | — |

### Notifications and language

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-248 | U-NF | Drivers get SMS or WhatsApp messages only after the platform has recorded the driver's agreement to booking messages, with its time and how it was given, and a STOP reply ends messages on that channel at once. | SRC-C2@00:02:58, CTX-097 | K (provisional) | A-023, Q-047 |
| REQ-249 | U-NF | Every WhatsApp message the platform starts outside a 24-hour window opened by the driver uses a pre-approved template in the driver's language. | SRC-C2@00:50:56, SRC-C2@00:51:03, CTX-097 | Y (provisional) | Q-034 |
| REQ-250 | U-NF | Consent texts, fee notices and their language versions exist in English, Spanish and Bengali, and the platform stores which version and language each driver accepted, with the time. | CTX-028, CTX-109 | Y (provisional) | A-024, Q-016, Q-002 |

### Reporting and metrics

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-251 | U-NF | Cloud and usage-priced vendor costs (messaging, maps, telematics, payments) are reported monthly per completed booking. | SRC-C2@00:06:05, SRC-C2@00:38:50, CTX-080, CTX-144 | I (provisional) | Q-025 |

### Migration and pilot data

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-252 | U-NF | The raw pilot export is stored read-only, accessible only to named people, and deleted at the end of the period counsel sets. | SRC-C2@00:58:37 | Y (provisional) | A-025, A-026, Q-022 |

### Security, privacy and compliance

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-253 | U-NF | Credentials and any licence or account numbers the platform holds are listed in the data register, encrypted at rest, readable only by named roles, and every read is audit-logged. | SRC-C2@00:50:18, SRC-D2#13, CTX-108 | K (provisional) | Q-022 |
| REQ-254 | U-NF | A breach-notification procedure that meets the NY SHIELD Act exists before launch, and the platform can list the individuals and data elements affected by a suspected breach. | SRC-C2@00:50:18, SRC-D2#13, CTX-108 | K (provisional) | Q-022 |
| REQ-255 | U-NF | Location is collected only after the driver's explicit opt-in, which is off by default, only between the pre-slot reminder and the end of grace, and never after the driver withdraws. | SRC-C2@00:39:22, SRC-D2#13, CTX-109 | K (provisional) | A-024, Q-016 |
| REQ-256 | U-NF | Location is kept only as derived arrival events, encrypted and access-controlled, and each raw location reading is deleted once its arrival event is derived. | SRC-C2@00:50:18, SRC-C2@00:50:34, CTX-108 | Y (provisional) | A-025, Q-022 |
| REQ-257 | U-NF | Vehicle data is read only for vehicles whose fleet has recorded its authorisation as account owner, and reading stops when the fleet revokes it. | SRC-C2@00:39:18, SRC-C2@00:39:22, CTX-109 | Y (provisional) | A-024, Q-014, Q-016 |
| REQ-258 | U-NF | Each portal user sees only their own organisation's data: a fleet user only that fleet's vehicles, drivers, bookings and invoices, a station operator only its own sites and no drivers' phone numbers, and an attendant only the current day's bookings at their site. | SRC-D2#10, SRC-D2#11, CTX-107, CTX-108 | K (provisional) | A-016, Q-048 |
| REQ-259 | U-NF | Ops users can view a driver's location evidence only within an open dispute for that booking. | SRC-C2@00:50:18, CTX-108 | Y (provisional) | A-024 |
| REQ-260 | U-NF | The platform rejects and logs inbound messaging and CSMS webhooks whose signature or shared secret does not verify. | SRC-C2@00:14:11, CTX-091, CTX-107 | Y (provisional) | — |
| REQ-261 | U-NF | Deprecated at P2.4 (2026-10-28): merged into REQ-081, which keeps the client's statement (SRC-C1@00:08:34). | SRC-C1@00:08:08, SRC-C1@00:25:00, CTX-033 | — | A-021, Q-049 | v1 | deprecated |
| REQ-262 | U-NF | The audit trail also records changes to capacity rules, fleet policies, partner terms, user roles and per-EVSE settings, with before and after values. | SRC-C2@00:50:39, CTX-065, CTX-110 | Y (provisional) | — |
| REQ-263 | U-NF | Every view or export of a driver's personal data by an ops, finance, fleet, station-operator or site-staff user is recorded in the audit trail. | SRC-C2@00:50:18, CTX-108, CTX-110 | Y (provisional) | — | v2 | approved |
| REQ-264 | U-NF | A register of every vendor that receives platform data records which data each receives and why. | SRC-C2@00:44:04, CTX-107, CTX-108 | I (provisional) | — |
| REQ-265 | U-NF | The platform stores no driver's licence, TLC licence or bank account numbers unless the data register records a purpose for them approved by Amperlane. | SRC-C2@00:50:18, CTX-108 | Y (provisional) | — |

### Availability, performance and operations

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-266 | U-NF | Ops can get the next bookings per site from a copy kept outside the primary system and refreshed at a set interval, so bookings can be honoured by phone during a platform outage. | SRC-C1@00:33:22, CTX-042, CTX-139 | Y (provisional) | — |
| REQ-267 | U-NF | Amperlane's engineers can export all platform data in open formats without Intellias' help. | SRC-C2@00:06:05, SRC-C2@00:06:41, CTX-005 | Y (provisional) | — |
| REQ-268 | U-NF | Every alert and every external-system outage has a written runbook that Amperlane's engineers have used at least once before hypercare ends. | SRC-C2@00:55:08, SRC-C2@00:55:26, CTX-006, CTX-007 | Y (provisional) | Q-039 |

### Delivery constraints and scope

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-269 | U-NF | For a set period before 1 March 2027 the platform runs real bookings with real drivers at all three pilot sites, and the Amperlane Concierge process is switched off only after the written go-live criteria are met. | SRC-C1@00:29:06, SRC-C1@00:48:45, CTX-079, CTX-082 | Y (provisional) | Q-025 |

## Parking lot

V means "not this release, visible and agreed" (constitution, KYIV rules). Each row keeps its ID. The Q/A column says
why it is parked and which decision it waits for. Option rows are priced as options in the proposal (P5); if the
client chooses one, it enters through a change request, which sets its KYIV. Rows the client deferred cite the
deferral.

### Parking lot · business-model options (Q-001)

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-270 | S-F | Each fleet invoice covers its drivers' energy, so fleet finance never handles drivers' card receipts. | SRC-C1@00:19:12, SRC-C2@00:35:57, CTX-032 | V | Q-001: options B and C only |
| REQ-271 | S-F | The platform invoices each fleet monthly for a fee per completed booking ($2 today). | SRC-C1@00:13:26, SRC-C2@00:03:28, CTX-051 | V | Q-001: today's booking-fee model only (CF-008); Q-017 |
| REQ-272 | S-F | After each completed session, the station operator's payable amount is recorded automatically. | SRC-D1#6 | V | Q-001: Amperlane pays stations (options B, C) |
| REQ-273 | S-F | The platform records each session's cost to Amperlane at the station operator's B2B tariff per kWh. | SRC-C1@00:19:54, SRC-C1@00:20:49, CTX-121, CTX-141 | V | Q-001: option B (eMSP spread) |
| REQ-274 | S-F | The platform bills fleets a bundled per-kWh rate that includes the guaranteed slot. | SRC-C1@00:19:54, SRC-C1@00:20:49, CTX-121, CTX-122 | V | Q-001: option B (eMSP spread) |
| REQ-275 | S-F | The platform charges station operators a take rate of 10–12% on charging GMV booked through Amperlane. | SRC-D1#8, CTX-116, CTX-117, CTX-118 | V | Q-001: option A, rejected by every station pitched (CTX-118) |
| REQ-276 | S-F | The platform charges station operators a fee only on incremental off-peak sessions, never on sessions they would have had anyway at peak. | SRC-C1@00:18:24, SRC-C1@00:18:56, SRC-C1@00:23:13, CTX-119 | V | Q-001: the COO's option; Q-046 |
| REQ-277 | S-F | When Amperlane holds station operators' money, they are paid weekly, with the payout frequency set per station operator. | SRC-C1@00:43:56, SRC-C2@00:35:42, SRC-C1@00:48:14, CTX-068 | V | Q-001, Q-005, CF-024 |
| REQ-278 | S-F | Fleets are invoiced through Stripe Invoicing and station operators are paid by Stripe Connect separate charges and transfers. | SRC-C2@00:45:58, SRC-C2@00:46:21, SRC-C2@00:56:15, SRC-C2@00:56:43, CTX-128 | V | Q-001: options B and C; Q-019, A-007 |
| REQ-279 | S-NF | Money owed to station operators is held and moved by Stripe and never sits in an Amperlane bank account, so Amperlane needs no New York money-transmitter licence. | SRC-C2@00:45:17, SRC-C2@00:45:33, CTX-106 | V | Q-001: only if money flows through Amperlane; Q-019 |
| REQ-280 | U-F | The ledger shows Amperlane's exposure between weekly payouts to station operators and net-30 fleet payments, and finance is alerted when a fleet invoice is overdue by a set number of days. | SRC-C2@00:46:23, SRC-D2#17, CTX-126 | V | Q-001, Q-021, CF-024 |
| REQ-281 | U-F | Each fleet has a credit limit on its outstanding balance, and exceeding it triggers the fleet's configured action. | SRC-D2#17, SRC-R1#risks, CTX-126 | V | Q-021, Q-001 |
| REQ-282 | S-NF | In a merchant-of-record model, energy is billed only from a matched session record that meets a set reconciliation tolerance. | SRC-C1@00:24:11, SRC-C1@00:24:35, CTX-124 | V | Q-001: options B and C; Q-009, Q-011, Q-012 |
| REQ-283 | U-F | Stripe files and delivers 1099 forms for station operators paid through the platform. | SRC-C2@00:46:46, SRC-C2@00:47:08, CTX-111 | V | Q-001: Amperlane pays stations |
| REQ-284 | U-F | A pricing module applies station operators' B2B tariffs and fleet bundled rates to session records, using the tariff version in force at session start. | SRC-D2#9, SRC-C1@00:19:54, CTX-121 | V | Q-001: options B and C |
| REQ-285 | U-F | As merchant of record, Amperlane issues receipts and tax lines for the energy it sells to fleets, showing kWh and price per kWh per session. | SRC-C2@00:48:32, CTX-129 | V | Q-001: merchant of record; Q-019 |
| REQ-286 | U-F | A fleet can dispute an energy charge, and ops resolves it against the operator's session record. | SRC-C1@00:21:44, CTX-122 | V | Q-001: options B and C |
| REQ-287 | U-F | A station operator sees its payouts in the station portal, each with a statement of the sessions and fee lines it covers. | SRC-D2#6, SRC-D2#14, SRC-C1@00:43:56 | V | Q-001: Amperlane pays stations |
| REQ-288 | U-F | A failed payout stays owed in the ledger, finance is alerted, and it is paid in the next payout once fixed. | SRC-C2@00:35:42, CTX-068 | V | Q-001: Amperlane pays stations |
| REQ-289 | U-F | Finance can hold a station operator's payout with a reason code until it is released. | SRC-C2@00:47:59, CTX-127 | V | Q-001: Amperlane pays stations |
| REQ-290 | U-F | A station operator completes payment-provider onboarding through the provider's hosted flow before any payout is attempted. | SRC-C2@00:45:33, CTX-128 | V | Q-001: Amperlane pays stations; Q-019 |
| REQ-291 | U-NF | No single user can both change a station operator's payout account details and approve a payout run. | SRC-C2@00:44:04, CTX-107 | V | Q-001: Amperlane pays stations |
| REQ-292 | U-F | A chargeback or bank return is recorded in the ledger and shown to finance with the booking evidence. | SRC-C1@00:21:44, CTX-122 | V | Q-001: Amperlane collects energy money; Q-002 |
| REQ-293 | S-F | The platform bills each fleet a subscription per vehicle per month ($15 in the brief), with a documented rule for vehicles added or removed mid-month. | SRC-D1#8, SRC-C1@00:19:12, CTX-116, CTX-120 | V | Q-001: fleet subscription, price open |
| REQ-294 | S-F | A fleet manager can restrict which sites the fleet's drivers may book. | SRC-C1@00:24:42, SRC-C1@00:25:00, CTX-031, CTX-125 | V | Q-032: spend controls, which depend on Q-001 |
| REQ-295 | S-F | A fleet manager can set a maximum number of bookings per driver per day, such as two. | SRC-C1@00:25:00, CTX-031, CTX-125 | V | Q-032: spend controls, which depend on Q-001 |
| REQ-296 | S-F | Drivers never pay at the charger with their own cards, because Amperlane bills the session. | SRC-D1#5, SRC-D1#6, CTX-002 | V | Q-001: options B and C; today drivers pay stations (CTX-051) |
| REQ-297 | U-F | Adyen for Platforms replaces Stripe for payouts to station operators. | SRC-C2@00:47:10 | V | Q-001, A-007: only for pricing at scale |

### Parking lot · no-show fee options (Q-002, Q-003)

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-298 | S-F | The payer of the no-show fee (fleet, driver, or fleet pays and deducts) is a setting per fleet. | SRC-C1@00:10:56, SRC-C1@00:11:26, SRC-C1@00:11:36, SRC-C2@00:30:36, CTX-077, CTX-134 | V | Q-002: payer undecided |
| REQ-299 | U-F | Where a fleet's policy is 'driver pays', the platform collects the no-show fee from the driver on a payment-provider-hosted page opened from a message link, with no account. | SRC-C1@00:11:26, SRC-C1@00:11:44, CTX-130, CTX-134 | V | Q-002: driver-pays option |
| REQ-300 | U-F | Before a driver's first booking under a 'driver pays' policy, the driver sees the fee and grace rule in their language and accepts them. | SRC-C1@00:11:44, SRC-C1@00:11:59, CTX-130 | V | Q-002: driver-pays option |
| REQ-301 | U-F | When a fee a driver already paid is reversed, the driver is refunded to the original payment method and told in their language. | SRC-C2@00:47:59, CTX-127 | V | Q-002: driver-pays option |
| REQ-302 | U-F | Under a 'fleet pays and deducts' policy, the fleet invoice shows each no-show fee with the driver it relates to. | SRC-C1@00:11:26, CTX-134 | V | Q-002: fleet-pays-and-deducts option |
| REQ-303 | S-F | No-show fees are passed through to the station operator, and reversing a fee reverses the station operator's share in the same ledger transaction. | SRC-C1@00:19:54, CTX-121 | V | Q-001, Q-002: option B pass-through |
| REQ-304 | U-F | Whether a no-show fee still applies after a late driver accepts the re-offer is a setting per fleet. | SRC-C2@00:30:11, CTX-133 | V | Q-003: fee after rebook undecided |

### Parking lot · grace extension options (CF-021)

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-305 | U-F | A 'running late' report either releases the stall to walk-ups at once or extends the hold up to the site's maximum, per the site's grace policy. | SRC-C1@00:12:26, SRC-C2@00:38:05, CTX-135 | V | CF-021 option (c), not in the baseline under A-020; Q-004 |
| REQ-306 | S-F | A driver whose vehicle is seen approaching the site is not marked a no-show when grace ends. | SRC-C2@00:38:05, CTX-101 | V | CF-021 option (d), not in the baseline under A-020; Q-014, Q-016 |
| REQ-307 | S-F | Grace is extended automatically while the vehicle is within a set distance of the site, up to the site's maximum. | SRC-C2@00:38:05, CTX-101 | V | CF-021 option (d), not in the baseline under A-020 |

### Parking lot · integration scope options (Q-036, CF-025, CF-004, Q-010, A-026, A-029)

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-308 | S-F | The platform integrates with the ChargePoint CSMS. | SRC-D1#10, CTX-142 | V | Q-036, CF-025: beyond the NYC launch sites (A-022) |
| REQ-309 | S-F | The platform integrates with the EVgo CSMS. | SRC-D1#10, CTX-142 | V | Q-036, CF-025: beyond the NYC launch sites (A-022) |
| REQ-310 | S-F | The platform integrates with the Electrify America CSMS. | SRC-D1#10, CTX-142 | V | Q-036, CF-025: beyond the NYC launch sites (A-022) |
| REQ-311 | S-F | The platform reads SoC for Tesla vehicles through the Tesla Fleet API, metered per fleet and only for vehicles with an upcoming booking. | SRC-D1#9, SRC-D1#10, SRC-C2@00:38:50, SRC-C2@00:40:39, CTX-099, CTX-144 | V | CF-004, Q-015: cost option |
| REQ-312 | U-F | The platform reads SoC, charging state and location through Smartcar for vehicles without another telematics source. | SRC-C2@00:39:34, SRC-C2@00:39:53 | V | CF-004, Q-015: cost option |
| REQ-313 | U-F | Hosts without a CSMS connect their chargers over OCPP to a CitrineOS back-end that Amperlane operates. | SRC-C2@00:21:55, SRC-C2@00:22:42, SRC-C2@00:23:04, SRC-C2@00:23:13, CTX-105 | V | Q-010: operator role undecided; A-021 |
| REQ-314 | U-F | Stripe Billing history and Twilio message logs are migrated with the pilot history. | SRC-D2#18, SRC-R1#open | V | A-026: priced separately; Q-020 |
| REQ-315 | U-NF | The workflow engine runs on Temporal Cloud instead of self-hosted. | SRC-C2@00:33:32, SRC-C2@00:34:04, CTX-094 | V | A-029, Q-026: priced as an option |

### Parking lot · operations, SOC 2 date and budget options (Q-023, Q-018, Q-025)

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-316 | U-F | An exception that needs ops while no ops person is signed in reaches an on-duty contact by SMS or call, and escalates to a second contact if nobody picks it up within a set time. | SRC-C1@00:07:40, SRC-C2@00:24:04, SRC-C2@00:53:49, CTX-045 | V | Q-023: ops hours undecided; A-019, A-028 |
| REQ-317 | U-NF | During the March 2027 hypercare, a production incident that affects booking is acknowledged within a set time inside the 05:00–01:00 window. | SRC-D2#15, CTX-083 | V | Q-025: budget coverage; Q-039 |
| REQ-318 | S-NF | The platform is ready for a SOC 2 Type I audit by the date Amperlane sets: 12 months from the rideshare pilot start, or earlier for the Series A. | SRC-C2@00:43:30, SRC-C2@00:43:54, CTX-078 | V | Q-018, CF-016: SOC 2 date undecided |
| REQ-319 | S-NF | An external penetration test is completed, and its critical and high findings are fixed, before the SOC 2 Type I audit. | SRC-C2@00:43:30, CTX-078 | V | Q-018, CF-016: follows the SOC 2 date |
| REQ-320 | U-NF | The platform exports SOC 2 evidence on demand: user and role lists, change records, restore-test results, incident records and scan results. | SRC-C2@00:44:04, CTX-107 | V | Q-018: follows the SOC 2 date |

### Parking lot · deferred by the client

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-321 | S-F | Drivers use a native iOS and Android app ('Driver App, Native iOS / Android'). | SRC-D1#9, SRC-D1#11, SRC-C1@00:06:33, SRC-C2@00:51:22, CTX-096 | V | CF-001: deferred, no native app in the MVP |
| REQ-322 | S-F | The platform receives trip and vehicle data from the Uber and Lyft driver apps to offer a slot when a trip ends near a site. | SRC-D1#10, SRC-C2@00:42:23, SRC-C2@00:43:30, CTX-098 | V | CF-005: deferred, deep links only in the MVP |
| REQ-323 | S-F | Every charger holds the booked slot through a real-time OCPP reservation ('Real-time reservation on every charger'). | SRC-D1#9, SRC-D1#5, SRC-C2@00:08:48, CTX-088 | V | CF-002: charger reservations only where supported, shortly before the slot |
| REQ-324 | S-F | The platform launches in Los Angeles in Q3 2027. | SRC-C1@00:31:33, SRC-C1@00:30:26, CTX-081 | V | Q-008: deferred, LA is out of the MVP ('LA can't count by June') |
| REQ-325 | S-F | LA sites connect over OCPI 2.2.1 rather than through per-operator integrations. | SRC-C2@00:25:17, CTX-071 | V | Q-008, A-015: deferred with LA |
| REQ-326 | S-F | The platform operates in 10 US metros by the end of 2027. | SRC-D1#11, SRC-C1@00:32:08, CTX-081 | V | CF-007: deferred, 'Ten metros is 2028' |
| REQ-327 | S-F | Ops can enable an overbooking policy for one site and one off-peak window once that site's station operator agrees. | SRC-C2@00:29:35, SRC-C2@00:29:41, CTX-132 | V | Q-006: deferred, 'later' |
| REQ-328 | U-F | The platform exchanges bookings with CPOs through the OCPI 2.3 Booking module. | SRC-C2@00:13:01, SRC-C2@00:13:32, SRC-D2#14, CTX-022 | V | deferred: 'maps onto 2.3 Booking later' (SRC-C2@00:13:32) |

### Parking lot · out of MVP scope (Intellias proposal)

| REQ | Q | Requirement | Sources | KYIV | Q/A |
|---|---|---|---|---|---|
| REQ-329 | U-F | Charging prices vary by time of use, based on utility tariff data from OpenEI URDB. | SRC-D2#10, SRC-D2#14, CTX-014 | V | out of MVP per SRC-D2#14 (Phase 2 or later) |
| REQ-330 | U-F | The platform takes part in OpenADR 3.0 demand response. | SRC-D2#14 | V | out of MVP per SRC-D2#14 |
| REQ-331 | U-F | The platform supports bookings for autonomous-vehicle fleets and depots. | SRC-D2#14, SRC-D2#15, CTX-016 | V | out of MVP per SRC-D2#14 (Phase 3) |

## KYIV suggestions for Gate 2

Proposal for the human decision at Gate 2 (prompt P5.1, constitution P1 and P4); nothing here sets a value. One row
per baseline requirement; parking-lot rows are V and not repeated. Each reason cites a date, the budget, a regulation,
a contract term, a success metric or a client deferral.

Sizing frame: fixed NYC production launch on 2027-03-01 with the three pilot sites and both pilot fleets (CTX-079),
a phase-one envelope of $0.9–1.2M through Q2 2027 whose coverage is open (CTX-080, Q-025), and K at most 80% of the
committed capacity (constitution P6, A-045). K is what the launch needs to run real bookings at all three supply
patterns without spreadsheets, collect fleet money, and stay SOC 2-ready and SHIELD-compliant. Many K rows are rules
or fields inside one feature (e.g. connector matching, capacity rules), not separate features. Y is planned last; I
is outside the committed plan. If the Gate 5 estimate puts K above 80%, the first K rows to reconsider are the
attendant view (REQ-158, REQ-192, if Q-049 shows the attendant has no device; ops phone calls remain the fallback),
the SMS text-code booking path (REQ-061, if the PWA link proves enough) and change-without-deployment for per-site
parameters (REQ-146); the date does not move (CTX-079).

| Requirement | Suggested | Reason |
|---|---|---|
| REQ-001 | K | Core promise 'see open slots, book in two taps' (CTX-002); no launch on 2027-03-01 without it (CTX-079). |
| REQ-002 | K | Booking is the product (CTX-002); launch date 2027-03-01 (CTX-079). |
| REQ-003 | K | Agreed booking model (CTX-092); every supply pattern depends on it (CTX-063). |
| REQ-004 | K | Stations' condition for joining (CTX-064); capacity commitment is a partner-agreement term (CTX-069). |
| REQ-005 | K | Every launch site has peak caps of 30–50% (CTX-064). |
| REQ-006 | I | None of the three launch sites is NEVI-funded; prospects are mostly outside NYC (CTX-017); the limit is undefined (Q-040). |
| REQ-007 | K | 'No double booking, ever' (CTX-093); a broken promise to drivers and stations. |
| REQ-008 | Y | Agreed burst behaviour (CTX-093); booking still works without it. |
| REQ-009 | K | Cab day drivers book for night drivers (CTX-029); Five Boroughs is a launch fleet (CTX-139). |
| REQ-010 | Y | Long-term cab drivers do this today (CTX-029); depends on overnight bookings (A-028, CF-015). |
| REQ-011 | Y | Brief step 2 (SRC-D1#6); at launch drivers book themselves and ops books for small fleets (CTX-030). |
| REQ-012 | K | Connector and power matching need it (CTX-100). |
| REQ-013 | K | Connector mismatches happen in the pilot (CTX-049); a mismatch is a failed charge. |
| REQ-014 | K | Prerequisite for connector matching (CTX-100). |
| REQ-015 | K | Prerequisite for connector matching (CTX-100). |
| REQ-016 | Y | CTO asked for it ('Put it in', CTX-100); bookings work without it. |
| REQ-017 | I | Needs SoC, and Geotab access is unconfirmed (Q-014); drivers can choose a duration without it. |
| REQ-018 | Y | Agreed MVP vehicle-data cut 'Geotab plus manual SoC' (CTX-099). |
| REQ-019 | K | Five Boroughs has no telematics and is a launch fleet (CTX-074, CTX-139). |
| REQ-020 | K | Station red line ('Never', CTX-066). |
| REQ-021 | K | Overstays are some days worse than no-shows (CTX-050); 'stall is held for you' (SRC-D1#5). |
| REQ-022 | K | Stated fallback 'ops gets pinged' (CTX-066); happens at JFK, a launch site. |
| REQ-023 | K | Agreed foundation (CTX-088, CF-002). |
| REQ-024 | K | Pattern A at Gowanus, a launch site (CTX-060). |
| REQ-025 | K | Six Gowanus chargers reject reservations until their firmware is fixed (CTX-060, CTX-072). |
| REQ-026 | K | JFK and LIC are launch sites without charger reservations (CTX-061, CTX-062). |
| REQ-027 | K | JFK is a launch site; 'Kinship stops calling me about cones' (CTX-139). |
| REQ-028 | K | All three patterns are launch sites (CTX-063). Gate 2: set to Y (provisional). |
| REQ-029 | Y | Agreed scope limit (CTX-090); stops an undeliverable 'all chargers live' promise. |
| REQ-030 | I | Convenience for drivers far from partner sites; not needed for the launch goal (CTX-079). |
| REQ-031 | K | Gowanus is a launch site (CTX-079, A-022). |
| REQ-332 | K | Split from REQ-031 (P2.4). Settlement and the completed-booking evidence need session records (CTX-127); depends on Q-009. Gate 2: set to Y (provisional). |
| REQ-032 | K | JFK is a launch site (CTX-079, A-022). |
| REQ-333 | I | Split from REQ-032 (P2.4). Serves only the price display (REQ-163, suggested I). |
| REQ-033 | K | 'Has to. Automatically.' (CTX-131); stations' first condition (CTX-067). |
| REQ-034 | K | Station term from the partner agreement (CTX-067, CTX-069). |
| REQ-035 | K | 'Cone comes off, walk-up gets it' (CTX-067); 'Kinship stops calling me about cones' (CTX-139). |
| REQ-036 | K | Stations require it (CTX-067); the payer is open (Q-002) but the line exists in every option. |
| REQ-037 | K | Station view of late arrivals (CTX-133); feeds the north-star metric (CTX-138). Gate 2: set to Y (provisional). |
| REQ-038 | Y | Many late drivers still charge today (CTX-133); every completion counts toward 10k (CTX-138). |
| REQ-039 | K | Main lever against 17% no-shows, which block the 10k target (CTX-135, CTX-138). |
| REQ-040 | Y | Agreed one-tap signal (CTX-135), but under A-020 it changes nothing automatically; cancel is the K lever. |
| REQ-041 | Y | Exists in the pilot (CTX-041); one-tap cancel is the main path. |
| REQ-042 | Y | CEO accepted overrides (CTX-035); auto-release works without it. |
| REQ-043 | K | Default arrival evidence while location is off by default (A-024); prevents wrongful auto-release. |
| REQ-044 | K | QR arrival is needed at all three launch sites (CTX-102). |
| REQ-045 | Y | Disputes start 'the moment we charge no-show fees' (CTX-035); who pays is still open (Q-002). |
| REQ-046 | Y | Liability for blocked stalls is a station's first question (CTX-068). |
| REQ-336 | Y | Added by CR-008 (2026-10-28): the COO's "move the booking to another free one" (SRC-C2@00:24:04); set to Y at the CR. |
| REQ-047 | K | The Gowanus fault went unnoticed for 25 minutes (CTX-047); launch success 'nobody picks up the phone' (CTX-139). |
| REQ-048 | K | A charger-down day costs two ops people an afternoon (CTX-047); launch success (CTX-139). Gate 2: set to Y (provisional). |
| REQ-049 | K | A cab driver was lost in the Gowanus fault (CTX-047). Gate 2: set to Y (provisional). |
| REQ-050 | K | Ops is the safety net for unplaced bookings (CTX-035). |
| REQ-051 | Y | The station was angry nobody told them (CTX-047); 'Kinship stops calling me' (CTX-139). |
| REQ-052 | K | False no-shows distort the north-star metric and fees (CTX-138, CF-018). |
| REQ-053 | K | Basis for disputes, SOC 2 and SHIELD evidence (CTX-110). |
| REQ-054 | Y | Automatic rebooking is K (CTX-136); the one-action manual path is the fallback. |
| REQ-055 | K | Small fleets and phone-in drivers depend on ops (CTX-030, CTX-035). |
| REQ-056 | Y | Accepted override (CTX-035); bookings confirm without it. |
| REQ-057 | Y | Accepted override (CTX-035); auto-release covers the normal case. |
| REQ-058 | K | Launch success 'Nobody opens Airtable' (CTX-139); no spreadsheets in the critical path (CTX-079). |
| REQ-059 | K | Agreed channel (CF-001); drivers refuse app installs (CTX-027). |
| REQ-060 | K | Otherwise 'he's gone' (CTX-027). |
| REQ-061 | K | Drivers book by text today ('He'll text', CTX-027). Gate 2: set to Y (provisional). |
| REQ-062 | Y | Half the drivers asked for it (CTX-027); not used in the pilot, sender set-up unknown (Q-034). |
| REQ-063 | K | 'He'll tap a link' (CTX-027); one-tap cancel depends on it (CTX-135). |
| REQ-064 | Y | Brief names directions (SRC-D1#9); deep links agreed (CTX-098). |
| REQ-065 | I | Brief lists ETA (SRC-D1#9) with no stated use; booking works without it. |
| REQ-066 | Y | Agreed deep-link scope (CTX-098). |
| REQ-067 | K | Brief step 3 (CTX-002); fewer no-shows means more completions (CTX-138). |
| REQ-069 | K | Fleet portal is in the client's scope (CTX-004). |
| REQ-070 | K | Connector matching needs vehicle profiles (CTX-100). Gate 2: set to Y (provisional). |
| REQ-071 | Y | Brief 'reporting for every EV in the fleet' (SRC-D1#8); content not specified. |
| REQ-072 | Y | Per-vehicle adapter settings make matching work at launch; the fleet-level default saves data entry. |
| REQ-073 | Y | Borough Green sees no-shows only because Amperlane shows them (CTX-140). |
| REQ-074 | Y | Five Boroughs' definition of success (CTX-140). |
| REQ-075 | I | Agreed MVP telematics (CTX-099) but access is unconfirmed (Q-014); manual SoC covers the gap. |
| REQ-076 | Y | Brief 'schedules' (SRC-D1#11); ops can set them at launch. |
| REQ-077 | Y | Stations want it (CTX-065), but ops can change caps on request at launch. |
| REQ-078 | I | How tariffs are used depends on the undecided model (Q-001). |
| REQ-079 | Y | Station-hold requests already tell JFK and LIC staff what is due; full view can follow (CTX-047). |
| REQ-080 | Y | Leverage with the stations' maintenance teams (CTX-037). |
| REQ-081 | K | LIC is a launch site whose only live feed is the attendant (CTX-062). |
| REQ-082 | Y | Walk-up capacity is the station's condition (CTX-064). |
| REQ-083 | K | Launch success 'one invoice' (CTX-139); fleet invoicing exists in every model (CF-008). |
| REQ-084 | K | 'Billing happens automatically' (CTX-002); no spreadsheets in the critical path (CTX-079). |
| REQ-085 | K | CTO requirement (CTX-095); money correctness. |
| REQ-086 | K | Fleet receivables exist in every model (CTX-129). Gate 2: set to Y (provisional). |
| REQ-087 | K | Fleets pay through Stripe today (CTX-051). |
| REQ-088 | K | Pilot behaviour drivers rely on (CTX-043). |
| REQ-089 | K | Known pilot defect, twice a week (CTX-044). |
| REQ-090 | K | Cause of duplicate confirmations (CTX-044); constitution N8. |
| REQ-091 | Y | Series A metric (CTX-138); computed from K evidence, and the June figure is reported after launch. |
| REQ-092 | Y | No-shows cut completions (CTX-138); reports can follow launch. |
| REQ-093 | I | Pilot headline was self-reported (CTX-040); needs session-start data that is unconfirmed (Q-009, Q-012). |
| REQ-094 | I | Sells 'we fill your quiet hours' (CTX-119); needs walk-up session data. |
| REQ-095 | Y | Series A is in H2 2027 (CTX-003), after launch. |
| REQ-096 | K | Only real behaviour dataset, needed for the data room (CTX-053). Gate 2: set to Y (provisional). |
| REQ-097 | K | Launch definition 'real stations, real fleets' (CTX-079). |
| REQ-100 | K | Brief promise 'book in two taps' (CTX-002); constitution N23. |
| REQ-101 | K | CTO: 'let Postgres say no' (CTX-093); constitution N7. |
| REQ-102 | Y | Agreed for fairness, not correctness (CTX-093). |
| REQ-103 | K | CTO: 'I'd have fired someone for not doing that' (CTX-093); constitution N8. |
| REQ-104 | K | Agreed NFR and proposal acceptance criterion (CTX-112, SRC-D2#13). |
| REQ-105 | K | CTO's lock-in condition (CTX-086). Gate 2: set to Y (provisional). |
| REQ-106 | K | Duplicates already seen (CTX-091); constitution N9. |
| REQ-107 | K | 'Never the only path' (CTX-091); keeps the 60-second target (CTX-112). |
| REQ-108 | I | Roadmap item; US adoption likely low (CTX-022). |
| REQ-109 | Y | CTO flinches at 'reconcile it later' (SRC-C2@00:01:07). |
| REQ-110 | Y | 'Same as payment webhooks. Never the only path.' (CTX-091). |
| REQ-111 | Y | CTO's lock-in point (SRC-C2@00:47:25). |
| REQ-112 | K | Many drivers prefer Spanish or Bengali (CTX-028); constitution N22. |
| REQ-113 | K | The CEO's first launch-success sentence (CTX-139). Gate 2: set to Y (provisional). |
| REQ-114 | Y | COO's launch-success sentence (CTX-139); depends on site staff behaviour. |
| REQ-115 | K | 'Properly — not a CSV dump' (CTX-053). Gate 2: set to Y (provisional). |
| REQ-116 | K | 'I don't want to lose a year of bookings' (SRC-C1@00:48:20). Gate 2: set to Y (provisional). |
| REQ-117 | Y | CTO would bin it (CTX-052); a constraint, not work. |
| REQ-118 | Y | CTO's practice for exports (SRC-C1@00:44:59). |
| REQ-119 | K | Contractual IP condition (CTX-005). |
| REQ-120 | K | SOC 2-ready from day one (CTX-107); rideshare pilot asks for it (CTX-078). |
| REQ-121 | K | SOC 2-ready from day one (CTX-107). Gate 2: set to Y (provisional). |
| REQ-122 | K | SOC 2-ready from day one (CTX-107). Gate 2: set to Y (provisional). |
| REQ-123 | K | SOC 2 and SHIELD safeguards (CTX-107, CTX-108). |
| REQ-124 | K | SOC 2-ready from day one (CTX-107). |
| REQ-125 | Y | Retention periods are not yet set by counsel (Q-022); purge jobs can follow launch inside the periods. |
| REQ-126 | K | Disputes, SHIELD and SOC 2 (CTX-110); constitution N17. |
| REQ-127 | Y | CTO's rule (CTX-085); checked per dependency. |
| REQ-128 | K | Agreed NFR and acceptance criterion (CTX-114); constitution N4. |
| REQ-129 | K | Agreed NFR (CTX-114); constitution N5. |
| REQ-130 | K | Agreed NFR (CTX-113); constitution N3. |
| REQ-131 | K | Agreed 5× test (CTX-115); the 4–5 PM wave is the launch risk (CTX-075). |
| REQ-132 | K | Series A milestone (CTX-138); constitution N12. |
| REQ-133 | K | Auto-release 'has to' happen (CTX-131); constitution N5, N10. |
| REQ-134 | Y | CTO: no extra vendor contract in year one (CTX-094); hosting cost is in the proposal. |
| REQ-135 | K | Two Amperlane engineers run it after handover (CTX-007, CTX-087). |
| REQ-136 | K | CTO's stack condition (CTX-085). |
| REQ-137 | Y | Budget envelope (CTX-080). |
| REQ-138 | Y | LA follows in Q3 2027 (CTX-081); designed for, not built. |
| REQ-139 | Y | Brief 'API-first' (SRC-D1#9). |
| REQ-140 | Y | Engineer's ask (CTX-103); de-risks fault handling before 2027-03-01. |
| REQ-141 | Y | Agreed regression case (CTX-103); proves launch success #1 (CTX-139). |
| REQ-142 | K | The date that matters (CTX-079). |
| REQ-143 | Y | Agreed delivery model (CTX-006); a way of working, not build scope. |
| REQ-144 | Y | CTO's ask (CTX-006). |
| REQ-145 | K | Two-tap booking at the burst needs it (CTX-002, CTX-115). |
| REQ-146 | K | Values come from partner agreements still being negotiated (CTX-069). Gate 2: set to Y (provisional). |
| REQ-147 | K | Closes the pool-to-EVSE gap behind 'no double booking' (CF-023). |
| REQ-148 | Y | A driver sent elsewhere was lost (SRC-C2@00:52:32); happens at JFK (CTX-066). |
| REQ-149 | Y | Keeps site failures out of no-show figures (CTX-036). |
| REQ-150 | K | 'The station gets the stall back early' (CTX-135). |
| REQ-151 | Y | NYC only at launch (CTX-079); first DST change after launch falls in March 2027. |
| REQ-152 | Y | Cab drivers book overnight slots (CTX-029); overnight demand is mostly walk-up (CTX-114). |
| REQ-153 | K | A stale reservation blocks walk-ups at Gowanus (CTX-066). |
| REQ-154 | Y | 'The hold sent' is dispute evidence (CTX-127). |
| REQ-155 | K | Reservations are optional and 6 of 16 Gowanus chargers reject them (CTX-060). |
| REQ-156 | Y | At 4 PM 'sometimes the cone doesn't happen' (CTX-061). |
| REQ-158 | K | Only live status source at LIC, a launch site (CTX-062). |
| REQ-159 | Y | Replaces the ops call to the attendant (CTX-043). |
| REQ-160 | K | Agreed with the freshness NFR (CTX-112); constitution N2. Gate 2: set to Y (provisional). |
| REQ-161 | Y | Unit of truth for settlement and disputes (CTX-127); record availability is unconfirmed. |
| REQ-162 | Y | Only session data at LIC (CTX-062). |
| REQ-163 | I | Useful while drivers pay stations directly (CTX-051); not asked for. |
| REQ-164 | Y | 'Station status at the time' is dispute evidence (CTX-127). |
| REQ-165 | Y | Three or four new sites by June 2027 (CTX-070); launch sites can be set up by the team. |
| REQ-166 | I | No NYC launch site uses OCPI (CTX-090); LA is out of the MVP (CTX-081); scope deferred to Gate 2 (A-015). |
| REQ-167 | Y | Keeps Gowanus bookable during vendor outages (CTX-091). |
| REQ-168 | Y | JFK fills up and status is its only live signal (CTX-066). |
| REQ-169 | Y | Silent failures went unnoticed in the pilot (CTX-047). |
| REQ-170 | Y | Ops is the safety net for patterns B and C (SRC-C2@00:53:49). |
| REQ-171 | Y | Makes one-tap cancel worth using (CTX-135); cut-off is a station term (Q-042). |
| REQ-334 | Y | Split from REQ-171 (P2.4). Makes one-tap cancel worth using (CTX-135); cut-off is a station term (Q-042). |
| REQ-172 | Y | 'What the driver sees' is part of Q-002 (SRC-C1@00:47:44). |
| REQ-173 | I | Opt-in is off by default (A-024); QR covers arrival. |
| REQ-174 | Y | Automatic arrival evidence at connected sites (CTX-102). |
| REQ-175 | I | Geotab access unconfirmed (Q-014); opt-in off by default (A-024). |
| REQ-176 | Y | Arrival evidence at LIC, which has no API (CTX-062). |
| REQ-177 | K | A wrongful release takes a stall from a driver who arrived (CTX-131). |
| REQ-178 | I | Not asked for by the client; session data unconfirmed. |
| REQ-179 | Y | Disputes expected daily once fees start (CTX-035). |
| REQ-180 | K | Fees for platform or site failures would create disputes and anger fleets (CTX-035, CTX-077). |
| REQ-181 | Y | Engineer's case 'driver showed up, charger didn't start' (SRC-C2@00:47:53). |
| REQ-182 | Y | Accepted ops overrides (CTX-035). |
| REQ-183 | Y | No-show terms come from each partner agreement (CTX-069); amounts are open (Q-002). |
| REQ-184 | Y | Proposed by Intellias on Call 2 (SRC-C2@00:53:00); maintenance can also be handled as a fault. |
| REQ-335 | Y | Split from REQ-184 (P2.4). Proposed by Intellias on Call 2 (SRC-C2@00:53:00); maintenance can also be handled as a fault. |
| REQ-185 | Y | Keeps maintenance out of no-show figures (CTX-036). |
| REQ-186 | Y | Stations lower caps on event days (CTX-065); nothing dropped silently. |
| REQ-187 | Y | Ops control over automation (CF-022). |
| REQ-188 | Y | Vendor addition (CF-022); ops can also rebook one by one. |
| REQ-189 | K | Ops is the safety net for patterns B and C (SRC-C2@00:53:49); 'nobody opens Airtable' (CTX-139). |
| REQ-190 | Y | Replaces the slot-grid sheet ops keep open (CTX-042). |
| REQ-191 | Y | Drivers are today's fault detectors (CTX-048); only signal at LIC besides the attendant. |
| REQ-192 | K | LIC is a launch site with no API (CTX-062). Gate 2: set to Y (provisional). |
| REQ-193 | I | Not asked for; stations email faults today (CTX-048). |
| REQ-194 | Y | A flapping EVSE would re-expose drivers (CTX-047). |
| REQ-195 | Y | Dozens of driver calls a day (CTX-045). |
| REQ-196 | I | Helpful for support; not asked for. |
| REQ-197 | Y | Ops text drivers when rebooking by hand (CTX-047). |
| REQ-198 | K | No accounts for drivers (CTX-027); booking needs an identity. Gate 2: set to Y (provisional). |
| REQ-199 | K | EN/ES/BN is a stated NFR (CTX-097). |
| REQ-200 | K | Pool booking means the driver learns the EVSE late (CTX-092); pilot confirmations name the stall (SRC-C1@00:05:34). |
| REQ-201 | Y | Owners book for the other shift's driver (CTX-029). |
| REQ-202 | K | Weekly leases change hands (CTX-026); access control. |
| REQ-203 | Y | Drivers will not install or register (CTX-027). |
| REQ-204 | K | Location is opt-in and off by default (A-024). |
| REQ-205 | K | Bookings need registered drivers and vehicles (A-023). Gate 2: set to Y (provisional). |
| REQ-206 | K | Five Boroughs will not use a portal (CTX-030) and is a launch fleet. |
| REQ-207 | Y | Borough Green has about 420 EVs (CTX-073). |
| REQ-208 | I | Nice to have against invoice surprises (CTX-139 #4). |
| REQ-209 | I | Sales argument (CTX-119); value depends on the model (Q-001). |
| REQ-210 | K | Settlement must start before the model is decided (CF-008, CTX-129). |
| REQ-211 | K | Holds in every fee option; constitution N19. |
| REQ-212 | K | Holds in every fee option; disputes expected daily (CTX-035). |
| REQ-213 | Y | 'Borough Green … doesn't email me about it' (CTX-139). |
| REQ-214 | Y | Session data is unconfirmed at all three sites (Q-009, Q-011, Q-012). |
| REQ-215 | Y | Finance actor accepted at Gate 1, client to confirm (Q-037). |
| REQ-216 | Y | Fleet receivables exist in every model (CTX-129). |
| REQ-217 | Y | One invoice without emails (CTX-139). |
| REQ-218 | Y | LIC session data arrives by hand, possibly late (CTX-062). |
| REQ-219 | Y | A missed reminder or re-offer becomes a no-show (CTX-041). |
| REQ-220 | Y | Drivers act while driving (CTX-041); fallback when the link cannot open. |
| REQ-221 | I | Helpful; ops number is known to pilot drivers. |
| REQ-222 | Y | Today a bilingual ops person reads every text (CTX-045). |
| REQ-223 | I | Outages are rare within the 99.9% target (CTX-114). |
| REQ-224 | K | Billing unit and Series A metric are undecided (Q-017). |
| REQ-225 | Y | Uncleaned pilot figures (CF-018); data room comparability. |
| REQ-226 | I | Operational insight; the monthly metrics are covered elsewhere. |
| REQ-227 | I | Measures launch success #1 (CTX-139); can follow launch. |
| REQ-228 | Y | Data-room figures depend on it (CF-018); raw history is migrated either way. |
| REQ-229 | Y | The sources disagree (CTX-054). |
| REQ-230 | Y | 'From about February it's decent' (CTX-054). |
| REQ-231 | K | No spreadsheets in the critical path from 2027-03-01 (CTX-079). |
| REQ-232 | K | Fleet invoicing continues through the launch month (CTX-051). |
| REQ-233 | Y | 'Delete the rest' meets an append-only ledger (CTX-095, CTX-108). |
| REQ-234 | I | No partner is leaving; can follow launch. |
| REQ-235 | I | Small fleets forget passwords (CTX-030); ops can act for them. |
| REQ-236 | K | The double tap on bad 4G hits cancel as much as booking (CTX-093); constitution N8. |
| REQ-237 | Y | Sandbox access requested from Kinship (CTX-072). |
| REQ-238 | I | Needed only if the discovery map is built. |
| REQ-239 | K | A half-done rebooking repeats the Gowanus afternoon (CTX-047). Gate 2: set to Y (provisional). |
| REQ-240 | K | No-account access must still be secure (CTX-107). |
| REQ-241 | Y | Links can be forwarded between shift drivers (CTX-029); A-006 left this to Step 2. |
| REQ-242 | K | Text commands change bookings and fees (CTX-043). |
| REQ-243 | Y | Five Boroughs barely uses a portal (CTX-030); covered by messaging and ops requirements. |
| REQ-244 | K | Money correctness; the CTO has payout 'scars' (SRC-C2@00:01:07). |
| REQ-245 | Y | Payment is not in the booking path today (CTX-051). |
| REQ-246 | Y | Keeps PCI scope minimal; fleets pay through Stripe today (CTX-051). |
| REQ-247 | K | Money audit trail (CTX-095, CTX-110); constitution N19. |
| REQ-248 | K | US carrier rules for application-to-person messaging; messaging is the driver channel (CTX-097). |
| REQ-249 | Y | WhatsApp Business rules; WhatsApp is a Y channel. |
| REQ-250 | Y | Counsel approves wording (A-024); the driver must understand it (CTX-028). |
| REQ-251 | I | Cost control within the budget (CTX-080); can follow launch. |
| REQ-252 | Y | It holds driver names and phone numbers (SRC-C1@00:44:59). |
| REQ-253 | K | State law (CTX-108); constitution N18. |
| REQ-254 | K | State law (CTX-108). |
| REQ-255 | K | Drivers are independent contractors; location is sensitive (CTX-108, CTX-109). |
| REQ-256 | Y | Minimisation (CTX-108); location is opt-in, so volume is low. |
| REQ-257 | Y | Needed once telematics is used (CTX-109). |
| REQ-258 | K | Multi-party data on one platform (CTX-107); SHIELD (CTX-108). |
| REQ-259 | Y | Location is sensitive (CTX-108). |
| REQ-260 | Y | Webhooks change bookings and EVSE status (CTX-091). |
| REQ-262 | Y | Disputes about caps and terms (CTX-065). |
| REQ-263 | Y | SHIELD and SOC 2 evidence (CTX-108). |
| REQ-264 | I | SOC 2 vendor management; a document, timing follows Q-018. |
| REQ-265 | Y | Keeps SHIELD-covered data out of scope (CTX-108). |
| REQ-266 | Y | No spreadsheet fallback once 'nobody opens Airtable' (CTX-139). |
| REQ-267 | Y | 'The IP has to be ours' (CTX-005). |
| REQ-268 | Y | Two engineers run the platform after handover (CTX-007). |
| REQ-269 | K | Plan 'including time to test with real drivers' (CTX-082); fixed date (CTX-079). Gate 2: set to Y (provisional). |
