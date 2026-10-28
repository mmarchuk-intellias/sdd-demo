---
id: GLOSSARY
type: context
title: Glossary
status: approved
owner: Mykola Marchuk
version: 1
kyiv: null
parents: [BUSINESS-CONTEXT]
sources: [SRC-D1, SRC-C1, SRC-C2, SRC-D2, SRC-R1]
---
# Glossary

One term per concept. Spec artefacts use the **Term** column. Words in the **Avoid** column appear in the sources;
when you quote a source, keep its wording, but do not use those words in requirements, stories or system stories.

## Supply: places and hardware

| Term | Definition | Avoid | Sources |
|---|---|---|---|
| Site | A partner location where Amperlane offers bookings, e.g. Gowanus FastHub. Equals an OCPI *Location*. | station (for the place), hub, plaza, lot | SRC-C2@00:18:52, SRC-C2@00:26:05, SRC-D2#7 |
| EVSE | One bookable charging point at a site: the unit that a single vehicle charges at, and that holds and allocations refer to. It has one or more connectors. The pilot counts 46 (A-004). | port, charger, stall, plug (when counting bookable units) | SRC-C2@00:24:36, SRC-C2@00:31:16, SRC-D2#7 |
| Connector | The physical plug of an EVSE, with a type (CCS1 or NACS) and a max power in kW. | plug type, socket | SRC-C2@00:41:32, SRC-D2#7 |
| Charger | The physical charging unit (hardware). Use it only for hardware and firmware topics (e.g. "firmware on six chargers rejects reservations"); it may host more than one EVSE (Q-013). | — | SRC-C2@00:14:11, SRC-C2@00:51:36 |
| Stall | The parking bay in front of an EVSE. Use it only for physical topics (cones, signs, blocked bay). | — | SRC-C1@00:08:08, SRC-C1@00:09:27 |
| CCS1 / NACS (SAE J3400) | The two DC connector standards at the pilot sites. NACS is being standardised as SAE J3400; Gowanus has four NACS ports. | "CCS", Tesla plug | SRC-C2@00:16:36, SRC-C2@00:40:58 |
| Adapter | A device that lets a vehicle use a connector type it does not natively have. Whether adapters are allowed is fleet policy, overridable per vehicle. | — | SRC-C2@00:41:53, SRC-C2@00:42:00 |
| Station operator (CPO) | The company that runs the chargers at a site and sells charging, e.g. Kinship Charging, Jamaica Bay Energy. | station (for the company), network | SRC-C2@00:11:56, SRC-D2#6 |
| Site host | The owner of a site that is not a CPO, e.g. Hunters Point Garages at LIC. | operator | SRC-C2@00:19:59, SRC-C2@00:22:42 |
| CSMS | Charging station management system: the operator's back-end for its chargers (AMPECO, ChargeLab, a legacy ChargePoint network). | — | SRC-C1@00:28:06, SRC-D1#10 |
| Supply pattern A / B / C | How a site integrates: **A**, API with reservations (Gowanus); **B**, status only (JFK); **C**, no API (LIC). Only the station-hold step differs between them. | — | SRC-C2@00:20:38, SRC-D2#8 |
| Walk-up | A driver who charges without an Amperlane booking and pays the public price. Walk-ups are never bumped. | — | SRC-C1@00:26:10, SRC-C2@00:24:04 |
| Attendant | Site staff who act on the platform's instructions on site (signs, cones, arrival checks), e.g. the LIC garage attendant. | garage guy, site guy | SRC-C1@00:08:04, SRC-C1@00:08:08, SRC-C1@00:08:44, SRC-D2#6 |

## Booking

| Term | Definition | Avoid | Sources |
|---|---|---|---|
| Slot calendar | Amperlane's own calendar of bookable capacity per site and time. The platform owns it, because chargers cannot hold future slots. | seat map, slot grid (the pilot's Google Sheet) | SRC-C2@00:08:48, SRC-D2#7 |
| Slot | One time interval on the slot calendar. Bookings cover 30, 45 or 60 minutes on a 15-minute grid (A-001). | — | SRC-C2@00:28:55, SRC-D2#7 |
| Booking | A confirmed claim on capacity at a site for a time window, for one vehicle. It is made against a *pool* of compatible EVSEs, not a specific EVSE. | reservation (that word belongs to the charger side) | SRC-C2@00:24:36, SRC-D2#12 |
| Booker / charging driver | The person who makes a booking, and the person who arrives and charges. They may differ (e.g. a cab day driver booking for the night shift). | — | SRC-C1@00:07:40, SRC-C1@00:07:53 |
| Hold | A temporary, unconfirmed claim on capacity, with a time-to-live (TTL, 3 minutes per A-001). It expires if not confirmed. | soft hold (when you mean this) | SRC-C2@00:27:21, SRC-D2#7 |
| Allocation | Assigning a booking to one specific EVSE, at about T-15 (A-002). | stall assignment | SRC-C2@00:24:36, SRC-D2#12 |
| Station hold | Securing the allocated EVSE on site before arrival. Pattern A: a charger reservation (ReserveNow). Patterns B and C: signage, a cone or the attendant, with ops as fallback. | cone, hold (unqualified) | SRC-C2@00:27:21, SRC-D2#7, SRC-D2#8 |
| ReserveNow | The OCPP command that reserves a charger "from now until expiry". It is not a future slot. It is optional and may be rejected. | real-time reservation | SRC-C2@00:07:35, SRC-C2@00:08:09 |
| T-15 / T-10 | Minutes before the booking start, used as timer points (station hold and allocation; reassignment check). | — | SRC-C2@00:08:48, SRC-C2@00:28:55 |
| Capacity rule | A station-set cap on bookable EVSEs per site and time window (e.g. "weekdays 4–7 PM, max 8"). The station can edit it. | quota | SRC-C1@00:26:44, SRC-C1@00:26:54 |
| Peak / off-peak | Time windows defined per site by its capacity rules. At Gowanus, off-peak means 10 AM–3 PM and 10 PM–5 AM. | — | SRC-D1#7, SRC-C1@00:26:10 |
| Buffer | Time kept free between consecutive bookings on one EVSE (10 minutes per A-001) to absorb overstays. | — | SRC-C2@00:28:55 |
| Grace period | The minutes after the booking start within which the driver must arrive (10 minutes per A-003). | — | SRC-C1@00:09:55 |
| Auto-release | Returning a booking's capacity automatically when grace expires without an arrival. | take the cone | SRC-C1@00:10:26 |
| No-show | A booking whose driver did not arrive within grace. It may carry a no-show fee. | cancelled (as the pilot data used it) | SRC-C1@00:08:56, SRC-C2@00:05:22 |
| Late arrival | Arrival more than 10 minutes after the booking start. For the station it is a no-show. Intellias proposes an instant re-offer; whether the fee still applies is open (Q-003). | — | SRC-C1@00:09:05, SRC-C2@00:29:56, SRC-C2@00:30:11 |
| Re-offer | An immediate alternative (another time or EVSE) offered to a driver who lost a slot. | — | SRC-C2@00:30:11, SRC-C2@00:32:16 |
| Overstay | The previous session still occupying the allocated EVSE when the next driver arrives. | sleeper, previous movie | SRC-C1@00:40:55, SRC-C2@00:28:17 |
| Charger fault | An EVSE reported as faulted (by webhook, poll or attendant), which triggers rebooking of its future bookings. | charger down | SRC-C2@00:34:48 |
| Rebook | Moving an existing booking to another EVSE, site or time, with a reason code. | move, redo | SRC-C2@00:53:00, SRC-C2@00:53:32 |
| Overbooking | Accepting more bookings than capacity. Off by default. | — | SRC-C2@00:28:55, SRC-C2@00:29:35 |
| Manual hold | Capacity blocked by Amperlane ops (maintenance, fleet priority). | — | SRC-C2@00:53:00 |
| Override | An ops action that forces a state: force-confirm, force-release, extend grace. | — | SRC-C2@00:53:00 |
| Reason code | The coded reason recorded with every booking state change, together with its actor. | note | SRC-C2@00:53:32, SRC-C2@00:53:40 |
| Arrival | The event that the driver is at the site: geofence, QR scan at the stall, or session start from the CSMS. | check-in | SRC-C2@00:40:06, SRC-D2#7 |
| Completed booking | A booking that turned into a charge; the north-star metric. The exact rule is a client decision (Q-017), because it is also the billing unit; until then the platform keeps the evidence to compute any definition and reports by the Completed state in data-model.md. | — | SRC-C1@00:29:22, SRC-C1@00:08:56 |

## Fleets, drivers and channels

| Term | Definition | Avoid | Sources |
|---|---|---|---|
| Fleet | A company that provides EVs to drivers: a lessor (Borough Green) or a medallion cab operator (Five Boroughs). | customer (ambiguous) | SRC-C1@00:04:48, SRC-C1@00:07:09 |
| Fleet manager | The fleet's person who sets policies and sees bookings, no-shows and invoices. | fleet ops director (except when quoting) | SRC-C1@00:25:00, SRC-D2#6 |
| Driver | A person who charges a fleet vehicle. At Borough Green: an independent contractor on a weekly lease. At Five Boroughs: a shift driver. | Jorge (illustrative persona in SRC-C1) | SRC-C1@00:04:48, SRC-C1@00:07:09 |
| FHV | For-hire vehicle (rideshare) licensed by the NYC TLC. | — | SRC-D1#4 |
| Medallion cab | A yellow taxi operating on a TLC medallion. | yellow cab | SRC-C1@00:07:09 |
| Shift change | The 4–5 PM handover of cabs, which causes the booking burst. | — | SRC-C1@00:07:09 |
| Driver PWA | The light mobile web app for drivers (no install), opened from SMS or WhatsApp links. | driver app, native app | SRC-C2@00:51:10, SRC-D2#14 |
| Deep link | A link that opens another app at a specific place (Amperlane ↔ navigation ↔ Uber/Lyft driver app). It carries no data exchange. | integration (for Uber/Lyft) | SRC-C2@00:43:07 |
| Fleet portal / station portal / ops console / attendant view | The four web front-ends: for fleet managers, station operators, Amperlane ops, and site attendants. | admin panel (for the ops console) | SRC-D1#11, SRC-C1@00:39:37, SRC-D2#6 |
| Ops (Amperlane ops) | The Amperlane team (four bilingual people today) that runs bookings by hand in the pilot and is the safety net afterwards. | concierge | SRC-C1@00:37:27, SRC-C2@00:53:49 |
| SoC | State of charge: the battery level in %. It comes from telematics or manual entry. | battery data | SRC-C2@00:38:05, SRC-C2@00:40:06 |
| Telematics | Vehicle data feeds: Geotab, Tesla Fleet API, Smartcar. | — | SRC-C2@00:38:24, SRC-D2#10 |

## Money

| Term | Definition | Avoid | Sources |
|---|---|---|---|
| Booking fee (pilot) | Today's $2 per completed booking, invoiced to fleets monthly. | — | SRC-C1@00:13:26 |
| Take rate | A percentage of charging GMV paid by stations (option A in the brief). | — | SRC-D1#8 |
| Charging GMV | The value of charging (energy) sold through Amperlane bookings. | revenue | SRC-D1#8 |
| eMSP | E-mobility service provider: the OCPI role holding the driver/fleet relationship. Amperlane's natural OCPI role. | — | SRC-C1@00:19:54, SRC-C2@00:11:56 |
| Merchant of record | The party that legally sells the charging session to the fleet and collects the money. Undecided (Q-001). | — | SRC-C1@00:19:54, SRC-C2@00:44:52 |
| B2B tariff / bundled rate / spread | The station's wholesale price per kWh to Amperlane (about $0.42 at Gowanus); Amperlane's price to the fleet including the guaranteed slot (about $0.49); and the difference between them. | margin (ambiguous) | SRC-C1@00:19:54, SRC-D2#9 |
| Fleet subscription | A per-vehicle monthly SaaS fee to fleets ($15 in the brief). | SaaS fee | SRC-D1#8 |
| No-show fee | A fee for a no-show. It is a separate line item, never mixed into energy, and passed through to the station in option B. Who pays it is open (Q-002). | penalty | SRC-C1@00:19:54, SRC-C2@00:47:59 |
| Idle fee / congestion fee | A station's or network's per-minute fee for occupying a charger after charging (Gowanus; Tesla). It is not an Amperlane fee. | — | SRC-C2@00:28:42, SRC-C1@00:10:26 |
| Session record / CDR | The CPO's record of a charging session (energy, start, end, cost); CDR is the OCPI charge detail record. It is the unit of truth for settlement. | receipt | SRC-C2@00:13:48, SRC-C2@00:47:29 |
| Payout | A transfer to a station operator; stations want them weekly. | — | SRC-C2@00:35:42 |
| Fleet invoice | One consolidated monthly invoice per fleet, net-30. | — | SRC-C1@00:19:12 |
| Cash gap | The period between paying stations (weekly) and being paid by fleets (net-30), up to about 8 weeks. | working-capital gap | SRC-C2@00:46:23, SRC-D2#17 |
| Ledger | The double-entry, append-only record of what is owed, paid and outstanding. | balance columns | SRC-C2@00:46:41 |
| Dispute | A challenge to a fee or charge, decided on evidence (booking, hold sent, station status, location or QR scan, session record). | — | SRC-C1@00:39:22, SRC-C2@00:47:59 |
| Settlement | Matching bookings to session records, invoicing fleets and paying stations. | billing (unqualified) | SRC-C2@00:47:29, SRC-D2#7 |

## Protocols, data sources and compliance

| Term | Definition | Avoid | Sources |
|---|---|---|---|
| OCPP | Charger-to-back-end protocol (versions 1.6, 2.0.1, 2.1). | — | SRC-C2@00:07:23, SRC-C2@00:22:19 |
| OCPI | Back-end-to-back-end roaming protocol between CPO and eMSP. Version 2.2.1 is the most widely deployed; 2.3.0 adds a Booking module. | — | SRC-C2@00:07:23, SRC-C2@00:12:24 |
| NLR AFDC | The station locator API of the National Laboratory of the Rockies (formerly NREL). Static data, for discovery only. | NREL API | SRC-C2@00:10:23 |
| Open Charge Map | Community station data (CC BY 4.0), for discovery only. | — | SRC-C2@00:11:03 |
| NEVI | A federal charger-funding programme with public-access and protocol obligations. | — | SRC-C1@00:27:12, SRC-C2@00:12:24 |
| Green Rides | The NYC TLC rule requiring zero-emission or WAV rideshare trips. | — | SRC-D1#4 |
| WAV | Wheelchair-accessible vehicle. | — | SRC-D1#4 |
| NY SHIELD Act | New York data security and breach notification law. | — | SRC-C2@00:50:18 |
| SOC 2 Type I | A point-in-time security controls audit, requested by a rideshare platform. | — | SRC-C2@00:43:30 |

## Programme

| Term | Definition | Avoid | Sources |
|---|---|---|---|
| Amperlane Concierge | Today's manual pilot (SMS, Sheets, Airtable, phone calls). | the pilot app | SRC-D1#7, SRC-R1#pilot |
| Amperlane Platform v1 | The platform to be built (the subject of this spec). | the app | SRC-D1#11 |
| MVP | The scope that goes live at the NYC production launch on 1 March 2027. | "12-week MVP" | SRC-C1@00:29:06, SRC-D2#14 |
| Phase 0 / 1 / 2 / 3 (Intellias) | The vendor's indicative phases: Phase 0 inception (9–27 Nov), Phase 1 MVP build (30 Nov–26 Feb), Phase 2 LA and scale (Q2–Q3 2027), Phase 3 the next wave. | — | SRC-D2#15 |
| Phase one (client budget) | The client's budget period, "through end of Q2 2027". **Not** the same as the vendor's Phase 1; say "budget period" (CF-013). | Phase 1 (in budget context) | SRC-C1@00:30:45, SRC-C1@00:31:02 |
| Hypercare | The month after launch (March 2027) with heightened support. | — | SRC-D2#15 |
