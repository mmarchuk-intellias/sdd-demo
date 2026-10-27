---
id: SRC-D2
type: source
title: 'Amperlane Platform: Our understanding and solution direction'
kind: vendor deck
origin: Intellias (vendor), sent to client
original: D2_Intellias_Amperlane_Solution_Direction_Oct2026.pptx
sha256: f7c233298ca46ffcdd84dd7d8dd145b3187270617b808f9a2705bcb9b025da8d
generated_by: tools/extract.py  # do not edit; regenerate instead
---

# SRC-D2 · Amperlane Platform: Our understanding and solution direction

_Prepared for Amperlane, Inc., October 16, 2026_ · author: Intellias

## SRC-D2#1 — Amperlane Platform

Amperlane Platform

Our understanding & solution direction

Prepared for Amperlane, Inc.  ·  October 16, 2026

Confidential  ·  For discussion, not an estimate

Book.
Arrive.
Charge.

**Speaker notes:**

Thank you for the brief and two very open calls. This deck is our playback: how we understood the request, what changed since the brief, and how we see the architecture and solution in general. It is a direction, not an estimate: the costed proposal follows on November 6.

## SRC-D2#2 — Where we are in the process

amperlane/01-understanding

Where we are in the process

Sep 22

Your brief

Platform Partner Brief

Sep 29

Discovery call

business and scope

Oct 8

Tech deep-dive

integrations, payments, NFRs

Oct 16

This deck

understanding and direction

Nov 6

Costed proposal

scope, plan, estimate

What this deck is

How we understood your request
Where the facts moved since the brief
Architecture and solution direction
Phase outline and team shape
The questions we need answered

What it is not (yet)

A detailed estimate or price
A fixed scope or delivery plan
A final business-model decision

2

**Speaker notes:**

Recap the path so far: your brief on September 22, discovery on September 29, the technical deep-dive on October 8. This deck closes the listening phase. Be explicit that it is not an estimate: we went back to think further, and the numbers come with the proposal on November 6.

## SRC-D2#3 — What we heard: the problem in your words

amperlane/01-understanding

What we heard: the problem in your words

25%

of Uber/Lyft trips must be zero-emission or WAV in 2026 (industry at 22.7% in March)

13,020

electric FHVs in NYC, against about 360 fast-charging ports

15.9%

average US DC fast-charger utilisation (21.1% in the top 30 metros)

Fleets and drivers

Drivers lose 30+ minutes finding and waiting for chargers, plus deadhead miles. On a weekly lease, idle time is lost income.

Pilot: median wait 31 → 6 min*

Charging stations

Low utilisation and thin margins after demand charges. A held stall that sits empty costs real money.

Pilot: Gowanus off-peak utilisation 14% → 23%

Sources: NYC TLC Green Rides rule (nyc.gov, Aug 2023); TLC testimony, Mar 17, 2026; Mayor’s Management Report FY2026 (Jul–Oct 2025 fleet data); TLC Climate Week, Sep 2025 (port count); Paren Q3 2026 via mgrid, Oct 16, 2026.  *Pilot figure, self-reported driver survey, n=212.

3

**Speaker notes:**

Both sides of the marketplace hurt. NYC regulation pushes rideshare to electric faster than fast charging grows, while stations nationally still sit idle most of the day. The pilot already shows the value on both sides. Market numbers are real and sourced at the bottom; the pilot numbers are yours.

## SRC-D2#4 — What changed since your brief (1/2)

amperlane/01-understanding

What changed since your brief (1/2)

Brief said

We learned

Implication

G1

Call 2

“Real-time reservation on every charger (OCPP)”

Only Gowanus can reserve, on 10 of 16 chargers. JFK: status only. LIC: CSV export. ReserveNow is optional and means “hold now”, not a future slot.

Amperlane owns the slot calendar: soft holds, ReserveNow at T-15 min where supported, ops fallback.

G2

Call 2

“NREL API for real-time station availability”

NREL is now NLR (since Dec 2025). The AFDC station API has static data only, no real-time availability.

Live status from CSMS APIs or OCPI 2.2.1 Locations. AFDC and Open Charge Map for discovery only.

G3

Call 1

“10–12% take rate on charging GMV, paid by stations”

Stations refuse a % of energy revenue (single-digit margins). They value incremental off-peak bookings. Fleets want one net-30 invoice.

Option on the table: Amperlane as eMSP and merchant of record, earning a spread. Decision needed.

G4

Call 1

No mention of no-shows or late arrivals

Pilot: 17% no-shows, 22% arrive more than 10 min late. Stations demand a no-show fee and a 10-min grace period.

Auto-release after 10-min grace; no-show fee with payer as fleet policy; one-tap “cancel / running late” and instant re-offer to late drivers.

G5

Call 1

“Driver app + fleet portal”

Five actor types (six with finance). Drivers live in the Uber/Lyft apps all day and won’t install a heavy app: SMS/WhatsApp, in EN, ES and BN.

Light mobile web app (PWA) plus messaging. Station portal and ops console join the scope.

4

**Speaker notes:**

The key slide. Each row traces one assumption from your brief to what we learned on the calls and what it means for the build. G1 is the biggest: chargers cannot give you future slots, so Amperlane must own the calendar. G3 and G4 change the money flows and the booking rules.

## SRC-D2#5 — What changed since your brief (2/2)

amperlane/01-understanding

What changed since your brief (2/2)

Brief said

We learned

Implication

G6

Call 1

Stations give all their ports

Bookable capacity is capped at 30–50% of ports at peak, more off-peak. Walk-up capacity and NEVI public-access rules apply.

Capacity rules per site and per time window are a first-class part of the domain.

G7

Call 2

“Tesla API for vehicle battery data”

Geotab covers the non-Teslas only. Teslas (~55%) have no integration and Tesla Fleet API is pay-per-use. The cab company has no telematics.

Pluggable telematics: Geotab, Tesla Fleet API, Smartcar fallback, manual SoC. Driver consent built in.

G8

Call 2

“Uber/Lyft driver apps (deep link + data)”

Uber Driver API is limited-access with no vehicle data; Lyft has no public API. A large platform’s EV team wants SOC 2 Type I within 12 months.

Deep links only in the MVP. Start the SOC 2 readiness path now.

G10

Call 1

“MVP in 12 weeks”, no budget, no date

Hard date: NYC production launch by March 1, 2027. Phase 1 budget around $1M. LA next (Q3 2027); 10 metros is a 2028 ambition.

Scope is cut to the date: NYC-first MVP, LA and scale in Phase 2.

G12

Call 2

Settlement not mentioned

Stations want weekly payouts, fleets pay net-30, and disputes are settled against OCPI CDRs or CSMS session records.

Stripe Connect for payouts (it can file & deliver 1099s), funds kept inside Stripe, CDR-based reconciliation.

5

**Speaker notes:**

Second half. Capacity caps, telematics and the Uber/Lyft reality shrink the integration list; the March 1 date and the settlement terms shape the MVP. G-numbers match the open-items log we keep with your team.

## SRC-D2#6 — Actors and their jobs

amperlane/01-understanding

Actors and their jobs

Fleet manager

Set booking policies, see no-shows and utilisation, get one monthly invoice

Fleet portal

Driver

Independent contractor. Grab a slot in seconds between trips, arrive, plug in

SMS / WhatsApp + PWA · EN, ES, BN

CPO / station operator

Publish capacity rules, protect walk-up capacity, see bookings and payouts

Station portal

Site attendant

See who is due at which stall, confirm arrivals at sites without an API

Attendant view (PWA)

Amperlane ops

Manual holds, overrides, “charger down → rebook everyone”, no-show disputes

Ops console

Finance

Weekly station payouts, net-30 fleet invoices, reconciliation against CDRs

Finance views + Stripe

6

**Speaker notes:**

Your brief named two users; we count six. The driver and the site attendant shape the channel choice: SMS or WhatsApp plus a light web app, not another heavy native app. Ops and finance are the users who make the marketplace run day to day.

## SRC-D2#7 — Core domain: the bookable slot

amperlane/02-solution

Core domain: the bookable slot

Inventory: what can be booked

Site

partner location

EVSE

one bookable charging point

Connector

CCS1 or NACS, max kW

Capacity rules

bookable % per time window

Slot calendar

15-min grid · 30/45/60-min bookings · 10-min buffer

Booking lifecycle

Hold
TTL 3 min to confirm

Confirmed
slot is reserved in our calendar

Reminder
SMS or WhatsApp

Station hold
ReserveNow at T-15 min where supported

Arrived
geofence, QR at stall or session start

Charging
live session status

Completed
CDR or session record

Settled
invoice and payout

Exceptions

Charger fault: automatic rebook to another EVSE; ops console if none is free

Station hold failed or previous session overruns → reassign to a compatible free EVSE at T-10; else ops

No-show: no arrival within the 10-min grace → auto-release, no-show fee

Dispute: checked against the CDR or CSMS session record

7

**Speaker notes:**

The heart of the platform is Amperlane's own slot calendar, because chargers cannot hold future slots. A booking moves through a fixed lifecycle; only the station-hold step depends on what the site supports. Exceptions are designed in from day one: a charger fault triggers automatic rebooking; if the station hold fails or the previous session overruns we reassign to a compatible free EVSE at T-10, else ops steps in; no-shows release automatically after the 10-minute grace; disputes are checked against the CDR. Durations, buffer and TTL are starting values to confirm with stations.

## SRC-D2#8 — Integration reality: three supply patterns

amperlane/02-solution

Integration reality: three supply patterns

A

API + reservations

Where

Gowanus · AMPECO (REST + webhooks), reservations on 10 of 16 chargers. LA prospects on OCPI 2.2.1 (reservation support to confirm).

How we hold a slot

Amperlane calendar + OCPP ReserveNow at T-15 min where the charger supports it

Station-side guarantee

B

Status only

Where

JFK Lot 9 · ChargeLab open API: status and pricing, no reservations. OCPI 2.2.1 maybe in 2027.

How we hold a slot

Soft hold in Amperlane, “Reserved” signage at the stall, ops fallback

Station-side guarantee

C

No API

Where

LIC Garage Depot · legacy ChargePoint contract, status only as a portal CSV export.

How we hold a slot

CSV ingest + attendant app, or move the host to direct OCPP via CitrineOS

Station-side guarantee

One booking engine for all three. Only the “station hold” step changes.

Roadmap: OCPI 2.3 Booking module
since June 2025; US adoption likely low

8

**Speaker notes:**

Today's three sites happen to cover the three patterns we will meet in every metro. The booking engine is the same for all three; only the station-hold step and the confidence of the guarantee change. Pattern C has a choice: an attendant workflow on top of the CSV, or moving the host to direct OCPP with CitrineOS. OCPI 2.3 Booking is the long-term native path, but US adoption is likely low, so it stays on the roadmap.

## SRC-D2#9 — Business model options: decision needed

amperlane/02-solution

Business model options: decision needed

Option A

Percentage take rate

10–12% of charging GMV, paid by stations, plus a $15/vehicle/month fleet fee

Station % rejected

Option B

eMSP spread, Amperlane as merchant of record

$0.42

$0.49

station B2B tariff /kWh

fleet bundled rate /kWh

incl. guaranteed slot, plus fleet subscription and pass-through no-show fees. Illustrative Gowanus numbers.

Option C

Hybrid

The spread plus a smaller booking or percentage fee, and the fleet subscription

Open

If B or C, the platform must add:

Stripe Connect: separate charges and transfers

Fleet invoicing, net-30, one invoice per fleet

eMSP role: OCPI 2.2.1 sessions, CDRs, tariffs

Pricing module and CDR reconciliation

9

**Speaker notes:**

We are not deciding this for you, but the choice drives the settlement design, so we need it before the proposal. Option A is off the table for stations. Option B uses the illustrative Gowanus numbers from the discovery call: about 7 cents per kWh on an average 28 kWh pilot session is roughly 1.96 dollars, close to today's 2 dollar pilot fee per booking, before subscription and no-show fees. Option C mixes a smaller fee with the spread. Proposal: a business-model workshop in the week of October 26.

## SRC-D2#10 — Solution architecture (logical)

amperlane/02-solution

Solution architecture (logical)

Channels

Edge

Core

Integration

Data

Platform

Driver PWA + SMS / WhatsApp

Fleet portal

Station portal

Ops console

API gateway
routing, rate limiting

Keycloak
identity, SSO, roles

Modular monolith  ·  TypeScript / NestJS

Inventory & Availability

Booking & Calendar

Pricing & Tariffs

Fleet & Vehicles

Settlement & Payouts

Notifications

Identity & Access

Audit

Temporal
workflow engine: hold TTLs, reminders, T-15 station hold, no-show release, rebook sagas. Self-hosted or Temporal Cloud

OCPI 2.2.1 eMSP gateway
Locations · Sessions · CDRs · Tariffs

CSMS adapters
AMPECO · ChargeLab · CSV ingest

CitrineOS
direct OCPP hosts (no CSMS)

Telematics adapters
Geotab · Tesla Fleet API · Smartcar

Stripe Connect
payouts · invoicing · 1099 filing

Twilio
SMS · WhatsApp

PostgreSQL + PostGIS
bookings, holds, geo

Time series
native partitioning on RDS

Valkey (ElastiCache)
rate limits, idempotency

Event bus
EventBridge/SQS → Kafka

AWS  ·  ECS Fargate, RDS

Terraform

OpenTelemetry + Grafana

Built for Amperlane (your IP)

Open source / open data

Commercial / managed

External data

NLR AFDC + Open Charge Map
discovery only

OpenEI URDB
tariff context

Valhalla on OSM
routing, ETA (or Mapbox)

10

**Speaker notes:**

A modular monolith in TypeScript keeps a small team fast and the IP yours; modules have clean seams so they can be split out later. Temporal runs everything with a timer: hold expiry, reminders, the station hold at T-15, no-show release, and rebooking sagas. The integration layer hides the three supply patterns from the core. Holds live in Postgres; Valkey only caches rate limits and idempotency keys. Status and metering series use native Postgres partitioning on RDS for the MVP; TimescaleDB only if volume justifies it. Discovery data from NLR AFDC and Open Charge Map never drives availability. Open source where it is mature, commercial services where they are commodity rails.

## SRC-D2#11 — Open source vs commercial

amperlane/02-solution

Open source vs commercial

Open source   own the code, no lock-in

NestJS (TypeScript)  ·  MIT

Modular monolith in the stack your team prefers

PostgreSQL + PostGIS  ·  PostgreSQL Licence / GPL-2.0

Exclusion constraints and geo queries in one database

PostgreSQL partitioning (RDS)  ·  built in

MVP time series; TimescaleDB later only if volume justifies (Timescale License)

Valkey (on ElastiCache)  ·  BSD-3

Rate limiting and idempotency cache; holds stay in Postgres

Temporal  ·  MIT

Durable timers; self-hosted vs Temporal Cloud, both costed in proposal

Keycloak  ·  Apache-2.0

SSO and roles across four portals

CitrineOS (LF Energy)  ·  Apache-2.0

Direct OCPP 1.6 / 2.0.1 / 2.1 for hosts without a CSMS

Valhalla + OpenStreetMap  ·  MIT / ODbL

Routing and arrival ETA

OpenTelemetry + Grafana  ·  Apache-2.0 / AGPL-3.0

Vendor-neutral observability, SOC 2 evidence

Commercial   buy the commodity rails

AWS (ECS Fargate, RDS)  ·  your $100k Activate credits

Your preferred cloud; managed ops for a small team

Stripe Connect  ·  per active account + per payout¹

Payouts; can file & deliver 1099s for connected accounts

Twilio  ·  usage-based

SMS and WhatsApp, already used in the pilot

Geotab · Tesla Fleet API · Smartcar  ·  paid APIs

Vehicle SoC across a mixed fleet

AMPECO · ChargeLab APIs  ·  partner CSMS

Live status and reservations at partner sites

Own the booking core. Buy the rails. Adapters keep every vendor swappable.

¹ Stripe Connect “you handle pricing”: $2 per monthly active account, plus 0.25% + 25¢ per payout (Stripe pricing). Tesla Fleet API: pay-per-use since late 2024.

11

**Speaker notes:**

Rule of thumb: own the booking core and the data model, use mature open source with permissive or well-understood licences, and buy the commodity rails: cloud, payments, messaging, vehicle data. Nothing here locks the core to a vendor; adapters isolate every commercial API. TimescaleDB is not offered on Amazon RDS and its key features (continuous aggregates, retention, compression) are under the Timescale License, so the MVP uses native Postgres partitioning. Valkey is the BSD-licensed fork; Redis 7.4+ is RSALv2/SSPL and Redis 8 adds AGPLv3. Licences to be re-confirmed in the proposal.

## SRC-D2#12 — The “no double booking” design

amperlane/02-solution

The “no double booking” design

Tap “Book”
driver, fleet or ops

Idempotency key
retries never duplicate

Per-site queue
single writer at burst

Capacity bucket
take 1 unit, FOR UPDATE

Soft hold
TTL 3 min to confirm

Confirmed
against the pool

T-15 allocation
one EVSE, exclusion constraint

-- 1  Book: take one unit from the pool
SELECT remaining FROM capacity_bucket
WHERE site_id = $1 AND connector_type = $2
AND slot_start = $3  FOR UPDATE;
UPDATE capacity_bucket SET remaining = remaining - 1 ...;
--    CHECK (remaining >= 0): cap never exceeded
-- 2  At T-15: assign a specific EVSE
ALTER TABLE evse_allocation ADD CONSTRAINT one_car_per_evse
EXCLUDE USING gist (evse_id WITH =, slot WITH &&);

One bucket row per site, connector type and 15-min slot; it also enforces the 30–50% bookable cap. The exclusion constraint needs btree_gist.

×5 headroom

Load test: 2,000 booking attempts in 10 min, against the ~400-attempt shift-change burst

Overbooking: off by default

A per-site policy later, only if the station agrees. Buffers absorb overstays from the previous session.

12

**Speaker notes:**

A booking is made against a pool, not a stall. The idempotency key stops double taps and SMS retries from creating two bookings. At the 4 to 5 PM shift change a single writer per site serialises attempts. Each booking takes one unit from a per-site, per-connector-type capacity bucket for each 15-minute slot, decremented in the same transaction under SELECT FOR UPDATE with a CHECK that remaining never goes below zero; that bucket is also where the station's 30 to 50 percent bookable cap lives. The soft hold has a 3-minute TTL. Around T-15 the booking is allocated to a specific EVSE, and the allocation table carries an exclusion constraint, so two cars can never be assigned to one EVSE. Overbooking stays off unless a station agrees to a policy. We load-test at five times the observed burst.

## SRC-D2#13 — NFRs and compliance

amperlane/02-solution

NFRs and compliance

≤ 60 s

station status freshness

< 300 ms

booking API latency, p95

99.9%

availability, 5 AM–1 AM ET

400 / 10 min

shift-change burst, tested ×5

NY SHIELD Act

Safeguards + breach notice for credentials, licence and account data. Location: consent, minimisation, retention by design.

SOC 2 Type I

+ pen test; readiness path from day one

Audit trail

every hold, override and payout

EN · ES · BN

notifications and driver PWA

13

**Speaker notes:**

These are the targets we heard on October 8; they become acceptance criteria in the proposal. Two items have lead time: SOC 2 Type I plus a pen test, which a large rideshare platform asked for within 12 months, and NY SHIELD Act safeguards and breach notice for credentials, licence and account data; driver location is handled by design with consent, minimisation and retention limits. Both are cheaper to design in now than to retrofit.

## SRC-D2#14 — MVP scope for the March 1, 2027 NYC launch

amperlane/03-delivery

MVP scope for the March 1, 2027 NYC launch

In: March 1, 2027

Booking for supply patterns A, B and C

Driver PWA + SMS / WhatsApp (EN, ES, BN)

Fleet portal (basic)

Station portal: capacity rules, payouts view

Ops console: holds, overrides, rebook, disputes

Attendant view (PWA)

OCPI 2.2.1 eMSP gateway (tested vs simulator CPO)

Stripe Connect payouts + fleet invoicing

Geotab + manual SoC entry

Migration of pilot history

Out: Phase 2 and later

Native iOS / Android apps

Dynamic pricing (TOU via OpenEI URDB)

OCPI 2.3 Booking module

OpenADR 3.0 demand response

Uber / Lyft beyond deep links

LA launch

Autonomous (AV) fleets

14

**Speaker notes:**

The date is fixed, so scope is the lever. In: everything needed to run real bookings at all three NYC supply patterns, get paid and pay stations, and migrate the pilot history. Out, but designed for: native apps, dynamic pricing, OCPI 2.3, OpenADR, deeper ride-hail integration, LA and autonomous fleets.

## SRC-D2#15 — Phasing (indicative)

amperlane/03-delivery

Phasing (indicative)

2026

2027

2028

Nov

Dec

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Phase 0 · Inception
3 weeks · Nov 9–27

Phase 1 · MVP build
~13 wks · Nov 30 – Feb 26

Phase 2 · LA and scale
Q2–Q3 2027

Phase 3 · Next wave
OCPI 2.3, dynamic pricing, AV depots

MVP build

hypercare (March)

Scale

LA launch target

Mar 1, 2027
NYC production launch

June 2027
10k completed bookings/mo

Indicative only. The plan and estimate come with the costed proposal on November 6.

15

**Speaker notes:**

Phase 0 is a three-week inception, November 9 to 27, to lock scope, the business model and integration access. Phase 1 builds the MVP in about thirteen weeks, November 30 to February 26, with slack for the holidays, so New York launches on March 1, followed by a hypercare month in March. Phase 2 takes the platform to LA and to scale through Q2 and Q3 2027; Phase 3 is the 2028 wave. Important: the 10,000 completed bookings per month by June 2027 must come from New York alone, through Phase 1 plus NYC supply growth; LA, in Phase 2 with a Q3 2027 target, does not count toward it.

## SRC-D2#16 — Team shape (indicative, not an estimate)

amperlane/03-delivery

Team shape (indicative, not an estimate)

1

Engagement lead / PO proxy

1

Solution architect

3–4

Full-stack TypeScript engineers

1

Integration engineer (EV protocols)

1

QA automation engineer

0.5

DevOps engineer

0.5

Product designer

part-time

Payments specialist

Plus your side: Priya and your product designer embedded in the squad, founders as product owners.

16

**Speaker notes:**

This is the shape of a Phase 1 team, not a quote. One cross-functional squad, led by an engagement lead acting as PO proxy alongside your founders. Integration and payments expertise sits in the team because that is where the risk is. We would like Priya and your product designer embedded with us, which also covers knowledge transfer and keeps the IP fully yours.

## SRC-D2#17 — Risks and assumptions

amperlane/03-delivery

Risks and assumptions

Station API readiness

AMPECO reservations work on 10 of 16 chargers; JFK and LIC have no reservations. Mitigation: patterns B and C from day one, sandbox access now.

Business model undecided

Merchant-of-record vs fee changes settlement, invoicing and the eMSP role. Mitigation: decide in the Oct 26 week.

Telematics cost and consent

Tesla Fleet API is pay-per-use; drivers must consent; the cab fleet has no telematics. Mitigation: manual SoC fallback.

Regulatory shifts

CPUC staff recommended pausing CA Clean Miles (June 2026); NEVI was suspended and re-issued in 2025. Mitigation: LA plan stays flexible.

Voltera–Revel

Combination announced May 26, 2026: 1,000+ stalls, operating or in development, across 11 US metros. Supply partner or competitor.

SOC 2 vs March 1

Type I within 12 months for the ride-hail pilot. Mitigation: controls and evidence built in, audit after launch.

Cash gap

Stations paid weekly, fleets pay net-30 (up to ~8 weeks exposed). Mitigation: ledger, per-fleet credit limits, financing decision in the workshop.

Real-world context: CPUC staff recommendation, June 2026; Voltera and Revel announcement, May 26, 2026 (announced, not closed); NEVI guidance, Aug 2025.

17

**Speaker notes:**

The top risks we see today, each with how we propose to handle it. The first two are on the critical path for the March date: station API access and the business-model decision. The cash gap needs a financing decision alongside the business model. The regulatory and competitive items are context, not blockers, but they shape LA and the station-partner pitch.

## SRC-D2#18 — Open questions before the proposal

amperlane/03-delivery

Open questions before the proposal

1

Business model: percentage fee, spread, or both? Is Amperlane merchant of record?

2

No-show policy: who pays by default, fee and station share, and is any overbooking acceptable?

3

Station terms: capacity caps, grace period and payout terms per site?

4

LA: which of the two OCPI 2.2.1 prospects, and when do we get access?

5

LIC: CSV + attendant, or migrate the host to direct OCPP (CitrineOS)?

6

Tesla vehicles: will Borough Green pay for Tesla Fleet API, or start with manual SoC?

7

SOC 2 Type I: target date, auditor, and is the ride-hail pilot in Phase 1?

8

Data migration: which pilot history (Airtable, Stripe Billing, Twilio logs)?

9

Funds flow: will your counsel confirm the Stripe Connect structure avoids NY money-transmitter licensing?

10

Supply: which new NYC sites and fleets are realistic by June 2027 to reach 10k completed bookings?

18

**Speaker notes:**

We need these answered, or at least an owner and a date for each, to turn this direction into a costed proposal. The first two are the most important; we suggest covering them in the business-model workshop.

## SRC-D2#19 — Next steps

amperlane/03-delivery

Next steps

Week of Oct 26

Business-model workshop

Founders + Intellias

ASAP

AMPECO sandbox and ChargeLab API docs

Amperlane (Luis)

Follow-up

Full raw pilot export (Airtable + Sheets)

Amperlane (Priya) · after the anonymised sample of Oct 5

Nov 6

Costed proposal

Intellias

Your Intellias team

Mark Feldman
Client Partner, North America

Kyrylo Shvedov
Engagement Lead

Olena Marchuk
Solution Architect

Andriy Bondar
Payments & Integrations Lead

19

**Speaker notes:**

Four concrete steps to get from here to the costed proposal on November 6. Two of them are on your side: sandbox and API access, and the full raw pilot export from Airtable and Sheets, following the anonymised sample you sent on October 5. Thank you, and we are happy to take questions now or in the workshop.
