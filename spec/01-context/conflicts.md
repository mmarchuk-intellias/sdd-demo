---
id: CONFLICTS
type: context
title: Conflicts between sources
status: approved
owner: Mykola Marchuk
version: 1
kyiv: null
parents: [BUSINESS-CONTEXT]
sources: [SRC-D1, SRC-C1, SRC-C2, SRC-D2, SRC-R1]
---
# Conflicts between sources

This file covers every place where sources disagree. The resolution rule is **later > earlier, specific > general,
data > estimate**. Source dates: SRC-D1 Sep 2026 (sent 22 Sep) · SRC-C1 29 Sep · SRC-C2 8 Oct · SRC-D2 16 Oct · SRC-R1 19 Oct.
A later *vendor* document does not override what the *client* said. SRC-D2 and SRC-R1 are Intellias' interpretation
(see AGENTS.md, "Who said it matters").

Status values:

- **resolved**: the rule settles it.
- **resolved-provisional**: the rule settles it for now, pending data or confirmation (linked Q/A).
- **needs-decision**: the rule does not settle it, or the conflict is a decision in disguise (playbook §10.7). It has an
  owner and a due date.

## Summary

| CF | Topic | Status | Owner · due |
|---|---|---|---|
| CF-001 | Driver channel: native app vs PWA + messaging | resolved | — |
| CF-002 | Real-time reservation on every charger | resolved | — |
| CF-003 | Real-time availability from the NREL API | resolved | — |
| CF-004 | Vehicle battery data from the Tesla API | needs-decision | Ravi Menon with Borough Green, via Dana Whitfield · cost model 2026-11-06, decision 2026-11-27 |
| CF-005 | Uber/Lyft "deep link + data" | resolved | — |
| CF-006 | "12 weeks to MVP" vs the 1 March 2027 launch | resolved | — |
| CF-007 | 10 US metros by end of 2027 | resolved | — |
| CF-008 | Revenue model | needs-decision | Dana Whitfield, Luis Ortega, Ravi Menon · 2026-11-13 (workshop not held on 2026-10-27) |
| CF-009 | What "Option C, hybrid" means | resolved | — (the choice is CF-008) |
| CF-010 | Was the station portal in the brief's scope? | resolved | — |
| CF-011 | Number of actor types (five vs six) | resolved-provisional | Accepted at Gate 1 (2026-10-27) · client to confirm, Q-037 |
| CF-012 | DC fast-charger utilisation figures | resolved | — |
| CF-013 | What the ~$1M phase-one budget covers | needs-decision | Mark Feldman with Dana Whitfield · 2026-11-02 |
| CF-014 | Total funding raised ($6.7M vs $5.5M seed) | resolved-provisional | Mark Feldman |
| CF-015 | Overnight bookings vs the 5 AM–1 AM availability window | needs-decision | Ravi Menon with Dana Whitfield · 2026-11-06 |
| CF-016 | SOC 2 Type I deadline anchor | needs-decision | Ravi Menon · 2026-11-06 |
| CF-017 | Where soft holds live (Postgres vs Redis/Valkey) | resolved-provisional | Olena Marchuk · Phase 0 |
| CF-018 | Reliability of the pilot no-show and completion figures | resolved-provisional | Priya Nair · raw export |
| CF-019 | "Stations give all their ports" | resolved | — |
| CF-020 | Maps and routing provider | resolved-provisional | Ravi Menon · Phase 0 (by 2026-11-27) |
| CF-021 | Extending grace when the car is close vs release after ten minutes | needs-decision | Luis Ortega with the station operators · 2026-11-06 |
| CF-022 | Charger fault: automatic reassignment vs ops bulk approval | resolved-provisional | Dana Whitfield (ops) to confirm · 2026-11-06 |
| CF-023 | What "no double booking in the database" covers before T-15 | resolved-provisional | Olena Marchuk with Ravi Menon · Phase 0 |
| CF-024 | Is there a cash gap whatever the business model? | resolved | — |
| CF-025 | "All major CSMS" in the brief vs the systems actually reachable | needs-decision | Ravi Menon, Luis Ortega, with Dana Whitfield · 2026-11-06 |
| CF-026 | Observed vs modelled shift-change burst | resolved | — |

## Details

### CF-001 · Driver channel: native app vs PWA + messaging
- **Source A:** "Driver App, Native iOS / Android" in the target architecture and the scope (SRC-D1#9, SRC-D1#11).
- **Source B:** "Honest answer is light mobile web plus messaging" in English, Spanish and Bengali; the deck was written
  for investors (SRC-C1@00:06:33). "No native app for MVP… Dana… agreed" (SRC-C2@00:51:10, SRC-C2@00:51:22).
- **Rule applied:** later > earlier, specific > general. **Result:** PWA + SMS/WhatsApp for drivers in the MVP; native
  apps in Phase 2 (CTX-096). **Status:** resolved.

### CF-002 · Real-time reservation on every charger
- **Source A:** "Charger APIs (OCPP): Real-time reservation on every charger" (SRC-D1#9); "The stall is held for you"
  (SRC-D1#5).
- **Source B:** OCPP reservations are optional and mean "hold now", not a future slot (SRC-C2@00:07:35,
  SRC-C2@00:08:09). Only Gowanus can reserve, on 10 of 16 chargers; JFK is status-only and LIC has no API
  (SRC-C2@00:14:11, SRC-C2@00:19:30, SRC-C2@00:19:59).
- **Rule applied:** later, specific, data. **Result:** Amperlane owns the slot calendar, and charger-side holds happen
  only where supported, about 15 minutes before the slot (CTX-088, CTX-063). **Status:** resolved.

### CF-003 · Real-time availability from the NREL API
- **Source A:** "NREL API: Real-time station availability" (SRC-D1#9); "NREL: Station data" (SRC-D1#10).
- **Source B:** NREL is now NLR, and the AFDC API is static only (SRC-C2@00:10:23). The client's engineer found no
  availability field (SRC-C2@00:10:01).
- **Rule applied:** later, specific. **Result:** AFDC and Open Charge Map are for discovery only. Live status comes
  from CSMS APIs or OCPI (CTX-089, CTX-090). **Status:** resolved.

### CF-004 · Vehicle battery data from the Tesla API
- **Source A:** "Tesla API: Vehicle battery data" (SRC-D1#9, SRC-D1#10).
- **Source B:** About 55% of Borough Green's fleet are Teslas with no integration. Tesla Fleet API is pay-per-use and
  needs account-owner authorisation and driver consent. Geotab covers the non-Teslas; the cab fleet has no telematics.
  The MVP cut is Geotab plus manual SoC, with Tesla as a costed option (SRC-C2@00:38:24, SRC-C2@00:38:43,
  SRC-C2@00:38:50, SRC-C2@00:39:22, SRC-C2@00:40:31, SRC-C2@00:40:50).
- **Rule applied:** later, specific settles the MVP baseline (Geotab + manual SoC, CTX-099). Whether to add Tesla Fleet
  API or Smartcar, and who pays for it, is a cost decision the rule cannot make.
- **Status:** needs-decision. Owner: Ravi Menon with Borough Green, through Dana Whitfield, who holds the relationship
  (integrations.md I-9). Intellias delivers the cost model with the proposal on 2026-11-06 (SRC-C2@00:40:50); the client
  decides by the end of Phase 0, 2026-11-27 (Gate 1 second review, Mykola Marchuk, 2026-10-28). The MVP baseline also
  depends on Geotab access (Q-014), and A-022 leaves Tesla to this conflict. Links: Q-015, Q-014, A-022.

### CF-005 · Uber/Lyft "deep link + data"
- **Source A:** "Uber / Lyft driver apps: Deep link + data" (SRC-D1#10).
- **Source B:** The Uber Driver API is limited-access with no vehicle data, and Lyft has no public API. Deep links only
  in the MVP; the CTO accepted ("Okay") (SRC-C2@00:42:43, SRC-C2@00:43:07, SRC-C2@00:43:30).
- **Rule applied:** later, specific. **Result:** deep links only in the MVP; beyond that is Phase 2 (CTX-098).
  **Status:** resolved.

### CF-006 · "12 weeks to MVP" vs the 1 March 2027 launch
- **Source A:** "12 weeks to MVP" (SRC-D1#11). On Call 1 the CEO still asked: "The deck says MVP in twelve weeks. Is that
  crazy?" (SRC-C1@00:48:36).
- **Source B:** "The date that matters is March first, 2027. NYC production launch." (SRC-C1@00:29:06, the CEO).
  Intellias: "Not crazy as a wish… March first is the real constraint" (SRC-C1@00:48:45); the CEO: "That's a fair
  non-answer" (SRC-C1@00:49:11). The Intellias build phase is about 13 weeks, 30 Nov–26 Feb (SRC-D2#15).
- **Rule applied:** specific > general. The client named 1 March as "the date that matters", so that is the binding
  constraint (CTX-079). The two are barely in conflict: 12 weeks from the brief and the ~13-week build both land before
  1 March. The client has not withdrawn "12 weeks"; it is Intellias who calls it a wish (CTX-082).
- **Status:** resolved: plan against 1 March 2027.

### CF-007 · 10 US metros by end of 2027
- **Source A:** "10 US metros by end of 2027" (SRC-D1#11).
- **Source B:** "Ten metros is 2028." LA is next, in Q3 2027 (SRC-C1@00:31:33, SRC-C1@00:32:08).
- **Rule applied:** later, specific. **Result:** NYC on 1 March 2027, LA targeted for Q3 2027, ten metros as a 2028
  ambition (CTX-081). **Status:** resolved.

### CF-008 · Revenue model
- **Source A:** A 10–12% take rate on charging GMV from stations plus $15/vehicle/month from fleets, giving $4.8M ARR
  in 2028 (SRC-D1#8). The brief also implies Amperlane bills the session and "the station gets paid" (SRC-D1#6).
- **Source B:** No station signed the percentage; stations pay only for incremental off-peak sessions
  (SRC-C1@00:17:22, SRC-C1@00:18:24). The CEO floated eMSP/merchant of record with a spread (SRC-C1@00:19:54).
  The founders are split (SRC-C1@00:23:07, SRC-C1@00:23:13, SRC-C1@00:23:24) and still undecided on Call 2:
  "Dana and I need a referee" (SRC-C2@00:36:37). Stations have not accepted the spread either (SRC-C1@00:22:36).
- **Source C:** SRC-D2#14 already puts "Stripe Connect payouts + fleet invoicing" in MVP scope. Fleet invoicing exists
  in every option (the pilot invoices fleets today, SRC-C1@00:13:26); only the Connect payouts presume option B or C,
  which SRC-D2#9 itself marks as conditional ("If B or C, the platform must add…").
- **Missing option:** the option lists in the sources leave out today's model, a booking fee only, with energy
  money staying between driver and station (SRC-C1@00:13:26); Intellias noted it is "much simpler"
  (SRC-C2@00:48:32). The workshop pre-read should include it.
- **Rule applied:** none. This is a pricing and business decision (playbook §10.7). The data says only that option A
  failed with stations (CTX-118).
- **Status:** needs-decision. Owners: Dana Whitfield, Luis Ortega, Ravi Menon. Due: the business-model workshop,
  requested for Tue 2026-10-27 (SRC-R1#c1); Intellias asked for the decision within three weeks of 8 Oct, i.e. by
  2026-10-29 (SRC-C2@00:48:32). Links: Q-001, CF-009.
- **Update (Gate 1 review, Mykola Marchuk, 2026-10-27):** the workshop did not take place on 2026-10-27 (postponed or
  cancelled; which one is still to be confirmed), and no new date is set. The 2026-10-29 deadline is at risk. The CEO
  travels the week after the workshop week (CTX-084), so if it is not held this week the decision may slip past
  2026-11-06. Until then, settlement, invoicing and ADR-011 stay generic. Due date (Gate 1 second review, Mykola
  Marchuk, 2026-10-28): 2026-11-13, after the CEO's travel week; Kyrylo Shvedov schedules the workshop (SRC-R1#open).
  The proposal of 2026-11-06 prices the options.

### CF-009 · What "Option C, hybrid" means
- **Source A (client):** No client speaker defined an "Option C". The founders' own positions: the CEO leans to "spread
  plus subscription" (SRC-C1@00:23:07); the COO to "whatever the stations sign. Maybe a small fee on incremental off-peak
  sessions only, plus the spread" (SRC-C1@00:23:13).
- **Source B (vendor, sent to client):** "The spread plus a smaller booking or percentage fee, and the fleet
  subscription" (SRC-D2#9).
- **Source C (vendor, internal):** "Stations pay only for incremental off-peak bookings; fleets get one monthly invoice,
  net-30". This leaves out the spread (SRC-R1#model).
- **Rule applied:** a vendor document does not override what the client said, so "Option C" means the founders' own
  positions, not either vendor paraphrase. Choosing between those positions is the business-model decision itself, a
  decision in disguise (playbook §10.7) tracked in CF-008.
- **Action:** the workshop pre-read with "the 3 options" (SRC-R1#c3) should present the founders' positions in their own
  words rather than either vendor paraphrase, and SRC-R1's version should not be used. SRC-D2#9, already sent to the
  client, drops "incremental off-peak only" and so reads as a fee on all sessions, which stations rejected
  (SRC-C1@00:18:24); the pre-read should correct it.
- **Status:** resolved (Gate 1 second review, Mykola Marchuk, 2026-10-28): the definition is the founders' own
  words; the choice stays needs-decision in CF-008.

### CF-010 · Was the station portal in the brief's scope?
- **Source A:** The target architecture shows only "Driver App" and "Fleet Web Portal" as channels (SRC-D1#9).
- **Source B:** The scope slide lists "Station portal: Slots, schedules, tariffs" (SRC-D1#11).
- **Source C:** SRC-D2#4 (G5) says the brief said "Driver app + fleet portal" and that the "station portal and ops
  console join the scope"; SRC-D2#6 says the brief "named two users".
- **Rule applied:** specific > general. The scope slide is the explicit scope statement.
- **Result:** the station portal was in the client's stated scope from the start. Only the ops console is new
  (SRC-C1@00:39:49, CTX-035). SRC-D2#4 misstates the brief on this point; Intellias may want to correct it before the
  proposal.
- **Status:** resolved.

### CF-011 · Number of actor types (five vs six)
- **Source A:** Five actor types (fleet manager, driver, station operator, site staff, Amperlane ops), confirmed by the
  CEO (SRC-C1@00:08:34, SRC-C1@00:08:44, SRC-C1@00:46:07).
- **Source B:** "Five actor types (six with finance)" (SRC-D2#4, G5) and a Finance actor (SRC-D2#6).
- **Rule applied:** not contradictory. Finance is an addition by Intellias, supported by client mentions of a fleet
  finance lead (SRC-C1@00:19:12, SRC-C2@00:35:57) and Amperlane's finance person (SRC-C2@00:47:08).
- **Result:** six actor types, with Finance marked as vendor-proposed (CTX-025, A-010).
- **Gate 1 decision (Mykola Marchuk, 2026-10-27):** accepted. Finance is a platform actor with its own views. Invoices
  or payouts exist under any business model (CTX-032, ADR-008).
- **Status:** resolved-provisional, until the client confirms Finance as a platform user (Q-037).

### CF-012 · DC fast-charger utilisation figures
- **Source A:** California public DC fast chargers 22.2% in Q1 2026, per the CPUC (SRC-D1#3).
- **Source B:** US national "about sixteen percent in Q2, per Paren" (SRC-C1@00:03:18, the CEO).
- **Source C:** US 15.9% (21.1% in the top 30 metros) (SRC-D2#3); US 15.9% national and 31.8% in LA, Q3 2026
  (SRC-R1#market, SRC-R1#r5).
- **Rule applied:** specific > general. The figures cover different periods and geographies, so they are not
  competing claims. Keep each one with its period and scope; never quote one as another.
- **Result:** CTX-012. The "21.1% in the top 30 metros" figure appears only in SRC-D2#3, so quote it with that source.
- **Status:** resolved.

### CF-013 · What the ~$1M phase-one budget covers
- **Source A (client):** "Around a million, give or take, for phase one. Through Q2 next year"; "$900K to $1.2M"; "That's
  the range we modelled. Through end of Q2 2027." (SRC-C1@00:30:45, SRC-C1@00:30:57, SRC-C1@00:31:02).
- **Source B (vendor):** "Phase 1 budget around $1M" (SRC-D2#5, G10), where Intellias' Phase 1 is the MVP build from
  30 Nov to 26 Feb, followed by March hypercare and Phase 2 "LA and scale" from Q2 2027 (SRC-D2#15). SRC-R1 says
  "Phase 1 ~$0.9–1.2M (T&M or fixed, TBD)".
- **Rule applied:** specific > general settles the *fact*: the client's envelope runs to the end of Q2 2027 (CTX-080).
  It does not settle the *scope*: whether the envelope also covers Phase 0, hypercare and the April–June NYC ramp, or
  only the MVP build. Nor does it say whether the envelope is Intellias' fee only or Amperlane's whole phase-one spend,
  which also covers cloud, Temporal, telematics, Stripe and the SOC 2 auditor (ADR-012). That is a commercial decision.
  "Phase 1" also means different things to the two sides (see the glossary).
- **Status:** needs-decision. Owner: Mark Feldman with Dana Whitfield; due 2026-11-02, before the costed proposal; if
  unanswered, the proposal states which reading it uses (Gate 1 second review, Mykola Marchuk, 2026-10-28). Links:
  Q-025.

### CF-014 · Total funding raised ($6.7M vs $5.5M seed)
- **Source A (client):** "$5.5M Seed, February 2026" (SRC-D1#2, SRC-C1@00:29:22). No pre-seed is mentioned.
- **Source B (vendor, internal):** "raised $6.7M"; "Pre-seed $1.2M (Jun 2024, angels) · Seed $5.5M (Feb 2026)"
  (SRC-R1#company).
- **Rule applied:** not strictly contradictory, since $6.7M is the pre-seed plus the seed, but the pre-seed exists only
  in SRC-R1.
- **Result:** quote "$5.5M seed" to the client; treat the $6.7M total as unverified. **Status:** resolved-provisional.
  Links: Q-031.

### CF-015 · Overnight bookings vs the 5 AM–1 AM availability window
- **Source A:** "Basically 5 AM to 1 AM. Overnight people walk up, they don't book." Agreed target: 99.9% from
  5 AM to 1 AM ET, with maintenance outside (SRC-C2@00:50:00, SRC-C2@00:50:06, SRC-C2@00:50:13).
- **Source B:** Long-term cab drivers book "the afternoon slot and the overnight slot in one go" (SRC-C1@00:07:40). The
  COO's value proposition is a driver "at eleven AM or two AM" (SRC-C1@00:18:24). The Gowanus off-peak window includes
  10 PM–5 AM (SRC-D1#7).
- **Rule applied:** data > estimate would settle overnight demand, but the pilot export is not in the inputs. The window
  may only concern *making* bookings; but an overnight slot still needs its hold, grace, auto-release and notifications
  to run between 1 and 5 AM, when maintenance is allowed.
- **Options:** (a) no bookings between 1 and 5 AM; (b) overnight bookings allowed, with timers that may fire late during
  maintenance but are never lost; (c) a 24/7 target. Overnight demand is a data question that waits for the raw pilot
  export (CF-018).
- **Status:** needs-decision. Owner: Ravi Menon with Dana Whitfield (ops hours, Q-023); due 2026-11-06 (the NFRs become
  proposal acceptance criteria, SRC-D2#13). Links: Q-024, Q-023. Working assumption: A-028, option (b) (Gate 1, revised
  2026-10-28).

### CF-016 · SOC 2 Type I deadline anchor
- **Source A (vendor):** "A large platform's EV team wants SOC 2 Type I within 12 months" (SRC-D2#5, G8). SRC-D2#17 and
  SRC-R1#risks frame it as "SOC 2 Type I within 12 months vs Mar 1 launch".
- **Source B (client):** "Twelve months from when?" "From pilot start, roughly — next spring if we're lucky. Earlier
  would be better, it helps the Series A too." (SRC-C2@00:43:51, SRC-C2@00:43:54).
- **Rule applied:** specific > general fixes the anchor: 12 months from the start of the rideshare pilot (not yet
  scheduled; possibly spring 2027). The actual target date is a client decision; Intellias noted that it changes the
  March scope (SRC-C2@00:44:34).
- **Options:** (a) audit-ready 12 months after the rideshare pilot starts; (b) earlier, before the Series A in the
  second half of 2027 ("Earlier would be better, it helps the Series A too", SRC-C2@00:43:54). The pen test asked for
  with it (SRC-C2@00:43:30) follows the same date (ADR-012).
- **Status:** needs-decision. Owner: Ravi Menon; due 2026-11-06. Links: Q-018.

### CF-017 · Where soft holds live (Postgres vs Redis/Valkey)
- **Source A:** Holds can be Postgres rows with status and expiry, or short-lived Redis keys with a TTL, with only
  confirmed bookings in Postgres. "I lean to the first for auditability, but we'd prototype both."
  (SRC-C2@00:31:51).
- **Source B:** "Holds live in Postgres; Valkey only caches rate limits and idempotency keys" (SRC-D2#10 notes,
  SRC-D2#11).
- **Rule applied:** later > earlier gives Postgres. Both statements are Intellias', the client has not confirmed
  either, and Call 2 promised a prototype of both.
- **Result:** the v0 design assumes holds in Postgres (A-005); confirm with the Phase 0 prototype.
  **Status:** resolved-provisional.

### CF-018 · Reliability of the pilot no-show and completion figures
- **Source A:** "~2,300 bookings per month" (SRC-D1#7, pilot data, Sep 2026). "About eighteen-fifty completed. No-shows
  are seventeen percent… late arrivals… twenty-two percent" (SRC-C1@00:08:56).
- **Source B:** Status values changed twice, and early no-shows were recorded as "cancelled" (SRC-C2@00:05:22). Bookings
  moved after a charger fault still show as no-shows in Airtable (SRC-C2@00:52:53).
- **Arithmetic:** the rounded figures are roughly consistent: 1,850 / 0.83 ≈ 2,230, against "about 2,300". They cannot
  show whether cancellations exist as a separate outcome.
- **Rule applied:** data > estimate. The figures are client-reported from uncleaned data, and the cleaning issues
  bias the no-show rate. Until the raw export (Airtable + Sheets) is analysed, quote them as "reported, uncleaned".
- **Status:** resolved-provisional. Links: Q-029, Q-020.

### CF-019 · "Stations give all their ports"
- **Source A (vendor):** "Brief said: Stations give all their ports" (SRC-D2#5, G6).
- **Source B (client):** The brief says "Operators share bookable capacity, schedules and tariffs" (SRC-D1#6). On
  Call 1 the client said a cap of 30–50% at peak (SRC-C1@00:26:10). The Intellias question on the call was about the
  deck's *impression* (SRC-C1@00:25:45).
- **Rule applied:** specific > general. The brief never states "all ports".
- **Result:** capacity is capped per site and time window (CTX-064, CTX-065). SRC-D2#5 overstates the brief.
- **Status:** resolved.

### CF-020 · Maps and routing provider
- **Source A (client):** "Google Maps: Maps, directions, ETA" (SRC-D1#9).
- **Source B (vendor):** "Valhalla on OSM: routing, ETA (or Mapbox)" (SRC-D2#10, SRC-D2#11).
- **Rule applied:** a later vendor document does not override what the client said, and the client's specific "Google
  Maps" (SRC-D1#9) beats its general "open source where possible / where it's mature" (SRC-D1#10, SRC-C2@00:06:05). The
  brief adds "we're open to yours" (SRC-D1#9), and vendors are the CTO's call (stakeholders.md).
- **Status:** resolved-provisional (Gate 1 second review, Mykola Marchuk, 2026-10-28): Google Maps behind an adapter
  (A-030). Ravi Menon confirms in Phase 0 (by 2026-11-27). Links: Q-027.

### CF-021 · Extending grace when the car is close vs release after ten minutes
- **Source A (client, COO):** "A short grace period. We've been talking ten minutes. After ten, the stall's released,
  cone comes off, walk-up gets it." (SRC-C1@00:09:55). The slot must release itself automatically (SRC-C1@00:10:26).
- **Source B (client, CTO):** "If we see the car approaching the site, it's not a no-show, and we can stretch grace if
  they're two blocks away." (SRC-C2@00:38:05). Intellias lists "extend grace" as an ops override (SRC-C2@00:53:00), and
  the CEO had already agreed to overrides such as "let him in, he's twelve minutes late" (SRC-C1@00:38:52,
  SRC-C1@00:39:22).
- **Rule applied:** later > earlier would favour the CTO, but the grace period is a station term (Q-004, Q-005), and
  the stations are not party to Call 2.
- **Options:** (a) a fixed 10 minutes; (b) ops extends up to a maximum each station sets; (c) the driver taps "running
  late" and gets up to that maximum; (d) automatic extension when location shows the car is close (the CTO's wish). They
  can be combined.
- **Status:** needs-decision. Owner: Luis Ortega with the station operators; due 2026-11-06. Until then the v0 design
  allows extension only as an ops override up to the site's maximum (design.md F4; working assumption A-020, option (b),
  Gate 1, revised 2026-10-28).

### CF-022 · Charger fault: automatic reassignment vs ops bulk approval
- **Source A:** On a fault the system reassigns each booking to a compatible EVSE at the same site and notifies the
  driver and ops only for bookings it cannot place (SRC-C2@00:34:48); the COO: "That'd be magic" (SRC-C2@00:35:14).
  "Charger fault: automatic rebook to another EVSE; ops console if none is free" (SRC-D2#7).
- **Source B:** "So for the ops console, on top of the automation: one, 'charger down — rebook everyone': the system
  proposes reassignments, ops approves in bulk, drivers get notified in their language" (SRC-C2@00:53:00); Amperlane's
  engineer added reason codes rather than objecting (SRC-C2@00:53:32).
- **Rule applied:** later > earlier gives SRC-D2#7 (automatic), as for CF-017. Both versions are Intellias' proposals;
  the only client reaction is to the automatic one ("magic"), and the COO wants a taken booking moved "to another free
  one" (SRC-C2@00:24:04). Read in full, bulk approval sits "on top of the automation".
- **Status:** resolved-provisional (Gate 1 second review, Mykola Marchuk, 2026-10-28): automatic reassignment within the
  same site; ops bulk-approves proposals for bookings that cannot be placed and can undo a move (A-017, design.md F5).
  Dana Whitfield confirms by 2026-11-06; Luis Ortega is consulted on the cap (Q-038).

### CF-023 · What "no double booking in the database" covers before T-15
- **Source A:** The exclusion constraint on EVSE × time range "applies only to active states — held or confirmed"
  (SRC-C2@00:31:51). The CTO had approved the constraint just before: "Yes. That's what I want." (SRC-C2@00:31:45).
- **Source B:** Bookings are made against a pool, and the EVSE is assigned only around T-15 (SRC-C2@00:24:36, agreed
  SRC-C2@00:24:52). Before allocation, capacity is protected by a per-site "capacity bucket" (SRC-D2#12).
- **Rule applied:** later > earlier gives SRC-D2#12. Held and confirmed bookings carry no EVSE, so the EVSE-level
  constraint can only bite at allocation. The bucket that protects capacity before then is Intellias' design and has
  not been put to the client.
- **Result:** ADR-006 records the agreed scope (database-enforced exclusion at EVSE level). The pre-allocation capacity
  check is assumption A-014, to be prototyped in Phase 0.
- **Gate 1 decision (Mykola Marchuk, 2026-10-28):** A-014 is accepted as a working hypothesis. It is not put to the
  client before the proposal; the Phase 0 prototype and simulator test it, and the CTO sees the result there.
- **Status:** resolved-provisional.

### CF-024 · Is there a cash gap whatever the business model?
- **Source A (vendor, internal):** "Whatever they pick: stations want weekly payouts, fleets pay net-30, so there's a
  cash gap of up to ~8 weeks" (SRC-R1#model).
- **Source B:** "So if you're merchant of record, that's a cash-flow gap" (SRC-C1@00:44:17). The weekly ask is
  conditional: "if you're holding our money, pay us weekly" (SRC-C2@00:35:42). The COO: "It's the eMSP idea… we'd sit
  in the middle of the money" (SRC-C2@00:36:18).
- **Rule applied:** specific > general. What the client actually said is conditional.
- **Result:** the cash gap exists only if Amperlane is merchant of record or otherwise holds station money (CTX-126). It
  depends on CF-008.
- **Status:** resolved.

### CF-025 · "All major CSMS" in the brief vs the systems actually reachable
- **Source A:** "All major CSMS: ChargePoint, EVgo, Electrify America, AMPECO, ChargeLab" (SRC-D1#10).
- **Source B:** The pilot touches AMPECO, ChargeLab and a legacy ChargePoint contract that has no usable API
  (SRC-C2@00:18:52, SRC-C2@00:19:30, SRC-C2@00:19:59). The CTO suspects "some aren't possible at all"
  (SRC-C1@00:41:59). Intellias' MVP scope covers AMPECO, ChargeLab, CSV and OCPI only (SRC-D2#10, SRC-D2#14).
- **Rule applied:** later, specific settles what the NYC sites use today. Whether any other network belongs in the March
  scope is a scope boundary, a decision in disguise (playbook §10.7); the CTO declined to commit to a list
  (SRC-C1@00:41:59).
- **Status:** needs-decision (Gate 1 second review, Mykola Marchuk, 2026-10-28; was resolved-provisional). Owners: Ravi
  Menon, Luis Ortega, with Dana Whitfield for the June supply plan (CTX-070); due 2026-11-06. Links: Q-036, CTX-142,
  CF-004. The proposal's baseline is A-022: March integrates only what the NYC launch sites and fleets use; other CSMS
  and Tesla Fleet API or Smartcar are priced as options.

### CF-026 · Observed vs modelled shift-change burst
- **Source A:** "We load-test at five times the observed burst" (SRC-D2#12 notes); "400 / 10 min shift-change burst,
  tested ×5" (SRC-D2#13).
- **Source B:** The observed worst 10 minutes today is 40–50 requests. The 400 is a launch model: "we modelled launch
  with the fleets in the pipeline and used about four hundred booking attempts in ten minutes" (SRC-C2@00:15:32).
- **Rule applied:** data > estimate, for what is *observed*.
- **Result:** observed is 40–50; 400 is the modelled launch burst, and the load-test target of 2,000 is 5× the model
  (CTX-055, CTX-115). SRC-D2#12 mislabels it.
- **Status:** resolved.
