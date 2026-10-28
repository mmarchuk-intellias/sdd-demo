---
id: STAKEHOLDERS
type: context
title: Stakeholders, decision rights and concerns
status: approved
owner: Mykola Marchuk
version: 1
kyiv: null
parents: [BUSINESS-CONTEXT]
sources: [SRC-D1, SRC-C1, SRC-C2, SRC-D2, SRC-R1]
---
# Stakeholders

Decision rights are what the sources show, not what we would like. Characterisations that come only from Intellias'
internal brief (SRC-R1#people) are marked *(Intellias' view)*.

## Amperlane

| Person / group | Role | Decision rights (per sources) | Concerns and definition of success | Sources |
|---|---|---|---|---|
| Dana Whitfield | Co-founder & CEO; 9 years in NYC for-hire vehicles; ran charging logistics for about 300 leased EVs | Business model, jointly with Luis and Ravi; launch date and Series A story; agreed to drop the native app. Economic buyer *(Intellias' view)*. | The 1 March launch and 10k completed bookings by June; "Five Boroughs' cabs are charged at five o'clock… without anyone on my team picking up the phone"; "Borough Green gets one invoice". Leans to spread plus subscription. Asked for a fixed price for "Phase 1" *(Intellias' internal note; which phase is meant is unclear, CF-013)*. | SRC-D1#2, SRC-C1@00:23:07, SRC-C1@00:33:03, SRC-C1@00:33:25, SRC-C2@00:51:22, SRC-R1#people, SRC-R1#c1 |
| Luis Ortega | Co-founder & COO, Partnerships; 6 years in DC fast-charging site acquisition | Station relationships and contracts; station-side policy (no bumping walk-ups, overbooking off). "Anything that costs stations money needs his OK" *(Intellias' view)*. | Station acceptance (no percentage; incremental off-peak only); "Kinship stops calling me about cones"; weekly payouts; NEVI compliance. Leans to "whatever the stations sign". | SRC-D1#2, SRC-C1@00:23:13, SRC-C1@00:33:16, SRC-C2@00:24:04, SRC-C2@00:29:24, SRC-R1#people |
| Ravi Menon | Co-founder & CTO; former staff engineer on marketplace payouts; joined January 2025 | Technical decisions: stack, architecture, vendors, IP. Co-decides the business model; wants it decided before settlement is built. | IP ownership and no lock-in; double-entry ledger; idempotency; money transmission risk; SOC 2; pilot history migration; "Nobody opens Airtable". | SRC-D1#2, SRC-C1@00:23:24, SRC-C1@00:33:22, SRC-C2@00:06:05, SRC-C2@00:46:41, SRC-C2@00:45:17 |
| Priya Nair | Senior software engineer; built the Retool/Airtable tooling and maintains the prototype | Delivers the data exports and the Supabase schema; to own the integration-layer knowledge (CTO's wish). | Duplicate SMS confirmations, messy pilot data; wants a simulator to "break chargers on purpose"; wants to be embedded in the squad. | SRC-C2@00:02:00, SRC-C2@00:33:20, SRC-C2@00:55:26, SRC-C2@00:55:37, SRC-R1#people |
| Ops team (4 people) | Driver support and operations, bilingual (EN/ES/BN) | Day-to-day booking decisions in the pilot; future users of the ops console. | Dozens of calls a day; manual rebooking on charger-down days; disputes coming once fees start. | SRC-C1@00:37:27, SRC-C1@00:38:15, SRC-C1@00:39:22 |
| Finance (1 person) | Amperlane finance | Not stated. | 1099s, payouts, reconciliation (A-010). | SRC-R1#company, SRC-C2@00:47:08 |
| Product designer | Amperlane design | Not stated; Intellias proposes embedding them in the squad. | — | SRC-D2#16, SRC-R1#company |
| Amperlane counsel | Legal | Confirms the funds-flow structure, data retention and consent. | Money transmission; SHIELD. | SRC-C2@00:50:39, SRC-C2@00:57:30 |
| Investors | Hudson Mobility Partners (lead), Gridline Ventures; future Series A investors | None in the platform; the Series A milestone drives the date. | 10,000 completed bookings a month by June 2027, NYC only; the pilot dataset in the data room. | SRC-D1#2, SRC-C1@00:29:22, SRC-C2@00:04:43 |

## Supply partners

| Organisation | Who / role | Decision rights | Concerns | Sources |
|---|---|---|---|---|
| Kinship Charging | CPO at Gowanus FastHub (AMPECO) | Capacity caps, grace, fees, API and sandbox access, firmware fix; renewal coming soon. | "If you hold my stall, you pay for my stall"; pays only for incremental sessions; weekly payouts; liability for blocked stalls. | SRC-C1@00:09:27, SRC-C1@00:18:24, SRC-C2@00:35:42, SRC-C2@00:36:37 |
| Jamaica Bay Energy | CPO at JFK Lot 9 (ChargeLab) | Capacity caps; API access; OCPI peering "sometime in 2027". | Busy at 4 PM, so the cone sometimes doesn't happen; weekly payouts. | SRC-C2@00:19:30, SRC-C2@00:21:33, SRC-C2@00:35:42 |
| Hunters Point Garages LLC | Site host at LIC Garage Depot (legacy ChargePoint contract) | Contract with ChargePoint; CSV export; whether to move to direct OCPP. | Not stated. | SRC-C2@00:19:59, SRC-C2@00:23:04 |
| LIC garage attendant | Site staff | Puts "Reserved" signs out; could put up QR codes. | One of the most reliable partners; the only real-time feed at LIC. | SRC-C1@00:08:08, SRC-C1@00:08:29, SRC-C2@00:20:33, SRC-C2@00:40:24 |
| Two LA CPO prospects | OCPI 2.2.1-capable; one NEVI-funded; one under NDA | Partner terms for LA (Phase 2). | Not stated. | SRC-C2@00:25:17, SRC-C2@00:26:53 |

## Demand partners

| Organisation | Who / role | Decision rights | Concerns | Sources |
|---|---|---|---|---|
| Borough Green Fleet LLC | Lessor of about 420 EVs to independent drivers; ops director, fleet manager, finance lead | Fleet policies (sites, frequency, adapters); whether it pays for Tesla telematics; whether Geotab data is shared. | Won't pay for drivers' behaviour, nor have drivers billed directly; one invoice, net-30; spend controls. | SRC-C1@00:10:56, SRC-C1@00:19:12, SRC-C1@00:25:00, SRC-C2@00:57:09 |
| Five Boroughs EV Cab Co. | Medallion cab operator (owner and a nephew); 24 drivers | Who books for which shift. | "Is my cab charged at five o'clock, yes or no"; won't use a portal. | SRC-C1@00:07:09, SRC-C1@00:12:58, SRC-C1@00:25:00 |
| Drivers | Independent contractors and shift drivers; EN/ES/BN | None formally; they vote with their feet. | Waiting time is lost income; no app or account; one-tap cancel; fees "they just hate". | SRC-C1@00:05:47, SRC-C1@00:10:26, SRC-C1@00:12:26 |
| Two more fleets in talks | Prospects | — | — | SRC-C1@00:42:50 |
| A large rideshare platform's EV team (not named) | Pilot prospect | Sets the security bar for its pilot. | SOC 2 Type I within 12 months of pilot start; pen test. | SRC-C2@00:43:30 |

## Market players and regulators (no decision rights in the platform)

| Party | Relevance | Sources |
|---|---|---|
| NYC TLC | Green Rides mandate (demand driver). | SRC-D1#4, SRC-C1@00:35:39 |
| CPUC / CARB | California Clean Miles; recommended pause (LA risk). | SRC-C1@00:36:12 |
| Federal NEVI programme | Public-access and protocol obligations at funded sites. | SRC-C1@00:27:12, SRC-C2@00:12:24 |
| Voltera + Revel | Announced combination; supply partner or competitor. | SRC-C1@00:34:36, SRC-C1@00:34:57 |

## Intellias

| Person | Role | Sources |
|---|---|---|
| Mark Feldman | Client Partner, North America; commercial lead and account owner | SRC-C1@00:01:01, SRC-R1#c1 |
| Kyrylo Shvedov | Engagement Lead, Product & BA; owner of the account brief | SRC-C1@00:01:33, SRC-R1#company |
| Olena Marchuk | Solution Architect; led the technical deep-dive | SRC-C1@00:02:02, SRC-C2@00:00:30 |
| Andriy Bondar | Payments & Integrations Lead | SRC-C2@00:00:30 |

## Decision-rights matrix (open decisions)

| Decision | Decides | Consulted | Status | Links |
|---|---|---|---|---|
| Revenue model and merchant of record | Dana Whitfield, Luis Ortega, Ravi Menon | Intellias (informs; "not break, inform"), stations | open; the workshop requested for 2026-10-27 did not take place; due 2026-11-13, scheduled by Kyrylo Shvedov | CF-008, Q-001 |
| Who pays no-shows | Dana Whitfield, Luis Ortega | fleets, stations | open | Q-002, Q-003 |
| Charger-fault handling: automatic vs ops approval | Dana Whitfield | ops, stations (Luis Ortega on the cap, Q-038) | provisional: automatic same-site moves (A-017), to confirm | CF-022 |
| Grace extension | Luis Ortega with the station operators | Ravi Menon | open | CF-021 |
| Station terms per site | Luis Ortega with each station operator | Intellias | open | Q-004, Q-005 |
| Tesla telematics and its cost | Ravi Menon with Borough Green | Dana Whitfield, Intellias (cost model) | open; cost model 2026-11-06, decision by 2026-11-27 | CF-004, Q-015 |
| March integration scope | Ravi Menon, Luis Ortega | Dana Whitfield (June supply plan) | open | CF-025, Q-036 |
| Operating charger back-ends (direct OCPP) | Ravi Menon, Luis Ortega, with Hunters Point Garages | Intellias | open; priced as an option | Q-010 |
| Completed-booking definition | Dana Whitfield, Ravi Menon | fleets (billing unit), investors | open | Q-017 |
| Ops coverage hours | Dana Whitfield | — | open | Q-023 |
| Funds-flow legality, retention, consent | Amperlane counsel (via Ravi Menon) | Intellias (describes the structure) | open | Q-019, Q-022, Q-016 |
| SOC 2 target date and auditor | Ravi Menon | rideshare platform | open | CF-016, Q-018 |
| Architecture and stack | Ravi Menon | Olena Marchuk | largely agreed (ADR-001 – ADR-013) | spec/10-design/adr |
| Final KYIV priorities | the client's product owner and Intellias' engagement lead | — | Step 5 | playbook §5 |

Source for "not break, inform": SRC-C1@00:50:13.
