---
id: SRC-C2
type: source
title: Amperlane Call 2 — Technical deep-dive transcript (Oct 8, 2026)
kind: call transcript
origin: Amperlane + Intellias (speaker per line)
original: C2_Amperlane_Call2_Tech_DeepDive_Transcript_2026-10-08.docx
sha256: 6537418932383fedac47bae958ac0aa6425399496d3f2905464d00ff9816a25a
generated_by: tools/extract.py  # do not edit; regenerate instead
---

# SRC-C2 · Amperlane Call 2 — Technical deep-dive transcript (Oct 8, 2026)

Microsoft Teams · Meeting transcript

Amperlane x Intellias — Technical deep-dive

| Date | Thursday, October 8, 2026, 11:00 AM ET |
| Duration | 60 min |
| Platform | Microsoft Teams (transcription on) |
| Organiser | Olena Marchuk (Intellias) |

## Attendees

| Name | Company | Role |
|---|---|---|
| Ravi Menon | Amperlane | Co-founder & CTO |
| Priya Nair | Amperlane | Senior Software Engineer |
| Luis Ortega | Amperlane | Co-founder & COO / Head of Partnerships (joined ~00:18, left ~00:38) |
| Olena Marchuk | Intellias | Solution Architect (leads the session) |
| Kyrylo Shvedov | Intellias | Engagement Lead, Product & Business Analysis |
| Andriy Bondar | Intellias | Payments & Integrations Lead |

## Transcript

[00:00:05] Kyrylo Shvedov (Intellias): Hi, hello — can you hear me okay? I think Ravi's connecting… there he is.
[00:00:14] Ravi Menon (Amperlane): Hey, yeah. Sorry, Teams made me prove I'm a human again.
[00:00:21] Olena Marchuk (Intellias): Every time. Hi Ravi. Hi Priya, nice to finally meet you.
[00:00:27] Priya Nair (Amperlane): Hi everyone, likewise.
[00:00:30] Kyrylo Shvedov (Intellias): Quick intros, since the group is a bit different from last time. Olena you met on the first call — well, Ravi, most of it. She's our solution architect and she'll drive today. And this is Andriy Bondar, he leads payments and integrations. He's done marketplace payouts on Stripe Connect and Adyen.
[00:00:58] Andriy Bondar (Intellias): Hi both. I heard you're a payments person, Ravi, so I'm a little nervous.
[00:01:07] Ravi Menon (Amperlane): [laughs] I'm the friendly kind. I just have scars. Four years on payouts at a fintech — if you say "we'll reconcile it later", I will flinch.
[00:01:21] Andriy Bondar (Intellias): That's fair. I flinch too.
[00:01:25] Kyrylo Shvedov (Intellias): Luis will join around quarter past, twenty past, for the station part — he's on a site visit in Queens. So, plan: first, what you have today, honestly. Then stations when Luis is on. Then the booking engine, vehicles, payments, NFRs. And I'll keep asking annoying "what happens when" questions. That's my job.
[00:01:53] Ravi Menon (Amperlane): Sounds good. Priya, you start? You know where the bodies are buried.
[00:02:00] Priya Nair (Amperlane): Ha. Yeah. So the Concierge pilot has been running since October last year. Ops side is Retool on top of Airtable. Airtable is the bookings database — every booking is a row: driver, fleet, site, slot, status. Then each site has a Google Sheet that's the slot grid. Rows are fifteen-minute slots, columns are stalls, and ops colour the cells.
[00:02:31] Olena Marchuk (Intellias): Colour them by hand?
[00:02:34] Priya Nair (Amperlane): By hand. Green free, yellow held, red taken. There's a nightly script that copies some of it back into Airtable, but honestly the source of truth is whatever the ops person on shift has open at 4:30 PM.
[00:02:54] Kyrylo Shvedov (Intellias): The cab shift change.
[00:02:58] Priya Nair (Amperlane): Exactly. For drivers there's a Twilio SMS bot. Driver texts a code — like "GOW 1645" — the bot drops a request into Airtable, and someone in ops confirms it manually. Then ops phone the station to put a cone or a "Reserved" tag on the stall. At LIC they call the garage attendant.
[00:03:25] Andriy Bondar (Intellias): And money?
[00:03:28] Priya Nair (Amperlane): Drivers pay the station directly, own card or the station app. We never touch charging money. We invoice the fleets monthly in Stripe Billing, two dollars per completed booking. Very thin Stripe setup — customers and invoices, no Connect.
[00:03:48] Olena Marchuk (Intellias): And the app Dana mentioned?
[00:03:52] Priya Nair (Amperlane): Right. A freelancer built a Next.js 14 plus Supabase driver app early this year. It's maybe thirty-five percent done — auth, a map with the three sites, a booking form that writes to a table. No tests. Never went to production. I "maintain" it, in the sense that I stop it from breaking.
[00:04:20] Ravi Menon (Amperlane): And honestly, I'd bin it. I'm not attached. The data model is Airtable in Postgres clothes — there's no EVSE, no connector, a slot is a timestamp string. I'd rather start clean.
[00:04:37] Olena Marchuk (Intellias): Good to hear early. So what do we keep?
[00:04:43] Ravi Menon (Amperlane): The history. A year of pilot data — bookings, no-shows, arrival times, which driver, which stall. That's the only real dataset on how fleet drivers actually behave, and it'll be in the Series A data room. So pilot history has to be migrated into whatever we build. Properly — not a CSV dump in an S3 bucket.
[00:05:12] Kyrylo Shvedov (Intellias): How clean is it? If I pull last December and this September, does a no-show look the same?
[00:05:22] Priya Nair (Amperlane): [laughs] No. We changed the status values twice. Early on a no-show was "cancelled" with a note. And the Sheets and Airtable sometimes disagree. From about February it's decent.
[00:05:38] Kyrylo Shvedov (Intellias): Okay, so migration is a real work item — mapping and cleansing, not a weekend script. I'll put the scope on the open list: how far back, and what "migrated" means for you.
[00:05:56] Olena Marchuk (Intellias): And stack preferences — I've heard them from Dana, but I'd rather hear them from you.
[00:06:05] Ravi Menon (Amperlane): TypeScript end to end if we can, Postgres, AWS. We have a hundred K in AWS Activate credits I'd like to use. Open source where it's mature — I don't want to be the first production user of somebody's weekend project. And the big one for me: the IP has to be ours. I've seen startups where the agency owns the platform and the startup rents its own product. Not doing that.
[00:06:41] Olena Marchuk (Intellias): Understood, and that's our default anyway: code in your repos, your AWS accounts, your Terraform.
[00:06:50] Ravi Menon (Amperlane): Good. Same with vendors generally. I don't want a CSMS vendor's SDK baked into the booking core. If a station switches CSMS tomorrow, I want to swap an adapter, not rewrite the engine.
[00:07:08] Olena Marchuk (Intellias): That's exactly the shape I'd propose — adapters at the edge. Which takes us into protocols. Ravi, how comfortable are you with OCPP and OCPI? No judgement.
[00:07:23] Ravi Menon (Amperlane): I know they exist. OCPP is charger-to-backend, OCPI is backend-to-backend, roaming. Beyond that I've been reading specs at night and falling asleep.
[00:07:35] Olena Marchuk (Intellias): That's actually a very accurate summary. Let me give the five-minute version, because it changes the booking design a lot. The brief says "real-time reservation on every charger via OCPP". OCPP does have ReserveNow and CancelReservation. But, two things. One: reservations are an optional feature. A charger can just reject it, and many do.
[00:08:03] Ravi Menon (Amperlane): Optional as in the firmware may not implement it?
[00:08:09] Olena Marchuk (Intellias): Yes, or the operator turned it off. Two — the bigger one: ReserveNow means "hold this from now until this expiry time". It's not a calendar. You can't say "EVSE 3, Thursday, 4:45 to 5:30". It's "lock it now for the next N minutes". In 2.0.1 the EVSE can even be unspecified, filtered by connector type, and the station reports expiry with a ReservationStatusUpdate. But no future slot.
[00:08:43] Ravi Menon (Amperlane): Huh. So the cinema seat thing —
[00:08:48] Olena Marchuk (Intellias): — the seat map lives in your system. Amperlane owns the slot calendar. The charger, at best, gets told "hold now" shortly before the slot. ReserveNow goes out about fifteen minutes before, where supported. Elsewhere it's a soft hold on our side plus a physical or ops fallback.
[00:09:13] Priya Nair (Amperlane): Which is basically the cones.
[00:09:17] Olena Marchuk (Intellias): Yes. Your cones are a manual ReserveNow. [laughs]
[00:09:22] Kyrylo Shvedov (Intellias): First "what happens when". We send the hold at T-minus-fifteen and someone from the street plugged in at T-minus-twenty. Then what?
[00:09:34] Olena Marchuk (Intellias): The charger rejects it or reports occupied. So the engine needs a "station hold failed" state and a decision: another matching EVSE at the same site, or notify the driver and ops. Part of that is a business question for Luis — how they treat walk-ups.
[00:09:58] Kyrylo Shvedov (Intellias): Parking it for Luis.
[00:10:01] Priya Nair (Amperlane): Can I ask a dumb one? The deck has the NREL API for live availability. I actually got a key in spring and couldn't find any "is it free right now" field. I assumed I was looking in the wrong place.
[00:10:23] Olena Marchuk (Intellias): Not dumb, and you weren't looking in the wrong place. Two things. NREL was renamed — since December last year it's the National Laboratory of the Rockies, NLR. The AFDC station API is at developer.nlr.gov now. Free key, a thousand requests an hour. But it's static data — location, connectors, power, network, hours. No real-time availability.
[00:10:52] Priya Nair (Amperlane): Okay. So that line in the deck is wrong twice.
[00:10:58] Ravi Menon (Amperlane): [laughs] Dana's going to love that.
[00:11:03] Olena Marchuk (Intellias): Very common mistake. So: use it for discovery, not availability. If a driver is in the Bronx and none of your partner sites is close, AFDC and Open Charge Map can show public fast chargers nearby — Open Charge Map's contributed data is CC BY 4.0, so we check attribution. But live status only comes from the CSMS APIs, or from OCPI 2.2.1 Locations if the operator peers with you.
[00:11:38] Ravi Menon (Amperlane): Partner sites live, everything else a static map layer.
[00:11:44] Kyrylo Shvedov (Intellias): Which helps scope, by the way. "All NYC chargers, live" was quietly sitting in the brief, and nobody can deliver that.
[00:11:56] Olena Marchuk (Intellias): Now OCPI, since it's background for Luis's part anyway. OCPI has roles; the two that matter are CPO, the charge point operator, and eMSP, the e-mobility service provider — the one with the driver relationship. Your natural role is eMSP, with an onboarding path for CPOs.
[00:12:20] Ravi Menon (Amperlane): And versions? I've seen four numbers.
[00:12:24] Olena Marchuk (Intellias): Yeah. 2.2.1 is the most widely deployed, and it matters in the US because NEVI-funded stations must support OCPP 2.0.1 and OCPI 2.2.1 — that's 23 CFR 680.108. Then 2.3.0 came out in February 2025, and in June 2025 they added a Booking module — calendars, booking by location or charge point, licence plate link, no-show fees. Basically your product, as a protocol.
[00:12:56] Ravi Menon (Amperlane): Oh. So we just use that?
[00:13:01] Olena Marchuk (Intellias): That's the catch — US adoption is likely low. The real example I know is Hubject with partners: they presented a Reservation Hub pilot in September 2025, built on the 2.3 booking module. But that's Europe, and it's trucks. So it validates the model, but it's a roadmap item, not March MVP. And 3.0 is still a draft — ignore it.
[00:13:32] Ravi Menon (Amperlane): Got it. Our own model, designed so it maps onto 2.3 Booking later.
[00:13:40] Olena Marchuk (Intellias): Exactly. We'd look at their data model when we design the slot entity.
[00:13:48] Andriy Bondar (Intellias): One addition: OCPI also has CDRs — charge detail records. Energy, time, cost, from the CPO. That becomes the backbone for settlement and disputes. I'll come back to it.
[00:14:03] Olena Marchuk (Intellias): Priya, Gowanus is the AMPECO one — what have you touched there?
[00:14:11] Priya Nair (Amperlane): So Kinship gave us credentials to the a pecko API — sorry, AMPECO, the transcript's going to love that. It's REST, with webhooks for status changes. I wired a listener into the prototype that just logs status. There's a reservation endpoint, I think it's OCPP ReserveNow underneath, but it only works on ten of the sixteen chargers. The other six reject it.
[00:14:43] Olena Marchuk (Intellias): Firmware?
[00:14:45] Priya Nair (Amperlane): That's what Kinship says. Luis knows whether they'll ever fix it.
[00:14:51] Andriy Bondar (Intellias): Do the webhooks retry? At-least-once?
[00:14:55] Priya Nair (Amperlane): I saw duplicates in the logs, so I'd guess yes.
[00:15:02] Andriy Bondar (Intellias): Fine — we assume duplicates and out-of-order anyway. Idempotent consumers plus a periodic poll to reconcile, because webhooks always get lost eventually.
[00:15:14] Ravi Menon (Amperlane): Same as payment webhooks. Never the only path.
[00:15:19] Kyrylo Shvedov (Intellias): Let me check scale too, because "burst" is in Dana's language but I don't have a number. Peak booking attempts at shift change?
[00:15:32] Priya Nair (Amperlane): Today the worst ten minutes is maybe forty, fifty requests. But we modelled launch with the fleets in the pipeline and used about four hundred booking attempts in ten minutes, around 4:30.
[00:15:49] Olena Marchuk (Intellias): Attempts, not successful bookings.
[00:15:52] Priya Nair (Amperlane): Attempts. Lots of retries, lots of people picking the same popular slot.
[00:16:00] Olena Marchuk (Intellias): That's the key point — it's contention, not throughput. Four hundred in ten minutes is nothing in requests per second. The hard part is a hundred of them wanting the same five stalls in the same quarter-hour.
[00:16:19] Ravi Menon (Amperlane): Like a concert ticket drop.
[00:16:23] Olena Marchuk (Intellias): Like a cinema on Friday night. We'll do that properly after Luis. Priya, how is a site modelled in Airtable — stalls, connectors?
[00:16:36] Priya Nair (Amperlane): Stall number, max kW, connector as a text field. Gowanus has four NACS ports, so those say "NACS". Everything else "CCS". That's it.
[00:16:49] Olena Marchuk (Intellias): Okay, I'll come back to connectors. That text field is going to grow.
[00:16:57] Kyrylo Shvedov (Intellias): While we wait — let me read you my other two "what happens when"s for the engine, you tell me if they're real. A driver's previous Uber trip runs long and they arrive twelve minutes late. And a charger faults at 2 PM with bookings on it until 7.
[00:17:22] Priya Nair (Amperlane): Both happened this month. The second one was last Tuesday. That was a day.
[00:17:30] Kyrylo Shvedov (Intellias): I'm saving that story for the ops console part.
[00:17:36] Ravi Menon (Amperlane): You'll enjoy it. Priya didn't.
[00:17:40] Kyrylo Shvedov (Intellias): I see someone in the lobby… "Luis O iPhone". Admitting.
[00:17:46] Kyrylo Shvedov (Intellias): Luis? I think you're on mute.
[00:17:51] Ravi Menon (Amperlane): Luis, you're muted, buddy.
[00:17:54] Kyrylo Shvedov (Intellias): He dropped. He'll come back.
[00:17:58] Kyrylo Shvedov (Intellias): Okay, Luis is back in the lobby. Admitting again.
[00:18:04] Luis Ortega (Amperlane): — so that's why I told them we can't — oh. Hi. Can you hear me now?
[00:18:13] Kyrylo Shvedov (Intellias): Now we can. Welcome.
[00:18:16] Luis Ortega (Amperlane): Sorry, I was explaining a whole thing to nobody. I'm in the car outside JFK Lot 9, which is perfect for this conversation.
[00:18:28] Olena Marchuk (Intellias): Perfect timing. You missed the bad news already — OCPP reservations are not a calendar, and NREL is now NLR and static.
[00:18:40] Luis Ortega (Amperlane): Oh, I live the bad news. [laughs] You want the three sites?
[00:18:47] Olena Marchuk (Intellias): Please. What they give you, what they won't.
[00:18:52] Luis Ortega (Amperlane): Gowanus FastHub, Kinship Charging. Independent CPO, sixteen ports, 150 up to 320 kW, CCS1 plus four NACS. On AMPECO. Best partner by far, technically and in attitude. REST, webhooks, reservations work on ten of sixteen. The other six, firmware. I've asked three times. The answer is "it's on the list", and you know what that means.
[00:19:19] Olena Marchuk (Intellias): So ten reservable and six soft-hold at Gowanus, as configuration — if the firmware gets fixed, ops flips a flag per EVSE.
[00:19:30] Luis Ortega (Amperlane): Per charger, yes, not per site. JFK Lot 9 — where I'm sitting — is Jamaica Bay Energy. Twenty ports, 150 kW, all CCS1, on ChargeLab. ChargeLab's open API gives us status and pricing. No reservations, none. And they plan OCPI 2.2.1 peering "sometime in 2027" — I'm doing air quotes in my car.
[00:19:56] Kyrylo Shvedov (Intellias): We believe you. [laughs]
[00:19:59] Luis Ortega (Amperlane): Then LIC Garage Depot in Long Island City. Not a CPO — a garage owner, Hunters Point Garages. Ten ports, 62.5 to 125 kW, CCS1. The chargers sit on a legacy ChargePoint network contract they signed years ago. They see status in the portal, we get a CSV export. No usable API for them. So effectively our API is the garage attendant.
[00:20:29] Ravi Menon (Amperlane): Who is a lovely man.
[00:20:33] Luis Ortega (Amperlane): A lovely man, and our only real-time feed. [laughs]
[00:20:38] Olena Marchuk (Intellias): This is the most useful ten minutes so far, because it means three supply patterns, not one. A: API-connected with reservation support — Gowanus. B: status only — JFK. C: no API — LIC.
[00:20:55] Luis Ortega (Amperlane): And in New York, C isn't rare. Garages, depots, private hosts — the chargers are whatever the installer sold them five years ago.
[00:21:07] Olena Marchuk (Intellias): I believe it. For A, the AMPECO adapter sends ReserveNow at T-minus-fifteen where the EVSE supports it, soft hold where it doesn't. For B we see live status, so we know if the stall's free before the driver arrives; the hold is ours, plus signage, plus ops fallback. Do they do cones at JFK?
[00:21:33] Luis Ortega (Amperlane): They grumble, but yes. At 4 PM they're busy and sometimes the cone doesn't happen.
[00:21:41] Olena Marchuk (Intellias): And C — short term, ingest the CSV. How often can they export?
[00:21:49] Luis Ortega (Amperlane): Whenever the attendant remembers. Twice a day, maybe. Not automatic.
[00:21:55] Olena Marchuk (Intellias): Then the CSV is for reconciliation, not live status. Plus a tiny attendant app — mobile web, a few buttons: stall free, occupied, faulted, driver arrived. Longer term, move the host off the legacy network to direct OCPP, with something like citrine O.S. as the backend.
[00:22:17] Ravi Menon (Amperlane): Citrine what?
[00:22:19] Olena Marchuk (Intellias): CitrineOS, one word. Open-source CSMS under LF Energy, Apache-2.0. TypeScript, Node, PostgreSQL with PostGIS, supports OCPP 1.6, 2.0.1 and 2.1, and it has an OCPI server. So, Ravi — literally your stack.
[00:22:35] Ravi Menon (Amperlane): Oh, that's interesting. So we'd become the CSMS for small hosts?
[00:22:42] Olena Marchuk (Intellias): For hosts with no CSMS, or who want out of a contract, yes. Chargers connect to your CitrineOS over OCPP and you get full control, including reservations where firmware allows. But it's a business decision — you'd be operating charger backends. Support, uptime, firmware headaches.
[00:23:04] Luis Ortega (Amperlane): And the LIC contract isn't ending tomorrow. But I like having it in the pitch to hosts.
[00:23:13] Kyrylo Shvedov (Intellias): So for MVP: LIC is CSV plus attendant app, and CitrineOS is a described option, not necessarily built by March?
[00:23:23] Olena Marchuk (Intellias): That's how I see it. And there's EVerest, also LF Energy, a charger-side stack — we'd use it as a charger simulator, so we can fake a hundred misbehaving chargers without driving to Queens.
[00:23:40] Luis Ortega (Amperlane): I would love to not drive to Queens.
[00:23:45] Ravi Menon (Amperlane): You're in Queens right now.
[00:23:49] Luis Ortega (Amperlane): Exactly my point.
[00:23:52] Kyrylo Shvedov (Intellias): Luis, the question we parked: we send the hold at T-minus-fifteen and a walk-up is already plugged in. Do stations let us bump walk-ups?
[00:24:04] Luis Ortega (Amperlane): Never. A walk-up paying full public price is real money. We can't ask them to unplug a guy. That's why the capacity caps exist — at peak only thirty to fifty percent of ports bookable — so there's always somewhere else at the site. If the stall is taken, move the booking to another free one. If the whole site's full, which happens at JFK, ops gets pinged.
[00:24:36] Olena Marchuk (Intellias): So a booking is against a pool of compatible EVSEs at the site, and the actual EVSE gets assigned late — around T-minus-fifteen. Not "you get stall 4" at booking time.
[00:24:52] Luis Ortega (Amperlane): Right. Drivers don't care about stall 4. They care about plugging in.
[00:24:59] Andriy Bondar (Intellias): That also helps concurrency — fewer hot rows.
[00:25:04] Olena Marchuk (Intellias): Partly. We'll get there.
[00:25:07] Luis Ortega (Amperlane): Can I add LA while I'm here? I have to drop at about twenty to.
[00:25:15] Olena Marchuk (Intellias): Please.
[00:25:17] Luis Ortega (Amperlane): The two LA prospects I'm talking to both speak O.C.P.I 2.2.1 already. One because they have NEVI-funded sites, one because they roam with the big networks. So LA should be standard OCPI, not three snowflakes like New York.
[00:25:36] Olena Marchuk (Intellias): Great news, and it changes priorities. The OCPI 2.2.1 eMSP gateway becomes the integration you'll reuse most. I'd build it in Phase 1 even if no New York site uses it on day one — against a test CPO — so it's proven before LA.
[00:25:58] Ravi Menon (Amperlane): What does the eMSP side actually give us? Status, I get. Reservations?
[00:26:05] Olena Marchuk (Intellias): In 2.2.1 the useful pieces are Locations — sites, EVSEs, connectors and live EVSE status — plus Tariffs, Sessions, CDRs, Tokens and Commands. Commands has RESERVE_NOW, which maps to OCPP ReserveNow at the station. Same semantics: hold now, not a calendar. The calendar is still yours.
[00:26:27] Ravi Menon (Amperlane): So whatever happens, the calendar is ours. That's reassuring, actually. That's the IP.
[00:26:34] Olena Marchuk (Intellias): The calendar and the matching are the product. The protocols are pipes.
[00:26:41] Kyrylo Shvedov (Intellias): Luis, can we get the two LA names? Not today necessarily. It changes how hard we lean on OCPI in the proposal.
[00:26:53] Luis Ortega (Amperlane): One's under NDA. Let me check with Dana and send what I can.
[00:27:00] Olena Marchuk (Intellias): Okay, let me share my screen, the next part is easier with a picture. Can you see my screen?
[00:27:10] Priya Nair (Amperlane): Yes — a whiteboard with lots of boxes.
[00:27:15] Luis Ortega (Amperlane): I'm on a phone, it's tiny, but I see colours.
[00:27:21] Olena Marchuk (Intellias): That's enough. This is the booking lifecycle, first sketch. Driver picks a site and time window, which creates a Hold with a TTL — say three minutes to confirm. Unconfirmed, it expires and the capacity goes back. Confirmed. Reminder. At T-minus-fifteen, the Station Hold step — ReserveNow for pattern A, signage or ops for B and C. Then Arrived, Charging, Completed with the CDR or session record, and Settled.
[00:27:54] Kyrylo Shvedov (Intellias): And the red arrows?
[00:27:57] Olena Marchuk (Intellias): Side paths. No-show: driver doesn't arrive within grace — ten minutes, from the first call — slot auto-releases, and a no-show fee is created. Charger fault: triggers rebooking. And the one I want to talk about: the previous movie overruns.
[00:28:17] Ravi Menon (Amperlane): The guy before me is still charging.
[00:28:21] Olena Marchuk (Intellias): Yes. In a cinema, the 7 PM film ends at 9 and the 9:15 starts after cleaning. With chargers, the previous movie is a driver at 74% who wants 80% and won't unplug, or a walk-up who just left the car.
[00:28:42] Luis Ortega (Amperlane): Honestly, some days that's a bigger problem than no-shows. Gowanus has idle fees, but a rideshare guy at 74% will pay a couple of bucks and wait.
[00:28:55] Olena Marchuk (Intellias): So, levers. Buffers between slots — in the sketch, fifteen-minute calendar granularity, bookings of thirty, forty-five or sixty minutes, and a ten-minute buffer. Live status — if at T-minus-ten the EVSE is still in a session, reassign to another free compatible one before the driver arrives. And an overbooking policy, like airlines — which I'd keep off by default.
[00:29:24] Luis Ortega (Amperlane): Please, off. If a cab driver shows up at 4:45 at shift change and there's no stall, he's not coming back. Ever.
[00:29:35] Ravi Menon (Amperlane): Off by default. Maybe a per-site setting off-peak, later.
[00:29:41] Olena Marchuk (Intellias): Exactly — a capacity rule, per site, per time window, same place as the peak cap.
[00:29:49] Kyrylo Shvedov (Intellias): The late driver — twelve minutes, beyond grace. Is that a no-show?
[00:29:56] Luis Ortega (Amperlane): For the station, yes. The stall sat empty.
[00:30:01] Priya Nair (Amperlane): But today we usually rebook them if something's free. A lot of the twenty-two percent late arrivals still charged.
[00:30:11] Olena Marchuk (Intellias): Then: grace expires, slot is released, booking goes to no-show, and the driver gets an instant offer for whatever's free now. Whether the fee still applies if they rebook is policy — ideally fleet-configurable.
[00:30:28] Kyrylo Shvedov (Intellias): And still open from Call 1 — who pays the no-show fee, fleet or driver.
[00:30:36] Luis Ortega (Amperlane): Dana and I haven't agreed on that. [laughs]
[00:30:41] Olena Marchuk (Intellias): Now concurrency. Andriy, you wanted to fight.
[00:30:46] Andriy Bondar (Intellias): [laughs] Not fight. Two schools for the burst. One: a single writer per EVSE, or per site — every booking command for that site goes through one consumer, so by construction there's no race. Two: everyone writes in parallel and Postgres says no.
[00:31:07] Ravi Menon (Amperlane): I'm a "let Postgres say no" person, I'll tell you now.
[00:31:13] Andriy Bondar (Intellias): I suspected.
[00:31:16] Olena Marchuk (Intellias): Honestly, we do both. The invariant lives in the database: a Postgres exclusion constraint. Each allocation has the EVSE ID and the slot as a tstzrange, and a GiST exclusion constraint says same EVSE plus overlapping range is not allowed. The database refuses the second one. That's "no double booking, ever", and it doesn't depend on our code being correct.
[00:31:45] Ravi Menon (Amperlane): Yes. That's what I want. Are holds rows in that table too?
[00:31:51] Olena Marchuk (Intellias): They can be, with status and expiry; the constraint applies only to active states — held or confirmed — and a timer expires stale holds. Or short-lived holds live in Redis with a TTL and only confirmed bookings hit Postgres. I lean to the first for auditability, but we'd prototype both.
[00:32:16] Andriy Bondar (Intellias): And on top, a single-writer queue per site at burst time. Not for correctness — Postgres does correctness — but fairness and UX. If a hundred people hit the same quarter-hour, you don't want ninety-five constraint errors and an ugly "try again". You process them in order, and the losers get an instant alternative: "4:45 is gone, 5:00 is free, take it?"
[00:32:46] Ravi Menon (Amperlane): Belt and braces. I can live with that.
[00:32:51] Andriy Bondar (Intellias): And idempotency keys on every booking request. The driver's on bad 4G by the canal, taps confirm, nothing happens, taps again. Same key, same result, one booking.
[00:33:05] Ravi Menon (Amperlane): I'd have fired someone for not doing that. [laughs] Same for SMS — if Twilio retries the inbound webhook —
[00:33:15] Andriy Bondar (Intellias): — message ID as the dedupe key, yes.
[00:33:20] Priya Nair (Amperlane): We have exactly that bug today. Twice a week someone gets two confirmations because the bot ran twice.
[00:33:30] Andriy Bondar (Intellias): Classic.
[00:33:32] Olena Marchuk (Intellias): And for timers — hold expiry, T-minus-fifteen, grace, auto-release — not cron jobs. Each booking is a small long-running workflow with timers and compensations. I'd use Temporal; it's open source with a mature TypeScript SDK, self-hosted or their cloud.
[00:33:51] Ravi Menon (Amperlane): We used Temporal for payouts at my last job. Fine. Self-host, though — no extra vendor contract in year one if we can avoid it.
[00:34:04] Olena Marchuk (Intellias): Noted, we'll cost both.
[00:34:07] Kyrylo Shvedov (Intellias): Load test target, so it goes in the proposal. Expected burst is four hundred attempts in ten minutes. I'd test at five times that, with heavy contention on a few sites.
[00:34:22] Ravi Menon (Amperlane): Five x is fine.
[00:34:26] Olena Marchuk (Intellias): Stopping share for a second. Luis — when a charger goes down at Gowanus, how do you find out today?
[00:34:36] Luis Ortega (Amperlane): Today? The driver texts "it's broken". Sometimes Kinship emails. The AMPECO status webhook exists — Priya logs it — but nothing acts on it.
[00:34:48] Olena Marchuk (Intellias): So the system would see "Faulted" via webhook or poll, find every booking allocated to that EVSE for the rest of the day, reassign each to a compatible EVSE at the same site, and for those it can't — notify the driver with alternatives and push to ops. And the station sees it too.
[00:35:14] Luis Ortega (Amperlane): That'd be magic. Stations would love a view that says "charger 7 is down and it's costing you six bookings". That's leverage for me with their maintenance people.
[00:35:29] Kyrylo Shvedov (Intellias): Station portal feature: bookings lost per fault. Writing it down.
[00:35:35] Andriy Bondar (Intellias): Luis, quick one on money before you go. Payouts — what do stations expect?
[00:35:42] Luis Ortega (Amperlane): Weekly. Kinship said it straight: "if you're holding our money, pay us weekly". Jamaica Bay too. They're small, cash flow matters.
[00:35:53] Andriy Bondar (Intellias): And fleets pay —
[00:35:57] Luis Ortega (Amperlane): Net-30, one invoice a month. Borough Green's finance lead said she will not deal with a hundred and sixty drivers' card receipts.
[00:36:08] Andriy Bondar (Intellias): So there's a working-capital gap built into the model: weekly out, monthly in. A finance discussion, but it shapes settlement.
[00:36:18] Luis Ortega (Amperlane): Dana knows. It's the eMSP idea from last week — we'd sit in the middle of the money.
[00:36:28] Kyrylo Shvedov (Intellias): Which is still the open business-model question — percentage, spread, or both. We'll propose a workshop.
[00:36:37] Luis Ortega (Amperlane): Please. Dana and I need a referee. Olena — anything I should ask stations for now, in contracts? I'm talking to Kinship about their renewal soon.
[00:36:50] Olena Marchuk (Intellias): Three things. API sandbox access, not just production — we want to test against AMPECO without touching real chargers. The firmware update on those six chargers, even as "best effort by date X". And per-session records — the CDR equivalent — via API, so we reconcile and handle disputes without email.
[00:37:15] Luis Ortega (Amperlane): Sandbox, firmware, session records. Kinship owes me a favour, I'll push for the sandbox this week.
[00:37:23] Kyrylo Shvedov (Intellias): And the ChargeLab API docs JFK gave you — the actual ones?
[00:37:30] Luis Ortega (Amperlane): I'll forward them.
[00:37:33] Luis Ortega (Amperlane): Okay — anything else on stations before I go?
[00:37:39] Kyrylo Shvedov (Intellias): Not from me. That covered a lot, thank you.
[00:37:44] Luis Ortega (Amperlane): Great. Then I'm off — parking enforcement is circling. This was super useful. Bye all.
[00:37:51] Olena Marchuk (Intellias): Thanks Luis, really helpful.
[00:37:54] Kyrylo Shvedov (Intellias): Bye Luis.
[00:37:56] Olena Marchuk (Intellias): Okay — vehicle data. The brief says "Tesla API for battery data". Ravi, what's the need behind it?
[00:38:05] Ravi Menon (Amperlane): Two things. State of charge helps us suggest slot length — at 15% you need forty-five minutes, at 50% maybe twenty. And arrival: if we see the car approaching the site, it's not a no-show, and we can stretch grace if they're two blocks away.
[00:38:24] Olena Marchuk (Intellias): Both make sense. Reality check: Borough Green has Geotab on the non-Teslas — Ioniq 5, Niro, Equinox. Geotab gives SoC and charging data for 300-plus EV models, but needs its hardware in the car, which they already have. That's the easy one.
[00:38:43] Priya Nair (Amperlane): And Teslas are about fifty-five percent of their fleet. We have nothing on them.
[00:38:50] Olena Marchuk (Intellias): For those, the Tesla Fleet API. Since late 2024 it's pay-per-use — about a dollar per hundred and fifty thousand streamed signals, a tenth of a cent per command, two-tenths of a cent per data request, two cents per wake, with a ten-dollar monthly credit. Small per unit, but streaming SoC and location on a couple of hundred cars all day adds up. We'd model it, and someone decides who pays — Amperlane or the fleet.
[00:39:18] Ravi Menon (Amperlane): And it needs authorisation from the account owner?
[00:39:22] Olena Marchuk (Intellias): Yes — and separately, the driver must consent to location tracking. They're independent contractors, and location is personal data. We'll come back to that under SHIELD.
[00:39:34] Andriy Bondar (Intellias): There's also Smartcar — one API across about thirty EV brands: SoC, charging state, location. The generic fallback for fleets without Geotab, and it saves you writing one integration per OEM.
[00:39:48] Ravi Menon (Amperlane): Smartcar for the Teslas too, or Fleet API direct?
[00:39:53] Andriy Bondar (Intellias): We'd compare cost and reliability in Phase 0. I wouldn't commit today.
[00:39:59] Kyrylo Shvedov (Intellias): And the cab company?
[00:40:02] Priya Nair (Amperlane): No telematics. Twelve cars, twenty-four drivers, personal phones.
[00:40:06] Olena Marchuk (Intellias): Then manual SoC entry — optional, one slider in the booking flow, "what's your battery at?" And arrival without telematics: phone location if the driver allows, a QR code at the stall, or simply the session-start event from the CSMS.
[00:40:24] Priya Nair (Amperlane): QR at the stall works at LIC too. The attendant could put them up.
[00:40:31] Kyrylo Shvedov (Intellias): So MVP: Geotab plus manual SoC. Tesla Fleet API and Smartcar after a cost check. Fair cut?
[00:40:39] Ravi Menon (Amperlane): I'm a bit sad about Tesla — it's more than half of Borough Green. But if the cost isn't modelled, I'd rather not promise it.
[00:40:50] Kyrylo Shvedov (Intellias): We'll show Tesla as an explicit option with a cost model, so you decide with numbers.
[00:40:58] Olena Marchuk (Intellias): Related — connectors, Priya's text field. The NACS transition, SAE J3400, is under way, and Gowanus has four NACS ports. A booking can't just be "a slot at Gowanus"; it has to match the vehicle's connector, whether an adapter is allowed, and max power.
[00:41:17] Priya Nair (Amperlane): We've had Teslas booked onto CCS stalls with no adapter. And an Ioniq landed on a NACS stall.
[00:41:26] Ravi Menon (Amperlane): Wait, that happened?
[00:41:28] Priya Nair (Amperlane): Twice. Ops fixed it on the spot.
[00:41:32] Olena Marchuk (Intellias): So the vehicle profile has native connector, allowed adapters, and max DC power. Each EVSE connector has type and max kW. Matching is part of availability. And power matters for slot length — a forty-five-minute estimate on a 320 kW stall is wrong on LIC's 62.5 kW unit.
[00:41:53] Kyrylo Shvedov (Intellias): Adapter policy is set by the fleet? "Borough Green allows CCS adapters on Teslas"?
[00:42:00] Olena Marchuk (Intellias): Fleet policy, overridable per vehicle. And power matching gives smarter allocation — the 320 kW stalls go to cars that can use them.
[00:42:11] Ravi Menon (Amperlane): That's real. Put it in.
[00:42:14] Kyrylo Shvedov (Intellias): Next — Uber and Lyft. The wishlist says "deep link plus data". Ravi, I think deep integration was yours?
[00:42:23] Ravi Menon (Amperlane): Guilty. The driver lives in the Uber driver app. If we could see when a trip ends, or get SoC from Uber, we could offer a slot at the perfect moment. "You just dropped off in Red Hook, Gowanus has a slot in eight minutes."
[00:42:43] Andriy Bondar (Intellias): Great product idea. The problem is access. The Uber Driver API is limited-access — you have to be approved — and it has no vehicle or EV data at all. No SoC. And Lyft has no public driver or fleet API.
[00:43:01] Ravi Menon (Amperlane): I kind of knew. I was hoping you knew a back door.
[00:43:07] Andriy Bondar (Intellias): No back doors. [laughs] So: drop it from the MVP. Deep links only — SMS opens Amperlane, Amperlane opens navigation or goes back to the driver app. Context like "trip ended" comes from the driver, not from Uber.
[00:43:24] Kyrylo Shvedov (Intellias): Uber and Lyft beyond deep links — Phase 2, explicitly out of MVP.
[00:43:30] Ravi Menon (Amperlane): Okay. But there's a related thing that's actually more important. One of the two big ones — can't say which — their EV team reached out. They're interested in a pilot. First thing they asked was security posture: SOC 2 Type I within twelve months, and a pen test.
[00:43:51] Kyrylo Shvedov (Intellias): Twelve months from when?
[00:43:54] Ravi Menon (Amperlane): From pilot start, roughly — next spring if we're lucky. Earlier would be better, it helps the Series A too.
[00:44:04] Olena Marchuk (Intellias): Then we build SOC 2-ready from day one — access control, audit logging, change management, encryption, separate prod account — so the audit is a process exercise, not a rebuild. Type I itself needs an auditor, usually a compliance tool, and that's on your side, but we design for it.
[00:44:25] Ravi Menon (Amperlane): That's what I want. I don't want to find out in a year we need to rewrite auth.
[00:44:34] Kyrylo Shvedov (Intellias): SOC 2 timing goes on the open list — when exactly you need to be audit-ready changes the March scope.
[00:44:43] Andriy Bondar (Intellias): Okay, payments. Ravi, I'll try not to bore you.
[00:44:48] Ravi Menon (Amperlane): Bore me. This is my part.
[00:44:52] Andriy Bondar (Intellias): [laughs] Today it's Stripe Billing, two dollars per booking, simple. But the model Dana described — Amperlane as eMSP and merchant of record, buying the session at the station's B2B tariff, the forty-two cents at Gowanus, and billing the fleet a bundled rate, the forty-nine — puts you in the money flow. Fleet pays you, you pay stations.
[00:45:17] Ravi Menon (Amperlane): Which immediately makes me think money transmission. If we receive money on behalf of stations and pass it on, are we a money transmitter in New York? I do not want to apply for that licence.
[00:45:33] Andriy Bondar (Intellias): Exactly the right question. I'm not your lawyer, counsel has to sign off. But architecturally: keep the funds flows inside Stripe Connect. Stations are connected accounts, Stripe holds and moves the funds, and you take your margin as the platform. Money never sits in your own bank account waiting to be paid out.
[00:45:56] Ravi Menon (Amperlane): Which charge type?
[00:45:58] Andriy Bondar (Intellias): Separate charges and transfers. One fleet invoice covers sessions at many stations over a whole month. Destination charges tie each charge to one connected account, which doesn't fit "one invoice, many stations". With separate charges and transfers, you invoice the fleet through Stripe Invoicing, net-30, and transfer to each station on your own schedule.
[00:46:21] Ravi Menon (Amperlane): Weekly.
[00:46:23] Andriy Bondar (Intellias): Weekly. So stations get paid up to seven or eight weeks before the fleet pays for those sessions. That's cash and credit risk — not technical — but the platform must model it: a ledger of owed, paid, outstanding per fleet.
[00:46:41] Ravi Menon (Amperlane): We'll need a real ledger. Double-entry, not "balance" columns.
[00:46:46] Andriy Bondar (Intellias): Agreed — double-entry, append-only. Cost-wise, on the "you handle pricing" Connect model it's two dollars per monthly active account plus 0.25% plus 25 cents per payout. With a few dozen stations paid weekly, that's small. And Stripe can file and deliver the 1099s for connected accounts, for a per-form fee, which your finance person will thank you for.
[00:47:08] Ravi Menon (Amperlane): She will. Adyen?
[00:47:10] Andriy Bondar (Intellias): Adyen for Platforms is a real alternative, but you're on Stripe and know it. I'd switch only for pricing at scale. The provider sits behind an interface anyway, given your lock-in point.
[00:47:25] Ravi Menon (Amperlane): Good. Now reconciliation. That's where I got burned.
[00:47:29] Andriy Bondar (Intellias): The unit of truth for consumption is the CPO's session record. OCPI: the CDR. AMPECO and ChargeLab: their session records via API. LIC: the CSV, unfortunately. Every booking gets matched to a session record — energy, start, end, cost at the B2B tariff. That's what you bill the fleet for and pay the station for.
[00:47:53] Priya Nair (Amperlane): And if there's no session? Driver showed up, charger didn't start?
[00:47:59] Andriy Bondar (Intellias): Then it's a no-show or a fault — a dispute case. That's why the no-show fee is a separate line item, never mixed into energy. If a fleet disputes a no-show, you reverse that line without touching energy. And disputes need evidence: the booking, the hold sent, station status at that time, the driver's location or QR scan. That's the audit trail.
[00:48:25] Kyrylo Shvedov (Intellias): Andriy, the settlement design depends on the business-model decision, right? Can it be config?
[00:48:32] Andriy Bondar (Intellias): Partly. Ledger and flows are the same either way. What changes is what you charge and who's merchant of record. If Amperlane is merchant of record for energy, there's more — receipts, tax questions, the eMSP role. If it's only a booking fee, it's much simpler. So we design the ledger generically, but we need the decision before we build settlement in detail. Ideally within three weeks.
[00:49:01] Kyrylo Shvedov (Intellias): That's the workshop. I'll propose dates.
[00:49:04] Ravi Menon (Amperlane): Dana will want to be there.
[00:49:08] Olena Marchuk (Intellias): NFRs — Kyrylo's been patient.
[00:49:11] Kyrylo Shvedov (Intellias): [laughs] I'll propose numbers, you tell me if they're wrong. Status freshness — how stale can station status be before it's useless?
[00:49:22] Priya Nair (Amperlane): For a driver five minutes away… a minute. Older than that I wouldn't trust it at 4:30.
[00:49:30] Kyrylo Shvedov (Intellias): Station status no older than sixty seconds for connected sites. For LIC, "last updated by attendant at…".
[00:49:38] Olena Marchuk (Intellias): And the UI shows the age, so nobody trusts stale data blindly.
[00:49:44] Kyrylo Shvedov (Intellias): Booking API — p95 under 300 milliseconds?
[00:49:48] Ravi Menon (Amperlane): Under 300 at p95, including the burst.
[00:49:52] Olena Marchuk (Intellias): Including the constraint check. Achievable.
[00:49:55] Kyrylo Shvedov (Intellias): Availability. Drivers work around the clock, but bookings?
[00:50:00] Priya Nair (Amperlane): Basically 5 AM to 1 AM. Overnight people walk up, they don't book.
[00:50:06] Kyrylo Shvedov (Intellias): So 99.9% availability from 5 AM to 1 AM Eastern, maintenance outside that.
[00:50:13] Ravi Menon (Amperlane): Honest. I don't want to pay for four nines.
[00:50:18] Kyrylo Shvedov (Intellias): Data protection: driver names, phones, and with telematics, location. SHIELD covers credentials and any licence or account numbers — reasonable safeguards, breach notification. Location isn't in SHIELD's definition, but we treat it as sensitive anyway. So encryption, access control, and retention rules for location — we don't keep raw traces forever.
[00:50:34] Ravi Menon (Amperlane): Keep what we need for disputes, delete the rest.
[00:50:39] Olena Marchuk (Intellias): We'll propose retention per data type, you decide with counsel. Plus a full audit trail — every booking state change, override, manual ops action, payout — append-only: who, what, when. That covers disputes, SHIELD and SOC 2 in one go.
[00:50:56] Kyrylo Shvedov (Intellias): Notifications: English, Spanish, Bengali, SMS plus WhatsApp, both through Twilio since you're already there.
[00:51:03] Priya Nair (Amperlane): WhatsApp would be huge. A lot of our Bengali-speaking drivers live on WhatsApp.
[00:51:10] Olena Marchuk (Intellias): And the driver interface is a light mobile web app — a PWA — plus messaging. No native app for MVP; that came out of the first call.
[00:51:22] Ravi Menon (Amperlane): Dana was a bit sad about the native app, but she agreed.
[00:51:29] Kyrylo Shvedov (Intellias): Native app, Phase 2. Priya — the charger-down story. We've teased it for half an hour.
[00:51:36] Priya Nair (Amperlane): [laughs] Okay. Last Tuesday, Gowanus. Around 1:50 PM one of the 320 kW units goes down — Kinship later said cooling. We didn't know. First driver arrives at 2:15, texts "charger dead". Ops calls Kinship, they confirm it's down for the day.
[00:51:55] Kyrylo Shvedov (Intellias): And it had bookings.
[00:51:58] Priya Nair (Amperlane): Nine, from 2:15 to about 7. So two of our ops people spent the afternoon redoing nine bookings manually. Open the Sheet, find a free cell that fits, check the connector — two were Teslas, so NACS or an adapter — text each driver, wait for "OK", update Airtable. Three couldn't fit at Gowanus at shift change, so they went to JFK, and one of those was a cab driver who did not want to go to JFK at 4:45.
[00:52:32] Ravi Menon (Amperlane): And we lost him.
[00:52:34] Priya Nair (Amperlane): We lost him. The station was angry because nobody told them the stall had bookings. And next morning Dana asked me why the dashboard showed nine no-shows.
[00:52:47] Kyrylo Shvedov (Intellias): Because the bookings were moved in the Sheet, not changed in Airtable.
[00:52:53] Priya Nair (Amperlane): Exactly. They're still no-shows in Airtable. Which is part of why the migration is messy.
[00:53:00] Kyrylo Shvedov (Intellias): Perfect example, thank you. So for the ops console, on top of the automation: one, "charger down — rebook everyone": the system proposes reassignments, ops approves in bulk, drivers get notified in their language. Two, manual holds — ops can block capacity for maintenance or a fleet priority. Three, overrides — force-confirm, force-release, extend grace. Four, a no-show dispute workflow — fleet disputes, ops sees the evidence, the fee line is reversed or kept.
[00:53:32] Priya Nair (Amperlane): And reason codes. If I move a booking, it should say "moved — charger fault", not "no-show".
[00:53:40] Olena Marchuk (Intellias): Every state change has a reason and an actor, system or human.
[00:53:46] Ravi Menon (Amperlane): All in the audit log.
[00:53:49] Kyrylo Shvedov (Intellias): All of it. And to say it clearly, because it's not in the brief: the ops console isn't a nice-to-have. Your ops people are the safety net for pattern B and C sites. Without it they'll be back in Sheets on day two.
[00:54:08] Olena Marchuk (Intellias): Let me show the architecture shape very briefly, so you have something to react to before the deck. Sharing again — can you see it?
[00:54:19] Ravi Menon (Amperlane): Yep.
[00:54:21] Olena Marchuk (Intellias): Channels on top: driver PWA plus SMS and WhatsApp, fleet portal, station portal, ops console. Keycloak for identity. Then a modular monolith in TypeScript, NestJS — not microservices, you have two engineers. Temporal for timers. Adapters at the bottom: OCPI eMSP gateway, AMPECO, ChargeLab, CSV ingest, telematics, Stripe Connect, Twilio. Postgres with PostGIS, all on AWS.
[00:54:45] Ravi Menon (Amperlane): That's pretty much what I'd have drawn, minus the protocol layer, which I couldn't have. Modular monolith — thank you. I was afraid of twelve services.
[00:54:57] Olena Marchuk (Intellias): [laughs] With two engineers, twelve services is twelve pagers.
[00:55:02] Priya Nair (Amperlane): Would we work on it with you, or is it build-and-hand-over?
[00:55:08] Kyrylo Shvedov (Intellias): Ties to IP. Our default is one team — your engineers in the same repos and rituals from Phase 0, so by the end you know every module. No black-box handover. The deck will show the team shape — indicative, not an estimate.
[00:55:26] Ravi Menon (Amperlane): Good. And I'd like Priya to own the integration-layer knowledge especially.
[00:55:32] Priya Nair (Amperlane): Uh — okay. [laughs] Yes, I'd like that.
[00:55:37] Priya Nair (Amperlane): Also, testing — you mentioned EVerest as a simulator. I'd love an environment where I can break chargers on purpose. Last Tuesday would've been so much easier if we'd rehearsed it.
[00:55:51] Olena Marchuk (Intellias): Exactly what I'd want. A simulated site with faults, overruns and late drivers — and we replay last Tuesday as a test case. "Gowanus, 1:50 PM, charger fault, nine bookings."
[00:56:04] Priya Nair (Amperlane): I'd frame that and hang it on the wall.
[00:56:09] Kyrylo Shvedov (Intellias): [inaudible] — sorry, my connection froze for a second. Okay, let's wrap up.
[00:56:15] Kyrylo Shvedov (Intellias): Let me not read the whole thing out — the full recap goes by email today. Headlines: prototype goes, pilot history migrates. Amperlane owns the calendar; ReserveNow only as a hold about fifteen minutes before. Three supply patterns. No double booking, enforced in Postgres. Stripe Connect with weekly payouts and net-30 invoicing. Deep links only for Uber and Lyft. Ops console is in scope.
[00:56:43] Ravi Menon (Amperlane): Yep, that's it.
[00:56:45] Kyrylo Shvedov (Intellias): Open questions. One: business model — percentage, eMSP spread, or both; it blocks detailed settlement design. Two: who pays no-shows, fleet or driver, and is it per fleet. Three: which LA partners, and their OCPI details. Four: SOC 2 timing. Five: data migration scope — how far back, how much cleansing, what the data room needs.
[00:57:09] Ravi Menon (Amperlane): Can I add one? Who pays for Tesla Fleet API usage — us or Borough Green. It changes whether it's worth it.
[00:57:20] Kyrylo Shvedov (Intellias): Six, telematics cost ownership.
[00:57:22] Priya Nair (Amperlane): And seven, maybe the money transmission thing with a lawyer? Even if it's all in Stripe.
[00:57:30] Andriy Bondar (Intellias): Yes — seven: legal confirmation of the funds-flow structure. We describe it, your counsel confirms.
[00:57:38] Kyrylo Shvedov (Intellias): Olena, next steps?
[00:57:40] Olena Marchuk (Intellias): On our side: by October 16, next Friday, a solution direction deck — what we understood, how we see the architecture, what changed since your brief. No detailed estimate in that one, just phases and team shape. Then, after the business-model workshop and your answers on the open questions, a costed proposal by November 6.
[00:58:04] Ravi Menon (Amperlane): October 16 and November 6. And on our side?
[00:58:09] Kyrylo Shvedov (Intellias): Luis: AMPECO sandbox access, ChargeLab API docs, the LA prospects if possible, and the per-charger reservation list. Priya: the full raw export from Airtable and the Sheets, beyond the anonymised sample you sent Monday — messy is fine, so we can size the migration. Ravi: the AWS account details and, if you can, what the rideshare platform asked for on security in writing.
[00:58:32] Ravi Menon (Amperlane): I have their email, I'll forward the relevant part.
[00:58:37] Priya Nair (Amperlane): Full export by Monday. Want the Supabase schema too?
[00:58:41] Olena Marchuk (Intellias): Yes, just the schema. Even if we bin it.
[00:58:46] Priya Nair (Amperlane): [laughs] Okay.
[00:58:48] Kyrylo Shvedov (Intellias): And I'll send dates for the business-model workshop — thinking the week of October 26, with Dana and Luis. Recap email with this list goes out today.
[00:59:01] Ravi Menon (Amperlane): Works. Dana travels the week after, so earlier is better.
[00:59:06] Kyrylo Shvedov (Intellias): Noted. Anything we didn't ask that we should have?
[00:59:11] Ravi Menon (Amperlane): No, I think we covered it. Honestly, this was the most useful technical call we've had with any vendor so far.
[00:59:21] Olena Marchuk (Intellias): Thank you. We'll try not to show you a generic reference architecture slide on the sixteenth. [laughs]
[00:59:29] Ravi Menon (Amperlane): [laughs] Please don't.
[00:59:31] Kyrylo Shvedov (Intellias): Thanks both, and thank Luis — the station part was gold. Talk soon.
[00:59:38] Priya Nair (Amperlane): Bye!
[00:59:39] Andriy Bondar (Intellias): Bye.
[00:59:41] Ravi Menon (Amperlane): Cheers.
