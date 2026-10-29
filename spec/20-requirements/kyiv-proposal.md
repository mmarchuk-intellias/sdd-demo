---
id: KYIV-PROPOSAL
type: kyiv-proposal
title: KYIV proposal for Gate 5 (P5.1) and the capacity check (P6)
status: draft
owner: Mykola Marchuk
version: 1
kyiv: null
parents: [REQUIREMENTS, TASKS]
sources: [SRC-C1@00:29:06, SRC-C1@00:31:02, SRC-D2#15, SRC-D2#16, SRC-R1#open]
---
# KYIV proposal for Gate 5

An agent proposal (constitution P4): it suggests values and gives a reason for each, and changes nothing. The final KYIV
is set at Gate 5 by Amperlane's product owner and the Intellias engagement lead (P1); until then requirements.md keeps
its provisional values.

## 1. Summary

- **Active requirements:** 331. Provisional (Gate 2): K 100 · Y 141 · I 28 · V 62. Proposed: K 152 · Y 89 · I 28 · V 62.
- **Only change proposed: 52 requirements Y → K** (section 2), because K work cannot be built without them. No K is proposed lower, and I and V stay as they are (section 4).
- **K tasks:** 243 → 335 of 378 (89%). K stories 64 → 103, K system stories 119 → 171.
- **Capacity (P6): K does not fit the indicative team in the build window** unless the average K task takes well under a day (section 3). KYIV changes cannot close that gap, because the K work is one connected graph.
- **Decisions for Gate 5** are in section 5.

## 2. Proposed changes: Y → K

The provisional K of Gate 2 is not closed under the task graph: 49 Y tasks are prerequisites of K tasks (tasks.md,
"Step 5 agenda"). A task cannot rank above its system story (P3), so the requirement behind the prerequisite has to
rise. Raising it pulls its other stories, system stories and tasks into K by inheritance (P2), and some of those depend
on further Y tasks, so the closure took three rounds. Round 0 is REQ-266, put on this agenda at Gate 3.

One exception is proposed instead of a raise. T-710 routes an undelivered WhatsApp message to the SMS resend and
"applies only where the WhatsApp channel is enabled"; it is K only because its system story SS-307 is K. Raising
WhatsApp (REQ-062, REQ-249) to K for it would be a scope decision with an unknown sender set-up (Q-034). The proposal is
a human override on T-710 (`kyiv: Y` with a `kyiv_override_reason`), which only a human writes (P4).

Reasons name the prerequisite tasks, the K tasks that need them and the K requirements those K tasks serve.

| REQ | Quadrant | Requirement | Round | Reason |
|---|---|---|---|---|
| REQ-266 | U-NF | Ops can get the next bookings per site from a copy kept outside the primary system and refreshed at a set … | 0 | SS-436 is K since Gate 3 (US-406 parent): the K cut-over check needs the outage copy (SS-422 clause 6). |
| REQ-037 | S-F | A driver who arrives after the booking's grace period, including any ops extension, keeps the booking … | 1 | T-333 needed by K work: T-546 (REQ-224). |
| REQ-038 | S-F | When a driver records arrival after the booking was released as a no-show, the driver gets, within a set … | 1 | T-333 needed by K work: T-546 (REQ-224). |
| REQ-040 | S-F | A driver reports 'running late' with one tap on the page opened from any message about that booking, or on … | 1 | T-334, T-352 needed by K work: T-734, T-768 (REQ-039, REQ-236, REQ-046). |
| REQ-042 | S-F | Ops can extend the grace period of a single booking with a reason code, up to a maximum set per site. | 1 | T-352 needed by K work: T-734, T-768 (REQ-039, REQ-236, REQ-040). |
| REQ-045 | S-F | A fleet or a driver can raise a dispute on a no-show within the dispute window (A-047), and ops records a … | 1 | T-729 needed by K work: T-531 (REQ-058, REQ-097). |
| REQ-046 | S-F | A driver can report that the allocated stall was blocked on arrival, and the report is stored with its time … | 1 | T-338 needed by K work: T-768 (REQ-039, REQ-236, REQ-040). |
| REQ-056 | S-F | Ops can confirm a held or unconfirmed booking with a reason code, under the same capacity and no-overlap … | 1 | T-144 needed by K work: T-310, T-321, T-532 (REQ-035, REQ-052, REQ-058). |
| REQ-057 | S-F | Ops can release a booking with a reason code, with the same effect on capacity, station hold and driver … | 1 | T-144 needed by K work: T-310, T-321, T-532 (REQ-035, REQ-052, REQ-058). |
| REQ-072 | S-F | A fleet sets whether its vehicles may use adapters, and the setting can be overridden per vehicle. | 1 | T-184 needed by K work: T-130, T-186, T-205 (REQ-013, REQ-015). |
| REQ-091 | S-F | The platform reports completed bookings per month for NYC sites, using the definition configured under … | 1 | T-549 needed by K work: T-931 (REQ-128). |
| REQ-096 | S-F | The pilot history since October 2025 (bookings, no-shows, arrival times, drivers and stalls) is migrated into … | 1 | T-983, T-984, T-1009 needed by K work: T-933, T-990 (REQ-132, REQ-231, REQ-116). |
| REQ-105 | S-NF | No CSMS vendor SDK is used inside the booking core, so moving a site to another CSMS changes only its … | 1 | T-500 needed by K work: T-317, T-318, T-321, T-324 and 6 more (REQ-020, REQ-023, REQ-024). |
| REQ-111 | S-NF | The payment provider sits behind an interface, so it can be replaced without changing the booking core. | 1 | T-955 needed by K work: T-958, T-961, T-1007 (REQ-083, REQ-084, REQ-087). |
| REQ-115 | S-NF | Migrated pilot history lives in the platform's own data model, linked to the same driver, fleet, site and … | 1 | T-983, T-984, T-1009 needed by K work: T-933, T-990 (REQ-132, REQ-231, REQ-116). |
| REQ-118 | S-NF | Pilot or platform data shared outside Amperlane or used outside production has driver names and phone numbers … | 1 | T-795 needed by K work: T-933 (REQ-132). |
| REQ-125 | S-NF | Personal data is kept only as long as disputes, finance and the retention period counsel sets for its data … | 1 | T-790 needed by K work: T-793 (REQ-254). |
| REQ-134 | S-NF | The workflow engine is self-hosted in Amperlane's AWS account. | 1 | T-165 needed by K work: T-503, T-506, T-520, T-521 (REQ-024, REQ-031, REQ-104). |
| REQ-138 | S-NF | A test site in a time zone other than Eastern is configured, booked, allocated and released end to end with … | 1 | T-108 needed by K work: T-501, T-505, T-519, T-523 (REQ-031, REQ-032, REQ-104). |
| REQ-139 | S-NF | Every booking function that the driver PWA, portals and ops console use is available through a versioned, … | 1 | T-911, T-912 needed by K work: T-102, T-104, T-106, T-107 and 47 more (REQ-001, REQ-002, REQ-004). |
| REQ-146 | U-F | Per-site parameters (time grid, durations, buffer, hold time, allocation and pre-arrival offsets, reminder … | 1 | T-782 needed by K work: T-105, T-548, T-733 (REQ-112, REQ-199, REQ-224). |
| REQ-156 | U-F | When site staff have not acknowledged a station-hold request by the pre-arrival check, ops gets an exception … | 1 | T-325 needed by K work: T-530 (REQ-058, REQ-097). |
| REQ-161 | U-F | Every booking for which the operator provides a session record is matched to it within a set time of the … | 1 | T-966 needed by K work: T-546 (REQ-224). |
| REQ-165 | U-F | Ops onboards a new site in the ops console (operator, address, time zone, supply pattern, EVSEs, connectors, … | 1 | T-108 needed by K work: T-501, T-505, T-519, T-523 (REQ-031, REQ-032, REQ-104). |
| REQ-174 | U-F | The platform records arrival from a CSMS session-start event on the booking's allocated EVSE between a set … | 1 | T-525 needed by K work: T-329 (REQ-204). |
| REQ-184 | U-F | Ops can place a maintenance hold that removes EVSEs or capacity at a site from booking for a time window. | 1 | T-145 needed by K work: T-301 (REQ-013, REQ-020). |
| REQ-190 | U-F | The ops console shows one live board per site for the current day with bookings by state, EVSE status with … | 1 | T-528 needed by K work: T-347, T-931 (REQ-128). |
| REQ-191 | U-F | A driver can report a faulted EVSE in one tap from the booking page or by message, which creates an ops alert … | 1 | T-517 needed by K work: T-734, T-768 (REQ-039, REQ-236, REQ-040). |
| REQ-197 | U-F | Ops can send a templated or free-text message to a driver on the driver's channel from the ops console, … | 1 | T-729 needed by K work: T-531 (REQ-058, REQ-097). |
| REQ-225 | U-F | Migrated pilot data is marked as pilot data in every report, reported under the same status definitions as … | 1 | T-549 needed by K work: T-931 (REQ-128). |
| REQ-229 | U-F | Where a site's pilot Google Sheet and Airtable disagree, the migration applies one documented precedence rule … | 1 | T-979 needed by K work: T-987 (REQ-231). |
| REQ-233 | U-F | Ops can anonymise one driver's personal data on request, keeping booking, audit and ledger records with the … | 1 | T-791 needed by K work: T-792 (REQ-254). |
| REQ-250 | U-NF | Consent texts, fee notices and their language versions exist in English, Spanish and Bengali, and the … | 1 | T-732 needed by K work: T-799 (REQ-255). |
| REQ-262 | U-NF | The audit trail also records changes to capacity rules, fleet policies, partner terms, user roles and … | 1 | T-782 needed by K work: T-105, T-548, T-733 (REQ-112, REQ-199, REQ-224). |
| REQ-263 | U-NF | Every view or export of a driver's personal data by an ops, finance, fleet, station-operator or site-staff … | 1 | T-785, T-791 needed by K work: T-792 (REQ-254). |
| REQ-269 | U-NF | For a set period before 1 March 2027 the platform runs real bookings with real drivers at all three pilot … | 1 | T-991, T-992 needed by K work: T-794, T-994 (REQ-097, REQ-142, REQ-254). |
| REQ-334 | U-F | A 'running late' report by itself never waives the no-show fee of a driver who then does not arrive within … | 1 | T-334, T-352 needed by K work: T-734, T-768 (REQ-039, REQ-236, REQ-040). |
| REQ-051 | S-F | When a fault or a maintenance hold changes bookings at a site, the station operator gets a notice within a … | 2 | T-543 needed by K work: T-558 (REQ-125, REQ-233). |
| REQ-079 | S-F | A station operator sees the upcoming bookings at its sites and the EVSE each one is allocated to. | 2 | T-542 needed by K work: T-558 (REQ-125, REQ-233). |
| REQ-092 | S-F | The platform reports per month, per fleet and per site the no-shows and the late arrivals, each as a share of … | 2 | T-550 needed by K work: T-551 (REQ-225). |
| REQ-116 | S-NF | A re-runnable pilot migration loads every source booking record or lists it as rejected with a reason, and … | 2 | T-977, T-981 needed by K work: T-549, T-978, T-979 (REQ-091, REQ-096, REQ-115). |
| REQ-140 | S-NF | A simulated site lets engineers make chargers fault, overrun and report late drivers on demand. | 2 | T-921, T-1004, T-1005 needed by K work: T-527, T-555 (REQ-105). |
| REQ-179 | U-F | For a disputed no-show, ops sees on one screen the booking's ordered history: states, actors, reason codes, … | 2 | T-342 needed by K work: T-349 (REQ-045, REQ-259). |
| REQ-186 | U-F | When a station operator lowers a capacity rule, or ops adds a fleet-priority hold, below the confirmed … | 2 | T-147 needed by K work: T-203 (REQ-184, REQ-335). |
| REQ-194 | U-F | After a fault, an EVSE returns to the pool only after it has reported available for a set time or ops returns … | 2 | T-514 needed by K work: T-528 (REQ-190). |
| REQ-228 | U-F | Migrated statuses are re-classified so that moved, no-show and cancelled are distinct outcomes, and each … | 2 | T-981, T-982 needed by K work: T-549, T-984, T-1011 (REQ-091, REQ-096, REQ-115). |
| REQ-230 | U-F | Migrated records from before February 2026 carry a data-quality flag. | 2 | T-981, T-982 needed by K work: T-549, T-984, T-1011 (REQ-091, REQ-096, REQ-115). |
| REQ-237 | U-NF | Staging runs every integration against a sandbox or simulator and never against production chargers, real … | 2 | T-921, T-1004, T-1005 needed by K work: T-527, T-555 (REQ-105). |
| REQ-259 | U-NF | Ops users can view a driver's location evidence only within an open dispute for that booking. | 2 | T-342 needed by K work: T-349 (REQ-045, REQ-179). |
| REQ-260 | U-NF | The platform rejects and logs inbound messaging and CSMS webhooks whose signature or shared secret does not … | 2 | T-526 needed by K work: T-555 (REQ-105). |
| REQ-335 | U-F | Ops can place a fleet-priority hold that keeps capacity at a site for a time window for one named fleet's … | 2 | T-146 needed by K work: T-203 (REQ-184, REQ-186). |
| REQ-252 | U-NF | The raw pilot export is stored read-only, accessible only to named people, and deleted at the end of the … | 3 | T-985 needed by K work: T-977 (REQ-116). |

## 3. Capacity check (P6)

P6 asks that the K estimates add up to at most 80% of the committed capacity (A-045). The tasks have no estimates
yet: the estimation workbook v1 and the staffing check are with Mark Feldman, due 2026-10-30 (SRC-R1#open, Q-072). Until
then this is a range check, not an estimate.

- **Window:** the MVP build runs 30 November 2026 – 26 February 2027 (SRC-D2#15): 65 weekdays, 61 without the four US
  federal holidays, 56 if the week of 24 December – 1 January is also off ("with slack for the holidays").
- **Team:** the indicative Phase 1 shape (SRC-D2#16) has 3–4 full-stack engineers, 1 integration engineer and 0.5 DevOps,
  so 4.5–5.5 people who build tasks. QA automation, design, the payments specialist, the engagement lead and the solution
  architect are not counted; Amperlane's embedded engineer is not counted either.
- **Task size:** each task is one PR of up to about 2 days (Gate 4).

| Builders | Working days | Capacity, person-days | 80% (A-045) | Average K task that fits: 243 tasks | 335 tasks |
|---|---|---|---|---|---|
| 4.5 (3 full-stack) | 61 (federal holidays out) | 274 | 220 | 0.90 days | 0.66 days |
| 4.5 (3 full-stack) | 56 (also 24 Dec – 1 Jan out) | 252 | 202 | 0.83 days | 0.60 days |
| 5.5 (4 full-stack) | 61 (federal holidays out) | 336 | 268 | 1.10 days | 0.80 days |
| 5.5 (4 full-stack) | 56 (also 24 Dec – 1 Jan out) | 308 | 246 | 1.01 days | 0.74 days |

**Reading.** With the closed K of 335 tasks, K fits the indicative team only if the average K task takes
0.6–0.8 days. At an average of 1 day, K needs
about 419 person-days of capacity, which is 6.9–7.5 builders over the window; at
1.5 days, 628 person-days and 10.3–11.2 builders. The indicative team has 4.5–5.5.

**KYIV changes do not close the gap.** Two tests on the task graph:
- Only three features can go from K to Y without leaving a K task that depends on them: FT-06.4, FT-10.1 and FT-14.5,
  which together save 4 K tasks. Every other feature has K work in other features depending on it.
- The K requirements whose sources give a due date after 1 March (fleet invoices at the first month close, 10,000
  completed bookings a month by June 2027, the retention purge inside the counsel's periods) free only 2 tasks, T-934 and
  T-971, because their tasks also serve requirements needed from day one.

**Levers for the engagement lead (P6: raise scope or date with the client before the proposal).** The date is fixed
(SRC-C1@00:29:06), so:
1. **Team.** Size the build team to the closed K once the workbook gives the estimates. This depends on the budget
   (Q-025, CF-013); above $1.2M needs "a very good reason" (SRC-C1@00:31:02).
2. **Launch scope at capability level.** For example fewer supply patterns or sites on 1 March, or a channel or portal
   later. Each option needs a client decision, a CR and re-planning of the task graph, not a KYIV change.
3. **Timing.** Start platform foundations (repositories, environments, the API and front-end skeletons) in Phase 0,
   9–27 November (SRC-D2#15), if the staffing check allows it.

## 4. Confirmed without change

- **K (100), the Y not listed in section 2 (89) and I (28):** the provisional values and their Gate 2
  reasons stand. Since Gate 2 the changes (CR-001 – CR-010) changed meaning, not priority, and no new source arrived.
- **V (62), the parking lot:** "not this release, visible and agreed" (constitution, KYIV rules). The client has
  not agreed it yet; the product owner should see it at Gate 5.

| Parking lot | Requirements | Count |
|---|---|---|
| business-model options (Q-001) | REQ-270, REQ-271, REQ-272, REQ-273, REQ-274, REQ-275, REQ-276, REQ-277, REQ-278, REQ-279, REQ-280, REQ-281, REQ-282, REQ-283, REQ-284, REQ-285, REQ-286, REQ-287, REQ-288, REQ-289, REQ-290, REQ-291, REQ-292, REQ-293, REQ-294, REQ-295, REQ-296, REQ-297 | 28 |
| no-show fee options (Q-002, Q-003) | REQ-298, REQ-299, REQ-300, REQ-301, REQ-302, REQ-303, REQ-304 | 7 |
| grace extension options (CF-021) | REQ-305, REQ-306, REQ-307 | 3 |
| integration scope options (Q-036, CF-025, CF-004, Q-010, A-026, A-029) | REQ-308, REQ-309, REQ-310, REQ-311, REQ-312, REQ-313, REQ-314, REQ-315 | 8 |
| operations, SOC 2 date and budget options (Q-023, Q-018, Q-025) | REQ-316, REQ-317, REQ-318, REQ-319, REQ-320 | 5 |
| deferred by the client | REQ-321, REQ-322, REQ-323, REQ-324, REQ-325, REQ-326, REQ-327, REQ-328 | 8 |
| out of MVP scope (Intellias proposal) | REQ-329, REQ-330, REQ-331 | 3 |

## 5. Decisions for Gate 5

1. **Engagement lead:** accept the Y → K changes of section 2 and the override on T-710, or name the ones to treat
   differently. Accepted changes enter requirements.md through a CR; the stories, system stories and tasks they affect
   copy the inherited value (P2).
2. **Engagement lead with Mark Feldman:** which capacity lever, or which mix, goes into the 6 November proposal
   (section 3), once the workbook estimates are in (Q-072).
3. **Amperlane's product owner with the engagement lead:** the final KYIV, and agreement on the parking lot (V).

**Recorded on 2026-10-29 (Mykola Marchuk):**
- Decision 1: accepted as proposed. requirements.md v4 carries the 52 changes as provisional K (CR-011); the stories,
  system stories and tasks copy the inherited value. The T-710 override is a human edit in tasks.yaml.
- Decision 2: waits for the estimation workbook (Q-072); the estimates go into the `estimate` field in tasks.yaml, and
  section 3 is then redone with them.
- Decision 3: open, for the client.

## 6. All requirements (P5.1)

| REQ | Quadrant | Provisional | Proposed | Reason |
|---|---|---|---|---|
| REQ-001 | S-F | K | K | Core promise 'see open slots, book in two taps' (CTX-002); no launch on 2027-03-01 without it (CTX-079). |
| REQ-002 | S-F | K | K | Booking is the product (CTX-002); launch date 2027-03-01 (CTX-079). |
| REQ-003 | S-F | K | K | Agreed booking model (CTX-092); every supply pattern depends on it (CTX-063). |
| REQ-004 | S-F | K | K | Stations' condition for joining (CTX-064); capacity commitment is a partner-agreement term (CTX-069). |
| REQ-005 | S-F | K | K | Every launch site has peak caps of 30–50% (CTX-064). |
| REQ-006 | S-F | I | I | None of the three launch sites is NEVI-funded; prospects are mostly outside NYC (CTX-017); the limit is undefined (Q-040). |
| REQ-007 | S-F | K | K | 'No double booking, ever' (CTX-093); a broken promise to drivers and stations. |
| REQ-008 | S-F | Y | Y | Agreed burst behaviour (CTX-093); booking still works without it. |
| REQ-009 | S-F | K | K | Cab day drivers book for night drivers (CTX-029); Five Boroughs is a launch fleet (CTX-139). |
| REQ-010 | S-F | Y | Y | Long-term cab drivers do this today (CTX-029); depends on overnight bookings (A-028, CF-015). |
| REQ-011 | S-F | Y | Y | Brief step 2 (SRC-D1#6); at launch drivers book themselves and ops books for small fleets (CTX-030). |
| REQ-012 | S-F | K | K | Connector and power matching need it (CTX-100). |
| REQ-013 | S-F | K | K | Connector mismatches happen in the pilot (CTX-049); a mismatch is a failed charge. |
| REQ-014 | S-F | K | K | Prerequisite for connector matching (CTX-100). |
| REQ-015 | S-F | K | K | Prerequisite for connector matching (CTX-100). |
| REQ-016 | S-F | Y | Y | CTO asked for it ('Put it in', CTX-100); bookings work without it. |
| REQ-017 | S-F | I | I | Needs SoC, and Geotab access is unconfirmed (Q-014); drivers can choose a duration without it. |
| REQ-018 | S-F | Y | Y | Agreed MVP vehicle-data cut 'Geotab plus manual SoC' (CTX-099). |
| REQ-019 | S-F | K | K | Five Boroughs has no telematics and is a launch fleet (CTX-074, CTX-139). |
| REQ-020 | S-F | K | K | Station red line ('Never', CTX-066). |
| REQ-021 | S-F | K | K | Overstays are some days worse than no-shows (CTX-050); 'stall is held for you' (SRC-D1#5). |
| REQ-022 | S-F | K | K | Stated fallback 'ops gets pinged' (CTX-066); happens at JFK, a launch site. |
| REQ-023 | S-F | K | K | Agreed foundation (CTX-088, CF-002). |
| REQ-024 | S-F | K | K | Pattern A at Gowanus, a launch site (CTX-060). |
| REQ-025 | S-F | K | K | Six Gowanus chargers reject reservations until their firmware is fixed (CTX-060, CTX-072). |
| REQ-026 | S-F | K | K | JFK and LIC are launch sites without charger reservations (CTX-061, CTX-062). |
| REQ-027 | S-F | K | K | JFK is a launch site; 'Kinship stops calling me about cones' (CTX-139). |
| REQ-028 | S-F | Y | Y | All three patterns are launch sites (CTX-063). Gate 2: set to Y (provisional). |
| REQ-029 | S-F | Y | Y | Agreed scope limit (CTX-090); stops an undeliverable 'all chargers live' promise. |
| REQ-030 | S-F | I | I | Convenience for drivers far from partner sites; not needed for the launch goal (CTX-079). |
| REQ-031 | S-F | K | K | Gowanus is a launch site (CTX-079, A-022). |
| REQ-032 | S-F | K | K | JFK is a launch site (CTX-079, A-022). |
| REQ-033 | S-F | K | K | 'Has to. Automatically.' (CTX-131); stations' first condition (CTX-067). |
| REQ-034 | S-F | K | K | Station term from the partner agreement (CTX-067, CTX-069). |
| REQ-035 | S-F | K | K | 'Cone comes off, walk-up gets it' (CTX-067); 'Kinship stops calling me about cones' (CTX-139). |
| REQ-036 | S-F | K | K | Stations require it (CTX-067); the payer is open (Q-002) but the line exists in every option. |
| REQ-037 | S-F | Y | K | Raised: T-333 needed by K work: T-546 (REQ-224). |
| REQ-038 | S-F | Y | K | Raised: T-333 needed by K work: T-546 (REQ-224). |
| REQ-039 | S-F | K | K | Main lever against 17% no-shows, which block the 10k target (CTX-135, CTX-138). |
| REQ-040 | S-F | Y | K | Raised: T-334, T-352 needed by K work: T-734, T-768 (REQ-039, REQ-236, REQ-046). |
| REQ-041 | S-F | Y | Y | Exists in the pilot (CTX-041); one-tap cancel is the main path. |
| REQ-042 | S-F | Y | K | Raised: T-352 needed by K work: T-734, T-768 (REQ-039, REQ-236, REQ-040). |
| REQ-043 | S-F | K | K | Default arrival evidence while location is off by default (A-024); prevents wrongful auto-release. |
| REQ-044 | S-F | K | K | QR arrival is needed at all three launch sites (CTX-102). |
| REQ-045 | S-F | Y | K | Raised: T-729 needed by K work: T-531 (REQ-058, REQ-097). |
| REQ-046 | S-F | Y | K | Raised: T-338 needed by K work: T-768 (REQ-039, REQ-236, REQ-040). |
| REQ-047 | S-F | K | K | The Gowanus fault went unnoticed for 25 minutes (CTX-047); launch success 'nobody picks up the phone' (CTX-139). |
| REQ-048 | S-F | Y | Y | A charger-down day costs two ops people an afternoon (CTX-047); launch success (CTX-139). Gate 2: set to Y (provisional). |
| REQ-049 | S-F | Y | Y | A cab driver was lost in the Gowanus fault (CTX-047). Gate 2: set to Y (provisional). |
| REQ-050 | S-F | K | K | Ops is the safety net for unplaced bookings (CTX-035). |
| REQ-051 | S-F | Y | K | Raised: T-543 needed by K work: T-558 (REQ-125, REQ-233). |
| REQ-052 | S-F | K | K | False no-shows distort the north-star metric and fees (CTX-138, CF-018). |
| REQ-053 | S-F | K | K | Basis for disputes, SOC 2 and SHIELD evidence (CTX-110). |
| REQ-054 | S-F | Y | Y | Automatic rebooking is K (CTX-136); the one-action manual path is the fallback. |
| REQ-055 | S-F | K | K | Small fleets and phone-in drivers depend on ops (CTX-030, CTX-035). |
| REQ-056 | S-F | Y | K | Raised: T-144 needed by K work: T-310, T-321, T-532 (REQ-035, REQ-052, REQ-058). |
| REQ-057 | S-F | Y | K | Raised: T-144 needed by K work: T-310, T-321, T-532 (REQ-035, REQ-052, REQ-058). |
| REQ-058 | S-F | K | K | Launch success 'Nobody opens Airtable' (CTX-139); no spreadsheets in the critical path (CTX-079). |
| REQ-059 | S-F | K | K | Agreed channel (CF-001); drivers refuse app installs (CTX-027). |
| REQ-060 | S-F | K | K | Otherwise 'he's gone' (CTX-027). |
| REQ-061 | S-F | Y | Y | Drivers book by text today ('He'll text', CTX-027). Gate 2: set to Y (provisional). |
| REQ-062 | S-F | Y | Y | Half the drivers asked for it (CTX-027); not used in the pilot, sender set-up unknown (Q-034). |
| REQ-063 | S-F | K | K | 'He'll tap a link' (CTX-027); one-tap cancel depends on it (CTX-135). |
| REQ-064 | S-F | Y | Y | Brief names directions (SRC-D1#9); deep links agreed (CTX-098). |
| REQ-065 | S-F | I | I | Brief lists ETA (SRC-D1#9) with no stated use; booking works without it. |
| REQ-066 | S-F | Y | Y | Agreed deep-link scope (CTX-098). |
| REQ-067 | S-F | K | K | Brief step 3 (CTX-002); fewer no-shows means more completions (CTX-138). |
| REQ-069 | S-F | K | K | Fleet portal is in the client's scope (CTX-004). |
| REQ-070 | S-F | Y | Y | Connector matching needs vehicle profiles (CTX-100). Gate 2: set to Y (provisional). |
| REQ-071 | S-F | Y | Y | Brief 'reporting for every EV in the fleet' (SRC-D1#8); content not specified. |
| REQ-072 | S-F | Y | K | Raised: T-184 needed by K work: T-130, T-186, T-205 (REQ-013, REQ-015). |
| REQ-073 | S-F | Y | Y | Borough Green sees no-shows only because Amperlane shows them (CTX-140). |
| REQ-074 | S-F | Y | Y | Five Boroughs' definition of success (CTX-140). |
| REQ-075 | S-F | I | I | Agreed MVP telematics (CTX-099) but access is unconfirmed (Q-014); manual SoC covers the gap. |
| REQ-076 | S-F | Y | Y | Brief 'schedules' (SRC-D1#11); ops can set them at launch. |
| REQ-077 | S-F | Y | Y | Stations want it (CTX-065), but ops can change caps on request at launch. |
| REQ-078 | S-F | I | I | How tariffs are used depends on the undecided model (Q-001). |
| REQ-079 | S-F | Y | K | Raised: T-542 needed by K work: T-558 (REQ-125, REQ-233). |
| REQ-080 | S-F | Y | Y | Leverage with the stations' maintenance teams (CTX-037). |
| REQ-081 | S-F | K | K | LIC is a launch site whose only live feed is the attendant (CTX-062). |
| REQ-082 | S-F | Y | Y | Walk-up capacity is the station's condition (CTX-064). |
| REQ-083 | S-F | K | K | Launch success 'one invoice' (CTX-139); fleet invoicing exists in every model (CF-008). |
| REQ-084 | S-F | K | K | 'Billing happens automatically' (CTX-002); no spreadsheets in the critical path (CTX-079). |
| REQ-085 | S-F | K | K | CTO requirement (CTX-095); money correctness. |
| REQ-086 | S-F | Y | Y | Fleet receivables exist in every model (CTX-129). Gate 2: set to Y (provisional). |
| REQ-087 | S-F | K | K | Fleets pay through Stripe today (CTX-051). |
| REQ-088 | S-F | K | K | Pilot behaviour drivers rely on (CTX-043). |
| REQ-089 | S-F | K | K | Known pilot defect, twice a week (CTX-044). |
| REQ-090 | S-F | K | K | Cause of duplicate confirmations (CTX-044); constitution N8. |
| REQ-091 | S-F | Y | K | Raised: T-549 needed by K work: T-931 (REQ-128). |
| REQ-092 | S-F | Y | K | Raised: T-550 needed by K work: T-551 (REQ-225). |
| REQ-093 | S-F | I | I | Pilot headline was self-reported (CTX-040); needs session-start data that is unconfirmed (Q-009, Q-012). |
| REQ-094 | S-F | I | I | Sells 'we fill your quiet hours' (CTX-119); needs walk-up session data. |
| REQ-095 | S-F | Y | Y | Series A is in H2 2027 (CTX-003), after launch. |
| REQ-096 | S-F | Y | K | Raised: T-983, T-984, T-1009 needed by K work: T-933, T-990 (REQ-132, REQ-231, REQ-116). |
| REQ-097 | S-F | K | K | Launch definition 'real stations, real fleets' (CTX-079). |
| REQ-100 | S-NF | K | K | Brief promise 'book in two taps' (CTX-002); constitution N23. |
| REQ-101 | S-NF | K | K | CTO: 'let Postgres say no' (CTX-093); constitution N7. |
| REQ-102 | S-NF | Y | Y | Agreed for fairness, not correctness (CTX-093). |
| REQ-103 | S-NF | K | K | CTO: 'I'd have fired someone for not doing that' (CTX-093); constitution N8. |
| REQ-104 | S-NF | K | K | Agreed NFR and proposal acceptance criterion (CTX-112, SRC-D2#13). |
| REQ-105 | S-NF | Y | K | Raised: T-500 needed by K work: T-317, T-318, T-321, T-324 and 6 more (REQ-020, REQ-023, REQ-024). |
| REQ-106 | S-NF | K | K | Duplicates already seen (CTX-091); constitution N9. |
| REQ-107 | S-NF | K | K | 'Never the only path' (CTX-091); keeps the 60-second target (CTX-112). |
| REQ-108 | S-NF | I | I | Roadmap item; US adoption likely low (CTX-022). |
| REQ-109 | S-NF | Y | Y | CTO flinches at 'reconcile it later' (SRC-C2@00:01:07). |
| REQ-110 | S-NF | Y | Y | 'Same as payment webhooks. Never the only path.' (CTX-091). |
| REQ-111 | S-NF | Y | K | Raised: T-955 needed by K work: T-958, T-961, T-1007 (REQ-083, REQ-084, REQ-087). |
| REQ-112 | S-NF | K | K | Many drivers prefer Spanish or Bengali (CTX-028); constitution N22. |
| REQ-113 | S-NF | Y | Y | The CEO's first launch-success sentence (CTX-139). Gate 2: set to Y (provisional). |
| REQ-114 | S-NF | Y | Y | COO's launch-success sentence (CTX-139); depends on site staff behaviour. |
| REQ-115 | S-NF | Y | K | Raised: T-983, T-984, T-1009 needed by K work: T-933, T-990 (REQ-132, REQ-231, REQ-116). |
| REQ-116 | S-NF | Y | K | Raised: T-977, T-981 needed by K work: T-549, T-978, T-979 (REQ-091, REQ-096, REQ-115). |
| REQ-117 | S-NF | Y | Y | CTO would bin it (CTX-052); a constraint, not work. |
| REQ-118 | S-NF | Y | K | Raised: T-795 needed by K work: T-933 (REQ-132). |
| REQ-119 | S-NF | K | K | Contractual IP condition (CTX-005). |
| REQ-120 | S-NF | K | K | SOC 2-ready from day one (CTX-107); rideshare pilot asks for it (CTX-078). |
| REQ-121 | S-NF | Y | Y | SOC 2-ready from day one (CTX-107). Gate 2: set to Y (provisional). |
| REQ-122 | S-NF | Y | Y | SOC 2-ready from day one (CTX-107). Gate 2: set to Y (provisional). |
| REQ-123 | S-NF | K | K | SOC 2 and SHIELD safeguards (CTX-107, CTX-108). |
| REQ-124 | S-NF | K | K | SOC 2-ready from day one (CTX-107). |
| REQ-125 | S-NF | Y | K | Raised: T-790 needed by K work: T-793 (REQ-254). |
| REQ-126 | S-NF | K | K | Disputes, SHIELD and SOC 2 (CTX-110); constitution N17. |
| REQ-127 | S-NF | Y | Y | CTO's rule (CTX-085); checked per dependency. |
| REQ-128 | S-NF | K | K | Agreed NFR and acceptance criterion (CTX-114); constitution N4. |
| REQ-129 | S-NF | K | K | Agreed NFR (CTX-114); constitution N5. |
| REQ-130 | S-NF | K | K | Agreed NFR (CTX-113); constitution N3. |
| REQ-131 | S-NF | K | K | Agreed 5× test (CTX-115); the 4–5 PM wave is the launch risk (CTX-075). |
| REQ-132 | S-NF | K | K | Series A milestone (CTX-138); constitution N12. |
| REQ-133 | S-NF | K | K | Auto-release 'has to' happen (CTX-131); constitution N5, N10. |
| REQ-134 | S-NF | Y | K | Raised: T-165 needed by K work: T-503, T-506, T-520, T-521 (REQ-024, REQ-031, REQ-104). |
| REQ-135 | S-NF | K | K | Two Amperlane engineers run it after handover (CTX-007, CTX-087). |
| REQ-136 | S-NF | K | K | CTO's stack condition (CTX-085). |
| REQ-137 | S-NF | Y | Y | Budget envelope (CTX-080). |
| REQ-138 | S-NF | Y | K | Raised: T-108 needed by K work: T-501, T-505, T-519, T-523 (REQ-031, REQ-032, REQ-104). |
| REQ-139 | S-NF | Y | K | Raised: T-911, T-912 needed by K work: T-102, T-104, T-106, T-107 and 47 more (REQ-001, REQ-002, REQ-004). |
| REQ-140 | S-NF | Y | K | Raised: T-921, T-1004, T-1005 needed by K work: T-527, T-555 (REQ-105). |
| REQ-141 | S-NF | Y | Y | Agreed regression case (CTX-103); proves launch success #1 (CTX-139). |
| REQ-142 | S-NF | K | K | The date that matters (CTX-079). |
| REQ-143 | S-NF | Y | Y | Agreed delivery model (CTX-006); a way of working, not build scope. |
| REQ-144 | S-NF | Y | Y | CTO's ask (CTX-006). |
| REQ-145 | U-F | K | K | Two-tap booking at the burst needs it (CTX-002, CTX-115). |
| REQ-146 | U-F | Y | K | Raised: T-782 needed by K work: T-105, T-548, T-733 (REQ-112, REQ-199, REQ-224). |
| REQ-147 | U-F | K | K | Closes the pool-to-EVSE gap behind 'no double booking' (CF-023). |
| REQ-148 | U-F | Y | Y | A driver sent elsewhere was lost (SRC-C2@00:52:32); happens at JFK (CTX-066). |
| REQ-149 | U-F | Y | Y | Keeps site failures out of no-show figures (CTX-036). |
| REQ-150 | U-F | K | K | 'The station gets the stall back early' (CTX-135). |
| REQ-151 | U-F | Y | Y | NYC only at launch (CTX-079); first DST change after launch falls in March 2027. |
| REQ-152 | U-F | Y | Y | Cab drivers book overnight slots (CTX-029); overnight demand is mostly walk-up (CTX-114). |
| REQ-153 | U-F | K | K | A stale reservation blocks walk-ups at Gowanus (CTX-066). |
| REQ-154 | U-F | Y | Y | 'The hold sent' is dispute evidence (CTX-127). |
| REQ-155 | U-F | K | K | Reservations are optional and 6 of 16 Gowanus chargers reject them (CTX-060). |
| REQ-156 | U-F | Y | K | Raised: T-325 needed by K work: T-530 (REQ-058, REQ-097). |
| REQ-158 | U-F | K | K | Only live status source at LIC, a launch site (CTX-062). |
| REQ-159 | U-F | Y | Y | Replaces the ops call to the attendant (CTX-043). |
| REQ-160 | U-F | Y | Y | Agreed with the freshness NFR (CTX-112); constitution N2. Gate 2: set to Y (provisional). |
| REQ-161 | U-F | Y | K | Raised: T-966 needed by K work: T-546 (REQ-224). |
| REQ-162 | U-F | Y | Y | Only session data at LIC (CTX-062). |
| REQ-163 | U-F | I | I | Useful while drivers pay stations directly (CTX-051); not asked for. |
| REQ-164 | U-F | Y | Y | 'Station status at the time' is dispute evidence (CTX-127). |
| REQ-165 | U-F | Y | K | Raised: T-108 needed by K work: T-501, T-505, T-519, T-523 (REQ-031, REQ-032, REQ-104). |
| REQ-166 | U-F | I | I | No NYC launch site uses OCPI (CTX-090); LA is out of the MVP (CTX-081); scope deferred to Gate 2 (A-015). |
| REQ-167 | U-F | Y | Y | Keeps Gowanus bookable during vendor outages (CTX-091). |
| REQ-168 | U-F | Y | Y | JFK fills up and status is its only live signal (CTX-066). |
| REQ-169 | U-F | Y | Y | Silent failures went unnoticed in the pilot (CTX-047). |
| REQ-170 | U-F | Y | Y | Ops is the safety net for patterns B and C (SRC-C2@00:53:49). |
| REQ-171 | U-F | Y | Y | Makes one-tap cancel worth using (CTX-135); cut-off is a station term (Q-042). |
| REQ-172 | U-F | Y | Y | 'What the driver sees' is part of Q-002 (SRC-C1@00:47:44). |
| REQ-173 | U-F | I | I | Opt-in is off by default (A-024); QR covers arrival. |
| REQ-174 | U-F | Y | K | Raised: T-525 needed by K work: T-329 (REQ-204). |
| REQ-175 | U-F | I | I | Geotab access unconfirmed (Q-014); opt-in off by default (A-024). |
| REQ-176 | U-F | Y | Y | Arrival evidence at LIC, which has no API (CTX-062). |
| REQ-177 | U-F | K | K | A wrongful release takes a stall from a driver who arrived (CTX-131). |
| REQ-178 | U-F | I | I | Not asked for by the client; session data unconfirmed. |
| REQ-179 | U-F | Y | K | Raised: T-342 needed by K work: T-349 (REQ-045, REQ-259). |
| REQ-180 | U-F | K | K | Fees for platform or site failures would create disputes and anger fleets (CTX-035, CTX-077). |
| REQ-181 | U-F | Y | Y | Engineer's case 'driver showed up, charger didn't start' (SRC-C2@00:47:53). |
| REQ-182 | U-F | Y | Y | Accepted ops overrides (CTX-035). |
| REQ-183 | U-F | Y | Y | No-show terms come from each partner agreement (CTX-069); amounts are open (Q-002). |
| REQ-184 | U-F | Y | K | Raised: T-145 needed by K work: T-301 (REQ-013, REQ-020). |
| REQ-185 | U-F | Y | Y | Keeps maintenance out of no-show figures (CTX-036). |
| REQ-186 | U-F | Y | K | Raised: T-147 needed by K work: T-203 (REQ-184, REQ-335). |
| REQ-187 | U-F | Y | Y | Ops control over automation (CF-022). |
| REQ-188 | U-F | Y | Y | Vendor addition (CF-022); ops can also rebook one by one. |
| REQ-189 | U-F | K | K | Ops is the safety net for patterns B and C (SRC-C2@00:53:49); 'nobody opens Airtable' (CTX-139). |
| REQ-190 | U-F | Y | K | Raised: T-528 needed by K work: T-347, T-931 (REQ-128). |
| REQ-191 | U-F | Y | K | Raised: T-517 needed by K work: T-734, T-768 (REQ-039, REQ-236, REQ-040). |
| REQ-192 | U-F | Y | Y | LIC is a launch site with no API (CTX-062). Gate 2: set to Y (provisional). |
| REQ-193 | U-F | I | I | Not asked for; stations email faults today (CTX-048). |
| REQ-194 | U-F | Y | K | Raised: T-514 needed by K work: T-528 (REQ-190). |
| REQ-195 | U-F | Y | Y | Dozens of driver calls a day (CTX-045). |
| REQ-196 | U-F | I | I | Helpful for support; not asked for. |
| REQ-197 | U-F | Y | K | Raised: T-729 needed by K work: T-531 (REQ-058, REQ-097). |
| REQ-198 | U-F | Y | Y | No accounts for drivers (CTX-027); booking needs an identity. Gate 2: set to Y (provisional). |
| REQ-199 | U-F | K | K | EN/ES/BN is a stated NFR (CTX-097). |
| REQ-200 | U-F | K | K | Pool booking means the driver learns the EVSE late (CTX-092); pilot confirmations name the stall (SRC-C1@00:05:34). |
| REQ-201 | U-F | Y | Y | Owners book for the other shift's driver (CTX-029). |
| REQ-202 | U-F | K | K | Weekly leases change hands (CTX-026); access control. |
| REQ-203 | U-F | Y | Y | Drivers will not install or register (CTX-027). |
| REQ-204 | U-F | K | K | Location is opt-in and off by default (A-024). |
| REQ-205 | U-F | Y | Y | Bookings need registered drivers and vehicles (A-023). Gate 2: set to Y (provisional). |
| REQ-206 | U-F | K | K | Five Boroughs will not use a portal (CTX-030) and is a launch fleet. |
| REQ-207 | U-F | Y | Y | Borough Green has about 420 EVs (CTX-073). |
| REQ-208 | U-F | I | I | Nice to have against invoice surprises (CTX-139 #4). |
| REQ-209 | U-F | I | I | Sales argument (CTX-119); value depends on the model (Q-001). |
| REQ-210 | U-F | K | K | Settlement must start before the model is decided (CF-008, CTX-129). |
| REQ-211 | U-F | K | K | Holds in every fee option; constitution N19. |
| REQ-212 | U-F | K | K | Holds in every fee option; disputes expected daily (CTX-035). |
| REQ-213 | U-F | Y | Y | 'Borough Green … doesn't email me about it' (CTX-139). |
| REQ-214 | U-F | Y | Y | Session data is unconfirmed at all three sites (Q-009, Q-011, Q-012). |
| REQ-215 | U-F | Y | Y | Finance actor accepted at Gate 1, client to confirm (Q-037). |
| REQ-216 | U-F | Y | Y | Fleet receivables exist in every model (CTX-129). |
| REQ-217 | U-F | Y | Y | One invoice without emails (CTX-139). |
| REQ-218 | U-F | Y | Y | LIC session data arrives by hand, possibly late (CTX-062). |
| REQ-219 | U-F | Y | Y | A missed reminder or re-offer becomes a no-show (CTX-041). |
| REQ-220 | U-F | Y | Y | Drivers act while driving (CTX-041); fallback when the link cannot open. |
| REQ-221 | U-F | I | I | Helpful; ops number is known to pilot drivers. |
| REQ-222 | U-F | Y | Y | Today a bilingual ops person reads every text (CTX-045). |
| REQ-223 | U-F | I | I | Outages are rare within the 99.9% target (CTX-114). |
| REQ-224 | U-F | K | K | Billing unit and Series A metric are undecided (Q-017). |
| REQ-225 | U-F | Y | K | Raised: T-549 needed by K work: T-931 (REQ-128). |
| REQ-226 | U-F | I | I | Operational insight; the monthly metrics are covered elsewhere. |
| REQ-227 | U-F | I | I | Measures launch success #1 (CTX-139); can follow launch. |
| REQ-228 | U-F | Y | K | Raised: T-981, T-982 needed by K work: T-549, T-984, T-1011 (REQ-091, REQ-096, REQ-115). |
| REQ-229 | U-F | Y | K | Raised: T-979 needed by K work: T-987 (REQ-231). |
| REQ-230 | U-F | Y | K | Raised: T-981, T-982 needed by K work: T-549, T-984, T-1011 (REQ-091, REQ-096, REQ-115). |
| REQ-231 | U-F | K | K | No spreadsheets in the critical path from 2027-03-01 (CTX-079). |
| REQ-232 | U-F | K | K | Fleet invoicing continues through the launch month (CTX-051). |
| REQ-233 | U-F | Y | K | Raised: T-791 needed by K work: T-792 (REQ-254). |
| REQ-234 | U-F | I | I | No partner is leaving; can follow launch. |
| REQ-235 | U-F | I | I | Small fleets forget passwords (CTX-030); ops can act for them. |
| REQ-236 | U-NF | K | K | The double tap on bad 4G hits cancel as much as booking (CTX-093); constitution N8. |
| REQ-237 | U-NF | Y | K | Raised: T-921, T-1004, T-1005 needed by K work: T-527, T-555 (REQ-105). |
| REQ-238 | U-NF | I | I | Needed only if the discovery map is built. |
| REQ-239 | U-NF | Y | Y | A half-done rebooking repeats the Gowanus afternoon (CTX-047). Gate 2: set to Y (provisional). |
| REQ-240 | U-NF | K | K | No-account access must still be secure (CTX-107). |
| REQ-241 | U-NF | Y | Y | Links can be forwarded between shift drivers (CTX-029); A-006 left this to Step 2. |
| REQ-242 | U-NF | K | K | Text commands change bookings and fees (CTX-043). |
| REQ-243 | U-NF | Y | Y | Five Boroughs barely uses a portal (CTX-030); covered by messaging and ops requirements. |
| REQ-244 | U-NF | K | K | Money correctness; the CTO has payout 'scars' (SRC-C2@00:01:07). |
| REQ-245 | U-NF | Y | Y | Payment is not in the booking path today (CTX-051). |
| REQ-246 | U-NF | Y | Y | Keeps PCI scope minimal; fleets pay through Stripe today (CTX-051). |
| REQ-247 | U-NF | K | K | Money audit trail (CTX-095, CTX-110); constitution N19. |
| REQ-248 | U-NF | K | K | US carrier rules for application-to-person messaging; messaging is the driver channel (CTX-097). |
| REQ-249 | U-NF | Y | Y | WhatsApp Business rules; WhatsApp is a Y channel. |
| REQ-250 | U-NF | Y | K | Raised: T-732 needed by K work: T-799 (REQ-255). |
| REQ-251 | U-NF | I | I | Cost control within the budget (CTX-080); can follow launch. |
| REQ-252 | U-NF | Y | K | Raised: T-985 needed by K work: T-977 (REQ-116). |
| REQ-253 | U-NF | K | K | State law (CTX-108); constitution N18. |
| REQ-254 | U-NF | K | K | State law (CTX-108). |
| REQ-255 | U-NF | K | K | Drivers are independent contractors; location is sensitive (CTX-108, CTX-109). |
| REQ-256 | U-NF | Y | Y | Minimisation (CTX-108); location is opt-in, so volume is low. |
| REQ-257 | U-NF | Y | Y | Needed once telematics is used (CTX-109). |
| REQ-258 | U-NF | K | K | Multi-party data on one platform (CTX-107); SHIELD (CTX-108). |
| REQ-259 | U-NF | Y | K | Raised: T-342 needed by K work: T-349 (REQ-045, REQ-179). |
| REQ-260 | U-NF | Y | K | Raised: T-526 needed by K work: T-555 (REQ-105). |
| REQ-262 | U-NF | Y | K | Raised: T-782 needed by K work: T-105, T-548, T-733 (REQ-112, REQ-199, REQ-224). |
| REQ-263 | U-NF | Y | K | Raised: T-785, T-791 needed by K work: T-792 (REQ-254). |
| REQ-264 | U-NF | I | I | SOC 2 vendor management; a document, timing follows Q-018. |
| REQ-265 | U-NF | Y | Y | Keeps SHIELD-covered data out of scope (CTX-108). |
| REQ-266 | U-NF | Y | K | Raised: SS-436 is K since Gate 3 (US-406 parent): the K cut-over check needs the outage copy (SS-422 clause 6). |
| REQ-267 | U-NF | Y | Y | 'The IP has to be ours' (CTX-005). |
| REQ-268 | U-NF | Y | Y | Two engineers run the platform after handover (CTX-007). |
| REQ-269 | U-NF | Y | K | Raised: T-991, T-992 needed by K work: T-794, T-994 (REQ-097, REQ-142, REQ-254). |
| REQ-270 | S-F | V | V | Parking lot · business-model options (Q-001). |
| REQ-271 | S-F | V | V | Parking lot · business-model options (Q-001). |
| REQ-272 | S-F | V | V | Parking lot · business-model options (Q-001). |
| REQ-273 | S-F | V | V | Parking lot · business-model options (Q-001). |
| REQ-274 | S-F | V | V | Parking lot · business-model options (Q-001). |
| REQ-275 | S-F | V | V | Parking lot · business-model options (Q-001). |
| REQ-276 | S-F | V | V | Parking lot · business-model options (Q-001). |
| REQ-277 | S-F | V | V | Parking lot · business-model options (Q-001). |
| REQ-278 | S-F | V | V | Parking lot · business-model options (Q-001). |
| REQ-279 | S-NF | V | V | Parking lot · business-model options (Q-001). |
| REQ-280 | U-F | V | V | Parking lot · business-model options (Q-001). |
| REQ-281 | U-F | V | V | Parking lot · business-model options (Q-001). |
| REQ-282 | S-NF | V | V | Parking lot · business-model options (Q-001). |
| REQ-283 | U-F | V | V | Parking lot · business-model options (Q-001). |
| REQ-284 | U-F | V | V | Parking lot · business-model options (Q-001). |
| REQ-285 | U-F | V | V | Parking lot · business-model options (Q-001). |
| REQ-286 | U-F | V | V | Parking lot · business-model options (Q-001). |
| REQ-287 | U-F | V | V | Parking lot · business-model options (Q-001). |
| REQ-288 | U-F | V | V | Parking lot · business-model options (Q-001). |
| REQ-289 | U-F | V | V | Parking lot · business-model options (Q-001). |
| REQ-290 | U-F | V | V | Parking lot · business-model options (Q-001). |
| REQ-291 | U-NF | V | V | Parking lot · business-model options (Q-001). |
| REQ-292 | U-F | V | V | Parking lot · business-model options (Q-001). |
| REQ-293 | S-F | V | V | Parking lot · business-model options (Q-001). |
| REQ-294 | S-F | V | V | Parking lot · business-model options (Q-001). |
| REQ-295 | S-F | V | V | Parking lot · business-model options (Q-001). |
| REQ-296 | S-F | V | V | Parking lot · business-model options (Q-001). |
| REQ-297 | U-F | V | V | Parking lot · business-model options (Q-001). |
| REQ-298 | S-F | V | V | Parking lot · no-show fee options (Q-002, Q-003). |
| REQ-299 | U-F | V | V | Parking lot · no-show fee options (Q-002, Q-003). |
| REQ-300 | U-F | V | V | Parking lot · no-show fee options (Q-002, Q-003). |
| REQ-301 | U-F | V | V | Parking lot · no-show fee options (Q-002, Q-003). |
| REQ-302 | U-F | V | V | Parking lot · no-show fee options (Q-002, Q-003). |
| REQ-303 | S-F | V | V | Parking lot · no-show fee options (Q-002, Q-003). |
| REQ-304 | U-F | V | V | Parking lot · no-show fee options (Q-002, Q-003). |
| REQ-305 | U-F | V | V | Parking lot · grace extension options (CF-021). |
| REQ-306 | S-F | V | V | Parking lot · grace extension options (CF-021). |
| REQ-307 | S-F | V | V | Parking lot · grace extension options (CF-021). |
| REQ-308 | S-F | V | V | Parking lot · integration scope options (Q-036, CF-025, CF-004, Q-010, A-026, A-029). |
| REQ-309 | S-F | V | V | Parking lot · integration scope options (Q-036, CF-025, CF-004, Q-010, A-026, A-029). |
| REQ-310 | S-F | V | V | Parking lot · integration scope options (Q-036, CF-025, CF-004, Q-010, A-026, A-029). |
| REQ-311 | S-F | V | V | Parking lot · integration scope options (Q-036, CF-025, CF-004, Q-010, A-026, A-029). |
| REQ-312 | U-F | V | V | Parking lot · integration scope options (Q-036, CF-025, CF-004, Q-010, A-026, A-029). |
| REQ-313 | U-F | V | V | Parking lot · integration scope options (Q-036, CF-025, CF-004, Q-010, A-026, A-029). |
| REQ-314 | U-F | V | V | Parking lot · integration scope options (Q-036, CF-025, CF-004, Q-010, A-026, A-029). |
| REQ-315 | U-NF | V | V | Parking lot · integration scope options (Q-036, CF-025, CF-004, Q-010, A-026, A-029). |
| REQ-316 | U-F | V | V | Parking lot · operations, SOC 2 date and budget options (Q-023, Q-018, Q-025). |
| REQ-317 | U-NF | V | V | Parking lot · operations, SOC 2 date and budget options (Q-023, Q-018, Q-025). |
| REQ-318 | S-NF | V | V | Parking lot · operations, SOC 2 date and budget options (Q-023, Q-018, Q-025). |
| REQ-319 | S-NF | V | V | Parking lot · operations, SOC 2 date and budget options (Q-023, Q-018, Q-025). |
| REQ-320 | U-NF | V | V | Parking lot · operations, SOC 2 date and budget options (Q-023, Q-018, Q-025). |
| REQ-321 | S-F | V | V | Parking lot · deferred by the client. |
| REQ-322 | S-F | V | V | Parking lot · deferred by the client. |
| REQ-323 | S-F | V | V | Parking lot · deferred by the client. |
| REQ-324 | S-F | V | V | Parking lot · deferred by the client. |
| REQ-325 | S-F | V | V | Parking lot · deferred by the client. |
| REQ-326 | S-F | V | V | Parking lot · deferred by the client. |
| REQ-327 | S-F | V | V | Parking lot · deferred by the client. |
| REQ-328 | U-F | V | V | Parking lot · deferred by the client. |
| REQ-329 | U-F | V | V | Parking lot · out of MVP scope (Intellias proposal). |
| REQ-330 | U-F | V | V | Parking lot · out of MVP scope (Intellias proposal). |
| REQ-331 | U-F | V | V | Parking lot · out of MVP scope (Intellias proposal). |
| REQ-332 | S-F | Y | Y | Split from REQ-031 (P2.4). Settlement and the completed-booking evidence need session records (CTX-127); depends on Q-009. Gate 2: set to Y (provisional). |
| REQ-333 | S-F | I | I | Split from REQ-032 (P2.4). Serves only the price display (REQ-163, suggested I). |
| REQ-334 | U-F | Y | K | Raised: T-334, T-352 needed by K work: T-734, T-768 (REQ-039, REQ-236, REQ-040). |
| REQ-335 | U-F | Y | K | Raised: T-146 needed by K work: T-203 (REQ-184, REQ-186). |
| REQ-336 | S-F | Y | Y | Added by CR-008 (2026-10-28): the COO's "move the booking to another free one" (SRC-C2@00:24:04); set to Y at the CR. |
