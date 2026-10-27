---
id: SRC-R1
type: source
title: Amperlane — Account brief
kind: internal recap
origin: Intellias presales (internal wiki page)
original: R1_Amperlane_Client_Recap_Oct2026.html
sha256: 12285f04bc10557f516e307f66ab7722745de283a0c84bed69eafbb6271914da
generated_by: tools/extract.py  # do not edit; regenerate instead
---

# SRC-R1 · Amperlane — Account brief

Presales · North America Team space

- 2026 Pipeline
- Mobility & EV
  - Amperlane
    - Account brief
    - Call notes 2026-09-29
    - Call notes 2026-10-08
    - Solution direction (v1.2)
    - Estimation workbook
  - Fleetwise RFP (lost)
  - Charging OEM — Q2 renewal
- Templates
- Archive

Presales · North America/Mobility & EV/Amperlane

# Amperlane — Account brief

Owned by Kyrylo Shvedov ·Last updated Oct 19, 2026 by Mark Feldman ·7 min read

[ev-charging] [marketplace] [new-logo] [us-east] [fy27-q1]

TL;DR Seed-stage Brooklyn startup (raised $6.7M) wants a partner to build its EV fleet ↔ charger booking platform. Hard date: NYC go-live Mar 1, 2027. Phase 1 budget "around a million, give or take". Solution direction sent Oct 16, costed proposal due Nov 6. Biggest blocker: their business model isn't decided, and that drives the settlement design.

| Status | [Solutioning] [Proposal due Nov 6] |
|---|---|
| Opportunity | [PRESALE-2291] · Phase 1 ~$0.9–1.2M (T&M or fixed, TBD) · follow-on LA + scale 2027–28 |
| Source | Referral, Hudson Mobility Partners board member (Sep 15) |
| Client partner | @Mark Feldman |
| Presales team | @Kyrylo Shvedov (engagement lead) · @Olena Marchuk (SA) · @Andriy Bondar (payments/integrations) |
| Delivery center | TBD, likely Mobility BU |

On this page

1. Company
2. People
3. Pilot
4. Business model
5. Market context
6. Competition
7. Risks
8. Open questions / next steps

## SRC-R1#company — Company

| Legal entity | Amperlane, Inc. (Delaware C-corp) |
|---|---|
| HQ | Industry City, Sunset Park, Brooklyn, NY |
| Founded | March 2024 |
| Headcount | 14 FTE (3 founders, 4 ops/driver support EN/ES/BN, 2 partnerships, 2 eng, 1 design, 1 finance, 1 marketing) |
| Funding | Pre-seed $1.2M (Jun 2024, angels) · Seed $5.5M (Feb 2026), led by Hudson Mobility Partners with Gridline Ventures |
| Runway | to ~Q4 2027. Series A planned H2 2027 |
| A-round milestone | 10,000 completed bookings/month by June 2027, NYC only (LA doesn't count) |
| Website | amperlane.io |

What they do: a two-sided marketplace. Charging stations publish bookable capacity (sites, EVSEs, connectors, power, schedule, live status, tariffs). EV taxi/rideshare fleets and their drivers book slots, Dana calls it "cinema-seat booking for chargers". Amperlane keeps the margin on the match.

Why NYC first: TLC Green Rides pushes Uber/Lyft trips to zero-emission (25% in 2026, 100% by 2030) and the city has ~13k electric FHVs on ~360 public fast-charging ports. Revel left rideshare in Aug 2025, so fleets lost a dedicated charging option.

## SRC-R1#people — People

| Name | Role | Background | Notes for us |
|---|---|---|---|
| Dana Whitfield | Co-founder, CEO | 9 yrs NYC FHV industry; ran EV charging logistics for ~300 cars at a Queens FHV base | Economic buyer. Fast, optimistic, no patience for "consultant talk". Owns the Mar 1 date and the A-round story. |
| Luis Ortega | Co-founder, COO / Partnerships | 6 yrs site acquisition & partnerships at a US DCFC network | Station-side reality check. Anything that costs stations money needs his OK. |
| Ravi Menon | Co-founder, CTO | Ex-staff eng, payments infra (marketplace payouts) at a NYC fintech. Joined Jan 2025 | Technical decision maker. Wants IP ownership + no lock-in. TS / Postgres / AWS ($100k Activate credits). Will grill us on settlement. |
| Priya Nair | Senior SWE | Built Retool/Airtable ops tooling, maintains the Supabase prototype | Best source on where the pilot breaks. Wants to be embedded in the squad. |

## SRC-R1#pilot — Pilot ("Amperlane Concierge")

Live since Oct 2025 in Brooklyn and Queens. Almost fully manual: Retool front-end, Airtable bookings, a Google Sheets slot grid per site, Twilio SMS bot, ops staff phoning stations to cone off stalls. Drivers still pay the station with their own card; Amperlane bills fleets $2.00 per completed booking through Stripe Billing.

### Numbers (Sep 2026, from client)

| Metric | Value | Comment |
|---|---|---|
| Bookings / month | ~2,300 | ~1,850 completed |
| No-show rate | 17% | [not in their deck] came out on Call 1 |
| Late >10 min | 22% | [not in their deck] |
| Arrival-to-plug wait (median) | 31 → 6 min | self-reported driver survey, n=212 |
| Gowanus off-peak utilisation | 14% → 23% | 10 AM–3 PM and 10 PM–5 AM |
| Avg energy / session | ~28 kWh | in line with public rideshare data (24–30 kWh) |
| Weekly active drivers | 186 |  |

### Supply: 3 sites / 46 DC ports

| Site | Operator | Ports | CSMS | Integration |
|---|---|---|---|---|
| Gowanus FastHub (Brooklyn) | Kinship Charging | 16 · 150–320 kW · CCS1 + 4 NACS | AMPECO | [API] REST + webhooks. Reservations only on 10/16 chargers (firmware) |
| JFK Lot 9 Charging Plaza (Queens) | Jamaica Bay Energy | 20 · 150 kW · CCS1 | ChargeLab | [Status only] status + pricing, no reservations. OCPI 2.2.1 "sometime in 2027" |
| LIC Garage Depot | Hunters Point Garages LLC | 10 · 62.5–125 kW · CCS1 | Legacy ChargePoint contract | [No API] portal CSV export; garage attendant on site |

### Demand: 2 fleets

- Borough Green Fleet LLC: ~420 EVs on weekly leases to independent Uber/Lyft drivers, ~160 drivers in the pilot. ~55% Tesla (no integration yet), rest on Geotab.
- Five Boroughs EV Cab Co.: 12 electric medallion cabs, 24 drivers on two shifts, no telematics. Shift change 4–5 PM = the booking burst.

Heads-up Last Tuesday before Call 2 a 320 kW unit at Gowanus went down at ~1:50 PM (cooling). Ops re-did 9 bookings by hand, 3 got moved to JFK. Good test scenario for the booking engine.

## SRC-R1#model — Business model

Not decided The model in their brief didn't survive the discovery call. Workshop with Dana + Luis planned for the week of Oct 26.

| Option | What | Status |
|---|---|---|
| A · Take rate (in the brief) | 10–12% of charging GMV paid by stations + $15/vehicle/month fleet SaaS. Their projection: $4.8M ARR in 2028 | [Stations refuse %] Gowanus runs single-digit margins after demand charges |
| B · eMSP spread | Amperlane is merchant of record: buys at station B2B tariff (~$0.42/kWh at Gowanus), bills fleets bundled rate (~$0.49/kWh incl. guaranteed slot) + fleet subscription + pass-through no-show fees | [Floated by Dana] Call 1 |
| C · Hybrid | Stations pay only for incremental off-peak bookings; fleets get one monthly invoice, net-30 | [Open] |

Whatever they pick: stations want weekly payouts, fleets pay net-30, so there's a cash gap of up to ~8 weeks. Ravi asked about money transmission; our line is to keep funds flows inside Stripe Connect, but their counsel has to confirm.

## SRC-R1#market — Market context

Checked Oct 2026. Use dates when quoting to the client.

- NYC Green Rides: 5% (2024) → 15% (2025) → 25% (2026) → 100% by 2030. Industry at 22.7% vs 25% in Mar 2026, TLC says "on track". [1] [2]
- NYC fleet (Jul–Oct 2025): 103,790 active FHVs, 13,020 electric. 13,587 medallion taxis, 31 electric. [3]
- ~360 public fast-charging ports in NYC (TLC, Sep 2025). [4]
- US DC fast charging Q3 2026: avg $0.540/kWh, utilisation 15.9% national, 31.8% in LA. [5]
- CA Clean Miles: 30% eVMT target in 2026, but CPUC staff recommended a 3-year pause (Jun 2026). Affects how hard LA demand is. [6]
- Uber electric share of US/Canada miles 9.1% in Q1 2026, first decline. [7]
- Federal 45W (commercial EVs) ended Sep 30, 2025; 30C (chargers) ended Jun 30, 2026. [8]

## SRC-R1#comp — Competition / adjacent players

| Who | What | So what |
|---|---|---|
| Voltera + Revel | Combination announced May 26, 2026, 1,000+ stalls operating or in development across 11 metros, fleet + AV focus [9] | Supply partner or competitor, Dana isn't sure which |
| Hubject Reservation Hub | EU pilot (Sep 2025) for truck slot booking across networks on OCPI 2.3 booking module [10] | Closest precedent. US adoption of OCPI 2.3 booking is low |
| EVgo | Launched reservations in 2021 on the West Coast [11] | Current status unknown, don't cite as live |
| Tesla Superchargers | Congestion fee $0.50/min (up to $1.00) after 5-min grace at busy sites [12] | Queue tax a booking layer could replace |
| Uber / Lyft | No public API with vehicle data [13] | Deep links only in MVP. One of them has an EV team interested in a pilot, needs SOC 2 Type I |

## SRC-R1#risks — Risks

| Risk | Impact | Mitigation / owner |
|---|---|---|
| Station APIs not ready (only Gowanus can hold a charger) | [High] | Own slot calendar + soft holds, CSV/attendant path for LIC. Olena |
| Business model undecided | [High] | Workshop wk of Oct 26. Kyrylo |
| Cash gap (weekly payouts vs net-30) | [Med] | Ledger, per-fleet credit limits; client's financing call. Andriy |
| Telematics cost / consent (Tesla Fleet API is pay-per-use) | [Med] | Manual SoC fallback in MVP |
| SOC 2 Type I within 12 months vs Mar 1 launch | [Med] | Controls built in from day one, audit after launch |
| 10k bookings/month by June needs new NYC supply, not just software | [Med] | Client side (Luis). Flag in proposal |
| Regulatory shifts (CA Clean Miles pause, NEVI) | [Low] | Keep LA plan flexible |

## SRC-R1#open — Open questions / next steps

▸ Open questions for the client (10)

1. Business model: % fee, spread or both? Merchant of record?
2. No-show policy: who pays by default, fee + station share, any overbooking?
3. Station terms: capacity caps, grace period, payout terms per site
4. LA: which of the two OCPI 2.2.1 prospects, when do we get access?
5. LIC: CSV + attendant, or move host to direct OCPP (CitrineOS)?
6. Teslas: will Borough Green pay for Tesla Fleet API or start with manual SoC?
7. SOC 2 Type I: target date, auditor, ride-hail pilot in Phase 1 or not?
8. Data migration scope (Airtable, Stripe Billing, Twilio logs)
9. Funds flow: counsel to confirm Stripe Connect structure
10. Which new NYC sites/fleets are realistic by June 2027?

### Action items

- Send solution direction deck to Dana/Ravi (@Olena Marchuk, Oct 16)
- Get anonymised pilot sample (received Oct 5)
- Schedule business-model workshop, wk of Oct 26 (@Kyrylo Shvedov)
- AMPECO sandbox + ChargeLab API docs via Luis (@Andriy Bondar)
- Full raw pilot export (Airtable + Sheets) from Priya
- Estimation workbook v1 + staffing check with Mobility BU (@Mark Feldman, by Oct 30)
- Costed proposal out by Nov 6

### Attachments

PPTX Amperlane_Platform_Partner_Brief_Sep2026.pptx client · Sep 22

DOCX Amperlane_Call1_Discovery_Transcript_2026-09-29.docx Sep 29

DOCX Amperlane_Call2_Tech_DeepDive_Transcript_2026-10-08.docx Oct 8

PPTX Intellias_Amperlane_Solution_Direction_Oct2026.pptx sent Oct 16

* * *
References

1. [SRC-R1#r1] NYC Mayor's Office, Green Rides rule (Aug 2023) <https://www.nyc.gov/mayors-office/news/2023/08/mayor-adams-tlc-new-rules-require-city-s-rideshare-vehicles-be-zero-emission>
2. [SRC-R1#r2] TLC testimony, preliminary budget (Mar 17, 2026) <https://www.nyc.gov/assets/tlc/downloads/pdf/testimony_preliminary_budget_3_17_26.pdf>
3. [SRC-R1#r3] Preliminary Mayor's Management Report FY2026, TLC <https://www.nyc.gov/assets/operations/downloads/pdf/pmmr2026/tlc.pdf>
4. [SRC-R1#r4] TLC, Climate Week 2025 update <https://www.nyc.gov/site/tlc/about/tlc-climate-week-2025-record-electrification-gains.page>
5. [SRC-R1#r5] mgrid on Paren Q3 2026 (Oct 16, 2026) <https://mgrid.org/2026/10/16/us-fast-chargers-pass-80964-ports-but-utilization-stays-flat-at-15-9-as-tesla-raises-prices/>
6. [SRC-R1#r6] CPUC, Clean Miles Standard progress report (Jun 2026) <https://www.cpuc.ca.gov/-/media/cpuc-website/divisions/consumer-protection-and-enforcement-division/documents/tlab/clean-miles-standard/cms-unanticipated-barriers-progress-report-june-2026.pdf>
7. [SRC-R1#r7] Uber sustainability report (Apr 2026) <https://www.uber.com/kr/zh/about/reports/sustainability-report>
8. [SRC-R1#r8] IRS FAQ, Public Law 119-21 credit changes <https://www.irs.gov/newsroom/faqs-for-modification-of-sections-25c-25d-25e-30c-30d-45l-45w-and-179d-under-public-law-119-21-139-stat-72-july-4-2025-commonly-known-as-the-one-big-beautiful-bill-act-obbb>
9. [SRC-R1#r9] Automotive World, Voltera and Revel (May 2026) <https://www.automotiveworld.com/news/voltera-and-revel-agree-ev-charging-merger-in-us/>; TechCrunch, Revel exits ride-hail (Aug 2025) <https://techcrunch.com/2025/08/11/revel-shuts-down-its-ride-hail-business-to-focus-on-ev-charging>
10. [SRC-R1#r10] electrive, Hubject reservation solution (Sep 2025) <https://www.electrive.com/2025/09/03/hubject-and-partners-present-reservation-solution-for-electric-commercial-vehicles>
11. [SRC-R1#r11] InsideEVs, EVgo reservations (2021) <https://insideevs.com/news/510452/evgo-launches-reservation-program/>
12. [SRC-R1#r12] Tesla Supercharger fees <https://www.tesla.com/support/charging/supercharger/fees>
13. [SRC-R1#r13] Uber Driver API reference <https://developer.uber.com/docs/drivers/references/api>

## SRC-R1#comments — Comments

3 comments

[SRC-R1#c1] Mark Feldman · Oct 19, 2026

Dana pinged me Friday, they liked the "what changed since your brief" slides. She wants the workshop on Tue Oct 27 if we can. Also asked if we can do fixed price for Phase 1, I said we'd look at it after Phase 0.

[SRC-R1#c2] Olena Marchuk · Oct 19, 2026

Fixed price is risky until the settlement model is decided and we've seen the AMPECO sandbox. I'd keep Phase 0 fixed and Phase 1 T&M with a cap.

[SRC-R1#c3] Kyrylo Shvedov · Oct 19, 2026

+1. Tue 27th works for me, will send the invite with the 3 options as pre-read.
