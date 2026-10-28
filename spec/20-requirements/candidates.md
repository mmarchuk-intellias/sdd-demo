---
id: REQ-CANDIDATES
type: working-notes
title: Requirement candidates and their closing-pass results (P2.3)
status: approved
owner: Mykola Marchuk
version: 1
kyiv: null
parents: [REQUIREMENTS]
sources: [SRC-D1, SRC-C1, SRC-C2, SRC-D2, SRC-R1]
---
# Candidates and closing-pass results

After the closing pass, the P2.4 critique (2026-10-28) deprecated REQ-068, REQ-098, REQ-099, REQ-157 and REQ-261
and split REQ-031, REQ-032, REQ-171 and REQ-184, adding REQ-332 – REQ-335; see requirements.md. The results below
are as of the closing pass.

Step 2, closing pass (prompt P2.3), 2026-10-28. Working notes behind [requirements.md](requirements.md); not a
requirements artefact.

- **Ids.** CAND-A-### from the exhaustive pass (P2.1) is renamed P21-###, and CAND-B-### from the unstated pass
  (P2.2) is renamed P22-###; the numbers are kept. The old prefix ended in an assumption-like id that trace.py would
  read as a reference.
- **Q** is the quadrant the pass gave the candidate. The requirement's own quadrant was re-checked against the
  speaker in the transcript; changes are listed just above the table.
- **Result:** `REQ-###` (the requirement written from this candidate); `merged into REQ-###`; `parked REQ-###`
  (parking lot, V); `converted to Q-### / A-###`; `design detail → Step 3` (a parameter or mechanism for a system
  story, e.g. a timeout, a retry count, a page weight); `covered by constitution N#`; `dropped: <reason>`.
- Numbers that P2.2 proposed as NEW-A (timeouts, thresholds, WCAG 2.1, a 3G profile, RPO/RTO, MFA scope) are not
  carried into requirements. Where they conflict with the constitution's assumptions (A-036, A-038, A-040, A-043),
  the constitution wins and the candidate is "covered by constitution N#".

Quadrant changed in the closing pass (first candidate of a REQ only; merged candidates take the REQ's quadrant): P21-023 S-F → S-NF (REQ-103); P21-282 S-F → S-NF (REQ-116); P21-090 U-NF → U-F (REQ-165); P21-144 S-F → U-F (REQ-184); P21-237 U-NF → U-F (REQ-210); P21-195 S-NF → U-NF (REQ-243); P21-289 U-F → U-NF (REQ-252); P21-156 U-NF → U-F (REQ-316).

| Candidate | Q | Candidate (short, ≤ 100 chars) | Result |
|---|---|---|---|
| P21-001 | S-F | The platform shows drivers and fleet users the open bookable slots at each partner site, by site… | REQ-001 |
| P21-002 | S-NF | A driver can confirm a booking with no more than two taps after opening the slot view. | REQ-100 |
| P21-003 | S-F | A booker can create a booking by picking a site and a start time. | REQ-002 |
| P21-004 | S-F | A driver who arrives within the booked slot finds a compatible EVSE at the booked site free to… | merged into REQ-021 |
| P21-005 | S-F | A driver books a specific stall, such as "Stall B", at the moment of booking. | dropped: superseded by pool booking with late allocation (CTX-092, client agreed); the driver learns the EVSE at allocation |
| P21-006 | S-F | A booking takes capacity from the pool of compatible EVSEs at the site, and a specific EVSE is… | REQ-003 |
| P21-007 | U-F | The time before slot start at which the EVSE is allocated is configurable, with a default of 15… | merged into REQ-146 |
| P21-008 | U-F | Picking a slot places a soft hold on one unit of capacity, which expires and returns the capacity… | REQ-145 |
| P21-009 | U-F | The slot calendar uses a configurable time grid with a default step of 15 minutes. | REQ-146 |
| P21-010 | U-F | A booking lasts one of a configurable set of durations, by default 30, 45 or 60 minutes. | merged into REQ-146 |
| P21-011 | U-F | The platform keeps a configurable buffer, by default 10 minutes, between consecutive bookings… | merged into REQ-146 |
| P21-012 | S-F | The number of bookings accepted for a site and time window never exceeds the bookable cap set for… | REQ-004 |
| P21-013 | S-F | A bookable cap can be defined per site and per time window, such as "weekdays 4–7 PM, at most 8… | REQ-005 |
| P21-014 | S-F | The platform does not accept a bookable cap for any time window that equals the site's total… | merged into REQ-082 |
| P21-015 | S-F | Where a site is flagged as NEVI-funded, the platform enforces that site's public-access limit on… | REQ-006 |
| P21-016 | S-F | Overbooking is off by default, so a site and time window never holds more confirmed bookings than… | merged into REQ-004 |
| P21-017 | S-F | Ops can enable an overbooking policy for one site and one off-peak time window once that station… | parked REQ-327 |
| P21-018 | S-F | Two allocations to the same EVSE never overlap in time. | REQ-007 |
| P21-019 | S-NF | The rule that EVSE allocations never overlap is enforced by a database constraint, so it holds… | REQ-101 |
| P21-020 | U-F | A booking is confirmed only if every confirmed booking for that site and slot can still be… | REQ-147 |
| P21-021 | S-NF | During a burst, booking attempts for the same site are processed one at a time in arrival order. | REQ-102 |
| P21-022 | S-F | When a booking attempt fails because the slot is full, the response offers the next free… | REQ-008 |
| P21-023 | S-F | Repeating a booking request with the same idempotency key creates at most one booking and returns… | REQ-103 |
| P21-024 | S-F | A booking records both the person who made it and the driver who will charge, who can be different… | REQ-009 |
| P21-025 | S-F | A booker can book an afternoon slot and an overnight slot for the same vehicle in one interaction. | REQ-010 |
| P21-026 | S-F | A fleet owner can book a slot for a named driver of the fleet. | merged into REQ-011 |
| P21-027 | S-F | A fleet manager can book a slot for one of the fleet's drivers in the fleet portal. | REQ-011 |
| P21-028 | S-F | Every booking names the vehicle to be charged. | REQ-012 |
| P21-029 | S-F | The platform offers a site for booking only when it has at least one EVSE whose connector matches… | REQ-013 |
| P21-030 | S-F | A booking is never allocated to an EVSE whose connector matches neither the vehicle's native… | merged into REQ-013 |
| P21-031 | S-F | Each EVSE connector records its connector type, such as CCS1 or NACS, and its maximum power in kW. | REQ-014 |
| P21-032 | S-F | Each vehicle profile records its native connector, its allowed adapters and its maximum DC… | REQ-015 |
| P21-033 | S-F | At allocation, EVSEs with the highest maximum power at the site (such as 320 kW) go first to… | REQ-016 |
| P21-034 | S-F | When the vehicle's battery level is known, the booking flow suggests a slot length from it (about… | REQ-017 |
| P21-035 | S-F | The suggested slot length takes into account the maximum power of the compatible EVSEs at the… | merged into REQ-017 |
| P21-036 | S-F | The booking flow lets the driver enter the vehicle's current battery level, optionally. | REQ-018 |
| P21-037 | S-F | The platform never asks a walk-up driver who is charging to unplug to make room for a booking. | REQ-020 |
| P21-038 | S-F | When the allocated EVSE is taken at hold time, the platform moves the booking to another free… | REQ-021 |
| P21-039 | S-F | When no compatible EVSE at the site is free for an allocated booking, the platform alerts ops. | REQ-022 |
| P21-040 | U-F | When the station hold fails and the whole site is full, the driver at once receives the next… | REQ-148 |
| P21-041 | U-F | A booking moved because its site was full carries no no-show fee and the reason code "moved — site… | REQ-149 |
| P21-042 | U-F | A booking enters a "station hold failed" state when the charger rejects the hold or reports the… | merged into REQ-021 |
| P21-043 | S-F | When a previous session overruns into a booked slot, the arriving driver gets another free… | merged into REQ-021 |
| P21-044 | U-F | At T-10 the platform checks live status and, if the allocated EVSE is still in a session… | merged into REQ-021 |
| P21-045 | U-F | Cancelling a booking before its slot starts makes its capacity bookable by others as soon as the… | REQ-150 |
| P21-046 | U-F | Slot times are stored as instants and shown in each site's local time zone. | REQ-151 |
| P21-047 | S-F | The platform keeps the authoritative slot calendar for every site, whether or not the site's… | REQ-023 |
| P21-048 | S-F | For an EVSE that supports reservations, the platform sends a charger-side hold for the allocated… | REQ-024 |
| P21-049 | S-F | Each EVSE carries a "supports charger-side reservation" flag that ops can change without a… | REQ-025 |
| P21-050 | U-F | When a booking with a charger-side hold is cancelled, released or moved, the platform cancels the… | REQ-153 |
| P21-051 | U-F | The platform records the charger's response to every hold request (accepted, rejected, expired)… | REQ-154 |
| P21-052 | S-F | For an EVSE without reservation support, the platform keeps a soft hold in its own calendar and… | REQ-026 |
| P21-053 | S-F | At a status-only site (pattern B), the platform asks station staff to put "Reserved" signage on… | REQ-027 |
| P21-054 | U-F | Station staff at a pattern B site confirm in the platform that the signage is in place, and a sign… | REQ-156 |
| P21-055 | U-F | The platform tells on-site staff at every site with a physical hold which stall to mark, when to… | REQ-157 |
| P21-056 | U-F | At LIC, the platform sends the garage attendant the stall and time of each booking to mark… | merged into REQ-157 |
| P21-057 | U-F | The attendant view lets the LIC attendant set each stall to free, occupied or faulted. | REQ-158 |
| P21-058 | U-F | The attendant view shows which driver is due at which stall and at what time. | REQ-159 |
| P21-059 | S-F | One booking engine serves sites of all three supply patterns (API with reservations, status only… | REQ-028 |
| P21-060 | S-NF | No CSMS vendor SDK is used inside the booking core, so moving a site to another CSMS changes only… | REQ-105 |
| P21-061 | S-F | Live EVSE status comes only from CSMS APIs or OCPI 2.2.1 Locations, and every other charger is… | REQ-029 |
| P21-062 | S-NF | Station status for API-connected sites is never older than 60 seconds. | REQ-104 |
| P21-063 | U-F | Every screen that shows station status also shows the age of that status. | REQ-160 |
| P21-064 | U-F | For LIC, the platform shows station status as "last updated by attendant at <time>". | merged into REQ-160 |
| P21-065 | S-NF | Consumers of CSMS webhooks process duplicate and out-of-order deliveries without changing the… | REQ-106 |
| P21-066 | S-NF | A periodic poll reconciles each connected site's EVSE status, so a lost webhook cannot leave… | REQ-107 |
| P21-067 | U-F | The platform reads EVSE status from the ChargeLab API at JFK often enough to meet the 60-second… | merged into REQ-104 |
| P21-068 | U-F | The platform retrieves per-session records from AMPECO through its API once Kinship provides them. | merged into REQ-031 |
| P21-069 | U-F | The platform retrieves per-session records from ChargeLab at JFK where the API provides them. | merged into REQ-161 |
| P21-070 | U-F | Where a CSMS provides pricing, the platform stores the site's public price and shows it to the… | REQ-163 |
| P21-071 | U-F | The platform ingests the LIC ChargePoint portal CSV and uses it to reconcile bookings with… | REQ-162 |
| P21-072 | U-F | The CSV ingest accepts exports uploaded by hand at irregular times and skips rows already ingested… | merged into REQ-162 |
| P21-073 | U-F | Hosts without a CSMS can connect their chargers to an Amperlane-operated CitrineOS back-end over… | parked REQ-313 |
| P21-074 | U-F | An OCPI 2.2.1 eMSP gateway is built in Phase 1 and tested against a simulated CPO before any… | REQ-166 |
| P21-075 | U-F | The OCPI gateway reads Locations, Tariffs, Sessions and CDRs from a peered CPO and uses Tokens and… | merged into REQ-166 |
| P21-076 | S-F | LA charging sites connect over OCPI 2.2.1 rather than through per-network adapters. | parked REQ-325 |
| P21-077 | U-F | JFK can move from the ChargeLab API to OCPI 2.2.1 peering without changes to the booking core. | merged into REQ-166 |
| P21-078 | U-NF | The platform can integrate with NEVI-funded stations, which must support OCPP 2.0.1 and OCPI 2.2.1. | merged into REQ-166 |
| P21-079 | S-NF | The booking and slot data model has a documented mapping to the OCPI 2.3 Booking module, so the… | REQ-108 |
| P21-080 | U-F | The platform exchanges bookings with CPOs through the OCPI 2.3 Booking module. | parked REQ-328 |
| P21-081 | S-F | The driver map shows public DC charging stations near the driver from NLR AFDC and Open Charge… | REQ-030 |
| P21-082 | S-F | The platform uses NREL (now NLR) AFDC station data. | merged into REQ-030 |
| P21-083 | S-F | The platform shows each charger's current availability from the NREL API. | dropped: impossible, the AFDC API is static (CF-003 resolved) |
| P21-084 | U-NF | Discovery data from AFDC and Open Charge Map never changes bookable availability. | merged into REQ-030 |
| P21-085 | U-NF | Requests to the NLR AFDC API stay within 1,000 per hour. | design detail → Step 3 |
| P21-086 | U-NF | Open Charge Map data is shown with the attribution its CC BY 4.0 licence requires. | REQ-238 |
| P21-087 | U-NF | Automated tests of the AMPECO adapter run against an AMPECO sandbox and never against production… | REQ-237 |
| P21-088 | U-F | For every booking the platform records which station-hold method applied (charger reservation… | merged into REQ-154 |
| P21-089 | U-F | The platform keeps a time-stamped history of every EVSE status change, so the status at any past… | REQ-164 |
| P21-090 | U-NF | A new site whose CSMS already has an adapter, or a new pattern C site, is onboarded by… | REQ-165 |
| P21-091 | S-F | If the driver has not arrived when the grace period after slot start ends, the platform releases… | REQ-033 |
| P21-092 | S-F | The grace period is 10 minutes by default. | REQ-034 |
| P21-093 | U-F | The grace period is stored per site, so a site's partner agreement can set a value other than 10… | merged into REQ-034 |
| P21-094 | S-F | When a slot is released after grace at a site with a physical hold, the platform tells on-site… | REQ-035 |
| P21-095 | S-F | A booking released after grace without an arrival creates a no-show fee line item. | REQ-036 |
| P21-096 | U-F | The no-show fee amount and the station's share of it are configurable per site. | REQ-183 |
| P21-097 | S-F | The payer of the no-show fee (fleet, driver, or fleet pays and deducts) is a setting per fleet. | parked REQ-298 |
| P21-098 | S-F | Where a fleet's policy is "driver pays", the platform collects the no-show fee from the driver. | parked REQ-299 |
| P21-099 | U-F | Where a fleet's policy is "fleet pays and deducts", the fleet receives a per-driver statement of… | parked REQ-302 |
| P21-100 | S-F | Borough Green is not charged for no-shows caused by its drivers, and Amperlane does not bill… | parked REQ-298 |
| P21-101 | S-F | No-show fees are passed through to the station. | parked REQ-303 |
| P21-102 | U-F | The booking confirmation tells the driver the grace period and the no-show fee terms that apply to… | REQ-172 |
| P21-103 | S-F | A driver can cancel a booking with one tap from the latest booking message or the driver page. | REQ-039 |
| P21-104 | S-F | A driver can report "running late" with one tap from the latest booking message or the driver page. | REQ-040 |
| P21-105 | S-F | A driver can cancel a booking by replying CANCEL to a booking SMS. | REQ-041 |
| P21-106 | U-F | A cancellation made before a set cutoff before slot start creates no no-show fee. | REQ-171 |
| P21-107 | U-F | A "running late" signal either releases the stall to walk-ups at once or extends the hold up to… | parked REQ-305 |
| P21-108 | S-F | A driver whose vehicle is seen approaching the site is not marked a no-show when grace ends. | parked REQ-306 |
| P21-109 | S-F | Grace is extended automatically while the vehicle is within about two blocks of the site. | parked REQ-307 |
| P21-110 | S-F | Ops can extend the grace period of a single booking with a reason code. | REQ-042 |
| P21-111 | U-F | An ops grace extension cannot exceed a maximum set per site. | merged into REQ-042 |
| P21-112 | S-F | A driver records arrival by scanning a QR code posted at the stall. | REQ-043 |
| P21-113 | S-F | The platform generates a printable QR code for each stall that site staff, such as the LIC… | REQ-044 |
| P21-114 | U-F | The platform records arrival from the phone's location only when the driver has opted in. | REQ-173 |
| P21-115 | U-F | The platform records arrival from the CSMS session-start event where the CSMS sends one. | REQ-174 |
| P21-116 | U-F | The platform records arrival when the vehicle's telematics location enters a geofence around the… | REQ-175 |
| P21-117 | U-F | The LIC attendant can confirm a driver's arrival in the attendant view. | REQ-176 |
| P21-118 | U-F | Once arrival is recorded, the booking moves to Arrived and is not released at the end of grace. | REQ-177 |
| P21-119 | U-F | While a session runs, the platform tracks its live status from the CSMS where the CSMS provides it. | REQ-178 |
| P21-120 | U-F | A booking moves to Completed when its CDR or CSMS session record shows the session ended. | merged into REQ-224 |
| P21-121 | S-F | A driver who arrives after grace has the booking recorded as a no-show. | REQ-037 |
| P21-122 | S-F | When a late driver's booking is released as a no-show, the driver receives an instant offer of any… | REQ-038 |
| P21-123 | U-F | Whether a no-show fee still applies after a late driver accepts the re-offer is a setting per fleet. | parked REQ-304 |
| P21-124 | S-F | A fleet can dispute a no-show, and ops reviews the evidence and either reverses or keeps the fee… | REQ-045 |
| P21-125 | S-F | A driver can report that the allocated stall was blocked on arrival, and the report is stored with… | REQ-046 |
| P21-126 | U-F | For a disputed no-show, ops sees the booking, the hold sent, the station status at that time, and… | REQ-179 |
| P21-127 | U-F | A no-show dispute is checked against the CDR or CSMS session record for the slot. | merged into REQ-179 |
| P21-128 | U-F | When the booker and the driver differ, a no-show is attributed to the driver named on the booking. | converted to Q-002 |
| P21-129 | S-NF | The platform's monthly no-show rate is lower than the pilot's reported 17%. | converted to Q-044 |
| P21-130 | S-F | The platform acts on an EVSE "Faulted" status received by webhook or poll without waiting for a… | REQ-047 |
| P21-131 | U-NF | Fault handling starts within 60 seconds of a connected site's CSMS reporting the fault. | design detail → Step 3 |
| P21-132 | S-F | On a fault, the platform finds every booking allocated, or due to be allocated, to that EVSE for… | merged into REQ-048 |
| P21-133 | S-F | Each booking affected by a fault is reassigned automatically to a free compatible EVSE at the same… | REQ-048 |
| P21-134 | S-F | Drivers whose bookings cannot be placed at the same site after a fault are notified with… | REQ-049 |
| P21-135 | S-F | Ops is notified of every fault-affected booking the platform could not place. | REQ-050 |
| P21-136 | S-F | The station sees which bookings a fault affected and what happened to each one. | REQ-051 |
| P21-137 | U-F | Ops sees a summary of the automatic fault moves and can undo any of them. | REQ-187 |
| P21-138 | U-F | For fault-affected bookings that cannot be placed, the platform proposes reassignments and ops… | REQ-188 |
| P21-139 | U-F | Drivers moved after a fault are notified in their own language. | merged into REQ-199 |
| P21-140 | U-F | A fault reassignment uses an EVSE beyond the site's bookable cap only if the station allows it. | converted to Q-038 |
| P21-141 | S-F | A booking moved because of a fault carries the reason code "moved — charger fault" and is never… | REQ-052 |
| P21-142 | S-F | Every booking state change records a reason code and its actor, either the system or a named person. | REQ-053 |
| P21-143 | S-F | Ops can make a booking on behalf of a driver. | REQ-055 |
| P21-144 | S-F | Ops can place a manual hold that blocks capacity at a site for maintenance or for a fleet priority. | REQ-184 |
| P21-145 | U-F | When a maintenance hold removes an EVSE that has allocated bookings, those bookings are reassigned… | REQ-185 |
| P21-146 | U-F | When a station lowers a cap, or ops adds a fleet-priority hold, below the confirmed bookings… | REQ-186 |
| P21-147 | S-F | Ops can force-confirm a booking. | REQ-056 |
| P21-148 | S-F | Ops can force-release a booking. | REQ-057 |
| P21-149 | S-F | Ops can rebook every booking on a failed charger in one action ("charger down, rebook everyone"). | REQ-054 |
| P21-150 | S-F | Ops can do all daily booking work in the ops console without opening Airtable or Google Sheets. | REQ-058 |
| P21-151 | U-F | The ops console lists every open exception (failed hold, full site, fault, unplaced booking, open… | REQ-189 |
| P21-152 | U-F | Ops can see the live status and the status age of every EVSE at every site. | merged into REQ-160 |
| P21-153 | U-F | A driver message reporting a broken charger creates an ops alert linked to the site. | REQ-191 |
| P21-154 | U-F | At LIC, a "faulted" status set by the attendant triggers the same reassignment as a CSMS fault. | REQ-192 |
| P21-155 | U-F | A station operator can mark an EVSE out of service in the station portal, which triggers the fault… | REQ-193 |
| P21-156 | U-NF | An exception that needs ops while no ops person is on duty reaches a named on-call contact or… | parked REQ-316 |
| P21-157 | S-NF | On a charger-down day, ops move the affected bookings without phoning the station or the attendant. | merged into REQ-141 |
| P21-158 | S-F | The ops console is in the platform scope as a core product for the four ops people, not as an… | merged into REQ-058 |
| P21-159 | S-F | The driver interface is a mobile web app that runs in the phone's browser with no app-store install. | REQ-059 |
| P21-160 | S-F | Drivers use native iOS and Android apps. | parked REQ-321 |
| P21-161 | S-F | A driver can book without installing an app, creating an account password or adding a payment card. | REQ-060 |
| P21-162 | S-F | A driver can request a booking by SMS. | REQ-061 |
| P21-163 | S-F | A driver can request a booking by texting a site code and a time, such as "GOW 1645". | merged into REQ-061 |
| P21-164 | S-F | A driver can book and receive booking messages through WhatsApp. | REQ-062 |
| P21-165 | S-F | Booking messages carry a link that opens the driver page for that booking. | REQ-063 |
| P21-166 | U-NF | Links in driver messages are signed, short-lived and single-use, and open the driver page without… | REQ-240 |
| P21-167 | U-NF | Opening a driver link on a device not seen before for that driver requires a one-time code sent to… | REQ-241 |
| P21-168 | U-F | A driver is identified by a mobile number registered to one or more fleets. | REQ-198 |
| P21-169 | U-F | A driver registered to more than one fleet can book any vehicle that each of those fleets'… | merged into REQ-198 |
| P21-170 | S-NF | The driver page is light enough to use on a phone in a cradle that is running Uber and Lyft with a… | covered by constitution N24 |
| P21-171 | S-NF | All driver messages and the driver page are available in English, Spanish and Bengali. | REQ-112 |
| P21-172 | U-F | Each driver has a stored language preference that the platform uses for every message and page. | REQ-199 |
| P21-173 | S-F | From a booking, the driver can open directions to the site in a maps app. | REQ-064 |
| P21-174 | S-F | The platform shows the driver's estimated arrival time at the site. | REQ-065 |
| P21-175 | U-F | Turn-by-turn navigation opens in the driver's own navigation app, not inside Amperlane. | merged into REQ-064 |
| P21-176 | S-F | From the driver page, the driver can return to the Uber or Lyft driver app with one tap. | REQ-066 |
| P21-177 | S-F | The platform receives trip and vehicle data from the Uber and Lyft driver apps to offer a slot… | parked REQ-322 |
| P21-178 | S-F | A driver receives a reminder before the slot starts. | REQ-067 |
| P21-179 | U-F | The reminder lead time is configurable, with a default to be agreed at Step 2 review. | merged into REQ-146 |
| P21-180 | S-NF | Apart from booking, a driver needs no interaction with Amperlane to charge and be billed. | dropped: contradicted by agreed driver steps (reminder, cancel, QR arrival); two-tap booking is kept |
| P21-181 | S-F | Drivers do not pay at the charger with their own cards, because billing runs through Amperlane… | parked REQ-296 |
| P21-182 | S-F | A fleet manager can see the fleet's bookings in the fleet portal. | REQ-069 |
| P21-183 | S-F | A fleet manager can add, edit and retire the fleet's vehicles in the fleet portal, including… | REQ-070 |
| P21-184 | S-F | The fleet portal gives the fleet manager reports on bookings for every vehicle in the fleet. | REQ-071 |
| P21-185 | S-F | A fleet manager can restrict which sites the fleet's drivers may book. | parked REQ-294 |
| P21-186 | S-F | A fleet manager can set a maximum number of bookings per driver per day, such as two. | parked REQ-295 |
| P21-187 | S-F | Where the fleet pays for energy, the fleet manager can set spend controls on which sites drivers… | parked REQ-294 |
| P21-188 | S-F | A fleet sets whether its vehicles may use adapters, such as CCS adapters on Teslas, and the… | REQ-072 |
| P21-189 | U-F | A fleet registers its drivers' mobile numbers and its vehicles in the fleet portal. | REQ-205 |
| P21-190 | U-F | Ops can register drivers and vehicles for a small fleet that does not use the portal. | REQ-206 |
| P21-191 | U-F | A fleet can register a booker-only number that books for the fleet and names the driver who will… | REQ-201 |
| P21-192 | U-F | When a fleet removes a driver, that driver's number can no longer book for the fleet. | REQ-202 |
| P21-193 | S-F | A fleet manager can see the no-shows of the fleet's drivers. | REQ-073 |
| P21-194 | U-F | A fleet manager can see the fleet's charging utilisation. | merged into REQ-071 |
| P21-195 | S-NF | A small fleet such as Five Boroughs can book and follow its charging through messaging and… | REQ-243 |
| P21-196 | S-F | A fleet owner can see, for each vehicle, whether today's booked charge took place. | REQ-074 |
| P21-197 | S-F | The platform bills each fleet a subscription per vehicle per month ($15 in the brief). | parked REQ-293 |
| P21-198 | U-F | Each fleet has a credit limit on its outstanding balance, and new bookings are flagged to ops when… | parked REQ-281 |
| P21-199 | S-F | The platform reads battery level, charging state and location of Borough Green's non-Tesla… | REQ-075 |
| P21-200 | S-F | The platform reads battery data for Tesla vehicles. | parked REQ-311 |
| P21-201 | U-F | The platform meters Tesla Fleet API usage per fleet, so the cost can be charged to whoever pays… | parked REQ-311 |
| P21-202 | U-F | The platform reads battery level, charging state and location through Smartcar for vehicles… | parked REQ-312 |
| P21-203 | U-NF | Vehicle-data sources (Geotab, Tesla Fleet API, Smartcar, manual entry) sit behind one interface… | design detail → Step 3 |
| P21-204 | S-F | A booking can be made for a vehicle that has no telematics, using the driver's own phone. | REQ-019 |
| P21-205 | S-F | A station operator can publish its sites' bookable capacity, schedules and tariffs. | merged into REQ-076 |
| P21-206 | S-F | A station operator can view its sites' bookable slots in the station portal. | merged into REQ-079 |
| P21-207 | S-F | A station operator can set the days and hours in which each site accepts bookings. | REQ-076 |
| P21-208 | S-F | A station operator can record the tariffs that apply at each site. | REQ-078 |
| P21-209 | S-F | A station operator can change a site's bookable cap for a time window in the station portal… | REQ-077 |
| P21-210 | S-F | A station operator sees the upcoming bookings at its sites and the EVSE each one is allocated to. | REQ-079 |
| P21-211 | S-F | A station operator sees, for each faulted charger, how many bookings the fault affected. | REQ-080 |
| P21-212 | U-F | A station operator sees its payouts in the station portal. | parked REQ-287 |
| P21-213 | U-F | A station operator sees the off-peak sessions Amperlane brought to each site. | REQ-209 |
| P21-214 | U-F | Station terms (bookable caps, grace, no-show fee, payout frequency) are configurable per site, so… | merged into REQ-146 |
| P21-215 | S-F | Site staff, such as the LIC garage attendant, are platform users with their own access. | REQ-081 |
| P21-216 | S-F | The station portal shows, for each time window, how many ports stay unbookable for walk-ups. | REQ-082 |
| P21-217 | S-F | Each fleet receives one consolidated invoice per month with net-30 payment terms. | REQ-083 |
| P21-218 | S-F | A fleet's monthly invoice covers all its drivers' charging, so the fleet's finance team never… | parked REQ-270 |
| P21-219 | S-F | The platform invoices each fleet monthly through Stripe for a fee per completed booking ($2 today). | parked REQ-271 |
| P21-220 | S-F | After a session, billing runs automatically, with no manual invoice preparation. | REQ-084 |
| P21-221 | S-F | After each completed session, the station's payable amount is recorded automatically. | parked REQ-272 |
| P21-222 | S-F | The platform records each session's cost to Amperlane at the station's B2B tariff per kWh (about… | parked REQ-273 |
| P21-223 | S-F | The platform bills fleets a bundled per-kWh rate (about $0.49 at Gowanus) that includes the… | parked REQ-274 |
| P21-224 | S-F | The platform charges stations a take rate of 10–12% on charging GMV booked through Amperlane. | parked REQ-275 |
| P21-225 | S-F | The platform charges stations a small fee only on incremental off-peak sessions. | parked REQ-276 |
| P21-226 | S-F | Stations are never charged on sessions they would have had anyway at peak. | parked REQ-276 |
| P21-227 | S-F | Stations are paid weekly when Amperlane holds their money. | parked REQ-277 |
| P21-228 | S-F | Stations are paid more often than monthly. | parked REQ-277 |
| P21-229 | U-F | The payout frequency is set per station. | parked REQ-277 |
| P21-230 | S-F | Fleets are invoiced net-30 through Stripe Invoicing, and stations are paid by weekly Stripe… | parked REQ-278 |
| P21-231 | S-NF | The funds flow never requires Amperlane to hold a New York money-transmitter licence. | parked REQ-279 |
| P21-232 | U-NF | Station money is held and moved by Stripe and never sits in an Amperlane bank account awaiting… | parked REQ-279 |
| P21-233 | S-F | The ledger is double-entry, with no balance columns. | REQ-085 |
| P21-234 | U-NF | Ledger entries are append-only, and corrections are made by new entries. | REQ-247 |
| P21-235 | S-F | The ledger shows what each fleet owes, has paid and has outstanding. | REQ-086 |
| P21-236 | U-F | The ledger shows Amperlane's exposure between weekly station payouts and net-30 fleet payments. | parked REQ-280 |
| P21-237 | U-NF | The ledger and money flows are the same in every business model, and only charge types and the… | REQ-210 |
| P21-238 | U-F | Every booking is matched to the CPO's session record (OCPI CDR, AMPECO or ChargeLab session… | REQ-161 |
| P21-239 | U-F | A booking without a matching session record is flagged as a no-show or fault case. | REQ-214 |
| P21-240 | U-F | The no-show fee is a separate line item, never mixed into energy charges. | REQ-211 |
| P21-241 | U-F | A disputed no-show fee line can be reversed without changing any energy line. | REQ-212 |
| P21-242 | S-NF | In a merchant-of-record model, each station's session data is complete and accurate enough to bill… | parked REQ-282 |
| P21-243 | S-NF | Every invoice line and every payout reconciles to ledger entries and session records when it is… | REQ-109 |
| P21-244 | U-F | Amperlane finance has views for station payouts, fleet invoices and reconciliation against session… | REQ-215 |
| P21-245 | U-F | Stripe files and delivers 1099 forms for the connected station accounts. | parked REQ-283 |
| P21-246 | S-NF | The payment provider sits behind an interface, so it can be replaced without changes to the… | REQ-111 |
| P21-247 | U-F | Adyen for Platforms replaces Stripe for payouts. | parked REQ-297 |
| P21-248 | S-NF | Payment webhooks are never the only source of payment status; a periodic check reconciles it. | REQ-110 |
| P21-249 | U-F | A pricing module holds station B2B tariffs and fleet bundled rates and applies them to session… | parked REQ-284 |
| P21-250 | U-F | As merchant of record for energy, Amperlane issues receipts and handles sales tax on the energy it… | parked REQ-285 |
| P21-251 | U-F | A fleet can dispute an energy charge, and ops resolves it against the CPO's session record. | parked REQ-286 |
| P21-252 | U-F | The platform tracks the payment status of every fleet invoice and flags any invoice unpaid after… | REQ-216 |
| P21-253 | U-F | A booking reaches the Settled state once it is invoiced to the fleet and, where applicable, paid… | design detail → Step 3 |
| P21-254 | S-F | After a booking is confirmed, the driver receives a confirmation message with the site, date and… | REQ-088 |
| P21-255 | S-F | A driver never receives more than one confirmation for one booking. | REQ-089 |
| P21-256 | S-F | Inbound SMS messages are de-duplicated by the provider's message ID, so a retried webhook does not… | REQ-090 |
| P21-257 | S-F | Driver notifications are sent by SMS and by WhatsApp, both through Twilio. | merged into REQ-062 |
| P21-258 | S-NF | Driver notifications are written in English, Spanish and Bengali. | merged into REQ-112 |
| P21-259 | U-F | When the EVSE is allocated, the driver is told which stall to use. | REQ-200 |
| P21-260 | U-F | The reminder goes out on the driver's channel, SMS or WhatsApp. | merged into REQ-067 |
| P21-261 | U-F | Ops alerts (full site, failed hold, unplaced fault booking) appear in the ops console within 60… | design detail → Step 3 |
| P21-262 | S-F | The station operator is notified when a fault affects bookings at its site. | merged into REQ-051 |
| P21-263 | U-F | When a WhatsApp message cannot be delivered, the platform sends the same message by SMS. | REQ-219 |
| P21-264 | U-F | Drivers can reply to booking messages with cancel and running-late keywords in English, Spanish… | REQ-220 |
| P21-265 | U-NF | Twilio remains the provider for SMS and WhatsApp, behind an adapter. | design detail → Step 3 |
| P21-266 | U-F | Site staff receive their hold instructions (place sign, remove sign) by SMS or in the attendant… | merged into REQ-157 |
| P21-267 | U-F | The fleet portal, station portal and attendant view are available in Spanish and Bengali as well… | covered by constitution N22 |
| P21-268 | S-F | The platform reports completed bookings per month for NYC sites only, excluding other metros. | REQ-091 |
| P21-269 | U-F | For each booking the platform stores the arrival, session-record match, moves and rebookings… | REQ-224 |
| P21-270 | S-F | The platform reports no-show and late-arrival (more than 10 minutes late) rates per month, per… | REQ-092 |
| P21-271 | S-F | The platform reports the median arrival-to-plug wait per site. | REQ-093 |
| P21-272 | S-F | The platform reports off-peak utilisation per site for the windows 10 AM–3 PM and 10 PM–5 AM. | REQ-094 |
| P21-273 | S-F | The platform produces a Series A data-room report on the cleaned pilot history and the platform… | REQ-095 |
| P21-274 | S-NF | Every day after launch, Five Boroughs' cabs are charged at the 5 PM shift change without any… | REQ-113 |
| P21-275 | S-NF | After launch, Kinship no longer needs to call Amperlane about cones. | REQ-114 |
| P21-276 | S-NF | After launch, nobody at Amperlane opens Airtable to run bookings. | merged into REQ-058 |
| P21-277 | S-NF | Borough Green receives one invoice a month and has no reason to email Amperlane about it. | merged into REQ-083 |
| P21-278 | U-F | The platform reports weekly active drivers. | dropped: found only in the internal brief (SRC-R1#pilot); no client need |
| P21-279 | U-F | Migrated pilot history and platform bookings are reported with the same status definitions, so… | REQ-225 |
| P21-280 | S-F | The pilot history since October 2025 (bookings, no-shows, arrival times, driver, stall) is… | REQ-096 |
| P21-281 | S-NF | Migrated history lives in the platform's own data model and can be queried with new bookings, not… | REQ-115 |
| P21-282 | S-F | No pilot booking is lost in migration: record counts reconcile with the source export. | REQ-116 |
| P21-283 | U-F | Migrated bookings link to the same driver, fleet, site and stall records that new bookings use. | merged into REQ-115 |
| P21-284 | U-F | Migrated statuses are re-classified so that moved, no-show and cancelled are distinct outcomes. | REQ-228 |
| P21-285 | U-F | Early pilot records marked "cancelled" with a note that shows a no-show are migrated as no-shows. | merged into REQ-228 |
| P21-286 | U-F | Pilot bookings moved in the Sheets but left as no-shows in Airtable, such as the nine Gowanus… | merged into REQ-228 |
| P21-287 | U-F | Where the slot-grid Sheets and Airtable disagree, the migration applies a documented precedence… | REQ-229 |
| P21-288 | U-F | Migrated records from before February 2026 carry a data-quality flag. | REQ-230 |
| P21-289 | U-F | The raw pilot export is kept read-only for the period counsel sets. | REQ-252 |
| P21-290 | U-F | Stripe Billing history and Twilio message logs are migrated with the pilot history. | parked REQ-314 |
| P21-291 | S-NF | No code from the freelancer-built prototype is reused; only its schema is consulted. | REQ-117 |
| P21-292 | S-NF | Pilot data shared for analysis outside Amperlane has driver names and phone numbers removed. | REQ-118 |
| P21-293 | S-NF | All platform code lives in Amperlane's repositories, and all infrastructure runs in Amperlane's… | REQ-119 |
| P21-294 | S-NF | Access to production systems is role-based and limited to named people from the first release. | REQ-120 |
| P21-295 | S-NF | Security-relevant actions are audit-logged from the first release. | REQ-121 |
| P21-296 | S-NF | Every production change goes through a recorded change-management process with review and approval. | REQ-122 |
| P21-297 | S-NF | Data is encrypted in transit and at rest. | REQ-123 |
| P21-298 | S-NF | Production runs in an AWS account separate from every non-production environment. | REQ-124 |
| P21-299 | S-NF | Authentication is built so that a SOC 2 audit does not require rewriting it. | merged into REQ-120 |
| P21-300 | S-NF | The platform is ready for a SOC 2 Type I audit within 12 months of the rideshare platform's pilot… | parked REQ-318 |
| P21-301 | S-NF | The platform is ready for a SOC 2 Type I audit before the Series A raise in the second half of 2027. | parked REQ-318 |
| P21-302 | S-NF | A penetration test is passed before the rideshare platform's pilot starts. | parked REQ-319 |
| P21-303 | U-NF | SOC 2 control evidence (logs, traces, change records) is collected automatically from day one. | merged into REQ-121 |
| P21-304 | U-NF | Credentials and licence or account numbers are protected with the NY SHIELD Act's reasonable… | REQ-253 |
| P21-305 | U-NF | A breach-notification procedure that meets the NY SHIELD Act exists before launch. | REQ-254 |
| P21-306 | U-NF | Location data is encrypted, access-controlled and kept for a limited period. | merged into REQ-256 |
| P21-307 | S-NF | The platform keeps personal data only as long as disputes need it and then deletes it. | REQ-125 |
| P21-308 | U-NF | Each data type has a retention period set by Amperlane's counsel, and data past its period is… | merged into REQ-125 |
| P21-309 | U-NF | Location is kept only as derived arrival events, and each raw location reading is deleted once its… | REQ-256 |
| P21-310 | U-NF | Location is collected only after the driver's explicit opt-in, which is off by default, and only… | REQ-255 |
| P21-311 | U-NF | Vehicle data is read only with the fleet's authorisation as the vehicle account owner. | REQ-257 |
| P21-312 | U-NF | Amperlane's counsel approves the consent wording shown to drivers before launch. | merged into REQ-255 |
| P21-313 | S-NF | An append-only audit trail records who did what and when for every booking state change, override… | REQ-126 |
| P21-314 | U-NF | The audit trail also records every hold placed or released. | merged into REQ-126 |
| P21-315 | U-NF | Each portal user can see only their own organisation's data: a fleet its own fleet, a station its… | REQ-258 |
| P21-316 | U-NF | One identity service provides sign-on and roles across the fleet portal, station portal, ops… | design detail → Step 3 |
| P21-317 | U-NF | Public APIs are rate-limited per client. | design detail → Step 3 |
| P21-318 | U-NF | The licence of every third-party component is listed and approved by Amperlane's CTO before… | dropped: covered by the constitution's open-source check (code conventions, row 3) |
| P21-319 | S-NF | Open-source components are used only where they are mature and already in production use elsewhere. | REQ-127 |
| P21-320 | U-NF | Use of Google Maps results complies with Google's terms on caching and on combining with other maps. | design detail → Step 3 |
| P21-321 | U-NF | Migrated pilot driver data falls under the same protection and retention rules as new data. | merged into REQ-125 |
| P21-322 | S-NF | The platform is available 99.9% of the time between 5 AM and 1 AM Eastern. | REQ-128 |
| P21-323 | S-NF | Planned maintenance happens only between 1 AM and 5 AM Eastern. | REQ-129 |
| P21-324 | U-NF | Booking timers that fall due during maintenance fire late but are never lost. | merged into REQ-133 |
| P21-325 | U-F | Drivers can make and keep bookings for slots between 1 AM and 5 AM. | REQ-152 |
| P21-326 | S-NF | Booking API responses take under 300 ms at the 95th percentile, including during the burst and the… | REQ-130 |
| P21-327 | S-NF | The platform handles a launch burst of about 400 booking attempts in 10 minutes around 4:30 PM… | REQ-131 |
| P21-328 | S-NF | A load test of 2,000 booking attempts in 10 minutes, with heavy contention on a few sites, meets… | merged into REQ-131 |
| P21-329 | S-NF | Booking timers (hold expiry, charger-side hold, grace, auto-release) run as durable workflows that… | REQ-133 |
| P21-330 | S-NF | The workflow engine is self-hosted in Amperlane's AWS account, with no extra vendor contract in… | REQ-134 |
| P21-331 | S-NF | The platform is a modular monolith, not a set of microservices. | REQ-135 |
| P21-332 | S-NF | The platform is written in TypeScript end to end, on PostgreSQL, hosted on AWS. | REQ-136 |
| P21-333 | S-NF | Hosting draws first on Amperlane's $100k AWS Activate credits. | REQ-137 |
| P21-334 | S-NF | Launching a new metro needs configuration (sites, time zone, partners), not changes to the booking… | REQ-138 |
| P21-335 | S-NF | The platform exposes its booking functions through a documented API. | REQ-139 |
| P21-336 | U-NF | The platform emits metrics, traces and logs that show the health of every adapter and workflow. | covered by constitution N21 |
| P21-337 | U-NF | Soft holds are stored durably with status and expiry, so every hold is auditable. | design detail → Step 3 |
| P21-338 | S-NF | The platform supports at least 10,000 completed bookings a month in NYC by June 2027. | REQ-132 |
| P21-339 | U-NF | The platform supports all of Borough Green's ~420 vehicles and at least two more fleets without… | merged into REQ-132 |
| P21-340 | S-NF | A simulated site lets the team break chargers on purpose, using the EVerest charger simulator. | REQ-140 |
| P21-341 | S-NF | The Gowanus fault of 1:50 PM with nine bookings is replayed as an automated test case. | REQ-141 |
| P21-342 | U-NF | The simulator also produces session overruns and late drivers. | merged into REQ-140 |
| P21-343 | S-NF | The platform goes live in NYC production on 1 March 2027 with real stations and real fleets and no… | REQ-142 |
| P21-344 | S-F | At launch, all three pilot sites (46 ports) and both pilot fleets book through the platform. | REQ-097 |
| P21-345 | S-F | The platform serves the five actor types (fleet manager, driver, station operator, site staff… | REQ-098 |
| P21-346 | S-NF | An MVP is ready 12 weeks after the build starts. | dropped: superseded by the 1 March 2027 launch date (CF-006) |
| P21-347 | S-F | The platform operates in 10 US metros by the end of 2027. | parked REQ-326 |
| P21-348 | S-F | The platform launches in Los Angeles in Q3 2027. | parked REQ-324 |
| P21-349 | S-NF | New York runs fully before a second city is added. | dropped: business sequencing preference, not a platform behaviour; LA and other metros are parked |
| P21-350 | S-NF | Phase one costs $0.9–1.2M through the end of Q2 2027, and anything above $1.2M needs an explicit… | converted to Q-025 |
| P21-351 | U-NF | Phase 0 is fixed price and Phase 1 is time and materials with a cap. | converted to Q-025 |
| P21-352 | S-NF | Amperlane engineers work in the same repositories and rituals as Intellias from Phase 0, with no… | REQ-143 |
| P21-353 | S-NF | By handover, Priya Nair owns the knowledge of the integration layer. | REQ-144 |
| P21-354 | U-NF | Amperlane's product designer is embedded in the delivery squad. | dropped: team-shape proposal (SRC-D2#16), not a platform requirement |
| P21-355 | U-NF | Delivery runs as Phase 0 (9–27 Nov 2026), the Phase 1 build (30 Nov 2026–26 Feb 2027) and… | dropped: indicative delivery plan (SRC-D2#15); belongs in the proposal |
| P21-356 | U-NF | The plan includes time to test with real drivers before 1 March 2027. | REQ-269 |
| P21-357 | S-NF | Detailed settlement is built only after the founders decide the business model. | dropped: sequencing rule, applied through constitution P5 and the parking lot |
| P21-358 | S-F | Platform v1 covers a driver interface, a fleet portal, a station portal, a booking engine and… | REQ-099 |
| P21-359 | U-F | The attendant view is in the March MVP. | merged into REQ-158 |
| P21-360 | S-F | The platform integrates with the AMPECO CSMS. | REQ-031 |
| P21-361 | S-F | The platform integrates with the ChargeLab CSMS. | REQ-032 |
| P21-362 | S-F | The platform integrates with the ChargePoint network. | parked REQ-308 |
| P21-363 | S-F | The platform integrates with the EVgo network. | parked REQ-309 |
| P21-364 | S-F | The platform integrates with the Electrify America network. | parked REQ-310 |
| P21-365 | S-F | The platform uses Stripe for payments and payouts. | REQ-087 |
| P21-366 | S-F | The platform uses Google Maps for maps, directions and ETA. | REQ-068 |
| P21-367 | U-F | The platform uses Valhalla on OpenStreetMap, or Mapbox, for routing and ETA. | dropped: alternative maps provider, replaceable behind the adapter (A-030, Q-027) |
| P21-368 | U-F | Charging prices vary by time of use, based on utility tariff data from OpenEI URDB. | parked REQ-329 |
| P21-369 | U-F | The platform takes part in OpenADR 3.0 demand response. | parked REQ-330 |
| P21-370 | U-F | The platform supports bookings for autonomous-vehicle fleets and depots. | parked REQ-331 |
| P22-001 | U-NF | Every state-changing command from any channel (confirm, cancel, running late, accept re-offer, ops… | REQ-236 |
| P22-002 | S-NF | An inbound SMS or WhatsApp message whose provider message id was already processed is not… | merged into REQ-090 |
| P22-003 | U-NF | The platform sends at most one notification per booking event, recipient and channel, even when… | merged into REQ-089 |
| P22-004 | U-NF | A CSMS status webhook delivered more than once changes the EVSE's current status, and starts any… | merged into REQ-106 |
| P22-005 | U-NF | A status event whose observed-at time is earlier than the EVSE's latest stored status is kept in… | merged into REQ-106 |
| P22-006 | U-NF | A payment-provider event delivered more than once is applied to the ledger once. | merged into REQ-106 |
| P22-007 | U-NF | A session record received more than once, from any source or in overlapping CSV exports, is stored… | merged into REQ-106 |
| P22-008 | S-NF | For every API-connected site, the platform polls the CSMS for EVSE status in addition to webhooks… | merged into REQ-107 |
| P22-009 | S-NF | Invoice and payout status at the payment provider is also reconciled by a scheduled query, so a… | merged into REQ-110 |
| P22-010 | U-F | When ReserveNow is rejected or not answered at T-15, the platform falls back to a signage request… | REQ-155 |
| P22-011 | U-F | When the AMPECO API is unreachable or its status is older than 60 seconds, the platform runs… | REQ-167 |
| P22-012 | U-F | When the JFK status feed is unavailable, the platform keeps accepting bookings within the capacity… | REQ-168 |
| P22-013 | U-F | When no LIC CSV has been ingested within a set period, ops is alerted, and LIC bookings without a… | merged into REQ-214 |
| P22-014 | U-F | At a status-only site, when site staff have not acknowledged a signage request by the T-10 check… | merged into REQ-156 |
| P22-015 | U-F | At a no-API site, when the attendant has not acknowledged a signage request by the T-10 check, ops… | merged into REQ-156 |
| P22-016 | U-F | Ops can put a site into manual mode, in which the platform keeps the slot calendar and gives ops a… | REQ-170 |
| P22-017 | U-F | When an API-connected EVSE sends no status for a set time, the platform marks it unknown, excludes… | REQ-169 |
| P22-018 | U-F | A driver can report "charger not working" in one tap from the booking link, which takes the… | merged into REQ-191 |
| P22-019 | U-F | When a booking has an arrival signal but no charging session starts, no no-show fee is created… | REQ-181 |
| P22-020 | U-F | After a fault, an EVSE returns to the pool only when it has reported available for a set period or… | REQ-194 |
| P22-021 | U-NF | If automatic rebooking after a fault stops partway, every affected booking ends rebooked, proposed… | REQ-239 |
| P22-022 | U-NF | Booking timers (hold expiry, reminder, T-15 hold, T-10 check, grace, auto-release) survive a… | merged into REQ-133 |
| P22-023 | U-F | A timer that fires late acts on the booking's current state, so a late auto-release never releases… | merged into REQ-177 |
| P22-024 | U-F | When a grace timer fires more than a set time late, the no-show fee is not created automatically… | merged into REQ-180 |
| P22-025 | U-F | A driver can cancel, report running late or accept an alternative by replying with a keyword to… | merged into REQ-220 |
| P22-026 | U-F | During a platform outage, a driver who texts the booking number gets an automatic reply in their… | REQ-223 |
| P22-027 | U-NF | Ops can get the upcoming bookings per site (driver, vehicle, window, allocated EVSE) from a copy… | REQ-266 |
| P22-028 | U-F | When Twilio is unreachable, outbound messages are queued and retried, and ops sees which drivers… | merged into REQ-219 |
| P22-029 | U-F | When a time-critical message to a driver fails, the platform resends it on the driver's other… | merged into REQ-219 |
| P22-030 | U-NF | When the payment provider is unavailable, bookings, arrivals and fee lines are still recorded in… | REQ-245 |
| P22-031 | U-F | When vehicle data for a vehicle is unavailable or older than a set age, the platform falls back to… | design detail → Step 3 |
| P22-032 | U-F | When the maps provider is unavailable, the driver PWA still shows the site address and a link that… | merged into REQ-064 |
| P22-033 | U-NF | Production runs in one AWS region across at least two availability zones, and a full-region outage… | covered by constitution N20 |
| P22-034 | U-NF | The production database supports point-in-time recovery with a recovery point objective of no more… | covered by constitution N20 |
| P22-035 | U-NF | A full restore of production completes within a set recovery time, proven by a restore drill at a… | covered by constitution N20 |
| P22-036 | U-F | After a restore, the platform re-creates the timers of every booking in a non-final state from the… | merged into REQ-133 |
| P22-037 | U-NF | Backups are encrypted and copied to an AWS account separate from production. | covered by constitution N14 |
| P22-038 | U-NF | All platform hosts synchronise their clocks to one time source, and timers, status observed-at… | design detail → Step 3 |
| P22-039 | U-NF | For every CSMS event, session record and message, the platform stores the external timestamp and… | design detail → Step 3 |
| P22-040 | U-F | Each site has its own time zone, and every time shown to a driver, attendant, station operator or… | merged into REQ-151 |
| P22-041 | U-F | On daylight-saving change days, booking windows, grace and timers run on absolute time, so a… | merged into REQ-151 |
| P22-042 | U-F | The ops console shows one live board per site for the current day (bookings by state, EVSE status… | REQ-190 |
| P22-043 | U-F | The ops console shows one queue of open exceptions (failed or unacknowledged station hold… | merged into REQ-189 |
| P22-044 | U-F | An exception that no ops user picks up within a set time is escalated to a second contact. | parked REQ-316 |
| P22-045 | U-F | When no ops user is signed in, time-critical exceptions go to an on-duty phone number by SMS or… | parked REQ-316 |
| P22-046 | U-F | Ops can find a driver's bookings, messages and fees by mobile number, plate or booking code in a… | REQ-195 |
| P22-047 | U-F | The ops console shows, per driver and booking, the full message history (inbound and outbound… | REQ-196 |
| P22-048 | U-F | Ops can send a templated or free-text message to a driver on the driver's channel from the ops… | REQ-197 |
| P22-049 | U-F | Every message to a driver tells the driver, in their language, how to reach ops (reply keyword or… | REQ-221 |
| P22-050 | U-F | When a fault or maintenance hold changes bookings at a site, the station operator receives the… | merged into REQ-051 |
| P22-051 | U-F | Ops can onboard a new site (operator, address, time zone, supply pattern, EVSEs, connectors, max… | merged into REQ-165 |
| P22-052 | U-F | A new site is shown to drivers and bookable only after ops marks it live, which requires its… | merged into REQ-165 |
| P22-053 | U-F | A site whose CSMS has no adapter can go live as a no-API site (attendant or ops station hold… | merged into REQ-165 |
| P22-054 | U-F | Ops can change per-site and per-EVSE settings (reservable flag, grace, maximum grace extension… | merged into REQ-146 |
| P22-055 | U-F | Ops can onboard a fleet (billing contact, invoice terms, fleet policy, vehicles, driver numbers)… | merged into REQ-206 |
| P22-056 | U-F | A fleet manager or ops can import a fleet's vehicles (plate, make and model, native connector… | REQ-207 |
| P22-057 | U-F | When a driver's number is registered, the driver gets a welcome message in their language… | REQ-203 |
| P22-058 | U-F | When a fleet removes a driver, that number can no longer book for that fleet, and the driver's… | merged into REQ-202 |
| P22-059 | U-F | The platform keeps the pilot's Twilio number and accepts the pilot's booking-code format (e.g.… | merged into REQ-061 |
| P22-060 | S-NF | A test environment contains a simulated site on which engineers can make chargers fault, overrun… | merged into REQ-140 |
| P22-061 | S-NF | An automated test replays the Gowanus fault (1:50 PM, nine bookings until about 7 PM) on the… | merged into REQ-141 |
| P22-062 | U-NF | Development, staging and production are separate environments, and staging runs every integration… | merged into REQ-237 |
| P22-063 | U-NF | Non-production environments hold only synthetic or anonymised data, including an anonymised copy… | merged into REQ-118 |
| P22-064 | U-NF | Before 1 March 2027 the platform runs with real drivers at the pilot sites for a set period… | merged into REQ-269 |
| P22-065 | U-NF | Deployments that can interrupt booking run only between 1 and 5 AM ET, and deployments inside the… | merged into REQ-129 |
| P22-066 | U-NF | During the March 2027 hypercare, a production incident that affects booking is acknowledged within… | parked REQ-317 |
| P22-067 | U-NF | Every alert and every external-system outage has a written runbook that Amperlane's engineers have… | REQ-268 |
| P22-068 | U-NF | Every production incident that affects bookings or money gets a written post-incident review… | dropped: delivery-process convention for Phase 0, not a platform requirement |
| P22-069 | U-F | Reversing a no-show fee after the fleet invoice is issued creates a credit line on the next… | REQ-213 |
| P22-070 | U-F | Ops can waive a no-show fee before it is invoiced, with a reason code, recorded as a separate… | REQ-182 |
| P22-071 | U-F | No no-show fee is created for a booking that was rebooked, whose station hold failed, or whose… | REQ-180 |
| P22-072 | U-F | A no-show fee on a booking whose reminder was not delivered is held for ops review instead of… | merged into REQ-180 |
| P22-073 | U-F | A fleet can dispute a no-show fee within a set window after the booking, and the evidence for that… | merged into REQ-045 |
| P22-074 | U-F | Each dispute is decided (fee kept or reversed) by a named ops user with a reason within a set… | merged into REQ-045 |
| P22-075 | U-F | A driver can contest a no-show from the booking link ("I was there, the stall was blocked"), which… | merged into REQ-045 |
| P22-076 | U-F | Ops can see on one screen, for any booking, its ordered history: states, actors, reason codes… | merged into REQ-179 |
| P22-077 | U-F | A cancellation before a per-site cut-off is free, and a later cancellation is treated under the… | merged into REQ-171 |
| P22-078 | U-F | A driver who cancels or reports running late before the slot starts pays no no-show fee for that… | merged into REQ-171 |
| P22-079 | U-F | Each fleet invoice lists every charged item (booking fee, energy, no-show fee, subscription) with… | REQ-217 |
| P22-080 | U-F | A fleet manager or fleet finance contact can see the running charges for the current month before… | REQ-208 |
| P22-081 | U-F | An invoice month closes at a set time after month end, and session records or fee changes that… | REQ-218 |
| P22-082 | U-F | Invoice months, payout weeks and the monthly completed-bookings count use period boundaries in the… | merged into REQ-218 |
| P22-083 | U-F | Every booking that ends without a matched session record, and every session record on a booked… | merged into REQ-214 |
| P22-084 | U-F | A booking marked completed by ops or the attendant without a session record is not billed for… | parked REQ-282 |
| P22-085 | U-F | Each booking-to-session match stores its method (EVSE and time overlap, CDR reference, manual) and… | design detail → Step 3 |
| P22-086 | U-F | Each weekly payout comes with a statement listing every session and fee line it covers, and the… | parked REQ-287 |
| P22-087 | U-NF | Every invoice and payout is submitted to the payment provider with an idempotency key, so a retry… | REQ-244 |
| P22-088 | U-F | When a payout transfer fails, the amount stays owed in the ledger, finance is alerted, and it is… | parked REQ-288 |
| P22-089 | U-F | Finance can hold a station operator's payout with a reason code, and the held amount stays owed in… | parked REQ-289 |
| P22-090 | U-F | A station operator completes payment-provider onboarding (bank account, tax identity) through the… | parked REQ-290 |
| P22-091 | U-F | When a fleet invoice is still unpaid a set number of days after its due date, finance is alerted… | parked REQ-280 |
| P22-092 | U-F | When a fleet's unpaid balance exceeds its credit limit, the platform applies the fleet's… | parked REQ-281 |
| P22-093 | U-NF | A daily job reconciles the ledger's payment-provider clearing account with the provider's balance… | covered by constitution N9 |
| P22-094 | U-NF | A daily job checks that every ledger transaction balances and that account balances equal the sum… | covered by constitution N19 |
| P22-095 | U-F | The ledger gives, for any past date, the owed, paid and outstanding amounts per fleet and per… | merged into REQ-086 |
| P22-096 | U-NF | Money is stored in integer US cents and energy in watt-hours, with one documented rounding rule… | design detail → Step 3 |
| P22-097 | U-F | Every energy charge records the tariff version in force at the session start, and a tariff change… | parked REQ-284 |
| P22-098 | U-F | If station operators pay only for incremental off-peak sessions, each completed booking is… | parked REQ-276 |
| P22-099 | U-F | If a fleet's policy makes the driver pay the no-show fee, the driver is shown the fee amount and… | parked REQ-300 |
| P22-100 | U-F | A driver who owes a fee pays it on a payment-provider-hosted page opened from a message link, with… | parked REQ-299 |
| P22-101 | U-F | When a fee a driver already paid is reversed, the driver is refunded to the original payment… | parked REQ-301 |
| P22-102 | U-F | Under a "fleet pays and deducts" policy, the fleet invoice shows each no-show fee with the driver… | parked REQ-302 |
| P22-103 | U-F | When a reversed no-show fee carried a station-operator share, that share is reversed in the same… | parked REQ-303 |
| P22-104 | U-F | When a payer reverses a card or bank payment (chargeback or return), the ledger records the… | parked REQ-292 |
| P22-105 | U-F | If station operators are paid through the platform, each station operator's yearly payment total… | parked REQ-283 |
| P22-106 | U-F | Fleet subscription charges follow a documented rule for vehicles added or removed during the month. | parked REQ-293 |
| P22-107 | U-F | If Amperlane is merchant of record for energy, each fleet invoice shows the energy (kWh) and the… | parked REQ-285 |
| P22-108 | U-NF | A driver's message link opens only that driver's own bookings, works once, and expires after a set… | merged into REQ-240 |
| P22-109 | U-NF | When a booking link is opened on a device not seen before for that driver, the PWA asks for a… | merged into REQ-241 |
| P22-110 | U-NF | A command received by SMS or WhatsApp that changes a booking is accepted only from the registered… | REQ-242 |
| P22-111 | U-NF | The platform rejects, and logs, inbound messaging and CSMS webhooks whose signature or shared… | REQ-260 |
| P22-112 | U-NF | A fleet user sees and changes only that fleet's vehicles, drivers, bookings and invoices, and a… | merged into REQ-258 |
| P22-113 | U-NF | A station operator user sees only its own sites' capacity rules, bookings, faults and payouts, and… | merged into REQ-258 |
| P22-114 | U-NF | An attendant sees only the current day's bookings at their own site (window, plate, EVSE) and can… | merged into REQ-258 |
| P22-115 | U-NF | An attendant can sign in on a shared site device through a site-scoped login that ops can revoke… | REQ-261 |
| P22-116 | U-NF | Finance users can view the ledger, invoices, payouts and disputes and run payouts, but cannot… | merged into REQ-215 |
| P22-117 | U-NF | Ops users can view a driver's location evidence only within an open dispute for that booking. | REQ-259 |
| P22-118 | U-NF | No single user can both change a station operator's payout account details and approve a payout run. | parked REQ-291 |
| P22-119 | U-NF | Amperlane and Intellias engineers reach production data only through a named, time-limited… | merged into REQ-120 |
| P22-120 | U-NF | Ops, finance and engineering users sign in with multi-factor authentication. | covered by constitution N15 |
| P22-121 | U-F | Fleet and station portal users can sign in with a one-time link or code sent to their email or… | REQ-235 |
| P22-122 | U-NF | Portal sessions end after a set period of inactivity. | design detail → Step 3 |
| P22-123 | U-NF | Location from the phone or the vehicle is collected only after the driver opts in for that purpose… | merged into REQ-255 |
| P22-124 | U-F | A driver who has not opted in to location can complete every booking step, with arrival taken from… | REQ-204 |
| P22-125 | U-NF | Location readings are taken only between the pre-slot reminder and the end of grace of an active… | merged into REQ-255 |
| P22-126 | U-NF | Each consent grant and withdrawal is stored with its time, purpose, wording version and language. | merged into REQ-250 |
| P22-127 | U-F | Vehicle data is read only for vehicles whose fleet has recorded its authorisation as account… | merged into REQ-257 |
| P22-128 | U-NF | No application role can change or delete an audit record, and each record holds actor, action… | merged into REQ-126 |
| P22-129 | U-NF | The audit log also records changes to capacity rules, fleet policies, partner terms, payout… | REQ-262 |
| P22-130 | U-NF | Every view or export of a driver's personal data (phone number, location evidence) by an ops… | REQ-263 |
| P22-131 | U-NF | Logs, traces and error reports contain no driver phone numbers, names, location coordinates, link… | covered by constitution N21 |
| P22-132 | U-NF | Credentials for CSMS, payment, messaging and telematics APIs are kept in a secrets store, never in… | covered by constitution N14 |
| P22-133 | U-F | A driver can hold at most a set number of unconfirmed holds at a time. | design detail → Step 3 |
| P22-134 | U-NF | The platform limits booking attempts per number and per client address, without throttling the… | design detail → Step 3 |
| P22-135 | U-NF | A QR scan at an EVSE counts as arrival only when made from the booking's own link session during… | design detail → Step 3 |
| P22-136 | U-F | Ops can delete or anonymise one driver's personal data on request, keeping booking, audit and… | REQ-233 |
| P22-137 | U-NF | Every production change is merged through a pull request reviewed by someone other than its… | merged into REQ-122 |
| P22-138 | U-NF | Access to production systems and every portal role is reviewed at a set interval, and the access… | merged into REQ-120 |
| P22-139 | U-NF | The platform exports SOC 2 evidence on demand: user and role lists, change records, backup and… | parked REQ-320 |
| P22-140 | U-NF | Dependencies and container images are scanned for known vulnerabilities on every build, and a… | covered by constitution N16 |
| P22-141 | U-NF | A register of every vendor that receives platform data (AWS, Stripe, Twilio, maps, telematics… | REQ-264 |
| P22-142 | S-NF | An external penetration test of the platform is completed, and its critical and high findings are… | parked REQ-319 |
| P22-143 | U-NF | Within a set time of a suspected breach, the platform can list the affected individuals and the… | merged into REQ-254 |
| P22-144 | U-NF | The platform does not store drivers' licence numbers, TLC licence numbers or bank account numbers… | REQ-265 |
| P22-145 | U-NF | Card details are entered only on payment-provider-hosted pages or fields, so card numbers never… | REQ-246 |
| P22-146 | S-NF | Money owed to station operators never sits in an Amperlane-owned bank account, so Amperlane does… | parked REQ-279 |
| P22-147 | S-F | For a site flagged as NEVI-funded, the platform rejects capacity rules that exceed the bookable… | merged into REQ-006 |
| P22-148 | U-NF | Drivers get SMS or WhatsApp messages only after their number is registered with their agreement to… | REQ-248 |
| P22-149 | U-NF | Every WhatsApp message that the platform starts outside a 24-hour window opened by the driver uses… | REQ-249 |
| P22-150 | U-NF | Load tests and capacity plans use the June 2027 target volume (10,000 completed bookings a month… | merged into REQ-132 |
| P22-151 | U-NF | During the shift-change burst, confirmations and alternatives reach drivers within a set time at… | covered by constitution N11 |
| P22-152 | U-NF | Automatic rebooking after a fault completes for all affected bookings within a set time, including… | design detail → Step 3 |
| P22-153 | U-NF | Status ingestion keeps every live EVSE within the 60-second freshness target when all EVSEs at a… | merged into REQ-130 |
| P22-154 | U-NF | Fleet-portal and station-portal reports and exports do not raise booking API latency above 300 ms… | merged into REQ-130 |
| P22-155 | U-NF | The ops console stays usable during the shift-change burst, with page loads within a set time at… | design detail → Step 3 |
| P22-156 | U-NF | Adding a metro (e.g. LA) needs only configuration and partner connections, with no change to the… | merged into REQ-138 |
| P22-157 | U-NF | Discovery data from NLR AFDC is fetched in bulk and cached, so driver traffic never takes the… | design detail → Step 3 |
| P22-158 | U-NF | Vehicle SoC is fetched only for vehicles with an upcoming booking, not streamed for the whole… | parked REQ-311 |
| P22-159 | S-NF | Each data type has a retention period, and records past it are deleted or anonymised… | merged into REQ-125 |
| P22-160 | U-NF | A raw location reading is deleted as soon as its arrival event is derived, and no location trace… | merged into REQ-256 |
| P22-161 | U-NF | EVSE status history, station-hold attempts and arrival evidence are kept at least until the… | merged into REQ-125 |
| P22-162 | U-NF | Ledger entries, invoices, payout records and the audit log are kept for the period counsel sets… | merged into REQ-233 |
| P22-163 | U-NF | The backup retention period is documented, so it is known when deleted personal data has also left… | design detail → Step 3 |
| P22-164 | U-NF | The pilot migration can be re-run from the raw export into an empty target, and each run produces… | merged into REQ-116 |
| P22-165 | U-NF | Every migrated booking whose status was re-classified records the rule applied and the evidence… | merged into REQ-228 |
| P22-166 | U-NF | Where Airtable and a site's slot-grid sheet disagree about a booking, the migration applies one… | merged into REQ-229 |
| P22-167 | U-F | Pilot records from before February 2026 are migrated with a data-quality flag, so reports can… | merged into REQ-230 |
| P22-168 | U-F | Migrated pilot drivers are linked, by mobile number, to the driver records the platform uses after… | merged into REQ-115 |
| P22-169 | U-F | At cut-over, every pilot booking for a slot after the cut-over moment exists in the platform with… | REQ-231 |
| P22-170 | U-F | Bookings completed before the cut-over are invoiced by the pilot process and bookings after it by… | REQ-232 |
| P22-171 | U-F | Migrated pilot bookings are marked as pilot data in every report, and every metric can be shown… | merged into REQ-225 |
| P22-172 | U-F | The platform produces a monthly series from October 2025 onwards of bookings, completed bookings… | merged into REQ-095 |
| P22-173 | U-NF | Data-room exports contain no driver names or phone numbers, and drivers appear only as stable… | merged into REQ-118 |
| P22-174 | U-F | Every figure in the data-room report can be traced to the list of booking ids it counts. | merged into REQ-095 |
| P22-175 | U-F | The completed-booking count can be recomputed from stored evidence under alternative definitions… | merged into REQ-224 |
| P22-176 | U-NF | Amperlane's engineers can export all platform data in open formats (database dump, CSV per entity)… | REQ-267 |
| P22-177 | U-NF | All production data and backups stay in AWS US regions inside Amperlane's accounts. | merged into REQ-119 |
| P22-178 | U-NF | Database schema changes are applied by versioned migrations that do not take booking offline… | merged into REQ-129 |
| P22-179 | U-F | When a fleet or station operator leaves the platform, its users are disabled, its future bookings… | REQ-234 |
| P22-180 | U-NF | The raw pilot export is stored read-only, accessible only to named people, and deleted at the end… | merged into REQ-252 |
| P22-181 | U-NF | Booking availability inside the 5 AM–1 AM ET window and booking API p95 latency are measured… | covered by constitution N4 |
| P22-182 | U-NF | Per site, the platform measures the age of the latest EVSE status and reports the share of time it… | covered by constitution N1 |
| P22-183 | U-NF | A synthetic probe makes and cancels a booking on a test site in production at a set interval… | covered by constitution N4 |
| P22-184 | U-NF | For each external system (each CSMS, Twilio, Stripe, telematics, maps), the platform shows error… | covered by constitution N21 |
| P22-185 | U-NF | The platform alerts when a booking timer fires more than a set time after its scheduled time… | covered by constitution N21 |
| P22-186 | U-NF | For every fault, the platform measures the time from the CSMS fault status to the affected drivers… | design detail → Step 3 |
| P22-187 | U-NF | Every log line, trace span, workflow step, external call and message linked to a booking carries… | covered by constitution N21 |
| P22-188 | U-NF | Technical alerts go to an on-call rota with an escalation path, and each alert links to its runbook. | converted to Q-039 |
| P22-189 | U-NF | Delivery rate and delivery time of outbound messages are measured per channel (SMS, WhatsApp) and… | covered by constitution N11 |
| P22-190 | U-F | The platform reports, per site and day: booking attempts, holds expired, confirmations… | REQ-226 |
| P22-191 | U-F | The platform reports the median wait from arrival to session start from measured events, replacing… | merged into REQ-093 |
| P22-192 | U-F | The platform reports, per site and time window, the share of EVSE time used by Amperlane bookings… | merged into REQ-094 |
| P22-193 | U-F | The platform reports ops workload: exceptions per day by type, time to pick up, and manual ops… | REQ-227 |
| P22-194 | U-NF | Cloud and usage-priced vendor costs (messaging, maps, telematics, payments) are reported monthly… | REQ-251 |
| P22-195 | U-NF | Security-relevant logs (sign-ins, role changes, admin actions, personal-data access) are kept for… | design detail → Step 3 |
| P22-196 | U-NF | The driver PWA conforms to the WCAG version and level agreed with the client, verified by an… | covered by constitution N24 |
| P22-197 | U-NF | The fleet portal and the station portal conform to the agreed WCAG version and level. | covered by constitution N24 |
| P22-198 | U-NF | The ops console and the attendant view conform to the agreed WCAG version and level. | covered by constitution N24 |
| P22-199 | U-NF | The attendant view's text and controls meet an enhanced contrast ratio and a minimum touch-target… | design detail → Step 3 |
| P22-200 | U-NF | Confirm, cancel, running late and accept-alternative are each one tap from the message link, with… | covered by constitution N23 |
| P22-201 | U-F | Keyword replies (cancel, late, yes or no to an alternative, help) are understood in English… | merged into REQ-220 |
| P22-202 | U-F | Each driver has a preferred language, set by the fleet, by ops, or by the driver with a language… | merged into REQ-199 |
| P22-203 | U-NF | Spanish and Bengali message templates are written for Unicode SMS segments (70 characters), so… | design detail → Step 3 |
| P22-204 | U-NF | Every Spanish and Bengali driver-facing text is reviewed by a native-speaking member of… | covered by constitution N22 |
| P22-205 | U-NF | Consent texts and fee notices exist in English, Spanish and Bengali, and the platform stores which… | REQ-250 |
| P22-206 | U-NF | Each driver message states the site, the time and the action needed within its first line. | design detail → Step 3 |
| P22-207 | U-NF | The driver PWA's booking page loads within a set time on a slow mobile connection and stays under… | covered by constitution N24 |
| P22-208 | U-NF | The driver PWA works in the browsers of drivers' own phones, across a set range of iOS and Android… | covered by constitution N24 |
| P22-209 | U-F | Inbound driver messages the platform cannot understand, in any language, go to ops with the… | REQ-222 |
| P22-210 | U-F | Where a site marks an EVSE as accessible (e.g. a wider access aisle), the platform can keep it for… | converted to Q-050 |
