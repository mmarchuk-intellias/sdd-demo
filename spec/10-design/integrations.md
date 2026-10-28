---
id: INTEGRATIONS
type: design
title: Integrations inventory (v0)
status: approved
owner: Mykola Marchuk
version: 0
kyiv: null
parents: [BUSINESS-CONTEXT]
sources: [SRC-D1, SRC-C1, SRC-C2, SRC-D2, SRC-R1]
---
# Integrations inventory, v0

Step 1b (prompt P1.3). This inventory lists **facts** about external systems as the sources give them; the rest of
`10-design/` is a v0 hypothesis (playbook §10.1).

**Status** means what exists today between Amperlane and the system: *in use* · *access granted* · *promised* ·
*proposed* (Intellias' idea, not agreed) · *not available*. **Risk** is H/M/L with the reason. "Unconfirmed" means
no source shows that the capability works for Amperlane.

## Inventory

| # | System | Purpose | Protocol / API · version | Current status | Data received | Data sent | Client-side owner | Risk | Sources |
|---|---|---|---|---|---|---|---|---|---|
| I-1 | **AMPECO** (Kinship, Gowanus) | Live status and charger-side holds at a pattern A site | REST + status webhooks; reservation endpoint, probably OCPP ReserveNow underneath. Version unknown. | Access granted (credentials); the prototype listener logs status, and nothing acts on it. | EVSE status (webhooks, at-least-once, duplicates seen); reservation result. Session records: **unconfirmed** (requested). | Reserve / cancel reservation. | Luis Ortega (relationship), Priya Nair (tech) | **M**: reservations work on 10 of 16 chargers only; no sandbox yet; session records unconfirmed | SRC-C2@00:14:11, SRC-C2@00:14:55, SRC-C2@00:34:36, SRC-C2@00:36:50 |
| I-2 | **ChargeLab** (Jamaica Bay, JFK Lot 9) | Live status at a pattern B site | "Open API": status and pricing. Version and push or poll: unknown. | Amperlane already holds the API docs from JFK; they are to be forwarded to Intellias. Whether Amperlane has API credentials is not stated. | EVSE status, pricing. Session records: **unconfirmed**. | None (no reservations). | Luis Ortega | **H**: status is the only live signal at the site that fills up, and its freshness and access are unconfirmed (Q-012) | SRC-C2@00:19:30, SRC-C2@00:37:23 |
| I-3 | **ChargePoint**, legacy network contract (Hunters Point, LIC) | Reconciliation only at a pattern C site; the CSV is not a live-status source | No usable API; CSV export from the portal, made by hand about twice a day. | In use (CSV export). | CSV with fields **unknown** (Q-011). | None. | Luis Ortega, the site host | **H**: no live status; billing-grade data unconfirmed | SRC-C2@00:19:59, SRC-C2@00:21:49 |
| I-4 | **OCPI 2.2.1 CPOs** (LA prospects; JFK "sometime in 2027") | Standard CPO connectivity in the eMSP role | OCPI 2.2.1: Locations, Tariffs, Sessions, CDRs, Tokens, Commands (RESERVE_NOW = hold now) | Proposed (Intellias: build in Phase 1 against a test CPO). No partner connected. | Locations, live EVSE status, tariffs, sessions, CDRs. | Tokens, commands (reserve). | Luis Ortega (partners) | **M**: no counterpart before LA; LA names and details pending (Q-008) | SRC-C2@00:11:56, SRC-C2@00:25:17, SRC-C2@00:25:36, SRC-C2@00:26:05 |
| I-5 | **Direct OCPP via CitrineOS** | Option for hosts without a CSMS (e.g. LIC) | OCPP 1.6 / 2.0.1 / 2.1; CitrineOS (Apache-2.0) exposes OCPI | Proposed option, not in the MVP (A-021); a business decision (Q-010), priced as an option | Full charger telemetry; reservations where firmware allows | OCPP commands | Ravi Menon, Luis Ortega | **M**: Amperlane would operate charger back-ends; the LIC contract is not ending soon | SRC-C2@00:21:55, SRC-C2@00:22:19, SRC-C2@00:22:42, SRC-C2@00:23:04 |
| I-6 | **OCPI 2.3 Booking module** | Native protocol-level booking (calendars, no-show fees) | Booking module added to OCPI 2.3 in June 2025; OCPI 2.3.0 itself came out in February 2025 | Roadmap only; US adoption likely low; out of MVP | — | — | — | **L** for the MVP (not planned) | SRC-C2@00:12:24, SRC-C2@00:13:01, SRC-D2#14 |
| I-7 | **NLR AFDC** (formerly NREL) | Discovery of non-partner chargers | REST at developer.nlr.gov; free key, 1,000 requests an hour | Priya Nair obtained a key in spring 2026 | Static data: location, connectors, power, network, hours. **No real-time availability.** | — | Priya Nair | **L** as discovery; the brief's "real-time availability" assumption is **contradicted** (CF-003) | SRC-C2@00:10:01, SRC-C2@00:10:23 |
| I-8 | **Open Charge Map** | Discovery of non-partner chargers | API; contributed data CC BY 4.0 (attribution check) | Proposed | Static station data | — | — | **L** | SRC-C2@00:11:03 |
| I-9 | **Geotab** (Borough Green, non-Tesla) | SoC, charging state, location for about 45% of Borough Green's fleet | Geotab API (version not stated); hardware already in the vehicles | Not in use; Amperlane's **access unconfirmed** (Q-014) | SoC, charging data, location (with consent) | — | Borough Green; Dana Whitfield (relationship) | **M**: access, consent and terms unknown | SRC-C1@00:06:52, SRC-C2@00:38:24 |
| I-10 | **Tesla Fleet API** | SoC and location for Borough Green Teslas (~55%) | Tesla Fleet API, pay-per-use since late 2024 | Not in use; an option pending a cost decision (CF-004) | SoC, location (streamed signals) | Commands (wake) | Ravi Menon, Borough Green | **M**: cost owner undecided; owner authorisation and driver consent needed | SRC-C2@00:38:50, SRC-C2@00:39:22, SRC-C2@00:40:39 |
| I-11 | **Smartcar** | Generic vehicle data across about 30 EV brands | Smartcar API | Proposed (compare with the Tesla Fleet API in Phase 0) | SoC, charging state, location | — | Ravi Menon | **L/M**: cost and reliability not compared yet | SRC-C2@00:39:34, SRC-C2@00:39:53 |
| I-12 | **Stripe** | Fleet invoicing today; payouts, invoicing and 1099s in options B/C | Today: Stripe Billing (customers, invoices), no Connect. Proposed: Connect, separate charges and transfers, Invoicing net-30. | In use (Billing). Connect (weekly payouts, net-30 invoicing) is in the Call 2 recap that the CTO confirmed, but it applies only if money flows through Amperlane (Q-001) and counsel confirms it (Q-019); see ADR-011. Adyen for Platforms was named as an alternative. | Payment status, payout status (webhooks) | Invoices, transfers to connected accounts | Ravi Menon | **M**: depends on the business model and legal confirmation (Q-001, Q-019) | SRC-C2@00:03:28, SRC-C2@00:45:58, SRC-C2@00:46:46, SRC-C2@00:47:10, SRC-C2@00:56:15, SRC-C2@00:56:43 |
| I-13 | **Twilio** | Driver messaging: booking by SMS, confirmations, reminders | SMS (inbound webhook bot); WhatsApp via Twilio proposed | SMS in use; **WhatsApp not in use** (Q-034) | Inbound messages (webhook retries cause duplicates today) | Outbound SMS/WhatsApp in EN/ES/BN | Priya Nair | **M**: the duplicate-message bug exists today; WhatsApp setup unconfirmed | SRC-C2@00:02:58, SRC-C2@00:33:05, SRC-C2@00:33:20, SRC-C2@00:50:56 |
| I-14 | **Uber / Lyft driver apps** | Hand-off between apps | Deep links only. The Uber Driver API is limited-access with no vehicle data; Lyft has no public API. | Not available beyond deep links; out of MVP | — | — | — | **L** for the MVP; the brief's "data" assumption is **contradicted** (CF-005) | SRC-C2@00:42:43, SRC-C2@00:43:07 |
| I-15 | **Maps / routing** | Directions, arrival ETA | Google Maps (brief) vs Valhalla on OSM or Mapbox (Intellias) | Provisional: Google Maps (CF-020, A-030); the CTO confirms in Phase 0 | Routes, ETA | Origin and destination | Ravi Menon | **L** | SRC-D1#9, SRC-D2#10 |
| I-16 | **OpenEI URDB** | Utility tariff context for dynamic pricing | API | Proposed for Phase 2 or later (dynamic pricing is out of MVP) | Tariffs | — | — | **L** | SRC-D2#10, SRC-D2#14 |
| I-17 | **Airtable, Google Sheets, Retool** (pilot tooling); also Stripe Billing and Twilio logs | Source of the pilot history migration | Airtable export, Sheets export; Stripe Billing and Twilio logs are candidate sources (Q-020) | In use; raw export promised | About a year of bookings, statuses, arrivals; status values changed twice; Sheets and Airtable disagree | — | Priya Nair | **M**: data quality, and moved bookings show as no-shows (CF-018) | SRC-C2@00:02:00, SRC-C2@00:05:22, SRC-C2@00:52:53, SRC-C2@00:58:37, SRC-D2#18 |
| I-18 | **Supabase prototype** (Next.js 14) | None (to be discarded); schema for reference only | Postgres (Supabase) | Exists, never in production; schema promised | Schema only | — | Priya Nair | **L** | SRC-C2@00:03:52, SRC-C2@00:04:20, SRC-C2@00:58:41 |
| I-19 | **CSMS wishlist beyond the pilot**: ChargePoint (as a network), EVgo, Electrify America | Supply from major networks | Not stated | **No source confirms any access, contact or API** for Amperlane | — | — | Luis Ortega | **H** if assumed for the MVP; none is needed at the three pilot sites | SRC-D1#10, SRC-C1@00:41:59, SRC-R1#comp |

Out of scope for the MVP and listed for completeness: **OpenADR 3.0** demand response (SRC-D2#14). **Adyen for Platforms** is an
alternative to Stripe Connect, considered "only for pricing at scale" (SRC-C2@00:47:10).

Test tooling, not a production integration: **EVerest** (LF Energy) as a charger simulator, to run many misbehaving
chargers and replay the Gowanus fault (SRC-C2@00:23:23, SRC-C2@00:55:51).

## Assumed but unconfirmed capabilities

These are capabilities that the client's brief, or Intellias' direction deck, assumes and that the sources do not
confirm. The v0 design must not depend on them without a flag. It uses U-6, U-7, U-13 and U-14 only where they are
flagged, each with a fallback, except settlement (U-6, U-7), which has none (design.md §6, risk 6). Gate 1 (Mykola
Marchuk, 2026-10-28) accepted this for v0; confirmation comes through Q-009, Q-011 and Q-012.

| # | Assumed capability | Assumed in | What the sources show | Follow-up |
|---|---|---|---|---|
| U-1 | Real-time reservation on every charger via OCPP | SRC-D1#9 | Only 10 of 16 Gowanus chargers; ReserveNow is "hold now", not a future slot | CF-002 (resolved) |
| U-2 | Real-time station availability from NREL | SRC-D1#9 | Static data only | CF-003 (resolved) |
| U-3 | Battery data from Tesla | SRC-D1#9, SRC-D1#10 | No integration; pay-per-use; consent required | CF-004, Q-015 |
| U-4 | Data from the Uber/Lyft driver apps | SRC-D1#10 | Not available | CF-005 (resolved) |
| U-5 | "All major CSMS" (ChargePoint, EVgo, Electrify America, AMPECO, ChargeLab) | SRC-D1#10 | Only AMPECO (Gowanus) and ChargeLab (JFK) touch the pilot. The CTO "suspects some aren't possible at all". | I-19 |
| U-6 | Per-session records (CDR equivalent) from AMPECO and ChargeLab | SRC-C2@00:47:29, SRC-D2#5 (G12) | Requested from Kinship; not confirmed for either CSMS | Q-009, Q-012 |
| U-7 | Billing-grade session data at LIC from the CSV | SRC-C2@00:47:29 | CSV fields unknown; export is manual | Q-011 |
| U-8 | Live status within 60 seconds at JFK | SRC-C2@00:49:30 | ChargeLab gives status, but push or poll and latency are unknown | Q-012 |
| U-9 | Access to Borough Green's Geotab data | SRC-D2#14 | Geotab is fitted, but nobody has confirmed access for Amperlane | Q-014 |
| U-10 | WhatsApp messaging via Twilio | SRC-C1@00:06:09, SRC-C2@00:51:03 (drivers ask for it); SRC-D2#13, SRC-D2#14 | The pilot uses Twilio SMS only | Q-034 |
| U-11 | Reservation support at the LA OCPI prospects | SRC-D2#8 ("to confirm") | Unknown | Q-008 |
| U-12 | Funds held and moved by Stripe avoid money-transmitter licensing | SRC-D2#5 (G12) | Intellias' view; counsel must confirm | Q-019 |
| U-13 | The LIC attendant will use an attendant app (report status, confirm arrivals, place signs) | SRC-C2@00:21:55, SRC-D2#6, SRC-D2#14 | Intellias' idea; no Amperlane speaker or site host agreed. The client only said the attendant could put up QR codes (SRC-C2@00:40:24) | Q-010, Q-005 |
| U-14 | A session-start event from the CSMS can serve as the arrival signal | SRC-C2@00:40:06, SRC-D2#7 | AMPECO is confirmed only to send "webhooks for status changes"; ChargeLab's events are unknown; LIC has none | Q-009, Q-012 |
