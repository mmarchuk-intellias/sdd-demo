---
id: BUSINESS-CONTEXT
type: context
title: Amperlane business and platform context
status: approved
owner: Mykola Marchuk
version: 1
kyiv: null
parents: []
sources: [SRC-D1, SRC-C1, SRC-C2, SRC-D2, SRC-R1]
---
# Business and platform context

Step 1a (prompt P1.1). Each fact is a `CTX-###` with its sources. The context describes what the sources say. It
does not design the platform.

**By** says who the fact comes from. This matters for the Requirements Quadrant in Step 2:

- **C**: stated by the client (SRC-D1, or an Amperlane speaker in SRC-C1/C2).
- **V**: Intellias' statement or interpretation only (SRC-D2, SRC-R1, or an Intellias speaker).
- **V→C**: proposed by an Intellias speaker and agreed on the record by an Amperlane speaker (both cited).

**Confidence** rates how well the statement is supported, separately from who made it: high (specific, on record,
consistent across sources) · medium (single mention, estimate, or contingent on an open decision) · low (unverified,
or found only in the internal brief SRC-R1). Conflicts are in [conflicts.md](conflicts.md); unknowns are in
[open-questions.md](open-questions.md).

## 1. Company and goals

| CTX | Statement | Sources | By | Confidence |
|---|---|---|---|---|
| CTX-001 | Amperlane, Inc. was founded in March 2024. It has its HQ in Industry City, Sunset Park, Brooklyn, and 14 people across ops, partnerships, product and engineering. | SRC-D1#2 | C | high |
| CTX-002 | Amperlane positions itself as "the booking layer between EV fleets and fast chargers" ("cinema-seat booking for chargers"). Stations publish slots, the fleet or driver books in two taps, gets a reminder, arrives and plugs in, and billing happens automatically. | SRC-D1#1, SRC-D1#5, SRC-D1#6, SRC-C1@00:03:57 | C | high |
| CTX-003 | Funding: a $5.5M seed (February 2026), led by Hudson Mobility Partners with Gridline Ventures. Runway lasts to about Q4 2027, and a Series A is planned for H2 2027. Total funding is disputed, see CF-014. | SRC-D1#2, SRC-C1@00:29:22 | C | high |
| CTX-004 | Amperlane wants a partner to build "Amperlane Platform v1" end to end: driver app, fleet portal, station portal, booking engine, and integrations (chargers, vehicles, payments, maps). | SRC-D1#11 | C | high |
| CTX-005 | The IP must belong to Amperlane: the code lives in Amperlane's repositories, in Amperlane's AWS accounts, managed by Amperlane's Terraform. | SRC-C2@00:06:05, SRC-C2@00:06:41 | V→C | high |
| CTX-006 | Delivery as one team: Amperlane engineers work in the same repos and rituals from Phase 0, with no black-box handover. The CTO wants Priya Nair to own the knowledge of the integration layer. | SRC-C2@00:55:08, SRC-C2@00:55:26, SRC-C2@00:55:32 | V→C | high |
| CTX-007 | Amperlane has two engineers. This is the reason given for a modular monolith over microservices. | SRC-C2@00:54:21, SRC-C2@00:54:57, SRC-R1#company | V | medium |
| CTX-008 | The rollout runs New York first, then Los Angeles. The CTO would rather "New York works perfectly than ten cities work badly". | SRC-C1@00:31:33, SRC-C1@00:32:38 | C | high |

## 2. Market and regulatory drivers

| CTX | Statement | Sources | By | Confidence |
|---|---|---|---|---|
| CTX-009 | The NYC TLC Green Rides rule requires 25% of Uber/Lyft trips to be zero-emission or wheelchair-accessible in 2026, rising to 100% by 2030. | SRC-D1#4, SRC-C1@00:03:18 | C | high |
| CTX-010 | In March 2026 the TLC testified that the industry was at 22.7% against the 25% target for 2026, and called it "on track". | SRC-C1@00:35:39, SRC-D2#3 | C | high |
| CTX-011 | NYC has 13,020 electric FHVs (Jul–Oct 2025) and about 360 fast-charging ports in the whole city (Sep 2025). | SRC-D1#4, SRC-C1@00:03:18, SRC-R1#market | C | high |
| CTX-146 | NYC has 13,587 medallion taxis, of which 31 are electric (Jul–Oct 2025). Five Boroughs' 12 electric cabs would be about 40% of them, so the electric cab segment is very small. | SRC-R1#market, SRC-C1@00:07:09 | V | low |
| CTX-012 | Public DC fast-charger utilisation, third-party data, each with its period and scope: US national about 16% (Q2 2026, Paren, quoted by the CEO) and 15.9% (Q3 2026, Paren); California 22.2% (Q1 2026, CPUC); Los Angeles 31.8% (Q3 2026). See CF-012. | SRC-C1@00:03:18, SRC-D1#3, SRC-R1#market, SRC-R1#r5 | C (US Q2, CA), V (US Q3, LA) | medium |
| CTX-013 | Fleet-side pain: drivers lose 30+ minutes per charge finding a free charger and waiting, plus deadhead miles, and shift changes collide at the same few sites. On a weekly lease, waiting time is lost income. | SRC-D1#3, SRC-C1@00:03:18, SRC-C1@00:05:11 | C | medium |
| CTX-143 | The CEO frames the problem as timing, not capacity: "it's not a shortage at all hours, it's a shortage at the wrong hours." | SRC-C1@00:03:18, SRC-C1@00:03:53, SRC-C1@00:03:57 | V→C | high |
| CTX-014 | Station-side economics: utility demand charges (one 5 PM spike sets much of the monthly bill) leave thin margins. Luis Ortega estimates Gowanus runs at single-digit margins after demand charges. | SRC-C1@00:17:22 | C | medium |
| CTX-015 | Revel shut down its NYC rideshare service on 11 Aug 2025 to focus on fast-charging hubs (five in New York, one in San Francisco at the time). | SRC-D1#4, SRC-C1@00:33:54 | C | high |
| CTX-016 | Voltera and Revel announced a combination on 26 May 2026 (announced, not known to be closed): 1,000+ stalls operating or in development across 11 US metros, focused on fleet and autonomous charging. It could be a supply partner or a competitor; there has been one friendly, non-committal conversation. | SRC-C1@00:34:36, SRC-C1@00:34:57, SRC-C1@00:35:17 | C | high |
| CTX-017 | Sites funded by the federal NEVI programme have public-access obligations, so for them the bookable cap is a compliance matter, not only a commercial one. None of the three pilot sites is NEVI-funded, but some prospects are, especially outside New York. The client wants this built in from day one. | SRC-C1@00:27:12, SRC-C1@00:27:37 | C | high |
| CTX-018 | NEVI-funded stations must support OCPP 2.0.1 and OCPI 2.2.1 (23 CFR 680.108). The NEVI programme was suspended and re-issued in 2025. | SRC-C2@00:12:24, SRC-D2#17 | V | medium |
| CTX-019 | California: CARB's Clean Miles Standard targets 30% electric miles in 2026, but CPUC staff recommended a three-year pause in June 2026. The LA case therefore rests on utilisation, not regulation. | SRC-C1@00:36:12, SRC-C1@00:36:33 | C | high |
| CTX-020 | Tesla Superchargers already charge congestion fees: typically $0.50/min, up to $1.00, after a 5-minute grace. Drivers understand the concept and hate it. | SRC-C1@00:10:26, SRC-R1#comp | C | medium |
| CTX-021 | Other market context: the federal 45W credit (commercial EVs) ended 30 Sep 2025 and 30C (chargers) ended 30 Jun 2026; Uber's electric share of US/Canada miles fell for the first time to 9.1% in Q1 2026; the average US DC fast-charging price is $0.540/kWh (Q3 2026). | SRC-R1#market | V | low |
| CTX-022 | OCPI 2.3.0 (Feb 2025) added a Booking module in June 2025 (calendars, licence-plate link, no-show fees). US adoption is likely low. The closest precedent is Hubject's Reservation Hub pilot (Sep 2025, Europe, trucks). | SRC-C2@00:12:24, SRC-C2@00:13:01, SRC-R1#comp | V | medium |
| CTX-023 | The Uber Driver API is limited-access and has no vehicle or EV data; Lyft has no public driver or fleet API. | SRC-C2@00:42:43, SRC-C2@00:43:01 | V→C | high |

## 3. Users and actors

| CTX | Statement | Sources | By | Confidence |
|---|---|---|---|---|
| CTX-024 | Five actor types touch a booking: fleet manager, driver, station operator, site staff (e.g. the garage attendant) and Amperlane ops. The CEO confirmed the attendant is a user. | SRC-C1@00:08:34, SRC-C1@00:08:44, SRC-C1@00:46:07 | V→C | high |
| CTX-025 | Intellias adds a sixth actor, Finance (weekly station payouts, net-30 fleet invoices, reconciliation). Fleet-side and Amperlane-side finance people appear in the calls, but the client has not confirmed Finance as a platform user. See CF-011. | SRC-D2#6, SRC-C1@00:19:12, SRC-C2@00:47:08 | V | medium |
| CTX-026 | Borough Green drivers are independent contractors who lease an EV weekly from the fleet and drive for Uber and Lyft all day, switching between the apps. The fleet is their "landlord", not their employer. | SRC-C1@00:04:48, SRC-C1@00:05:11 | C | high |
| CTX-027 | Drivers will not download an app, create an account and add a card. They will text, or tap a link to a light browser page. About half of them asked for WhatsApp. | SRC-C1@00:05:47, SRC-C1@00:06:09 | C | high |
| CTX-028 | Many drivers are more comfortable in Spanish or Bengali; the ops team is bilingual for that reason. Many Bengali-speaking drivers live on WhatsApp. | SRC-C1@00:06:13, SRC-C2@00:51:03 | C | high |
| CTX-029 | The person who books is not always the person who charges. At the cab company the day driver usually books; long-term drivers who lease both shifts book the afternoon and the overnight slot together; sometimes the owner books. | SRC-C1@00:07:40, SRC-C1@00:11:16 | C | high |
| CTX-030 | Small fleets barely use a portal. Five Boroughs is the owner and a nephew ("give them a login, they'll forget the password"). Intellias' reading, not confirmed by the client: for such fleets the value is in messaging and in Amperlane ops. | SRC-C1@00:25:00, SRC-C1@00:25:21 | C (portal), V (where the value is) | high |
| CTX-031 | Borough Green's fleet manager asked for booking controls: "My drivers only book at these sites, max twice a day." | SRC-C1@00:25:00 | C | high |
| CTX-032 | Borough Green's finance lead wants one consolidated invoice a month, net-30, and will not deal with 160 drivers' card receipts. | SRC-C1@00:19:12, SRC-C2@00:35:57 | C | high |
| CTX-033 | At LIC there is no operator in the usual sense. A garage attendant in a booth physically puts a "Reserved" sign on the stall when ops call, and is one of the most reliable partners. | SRC-C1@00:08:08, SRC-C1@00:08:29 | C | high |
| CTX-034 | The physical part (cones, signs, the attendant) will stay at some sites for a while. Intellias concludes that the platform must therefore tell the people on site what to do, not only the chargers. | SRC-C1@00:40:15, SRC-C1@00:40:25 | C (physical part stays), V (conclusion) | high |
| CTX-035 | The ops console is a core product, not an admin panel. It needs: manual holds and booking on behalf of a driver, overrides (force-confirm, force-release, extend grace), "charger down, rebook everyone" with bulk approval, and a no-show dispute workflow. It is not in the brief's architecture. Bulk approval was added by Intellias on Call 2 (SRC-C2@00:53:00), after the CEO's "All of those", so that part is a vendor proposal (CF-022). | SRC-C1@00:38:52, SRC-C1@00:39:22, SRC-C1@00:39:49, SRC-C2@00:53:00, SRC-C2@00:53:49 | V→C | high |
| CTX-036 | Every booking state change carries a reason code and an actor (system or human), e.g. "moved — charger fault", not "no-show". All of it goes into the audit log. | SRC-C2@00:53:32, SRC-C2@00:53:40, SRC-C2@00:53:46 | V→C | high |
| CTX-037 | Stations would value seeing what a fault costs them ("charger 7 is down and it's costing you six bookings"). Luis Ortega sees this as leverage with their maintenance teams. | SRC-C2@00:35:14 | C | high |

## 4. Current process: the "Amperlane Concierge" pilot

| CTX | Statement | Sources | By | Confidence |
|---|---|---|---|---|
| CTX-038 | The concierge pilot has been live in Brooklyn and Queens since October 2025: 3 partner sites, 46 DC fast-charging ports, 2 fleets, about 2,300 bookings per month. | SRC-D1#7, SRC-C1@00:03:57 | C | high |
| CTX-039 | Pilot outcomes (Sep 2026): about 1,850 bookings a month complete. No-shows are 17%, and 22% of all bookings arrive more than 10 minutes late. Neither figure is in the deck. Data quality caveat: see CF-018. | SRC-C1@00:08:56, SRC-C1@00:09:10 | C | medium |
| CTX-040 | Median arrival-to-plug wait fell from 31 to 6 minutes (self-reported driver survey, n=212). Off-peak utilisation at Gowanus (10 AM–3 PM, 10 PM–5 AM) rose from 14% to 23%. | SRC-D1#7, SRC-C1@00:45:14 | C | medium |
| CTX-041 | Main cause of late arrivals and no-shows: a ride request comes in on the way to the charger ("the forty-dollar ride"). Drivers can text CANCEL today, but nobody does because they are driving. | SRC-C1@00:12:08, SRC-C1@00:12:20, SRC-C1@00:12:42 | C | high |
| CTX-042 | Pilot tooling: Retool on top of Airtable, where each booking is a row (driver, fleet, site, slot, status). Each site has a Google Sheet slot grid (15-minute rows × stall columns, coloured by hand). A nightly script copies some of it to Airtable. In practice the source of truth is the sheet the ops person on shift has open. | SRC-C2@00:02:00, SRC-C2@00:02:34 | C | high |
| CTX-043 | Booking flow today: the driver texts a code (e.g. "GOW 1645") to a Twilio SMS bot; the bot drops a request into Airtable; ops confirm it by hand. For the stall: at Gowanus ops sometimes make the hold in the system and sometimes phone the site; at JFK they phone; at LIC they phone the attendant, who puts up the sign. | SRC-C1@00:05:34, SRC-C2@00:02:58, SRC-C1@00:37:27 | C | high |
| CTX-044 | The SMS bot sometimes runs twice on one message, so about twice a week a driver gets two confirmations. | SRC-C2@00:33:20 | C | high |
| CTX-045 | Four people work on driver support and ops, all bilingual. A normal day means dozens of phone calls. | SRC-C1@00:37:27, SRC-C1@00:38:15 | C | high |
| CTX-046 | Held stalls are released by hand: whoever is on site gets tired of waiting and takes the cone, or ops calls them. | SRC-C1@00:10:12 | C | high |
| CTX-047 | Charger faults are found and handled by hand. Example: a 320 kW unit at Gowanus failed around 1:50 PM (cooling). Nobody at Amperlane knew until a driver texted at 2:15. Nine bookings (2:15 to about 7 PM) were redone by two ops people; three moved to JFK, and one cab driver was lost. The station was angry "because nobody told them the stall had bookings". The moved bookings still show as no-shows in Airtable. | SRC-C2@00:51:36, SRC-C2@00:51:58, SRC-C2@00:52:32, SRC-C2@00:52:34, SRC-C2@00:52:53 | C | high |
| CTX-048 | Today Amperlane learns of a charger fault when a driver texts "it's broken", or sometimes from an email by Kinship. The AMPECO status webhook is logged, but nothing acts on it. | SRC-C2@00:34:26, SRC-C2@00:34:36 | C | high |
| CTX-049 | Connector mismatches happen. Teslas have been booked onto CCS stalls without an adapter, and an Ioniq onto a NACS stall (twice); ops fixed them on the spot. | SRC-C2@00:41:17, SRC-C2@00:41:28 | C | high |
| CTX-050 | Overstays ("sleepers", "the previous movie runs over") happen. Some days they are a bigger problem than no-shows: Gowanus has idle fees, but a rideshare driver at 74% will pay a couple of dollars and wait. | SRC-C1@00:40:55, SRC-C2@00:28:42 | C | high |
| CTX-051 | Money today: the driver pays the station directly (own card or station app), so energy money never touches Amperlane. Amperlane invoices fleets monthly in Stripe Billing, $2 per completed booking (customers and invoices only, no Connect). Stations pay Amperlane nothing. | SRC-C1@00:13:26, SRC-C1@00:13:40, SRC-C2@00:03:28 | C | high |
| CTX-052 | A freelancer-built Next.js 14 + Supabase driver app is about 35% done (auth, a map, a booking form), has no tests and never went to production. The CTO would discard it: there is no EVSE or connector in the data model, and a slot is a timestamp string. | SRC-C2@00:03:52, SRC-C2@00:04:20 | C | high |
| CTX-053 | A year of pilot history (bookings, no-shows, arrival times, driver, stall) is the only real dataset on how fleet drivers behave, and it will be in the Series A data room. It must be migrated properly, "not a CSV dump in an S3 bucket". | SRC-C2@00:04:43, SRC-C1@00:48:20 | C | high |
| CTX-054 | Pilot data quality: status values changed twice (early no-shows were recorded as "cancelled" with a note), and the Sheets and Airtable sometimes disagree. The data is decent from about February 2026. | SRC-C2@00:05:22 | C | high |
| CTX-055 | Today's worst 10 minutes bring 40–50 booking requests. | SRC-C2@00:15:32 | C | high |
| CTX-056 | The average pilot session is about 28 kWh. | SRC-C1@00:21:11 | C | medium |
| CTX-057 | The pilot has 186 weekly active drivers. This figure appears only in the internal brief. | SRC-R1#pilot | V | low |
| CTX-058 | A site is modelled today as stall number, max kW and a free-text connector field ("NACS" or "CCS"). | SRC-C2@00:16:36 | C | high |
| CTX-059 | Vehicle location and battery level come mostly from the driver. Borough Green has telematics on part of its fleet, but the pilot does not use it. | SRC-C1@00:06:52 | C | high |

## 5. Supply: partner sites and station terms

| CTX | Statement | Sources | By | Confidence |
|---|---|---|---|---|
| CTX-060 | Gowanus FastHub (Brooklyn) is run by Kinship Charging, an independent CPO: 16 ports, 150–320 kW, CCS1 plus four NACS, on the AMPECO CSMS (REST and webhooks). Reservations work on 10 of 16 chargers; the other six reject them (firmware, fix "on the list" after three requests). It is the best partner technically and in attitude. | SRC-C2@00:18:52, SRC-C2@00:14:11, SRC-C1@00:28:06 | C | high |
| CTX-061 | JFK Lot 9 (Queens) is run by Jamaica Bay Energy: 20 ports, 150 kW, all CCS1, on ChargeLab. ChargeLab's open API gives status and pricing, with no reservations. OCPI 2.2.1 peering is planned "sometime in 2027". At 4 PM the cone sometimes doesn't happen. | SRC-C2@00:19:30, SRC-C2@00:21:33 | C | high |
| CTX-062 | LIC Garage Depot (Long Island City) belongs to Hunters Point Garages, a garage owner, not a CPO: 10 ports, 62.5–125 kW, CCS1, on a legacy ChargePoint network contract. Status is visible in their portal, and Amperlane gets a CSV export made by hand "whenever the attendant remembers" (about twice a day). There is no usable API, and the contract "isn't ending tomorrow". | SRC-C2@00:19:59, SRC-C2@00:21:49, SRC-C2@00:23:04 | C | high |
| CTX-063 | The three sites are three supply patterns: A, API with reservations (Gowanus); B, status only (JFK); C, no API (LIC). Pattern C is not rare in New York (garages, depots, private hosts). | SRC-C2@00:20:38, SRC-C2@00:20:55 | V→C | high |
| CTX-064 | Stations never make all their ports bookable, because walk-ups need capacity. At peak 30–50% of ports at most are bookable (Gowanus about half, JFK about a third), and more off-peak. | SRC-C1@00:26:10 | C | high |
| CTX-065 | Bookable caps are set per site and per time window, and stations want to change them themselves (e.g. lower the cap for a big game at Citi Field). | SRC-C1@00:26:44, SRC-C1@00:26:54 | V→C | high |
| CTX-066 | Stations never bump a walk-up who is paying full public price. If the stall is taken, the booking moves to another free stall at the site; if the whole site is full (it happens at JFK), ops is pinged. | SRC-C2@00:24:04 | C | high |
| CTX-067 | Stations want a no-show fee and a short grace period (10 minutes is being discussed), with the stall released automatically after grace. They want the stall back more than the money: "If you hold my stall, you pay for my stall." | SRC-C1@00:09:27, SRC-C1@00:09:55, SRC-C1@00:10:26 | C | high |
| CTX-068 | Stations' first questions are "who's liable when a stall is blocked" and "how fast do I get paid"; they want money faster than monthly. If Amperlane holds their money, they want weekly payouts (Kinship: "if you're holding our money, pay us weekly"; Jamaica Bay the same). | SRC-C1@00:43:56, SRC-C2@00:35:42 | C | high |
| CTX-069 | Station contracts today are 2–3 page pilot letters. A draft partner agreement template (capacity commitment, no-show terms, payment terms) is under negotiation. It was promised for 1 Oct 2026 but is not among the inputs. | SRC-C1@00:43:27, SRC-C1@00:50:47 | C | high |
| CTX-070 | Supply growth by June 2027: the three sites plus three or four new ones is "possible, but tight". Prospects say "call us when it's real". | SRC-C1@00:42:37 | C | medium |
| CTX-071 | Two LA prospects already speak OCPI 2.2.1 (one has NEVI-funded sites, one roams with the big networks). One is under NDA. | SRC-C2@00:25:17, SRC-C2@00:26:53 | C | high |
| CTX-072 | Kinship's renewal is coming soon. Luis Ortega will ask for API sandbox access, the firmware fix on the six chargers, and per-session records via API. | SRC-C2@00:36:37, SRC-C2@00:36:50, SRC-C2@00:37:15 | V→C | high |

## 6. Demand: partner fleets

| CTX | Statement | Sources | By | Confidence |
|---|---|---|---|---|
| CTX-073 | Borough Green Fleet LLC has about 420 EVs leased weekly to independent Uber/Lyft drivers, about 160 of them in the pilot. About 55% are Teslas with no integration. Intellias says the non-Teslas (Ioniq 5, Niro, Equinox) carry Geotab, and Amperlane's engineer did not dispute it. | SRC-C1@00:04:48, SRC-C1@00:42:50, SRC-C2@00:38:24, SRC-C2@00:38:43 | C; Geotab detail V→C | high |
| CTX-074 | Five Boroughs EV Cab Co. is a small medallion operator: 12 electric cabs, 24 drivers on two shifts, no telematics, drivers on personal phones. | SRC-C1@00:07:09, SRC-C2@00:40:02 | C | high |
| CTX-075 | The cab shift change around 4–5 PM produces a wave of bookings, at the time stations are busiest. | SRC-C1@00:07:09, SRC-C1@00:07:31 | C | high |
| CTX-076 | Two more fleets are in talks. | SRC-C1@00:42:50 | C | medium |
| CTX-077 | Borough Green does not want to pay for drivers' behaviour (no-shows), but also does not want Amperlane to bill drivers directly. | SRC-C1@00:10:56 | C | high |
| CTX-078 | The EV team of one of the two big rideshare platforms (not named) wants a pilot. Its first request: SOC 2 Type I within 12 months of pilot start (roughly spring 2027 "if we're lucky") and a pen test. The CTO adds: "Earlier would be better, it helps the Series A too." | SRC-C2@00:43:30, SRC-C2@00:43:54 | C | high |

## 7. Constraints

### 7.1 Dates and budget

| CTX | Statement | Sources | By | Confidence |
|---|---|---|---|---|
| CTX-079 | Hard date: NYC production launch on 1 March 2027, with real stations, real fleets and no spreadsheets in the critical path. | SRC-C1@00:29:06 | C | high |
| CTX-080 | The phase-one budget is "around a million, give or take" ($0.9–1.2M), through the end of Q2 2027. Going above $1.2M needs "a very good reason". See CF-013. | SRC-C1@00:30:45, SRC-C1@00:30:57, SRC-C1@00:31:02 | C | high |
| CTX-081 | LA comes next, targeting Q3 2027. Ten metros is a 2028 ambition. See CF-007. | SRC-C1@00:31:33, SRC-C1@00:32:08 | C | high |
| CTX-082 | The brief asks for an "MVP in 12 weeks"; the CEO asked whether that is crazy. Intellias' answer, which the CEO called "a fair non-answer": a wish, with the plan worked backwards from 1 March, including time to test with real drivers. The CEO had already named 1 March as "the date that matters". See CF-006. | SRC-D1#11, SRC-C1@00:48:36, SRC-C1@00:48:45, SRC-C1@00:49:11, SRC-C1@00:29:06 | V | medium |
| CTX-083 | Vendor milestones: the solution-direction deck was sent on 16 Oct 2026 and the costed proposal is due 6 Nov 2026. Indicative phases: Phase 0 on 9–27 Nov, Phase 1 on 30 Nov–26 Feb, hypercare in March 2027. | SRC-C2@00:57:40, SRC-D2#15 | V | medium |
| CTX-084 | The business model must be decided before settlement is designed in detail, ideally within three weeks of 8 Oct. The workshop is planned for the week of 26 Oct; the CTO said "earlier is better" because the CEO travels the week after. Per Intellias' internal notes, the CEO asked for Tue 27 Oct. | SRC-C2@00:48:32, SRC-C2@00:58:48, SRC-C2@00:59:01, SRC-R1#c1 | V→C; the date is V | high |

### 7.2 Technology

| CTX | Statement | Sources | By | Confidence |
|---|---|---|---|---|
| CTX-085 | Stack preference: TypeScript end to end, PostgreSQL, AWS (using $100k in AWS Activate credits). Open source only where it is mature. | SRC-C2@00:06:05 | C | high |
| CTX-086 | No CSMS vendor SDK may sit in the booking core. If a station switches CSMS, Amperlane swaps an adapter and does not rewrite the engine. | SRC-C2@00:06:50, SRC-C2@00:07:08 | C | high |
| CTX-087 | Architecture is a modular monolith, not microservices. | SRC-C2@00:54:21, SRC-C2@00:54:45 | V→C | high |
| CTX-088 | OCPP reservations are optional (firmware or operator may reject them), and ReserveNow means "hold from now until expiry", not a future slot. Amperlane therefore owns the slot calendar; a charger at best gets "hold now" about 15 minutes before the slot. | SRC-C2@00:07:35, SRC-C2@00:08:09, SRC-C2@00:08:48, SRC-C2@00:13:32, SRC-C2@00:26:27 | V→C | high |
| CTX-089 | NREL is now the National Laboratory of the Rockies (NLR). Its AFDC station API holds static data only (location, connectors, power, network, hours): free key, 1,000 requests an hour, no real-time availability. It is suitable for discovery only. | SRC-C2@00:10:01, SRC-C2@00:10:23, SRC-C2@00:11:03 | V→C | high |
| CTX-090 | Live status comes only from CSMS APIs, or from OCPI 2.2.1 Locations where the operator peers with Amperlane. Partner sites with an API are live; LIC's only live feed is the attendant (CTX-062); everything else is a static map layer. | SRC-C2@00:11:03, SRC-C2@00:11:38, SRC-C2@00:20:33 | V→C | high |
| CTX-091 | Duplicate AMPECO webhooks have been seen in the logs, and at-least-once delivery is "a guess". Intellias assumes duplicates and out-of-order delivery for all webhooks (AMPECO, payments, Twilio), so consumers must be idempotent and a periodic poll must reconcile. The CTO agrees webhooks are "never the only path". | SRC-C2@00:14:55, SRC-C2@00:15:02, SRC-C2@00:15:14, SRC-C2@00:33:05 | V→C | high |
| CTX-092 | A booking is made against a pool of compatible EVSEs at the site; the actual EVSE is assigned late, around T-15 min ("drivers don't care about stall 4"). | SRC-C2@00:24:36, SRC-C2@00:24:52 | V→C | high |
| CTX-093 | No double booking, ever, enforced by the database (exclusion constraint on EVSE × time range). A single-writer queue per site at burst time gives fairness and instant alternatives. Every booking request carries an idempotency key, and inbound SMS is deduplicated by message ID. | SRC-C2@00:31:16, SRC-C2@00:31:45, SRC-C2@00:32:16, SRC-C2@00:32:46, SRC-C2@00:32:51, SRC-C2@00:33:05, SRC-C2@00:33:15 | V→C | high |
| CTX-094 | Timers (hold expiry, T-15 hold, grace, auto-release) run as durable workflows, not cron jobs, on Temporal. The CTO prefers self-hosting (no extra vendor contract in year one). | SRC-C2@00:33:32, SRC-C2@00:33:51 | V→C | high |
| CTX-095 | The ledger is double-entry, not "balance" columns (CTO). Intellias added "append-only", and the CTO did not object. | SRC-C2@00:46:41, SRC-C2@00:46:46 | C (double-entry), V (append-only) | high |
| CTX-096 | The driver interface is a light mobile web app (PWA) plus messaging, with no native app in the MVP; the CEO agreed. Intellias puts native apps in Phase 2; the client has not said so. See CF-001. | SRC-C1@00:06:33, SRC-C2@00:51:10, SRC-C2@00:51:22, SRC-C2@00:51:29 | V→C; Phase 2 is V | high |
| CTX-097 | Notifications go out in English, Spanish and Bengali, by SMS and WhatsApp, both through Twilio. | SRC-C2@00:50:56, SRC-C2@00:51:03 | V→C | high |
| CTX-098 | Uber and Lyft: deep links only in the MVP. Context such as "trip ended" comes from the driver. Anything beyond deep links is Phase 2. | SRC-C2@00:43:07, SRC-C2@00:43:24, SRC-C2@00:43:30 | V→C | high |
| CTX-099 | Vehicle data in the MVP: Geotab plus optional manual battery (SoC) entry. Tesla Fleet API and Smartcar come after a cost check; Tesla is shown as an option with a cost model, for the client to decide. | SRC-C2@00:40:31, SRC-C2@00:40:39, SRC-C2@00:40:50 | V→C | medium |
| CTX-144 | Tesla Fleet API pricing (pay-per-use since late 2024): about $1 per 150,000 streamed signals, $0.001 per command, $0.002 per data request, $0.02 per wake, and a $10 monthly credit. Streaming SoC and location for a couple of hundred cars all day adds up. | SRC-C2@00:38:50 | V | medium |
| CTX-100 | A booking must match the vehicle's native connector, its allowed adapters (fleet policy, overridable per vehicle) and its max DC power. Each EVSE connector has a type and max kW. Power also drives slot length and smarter allocation (320 kW stalls go to cars that can use them). | SRC-C2@00:40:58, SRC-C2@00:41:32, SRC-C2@00:42:00, SRC-C2@00:42:11 | V→C | high |
| CTX-101 | Vehicle data has two uses: battery level suggests slot length (at 15% about 45 min, at 50% about 20), and seeing the car approach avoids false no-shows and lets grace stretch when the driver is close. | SRC-C2@00:38:05 | C | high |
| CTX-102 | Without telematics, arrival can be detected by phone location (if the driver allows), a QR code at the stall (the LIC attendant could put them up), or the session-start event from the CSMS. | SRC-C2@00:40:06, SRC-C2@00:40:24 | V→C | high |
| CTX-103 | The client wants a simulated site to "break chargers on purpose" (EVerest as a charger simulator), and the Gowanus fault ("1:50 PM, nine bookings") replayed as a test case. | SRC-C2@00:23:23, SRC-C2@00:55:37, SRC-C2@00:55:51 | V→C | high |
| CTX-104 | Amperlane's natural OCPI role is eMSP. Intellias proposes building the OCPI 2.2.1 eMSP gateway in Phase 1 against a test CPO, so it is proven before LA. The client has not confirmed this. | SRC-C2@00:11:56, SRC-C2@00:25:36 | V | medium |
| CTX-105 | CitrineOS (open-source CSMS under LF Energy, Apache-2.0, TypeScript/PostgreSQL, OCPP 1.6/2.0.1/2.1, OCPI server) is an option for hosts without a CSMS. Choosing it is a business decision (Amperlane would operate charger backends), and it is described as an option, not necessarily built by March. | SRC-C2@00:22:19, SRC-C2@00:22:42, SRC-C2@00:23:04, SRC-C2@00:23:13 | V | medium |
| CTX-142 | The brief's integration wishlist: "All major CSMS" (ChargePoint, EVgo, Electrify America, AMPECO, ChargeLab), Uber/Lyft, Tesla, Stripe, NREL. The CTO does not know which are real for March and suspects "some aren't possible at all". See CF-025. | SRC-D1#10, SRC-C1@00:41:59 | C | high |

### 7.3 Regulation, security and compliance

| CTX | Statement | Sources | By | Confidence |
|---|---|---|---|---|
| CTX-106 | The CTO does not want Amperlane to need a New York money-transmitter licence. Intellias' line is to keep funds flows inside Stripe Connect (Stripe holds and moves funds, Amperlane takes its margin as the platform). Amperlane's counsel must confirm this. | SRC-C2@00:45:17, SRC-C2@00:45:33, SRC-C2@00:57:30 | V→C | high |
| CTX-107 | Build SOC 2-ready from day one: access control, audit logging, change management, encryption, a separate production account. The Type I audit, auditor and compliance tool are on Amperlane's side. | SRC-C2@00:44:04, SRC-C2@00:44:25 | V→C | high |
| CTX-108 | The NY SHIELD Act covers credentials and licence or account numbers (reasonable safeguards, breach notification). Location is outside SHIELD's definition but is treated as sensitive: encryption, access control and retention limits. The CTO's rule: "keep what we need for disputes, delete the rest". | SRC-C2@00:50:18, SRC-C2@00:50:34 | V→C | medium |
| CTX-109 | Vehicle data needs authorisation from the vehicle account owner, and drivers (independent contractors) must separately consent to location tracking. | SRC-C2@00:39:22 | V | high |
| CTX-110 | A full audit trail covers every booking state change, override, manual ops action and payout. It is append-only and records who, what and when, serving disputes, SHIELD and SOC 2. | SRC-C2@00:50:39, SRC-C2@00:53:46 | V→C | high |
| CTX-111 | Stripe can file and deliver 1099s for connected accounts, for a per-form fee. | SRC-C2@00:46:46, SRC-C2@00:47:08 | V | medium |

### 7.4 Non-functional targets agreed on Call 2

| CTX | Statement | Sources | By | Confidence |
|---|---|---|---|---|
| CTX-112 | Station status is no older than 60 seconds for connected sites. For LIC the UI shows "last updated by attendant at …", and the UI always shows the age of status data. | SRC-C2@00:49:22, SRC-C2@00:49:30, SRC-C2@00:49:38 | V→C | high |
| CTX-113 | Booking API latency is under 300 ms at p95, including during the burst and the constraint check. | SRC-C2@00:49:44, SRC-C2@00:49:48, SRC-C2@00:49:52 | V→C | high |
| CTX-114 | Availability is 99.9% from 5 AM to 1 AM Eastern, with maintenance outside that window ("overnight people walk up, they don't book"). See CF-015. | SRC-C2@00:50:00, SRC-C2@00:50:06, SRC-C2@00:50:13 | V→C | high |
| CTX-115 | Burst: launch is modelled at about 400 booking attempts in 10 minutes around 4:30 PM. The problem is contention (many attempts on the same few stalls in the same quarter-hour), not throughput. Load test at 5× (2,000 attempts in 10 min) with heavy contention on a few sites. | SRC-C2@00:15:32, SRC-C2@00:16:00, SRC-C2@00:34:07, SRC-C2@00:34:22 | V→C | high |

## 8. Business model (undecided)

| CTX | Statement | Sources | By | Confidence |
|---|---|---|---|---|
| CTX-116 | The brief's model has two recurring streams: a 10–12% take rate on charging GMV paid by stations, and a $15/vehicle/month fleet SaaS fee, projecting $4.8M ARR in 2028. | SRC-D1#8 | C | high |
| CTX-117 | The 10–12% figure came "from benchmarks, mostly", and the ARR projection is a spreadsheet extrapolation of it. | SRC-C1@00:16:54 | C | high |
| CTX-118 | No station signed the percentage (all three sites and a couple of prospects were pitched). It exceeds their margin, on sessions they would mostly get anyway at peak. | SRC-C1@00:17:22, SRC-C1@00:18:08 | C | high |
| CTX-119 | Stations would pay only for incremental, off-peak sessions: "Pay you for sessions I wouldn't have had — fine. A cut of the sessions I already have at five PM — no." | SRC-C1@00:18:24, SRC-C1@00:18:56 | C | high |
| CTX-120 | Borough Green would pay a fleet subscription "if the number's right". | SRC-C1@00:19:12 | C | medium |
| CTX-121 | Option floated by the CEO: Amperlane as eMSP and merchant of record. It buys sessions at the station's B2B tariff (about $0.42/kWh at Gowanus) and bills the fleet a bundled rate (about $0.49/kWh, including the guaranteed slot), plus the fleet subscription, plus no-show fees passed through to the station. | SRC-C1@00:19:54, SRC-C1@00:20:49 | C | high |
| CTX-122 | The spread of about $0.07/kWh × 28 kWh ≈ $1.96 per session is close to today's $2 fee. The spread changes Amperlane's place in the money flow, not revenue per session. As merchant of record Amperlane carries payment risk and sits in the middle of energy disputes. | SRC-C1@00:21:15, SRC-C1@00:21:32, SRC-C1@00:21:44 | V→C | high |
| CTX-141 | Stations have not accepted the spread either. It is "easier to sell than the percentage, but not a done deal": Kinship will ask "why is Amperlane making seven cents on my electrons?" | SRC-C1@00:22:36 | C | high |
| CTX-123 | The founders have not decided. The CEO leans to spread plus subscription. The COO leans to "whatever the stations sign", perhaps a small fee on incremental off-peak sessions only plus the spread. The CTO wants it decided before the settlement module is built. | SRC-C1@00:23:07, SRC-C1@00:23:13, SRC-C1@00:23:24 | C | high |
| CTX-124 | In the merchant model, each station's session data must be good enough to bill real money on, so per-station data quality becomes critical. | SRC-C1@00:24:11, SRC-C1@00:24:35 | V→C | high |
| CTX-125 | The decision reaches into the product. If the fleet pays for energy, fleet managers want spend controls; if the driver pays, they do not care. It shapes settlement, the fleet portal, the station portal, "basically everything with money in it". | SRC-C1@00:24:42, SRC-C1@00:25:00, SRC-C1@00:25:33, SRC-C1@00:46:31 | V→C | high |
| CTX-126 | Cash gap, **only if Amperlane is merchant of record or otherwise holds station money** (CF-024): stations would be paid weekly while fleets pay net-30, so up to seven or eight weeks before the fleet pays for those sessions. The platform would then model owed, paid and outstanding per fleet. | SRC-C1@00:44:17, SRC-C1@00:44:29, SRC-C2@00:35:42, SRC-C2@00:36:18, SRC-C2@00:46:21, SRC-C2@00:46:23 | V→C | high |
| CTX-127 | The unit of truth for consumption is the CPO's session record: the OCPI CDR, AMPECO or ChargeLab session records, or the CSV at LIC. Each booking is matched to a session record. A no-show fee is a separate line item, never mixed into energy, so it can be reversed alone. Disputes need evidence: the booking, the hold sent, station status at the time, and the driver's location or QR scan. | SRC-C2@00:47:29, SRC-C2@00:47:59 | V | high |
| CTX-128 | If Amperlane is merchant of record (options B or C), Intellias proposes Stripe Connect with separate charges and transfers: the fleet is invoiced through Stripe Invoicing, net-30, and transfers go to each station weekly. | SRC-C2@00:45:58, SRC-C2@00:46:21, SRC-D2#9 | V→C | medium |
| CTX-145 | Stripe Connect cost on the "you handle pricing" model: $2 per monthly active account plus 0.25% + 25¢ per payout. Stripe can file and deliver 1099s for a per-form fee. | SRC-C2@00:46:46, SRC-D2#11 | V | medium |
| CTX-129 | The ledger and flows are the same in every model; what changes is what is charged and who is merchant of record (receipts, tax, the eMSP role). The ledger is designed generically, and detailed settlement waits for the decision. | SRC-C2@00:48:32 | V | high |
| CTX-130 | If the no-show fee lands on the driver, it is the first time Amperlane ever takes money from a driver. | SRC-C1@00:11:44, SRC-C1@00:11:59 | V→C | medium |

## 9. Business rules and policies stated so far

| CTX | Statement | Sources | By | Confidence |
|---|---|---|---|---|
| CTX-131 | After the grace period the slot releases itself automatically; otherwise "we're back to phone calls". | SRC-C1@00:10:20, SRC-C1@00:10:26 | V→C | high |
| CTX-132 | Overbooking is off by default; at most it becomes a per-site, off-peak setting later. | SRC-C2@00:29:24, SRC-C2@00:29:35, SRC-C2@00:29:41 | V→C | high |
| CTX-133 | A driver arriving after grace is a no-show for the station (the stall sat empty). Today such drivers are usually rebooked if something is free, and many of the 22% late arrivals still charged. Proposed handling: release the slot, mark the booking no-show, instantly offer whatever is free. Whether the fee still applies after a rebook is undecided. | SRC-C2@00:29:56, SRC-C2@00:30:01, SRC-C2@00:30:11 | V→C | high |
| CTX-134 | Who pays the no-show fee (fleet, driver, or fleet pays and deducts) is undecided. A per-fleet setting is a candidate answer that the CEO likes. | SRC-C1@00:11:26, SRC-C1@00:11:36, SRC-C2@00:30:36 | V→C | high |
| CTX-135 | Since the no-show is a rational choice in the moment, a fee alone won't fix it: cancelling or saying "running late" must be effortless (one tap). | SRC-C1@00:12:26, SRC-C1@00:12:42, SRC-C1@00:46:10 | V→C | medium |
| CTX-136 | Intellias' proposal for a charger fault: the system detects "Faulted", reassigns every affected booking to a compatible EVSE at the same site, notifies drivers it cannot place (with alternatives) and ops, and shows the station what happened. The COO called it "magic". A later Intellias version adds ops bulk approval "on top of the automation" (CTX-035); see CF-022. | SRC-C2@00:34:48, SRC-C2@00:35:14, SRC-C2@00:53:00 | V→C | high |
| CTX-137 | Proposed overstay levers: buffers between slots, and a check at T-10 that reassigns the booking to another free compatible EVSE if the allocated one is still in a session. | SRC-C2@00:28:55, SRC-D2#7 | V | medium |

## 10. Success metrics

| CTX | Statement | Sources | By | Confidence |
|---|---|---|---|---|
| CTX-138 | North star: 10,000 completed bookings a month by June 2027, NYC only (LA does not count), from about 1,850 today, so 5× or more in nine months. Every no-show is a booking not completed, so cutting no-shows is growth. | SRC-C1@00:29:22, SRC-C1@00:30:00, SRC-C1@00:30:13, SRC-C1@00:30:26 | C | high |
| CTX-139 | What makes 2 March 2027 a success, verbatim from the founders: (1) "Five Boroughs' cabs are charged at five o'clock, every day, without anyone on my team picking up the phone"; (2) "Kinship stops calling me about cones"; (3) "Nobody opens Airtable"; (4) "Borough Green gets one invoice and doesn't email me about it". | SRC-C1@00:33:03, SRC-C1@00:33:16, SRC-C1@00:33:22, SRC-C1@00:33:25 | C | high |
| CTX-140 | Success for Five Boroughs is "is my cab charged at five o'clock, yes or no". Borough Green sees no-shows only because Amperlane shows them. | SRC-C1@00:12:58 | C | high |

## 11. Decided and undecided

| Topic | State | Facts | Open items |
|---|---|---|---|
| NYC production launch on 1 March 2027, NYC first | decided | CTX-079, CTX-008 | — |
| LA in Q3 2027 | **target**, not decided (one prospect under NDA, the mandate is "wobbly", out of MVP) | CTX-019, CTX-071, CTX-081 | Q-008 |
| Driver channel: PWA + SMS/WhatsApp, no native app in MVP | decided | CTX-096, CTX-097 | — |
| Amperlane owns the slot calendar; ReserveNow only as a hold shortly before the slot | decided (exact lead time is A-002) | CTX-088 | A-002 |
| Booking against a pool, late EVSE assignment | decided | CTX-092 | A-002 |
| No double booking enforced in the database | decided | CTX-093 | CF-017 |
| Overbooking off by default | decided | CTX-132 | — |
| Ops console in scope | decided | CTX-035 | Q-023 |
| Uber/Lyft deep links only | decided | CTX-098 | — |
| Pilot history migrates; prototype is discarded | decided | CTX-052, CTX-053 | Q-020 |
| Charger fault: automatic same-site reassignment, ops handles the rest | provisional (A-017), client to confirm | CTX-035, CTX-136 | CF-022, Q-038 |
| Grace extension when the car is close | **undecided** | CTX-067, CTX-101 | CF-021 |
| Business model (percentage, spread, hybrid; merchant of record) | **undecided** | CTX-116 – CTX-125 | CF-008, Q-001 |
| Who pays no-shows; fee after rebook; fee amount and station share | **undecided** | CTX-133, CTX-134 | Q-002, Q-003 |
| Station terms per site (caps, grace, payout) | **undecided** | CTX-064 – CTX-069 | Q-004, Q-005 |
| Tesla Fleet API / Smartcar and who pays telematics | **undecided** | CTX-099 | CF-004, Q-015 |
| LIC: CSV + attendant, or direct OCPP via CitrineOS | **undecided** | CTX-062, CTX-105 | Q-010 |
| SOC 2 Type I target date | **undecided** | CTX-078, CTX-107 | CF-016, Q-018 |
| Funds-flow legality (money transmission) | **undecided** | CTX-106 | Q-019 |
| Cash-gap financing | **undecided** | CTX-126 | Q-021 |
| What the phase-one budget covers; fixed price vs T&M | **undecided** | CTX-080 | CF-013, Q-025 |
| Temporal hosting (self-hosted vs cloud) | **undecided** | CTX-094 | Q-026 |
| Maps and routing provider | provisional: Google Maps (A-030), CTO to confirm in Phase 0 | — | CF-020, Q-027 |
| Availability window vs overnight slots | **undecided** | CTX-114 | CF-015, Q-024 |
| Completed-booking definition (billing unit and Series A metric) | **undecided** | CTX-138 | Q-017 |
| March integration scope beyond the NYC sites | **undecided** | CTX-142 | CF-025, Q-036 |
| Ops coverage early in the morning and at night | **undecided** | — | Q-023 |
