---
id: SRC-C1
type: source
title: Amperlane Call 1 — Discovery transcript (Sep 29, 2026)
kind: call transcript
origin: Amperlane + Intellias (speaker per line)
original: C1_Amperlane_Call1_Discovery_Transcript_2026-09-29.docx
sha256: cc8e8aa535a84ea711f8ccf0f0a31604294b9992f6322ded0f0ff12159017844
generated_by: tools/extract.py  # do not edit; regenerate instead
---

# SRC-C1 · Amperlane Call 1 — Discovery transcript (Sep 29, 2026)

Microsoft Teams · Meeting transcript

Amperlane x Intellias — Discovery (business & scope)

| Date | Tuesday, September 29, 2026, 10:00 AM ET |
| Duration | 55 min |
| Platform | Microsoft Teams (transcription on) |
| Organiser | Mark Feldman (Intellias) |

## Attendees

| Name | Company | Role |
|---|---|---|
| Dana Whitfield | Amperlane, Inc. | Co-founder & CEO |
| Luis Ortega | Amperlane, Inc. | Co-founder & COO / Head of Partnerships |
| Ravi Menon | Amperlane, Inc. | Co-founder & CTO (joined at 00:14) |
| Mark Feldman | Intellias | Client Partner, North America (organiser) |
| Kyrylo Shvedov | Intellias | Engagement Lead, Product & Business Analysis |
| Olena Marchuk | Intellias | Solution Architect |

## Transcript

[00:00:04] Mark Feldman (Intellias): Morning, morning. Can everyone hear me okay?
[00:00:08] Dana Whitfield (Amperlane): Loud and clear. Hi Mark.
[00:00:10] Luis Ortega (Amperlane): Hey, good morning. Sorry, I'm in the car park at Gowanus, so if you hear a truck backing up, that's — that's just Brooklyn.
[00:00:19] Mark Feldman (Intellias): Most authentic background noise we could ask for on an EV charging call.
[00:00:25] Luis Ortega (Amperlane): Ha. Yeah, there's a Model Y on stall six right now, so, you know. Live demo.
[00:00:31] Mark Feldman (Intellias): Perfect. Kyrylo and Olena are on too. Olena's in Kraków, Kyrylo's — where are you this week?
[00:00:38] Kyrylo Shvedov (Intellias): Lisbon. So it's afternoon here, coffee number three.
[00:00:42] Dana Whitfield (Amperlane): Jealous. It's raining sideways in Sunset Park.
[00:00:46] Olena Marchuk (Intellias): Hello everyone. Kraków is also raining, so we're in solidarity.
[00:00:50] Dana Whitfield (Amperlane): Love that. So Ravi, our CTO, is stuck on an investor diligence call that ran over. Ten, fifteen minutes, he said. Let's just go and we'll catch him up.
[00:01:01] Mark Feldman (Intellias): Sure. Quick intros, and I'll keep mine short because I'm the least interesting person here. Mark Feldman, I run client partnerships for Intellias in North America, based in New York, so not far from you, Dana. And thank you again for reaching out. When the Hudson Mobility board member mentioned you, he said — I quote — "she's the person who actually knows where the chargers are." So, high expectations.
[00:01:25] Dana Whitfield (Amperlane): [laughs] That's generous. I know where the broken chargers are, mostly.
[00:01:30] Mark Feldman (Intellias): Which is the more valuable knowledge. Kyrylo?
[00:01:33] Kyrylo Shvedov (Intellias): Yeah. Kyrylo Shvedov, engagement lead on our side, background in product and business analysis. I've spent the last years mostly on mobility and marketplace products — two-sided things where you have supply, demand, and an ops team in the middle holding it together with tape. So today I'll mostly ask annoying questions about how things actually work, not how they work on the slide.
[00:01:55] Dana Whitfield (Amperlane): Good, because the slide is very pretty.
[00:01:59] Kyrylo Shvedov (Intellias): It is a very good slide. [laughs]
[00:02:02] Olena Marchuk (Intellias): And I'm Olena Marchuk, solution architect. I've worked on EV and IoT platforms — charging back-ends, device connectivity. Today I'm mostly listening. I may ask a few technical questions, but I know the deep part we want to do with Ravi separately.
[00:02:17] Dana Whitfield (Amperlane): Definitely, he'd kill me if I answered protocol questions. Okay — Dana Whitfield, co-founder and CEO. Nine years in the for-hire vehicle world here in New York. Most recently director of fleet operations at an FHV base in Queens — we leased EVs to Uber and Lyft drivers, and I ran charging logistics for about three hundred cars. Which basically means I spent four years on the phone trying to find drivers a plug.
[00:02:43] Luis Ortega (Amperlane): And I was on the other end of those calls. Luis Ortega, co-founder, COO, I run partnerships. Six years before this in site acquisition and partnerships at a DC fast-charging network — won't say which, but you've seen the logo. So I know the station side. What a site costs, how utilisation works, why every CPO is nervous about their electricity bill.
[00:03:05] Mark Feldman (Intellias): Demand and supply in one company. Nice.
[00:03:08] Dana Whitfield (Amperlane): That's the pitch! [laughs] Want me to walk the story? I assume you've seen the deck.
[00:03:14] Kyrylo Shvedov (Intellias): We have. Go ahead, I'll jump in.
[00:03:18] Dana Whitfield (Amperlane): Okay, short version. New York is forcing rideshare electric. The TLC Green Rides rule — twenty-five percent of trips zero-emission or wheelchair-accessible this year, a hundred percent by 2030. There are already thirteen thousand and twenty electric FHVs, and about three hundred and sixty fast-charging ports in the whole city. So drivers lose thirty, forty minutes circling and waiting. And meanwhile stations are empty half the day — national fast-charging utilisation was about sixteen percent in Q2, per Paren, and the CPUC says California's public fast chargers were at twenty-two percent in Q1. LA runs hotter than anywhere. So it's not a shortage at all hours, it's a shortage at the wrong hours.
[00:03:53] Kyrylo Shvedov (Intellias): A timing problem more than a capacity problem.
[00:03:57] Dana Whitfield (Amperlane): Exactly. So Amperlane is the booking layer. Cinema seats for chargers. Station publishes slots, fleet or driver books in two taps, gets a reminder, shows up, plugs in, billing's automatic. We've run it as a concierge pilot since last October in Brooklyn and Queens. Three sites, forty-six ports, two fleets, about twenty-three hundred bookings a month. Wait time thirty-one minutes down to six. And at Gowanus, where Luis is sitting, off-peak utilisation went from fourteen to twenty-three percent.
[00:04:24] Mark Feldman (Intellias): Strong numbers for a manual pilot.
[00:04:27] Dana Whitfield (Amperlane): It's very manual. I'll be honest about that. We'll get to it.
[00:04:32] Kyrylo Shvedov (Intellias): Before we go to the platform — can I ask for something a bit different? Pick one Borough Green driver, a real one if you like, no names. Walk me through his day, from picking up the car to going home. Where does charging actually fit?
[00:04:48] Dana Whitfield (Amperlane): Ooh. Okay. Let's call him Jorge. So, first thing people get wrong — Jorge doesn't work for Borough Green. They lease about four hundred and twenty EVs, and Jorge is an independent contractor who leases one weekly. Pays every week, then drives Uber and Lyft. Both apps, all day, flipping between them.
[00:05:07] Kyrylo Shvedov (Intellias): So Borough Green is his landlord, not his employer.
[00:05:11] Dana Whitfield (Amperlane): Landlord is a great word. Yes. So Jorge starts six, six-thirty in Queens, airport runs, the commute into Manhattan. Late morning he's at, I don't know, forty percent, thinking where do I charge before the afternoon. Without us he opens a station app, drives to the nearest fast charger, there's four cars waiting. He sits there. Thirty minutes, zero dollars.
[00:05:32] Kyrylo Shvedov (Intellias): And with the pilot?
[00:05:34] Dana Whitfield (Amperlane): He texts our number. Like "GOW 1130", and one of our ops people confirms — "booked, stall four, eleven-thirty."
[00:05:42] Kyrylo Shvedov (Intellias): Why text and not an app? Pilot speed, or what he actually wants?
[00:05:47] Dana Whitfield (Amperlane): Both. We started with text because it was fast, then learned it's what they want. These guys have Uber and Lyft open all day, phone in a cradle, battery dying. If I say "download the Amperlane app, make an account, add a card" — he's gone. He'll text. He'll tap a link. A light thing in the browser, fine. A big app, no.
[00:06:09] Luis Ortega (Amperlane): And WhatsApp. Half of them asked for WhatsApp.
[00:06:13] Dana Whitfield (Amperlane): Right. And language is big. A lot of our drivers are more comfortable in Spanish or Bengali — our ops team is bilingual exactly for that.
[00:06:23] Kyrylo Shvedov (Intellias): That's useful, because the deck says native iOS and Android. What I'm hearing is the real channel is SMS or WhatsApp plus a lightweight web page, in three languages.
[00:06:33] Dana Whitfield (Amperlane): Ugh. Yeah. The deck was written for investors a bit. Honest answer is light mobile web plus messaging. Ravi will have opinions, but yeah.
[00:06:42] Olena Marchuk (Intellias): One small question — when Jorge texts, how do you know where the car is and the battery level? From the driver, or from the car?
[00:06:52] Dana Whitfield (Amperlane): Mostly the driver tells us. Borough Green has telematics on part of the fleet, we don't really use it yet. That's a Ravi question.
[00:07:01] Olena Marchuk (Intellias): Okay, I'll keep it for the technical session.
[00:07:05] Kyrylo Shvedov (Intellias): And the yellow cabs — same story?
[00:07:09] Dana Whitfield (Amperlane): Totally different. Five Boroughs EV Cab — small medallion operator, twelve electric cabs, twenty-four drivers on two shifts. No telematics, personal phones. And the thing is shift change. Around four, five PM the day driver brings the cab back, the night driver takes it out, and it needs to be charged. So between four and five it's like a wave. Everyone books at once.
[00:07:31] Luis Ortega (Amperlane): Which is exactly when the stations are busiest. So. Fun.
[00:07:35] Kyrylo Shvedov (Intellias): Who books — the day driver or the night driver?
[00:07:40] Dana Whitfield (Amperlane): Usually the day driver, he's bringing it in. But some of the long-term drivers, the ones who lease both shifts, book for both — the afternoon slot and the overnight slot in one go. So it's not always "one driver books for himself".
[00:07:53] Kyrylo Shvedov (Intellias): So the person booking isn't always the person charging. Let me list who touches a booking and you correct me. Fleet manager. Driver. Station operator. Your ops team. Anyone else?
[00:08:04] Luis Ortega (Amperlane): The garage guy.
[00:08:06] Kyrylo Shvedov (Intellias): The garage guy?
[00:08:08] Luis Ortega (Amperlane): At LIC, Long Island City. That site is a parking garage — Hunters Point Garages own the building and the chargers. There's no "operator" the way you'd think, there's an attendant in a booth. When we have a booking, our ops person calls him, and he physically puts a "Reserved" sign on the stall.
[00:08:27] Mark Feldman (Intellias): Old school.
[00:08:29] Luis Ortega (Amperlane): Very. And honestly he's one of our most reliable partners.
[00:08:34] Kyrylo Shvedov (Intellias): So five actors: fleet manager, driver, station operator, site staff like the attendant, and Amperlane ops. And the driver is the one who isn't anyone's employee.
[00:08:44] Dana Whitfield (Amperlane): Yeah. I never thought of the attendant as a user, but he totally is.
[00:08:49] Kyrylo Shvedov (Intellias): Okay, now the slightly uncomfortable question. Twenty-three hundred bookings a month — how many turn into a charge?
[00:08:56] Dana Whitfield (Amperlane): [pause] Yeah. I knew you'd ask. About eighteen-fifty completed. No-shows are seventeen percent. And late arrivals, more than ten minutes late, twenty-two percent.
[00:09:05] Kyrylo Shvedov (Intellias): Twenty-two of all bookings, or of the ones who showed?
[00:09:10] Dana Whitfield (Amperlane): Of all bookings.
[00:09:12] Kyrylo Shvedov (Intellias): Thanks for being straight. Honestly, not terrible for a pilot run on text messages. But it's not on the slide.
[00:09:20] Dana Whitfield (Amperlane): Because investors read slides. [laughs] But you need to know it. Luis can tell you what the stations think.
[00:09:27] Luis Ortega (Amperlane): Yeah — they're not happy. When we hold a stall at Gowanus at eleven-thirty and Jorge doesn't show, that stall sits there empty with a cone on it while a walk-up driver stands next to it staring, maybe yelling at the site guy. The station loses the session and gets the angry customer. Kinship, the Gowanus operator, told me in so many words: "If you hold my stall, you pay for my stall."
[00:09:52] Kyrylo Shvedov (Intellias): So they want a no-show fee.
[00:09:55] Luis Ortega (Amperlane): A no-show fee, and a short grace period. We've been talking ten minutes. After ten, the stall's released, cone comes off, walk-up gets it. Though honestly they want the stall back more than the money. The fee is the stick.
[00:10:10] Kyrylo Shvedov (Intellias): Today who releases it?
[00:10:12] Luis Ortega (Amperlane): Whoever's on site gets tired of waiting and takes the cone. Sometimes our ops calls them. It's not a system.
[00:10:20] Olena Marchuk (Intellias): So in the platform the slot would release itself after the grace period.
[00:10:26] Luis Ortega (Amperlane): Has to. Automatically. Otherwise we're back to phone calls. And Tesla already trained everyone on clocks — their congestion fee is typically fifty cents a minute, up to a dollar, after a five-minute grace. Drivers understand the concept. They just hate it.
[00:10:41] Mark Feldman (Intellias): Everyone hates the clock.
[00:10:43] Kyrylo Shvedov (Intellias): Here's what I really want to understand. Who pays the no-show fee? Jorge is an independent contractor leasing from Borough Green. If he no-shows, does Borough Green eat it, or pass it on to him?
[00:10:56] Dana Whitfield (Amperlane): [sighs] That's literally the argument I had with Borough Green's ops director last Thursday. They don't want to pay for a driver's behaviour. But they also don't want us billing drivers directly, because then the driver's mad at the fleet, and the fleet needs drivers to keep leasing. So it's —
[00:11:14] Luis Ortega (Amperlane): — a hot potato.
[00:11:16] Dana Whitfield (Amperlane): A hot potato. And the cab company's different again — sometimes the owner books and the other shift's driver is the one who doesn't show.
[00:11:26] Kyrylo Shvedov (Intellias): So maybe it's not one decision for the whole platform. Maybe it's a policy each fleet sets. Fleet pays, driver pays, or fleet pays and deducts on their side.
[00:11:36] Dana Whitfield (Amperlane): Huh. A setting per fleet. I like that, because I'm never winning that argument with all of them.
[00:11:44] Kyrylo Shvedov (Intellias): I'm not saying it's the answer — I'm writing it as an open question with a candidate answer. And note, if the fee lands on Jorge, that's the first time Amperlane ever takes money from a driver. That's a big moment for the relationship.
[00:11:59] Dana Whitfield (Amperlane): [pause] Yeah. I hadn't thought of it that way.
[00:12:03] Kyrylo Shvedov (Intellias): And the late ones — why are they late? Traffic?
[00:12:08] Dana Whitfield (Amperlane): A ride came in. Nine times out of ten. Jorge's on his way to charge, gets a ping for a forty-dollar airport ride. Of course he takes it. Then he's late, or a no-show.
[00:12:20] Luis Ortega (Amperlane): That's the real competitor, by the way. Not anyone in the market. The forty-dollar ride.
[00:12:26] Kyrylo Shvedov (Intellias): [laughs] Great line. And a real insight — the no-show is a rational choice in the moment, so a fee alone won't fix it. If cancelling or saying "running late" took one tap, the station gets the stall back early and the driver doesn't pay.
[00:12:42] Dana Whitfield (Amperlane): They can text "CANCEL" today. Nobody does. They're driving.
[00:12:46] Kyrylo Shvedov (Intellias): Right. Okay, I'll stop designing on the call.
[00:12:50] Mark Feldman (Intellias): He never stops. [laughs] Quick commercial one — do the fleets see no-shows as a problem, or only the stations?
[00:12:58] Dana Whitfield (Amperlane): Borough Green sees it because I show it to them. Five Boroughs doesn't think about it. Their problem is, "is my cab charged at five o'clock, yes or no." That's success for them.
[00:13:10] Kyrylo Shvedov (Intellias): That's a great definition of success. I'm stealing it.
[00:13:14] Dana Whitfield (Amperlane): It's yours.
[00:13:16] Kyrylo Shvedov (Intellias): Let me just check the shape of this before money. Two dollars per completed booking today, invoiced to fleets, and the driver pays the station himself?
[00:13:26] Dana Whitfield (Amperlane): Right. Two bucks a completed booking, fleet pays through Stripe, monthly. Driver pays the station with his own card or the station app. Energy money never touches us.
[00:13:36] Kyrylo Shvedov (Intellias): And the stations pay you nothing today.
[00:13:40] Dana Whitfield (Amperlane): Nothing today. Which brings us to the money slide — oh wait, I think Ravi's in the lobby. Mark?
[00:13:47] Mark Feldman (Intellias): Admitting — hmm, it says he's connecting. His Wi-Fi might be fighting him. Give it a sec.
[00:14:02] Ravi Menon (Amperlane): Hey — sorry, sorry everyone. Diligence call. The lawyer had forty more questions about our cap table. Ravi, CTO. Can you hear me?
[00:14:15] Mark Feldman (Intellias): We hear you. Welcome, Ravi, no worries. Mark Feldman, Intellias — with Kyrylo, our engagement lead, and Olena, our solution architect.
[00:14:26] Olena Marchuk (Intellias): Hi Ravi.
[00:14:29] Ravi Menon (Amperlane): Hi all. What did I miss? Did Dana already promise ten cities?
[00:14:36] Dana Whitfield (Amperlane): Not yet!
[00:14:39] Mark Feldman (Intellias): [laughs] Let me catch you up. Dana walked us through the story and the pilot. Kyrylo had them do a day in the life of a Borough Green driver. Big takeaways: drivers are independent contractors on weekly leases, on Uber and Lyft all day, so they want SMS or WhatsApp and a light web page, not a heavy native app — in English, Spanish and Bengali. The cabs have the shift-change crunch around four to five PM. We counted five types of users, including my favourite, the garage attendant at LIC. Then the pilot reality: seventeen percent no-shows, twenty-two percent late. Stations want a ten-minute grace with auto-release and a no-show fee, and who pays — fleet or driver — is open; Kyrylo floated a per-fleet policy. And Dana was just about to get to the money slide. Fair?
[00:15:47] Dana Whitfield (Amperlane): Very fair. Better than I'd have done.
[00:15:52] Ravi Menon (Amperlane): Great. The no-show thing — yeah, I've seen the numbers. Grim. [laughs] Look, at some point we'll get into how we actually build this, what each station can technically do. I'd rather do that properly in a separate session with Priya, our senior engineer — she knows where the bodies are buried in the current tooling. Today I'll listen and chime in on money.
[00:16:24] Olena Marchuk (Intellias): That's exactly what we hoped. A separate technical deep-dive with you and Priya.
[00:16:32] Ravi Menon (Amperlane): Perfect.
[00:16:34] Kyrylo Shvedov (Intellias): And money is exactly where we are. Dana, the slide says ten to twelve percent take rate on charging GMV, paid by stations, plus fifteen dollars per vehicle per month from fleets. Where did ten to twelve come from?
[00:16:54] Dana Whitfield (Amperlane): Benchmarks, mostly. Marketplaces, booking platforms, they take a percentage. And it scales beautifully in a spreadsheet. That's where the four-point-eight million ARR in 2028 comes from.
[00:17:08] Kyrylo Shvedov (Intellias): Have stations agreed to it?
[00:17:12] Luis Ortega (Amperlane): Can I be the bad guy?
[00:17:17] Dana Whitfield (Amperlane): You're always the bad guy. [laughs] Go.
[00:17:22] Luis Ortega (Amperlane): I've pitched the percentage to all three sites and a couple of prospects. Nobody signed. And it's not greed, it's the economics. You've got demand charges from the utility — you pay for your peak power, not just energy — so one spike at five PM sets a big chunk of the monthly bill. Gowanus, by my estimate, runs at single-digit margins after demand charges. Single digits. So I walk in and say "give me ten to twelve percent of your energy revenue"…
[00:18:03] Kyrylo Shvedov (Intellias): You're asking for more than their margin.
[00:18:08] Luis Ortega (Amperlane): More than their margin. On sessions they'd mostly get anyway at peak. They laugh me out of the room. Nicely.
[00:18:19] Kyrylo Shvedov (Intellias): So what would they pay for?
[00:18:24] Luis Ortega (Amperlane): Incremental. Off-peak. If I bring them a driver at eleven AM or two AM when the site's at fourteen percent, that's new money. Kinship said: "Pay you for sessions I wouldn't have had — fine. A cut of the sessions I already have at five PM — no."
[00:18:48] Kyrylo Shvedov (Intellias): Which fits — the Gowanus result you're proudest of is the off-peak jump.
[00:18:56] Luis Ortega (Amperlane): Exactly. "We fill your quiet hours" sells. "We fill your peak" doesn't — they're already full at peak.
[00:19:06] Mark Feldman (Intellias): And the fleet side, the fifteen per vehicle?
[00:19:12] Dana Whitfield (Amperlane): Borough Green would pay a subscription if the number's right. But what they keep telling me is something else. Their finance person hates drivers paying the station with their own cards — reimbursements, disputes, who charged what. What they want is one invoice. One consolidated invoice a month, net-thirty, everything on it.
[00:19:38] Dana Whitfield (Amperlane): Which brings me to the idea I actually want to put on the table. Ravi, Luis and I have been arguing about this for two weeks.
[00:19:52] Ravi Menon (Amperlane): Three.
[00:19:54] Dana Whitfield (Amperlane): Three weeks. So — what if we become the — I think the term is eMSP? Mobility service provider. We're the merchant of record. We buy sessions from the station at their B2B rate and sell to the fleet at a bundled rate that includes the guaranteed slot. At Gowanus, Kinship's B2B tariff is about forty-two cents a kilowatt-hour. We'd bill the fleet about forty-nine, and that includes "your stall is waiting". Plus the fleet subscription. Plus no-show fees, passed through to the station.
[00:20:36] Kyrylo Shvedov (Intellias): So the station sees you as a big B2B customer buying wholesale, and the fleet sees you as its charging supplier with one invoice.
[00:20:49] Dana Whitfield (Amperlane): Yes! The station gives up no percentage of anything. They get a B2B customer filling their off-peak, and the fleet gets one bill.
[00:21:02] Kyrylo Shvedov (Intellias): Quick arithmetic, just to get a feel. Seven cents spread per kilowatt-hour. Average session in the pilot?
[00:21:11] Luis Ortega (Amperlane): About twenty-eight kilowatt-hours.
[00:21:15] Kyrylo Shvedov (Intellias): Seven cents times twenty-eight — about a dollar ninety-six a session. Which is, funnily enough, almost exactly your two dollars a booking today.
[00:21:27] Dana Whitfield (Amperlane): [laughs] Oh my God. Okay. Huh.
[00:21:32] Ravi Menon (Amperlane): That's the point I keep making. The spread doesn't magically make more per session. It changes who you are in the money flow.
[00:21:44] Kyrylo Shvedov (Intellias): Right, so I'd compare the options on more than revenue. As merchant of record you carry payment risk — the fleet pays you net-thirty, you pay the station… when? You're in the middle of energy disputes. Operationally, that's a very different company than "two dollars a booking".
[00:22:08] Ravi Menon (Amperlane): And that's my world — I did marketplace payouts at my last job. If we're merchant of record, we're holding money between two parties, and how that flow is structured matters legally and in the build. I kind of like it, actually. But it's a big design decision and definitely a tech-session topic too.
[00:22:36] Luis Ortega (Amperlane): And from the station side, the spread is easier to sell than the percentage, but not a done deal. Kinship will ask, "why is Amperlane making seven cents on my electrons?" The answer is "because I brought you the session at eleven AM". Still a conversation.
[00:22:59] Kyrylo Shvedov (Intellias): So honestly, where are you as a founding team? Percentage, spread, both?
[00:23:07] Dana Whitfield (Amperlane): [pause] Not decided. I'm leaning spread plus subscription. Luis?
[00:23:13] Luis Ortega (Amperlane): I'm leaning "whatever the stations sign". Maybe a small fee on incremental off-peak sessions only, plus the spread. I don't know.
[00:23:24] Ravi Menon (Amperlane): And I'm leaning "decide before we build the settlement module". [laughs]
[00:23:31] Kyrylo Shvedov (Intellias): Very CTO answer. And correct. I won't try to solve it today. Playback: the station percentage isn't landing, because of demand charges and thin margins; stations pay only for incremental off-peak; fleets want one monthly invoice, net-thirty. On the table: Amperlane as eMSP and merchant of record, about forty-two in, forty-nine out at Gowanus, plus subscription and pass-through no-show fees. Open: percentage, spread, or both. Right?
[00:24:04] Dana Whitfield (Amperlane): That's scary-good.
[00:24:07] Mark Feldman (Intellias): It's his party trick.
[00:24:11] Olena Marchuk (Intellias): One remark from architecture, without going deep. In the percentage model you mostly need to receive data about sessions. In the merchant model the session data also has to be good enough to bill real money on. So the quality of each station's session data becomes very important.
[00:24:35] Ravi Menon (Amperlane): A hundred percent. Let's go deep on that next week.
[00:24:42] Kyrylo Shvedov (Intellias): And it ripples into the product too. If the fleet pays for energy, the fleet manager will want spend controls — which sites, how many bookings a day. If the driver pays, he doesn't care.
[00:25:00] Dana Whitfield (Amperlane): That's true, Borough Green's manager already asked me for that. "My drivers only book at these sites, max twice a day." Five Boroughs, on the other hand — it's the owner and his nephew. Give them a login, they'll forget the password.
[00:25:21] Kyrylo Shvedov (Intellias): So for small fleets the portal is almost invisible, and the value is in the messaging and your ops team.
[00:25:33] Ravi Menon (Amperlane): See, this is why I want the decision early. It ripples everywhere.
[00:25:40] Dana Whitfield (Amperlane): Okay, okay, I hear you. [laughs]
[00:25:45] Kyrylo Shvedov (Intellias): Still on stations, Luis. The deck gives the impression a station joins and publishes its ports. All of them?
[00:25:55] Luis Ortega (Amperlane): Oh, no. No, no. Never all of them. Nobody gives you all the ports.
[00:26:07] Kyrylo Shvedov (Intellias): Tell me more.
[00:26:10] Luis Ortega (Amperlane): A station always needs walk-up capacity. If a regular person with a Kia pulls in and every stall has a cone, that's a disaster — bad reviews, the app says "available", angry calls. So they agree to a cap. At peak, thirty to fifty percent of the ports, max. Gowanus does about half at peak, JFK more like a third. Off-peak they'll give more, nobody's there anyway.
[00:26:44] Olena Marchuk (Intellias): So a rule per site and per time window. Like, "weekdays four to seven PM, maximum eight ports bookable".
[00:26:54] Luis Ortega (Amperlane): Exactly. And they want to change it themselves. Big game at Citi Field, [inaudible] — sorry, truck — they want to go into a screen and lower it.
[00:27:07] Kyrylo Shvedov (Intellias): That's a station portal requirement right there.
[00:27:12] Luis Ortega (Amperlane): And one more, matters more as we grow. Sites that took NEVI money — the federal program — have public-access obligations. They can't turn into a private fleet depot. So for those the cap isn't just commercial, it's compliance.
[00:27:32] Kyrylo Shvedov (Intellias): Are any of your three NEVI-funded?
[00:27:37] Luis Ortega (Amperlane): Not our three. Some prospects are, especially outside New York. I'd rather build for it from day one.
[00:27:47] Olena Marchuk (Intellias): Luis, may I ask very quickly — at Gowanus, when you hold a stall, does the charger itself know? Or only the cone?
[00:28:00] Luis Ortega (Amperlane): At Gowanus, partly. Kinship runs on a pecko —
[00:28:06] Luis Ortega (Amperlane): — and I can see the transcript just wrote "a pecko". A-M-P-E-C-O. AMPECO. It's their charging management system. Through it some of the chargers can actually be put on reservation. Not all. The rest is cones.
[00:28:25] Olena Marchuk (Intellias): AMPECO, yes, I know it. Good — I won't go further. That's for Ravi and Priya.
[00:28:34] Ravi Menon (Amperlane): There's a lot to unpack there. The other two sites are a whole different story. Next week.
[00:28:44] Olena Marchuk (Intellias): Now I'm curious.
[00:28:47] Mark Feldman (Intellias): Let me switch us to the boring-but-important part. Timelines and budget. The deck says MVP in twelve weeks and ten metros by end of 2027, but no budget and no launch date. Help me understand what's real.
[00:29:06] Dana Whitfield (Amperlane): Sure. The date that matters is March first, 2027. NYC production launch. Real stations, real fleets, no more spreadsheets in the critical path.
[00:29:19] Mark Feldman (Intellias): Why March first specifically?
[00:29:22] Dana Whitfield (Amperlane): The Series A. We raised our seed in February — five and a half million, Hudson Mobility led, Gridline Ventures participated. Runway to about Q4 2027. We want to raise the A in the second half of 2027, and the milestone investors care about is ten thousand completed bookings a month by June 2027. So I need the platform live in March to have three months to ramp.
[00:29:56] Kyrylo Shvedov (Intellias): From eighteen-fifty completed today.
[00:30:00] Dana Whitfield (Amperlane): From eighteen-fifty. Five-plus x in nine months. I know. Which is why no-shows matter — every no-show is a booking I didn't complete.
[00:30:13] Kyrylo Shvedov (Intellias): Right — the north star is completed bookings, so cutting no-shows is growth, not just station happiness. Is the ten thousand New York only?
[00:30:26] Dana Whitfield (Amperlane): New York only. LA can't count by June.
[00:30:31] Mark Feldman (Intellias): And budget for that first phase — I'm not trying to pin you down, I just want us to propose something in the right universe.
[00:30:45] Dana Whitfield (Amperlane): [pause] Around a million, give or take, for phase one. Through Q2 next year.
[00:30:53] Mark Feldman (Intellias): Give or take meaning…?
[00:30:57] Dana Whitfield (Amperlane): Nine hundred K to one-point-two, I'd say. Ravi?
[00:31:02] Ravi Menon (Amperlane): That's the range we modelled. Through end of Q2 2027. Above one-two we'd need a very good reason.
[00:31:13] Mark Feldman (Intellias): Very helpful, thank you.
[00:31:16] Kyrylo Shvedov (Intellias): And ten metros by end of 2027 — how does that fit with a March New York launch?
[00:31:26] Dana Whitfield (Amperlane): [laughs] You noticed.
[00:31:30] Kyrylo Shvedov (Intellias): I'm paid to notice.
[00:31:33] Dana Whitfield (Amperlane): Honestly? LA is next. That's the real plan. LA in Q3 2027 — California's already at twenty-two percent and LA is the busiest part of it, so the peak pain is real. And Luis has two prospects there already.
[00:31:51] Kyrylo Shvedov (Intellias): Let me reframe and tell me if it's wrong. New York production March first, 2027. LA second, targeting Q3 2027. And ten metros is the ambition — more of a 2028 story.
[00:32:08] Dana Whitfield (Amperlane): [pause] Yeah. That's fair. Ten metros is 2028. Don't put that in writing to my investors. [laughs] Actually, do, they know.
[00:32:19] Mark Feldman (Intellias): We'll be discreet.
[00:32:22] Kyrylo Shvedov (Intellias): It matters a lot for us. "Multi-metro from day one" and "New York really well, then LA" are two quite different things to build in the first few months.
[00:32:38] Ravi Menon (Amperlane): Agreed. I'd rather New York works perfectly than ten cities work badly.
[00:32:45] Kyrylo Shvedov (Intellias): My favourite question, then. Imagine it's March second, 2027 — the day after launch. What has to be true for you to say "that worked"? Not the Series A number. The day after.
[00:33:03] Dana Whitfield (Amperlane): Hmm. Five Boroughs' cabs are charged at five o'clock, every day, without anyone on my team picking up the phone. Seriously. That's the one.
[00:33:16] Luis Ortega (Amperlane): For me — Kinship stops calling me about cones.
[00:33:22] Ravi Menon (Amperlane): Nobody opens Airtable.
[00:33:25] Dana Whitfield (Amperlane): And Borough Green gets one invoice and doesn't email me about it.
[00:33:32] Kyrylo Shvedov (Intellias): That's a great list. Those four sentences are a better MVP definition than most specs I read. Writing them down verbatim.
[00:33:44] Mark Feldman (Intellias): A few minutes on the market? We'll get asked internally, "why won't someone bigger just do this?"
[00:33:54] Dana Whitfield (Amperlane): Sure. Obvious one in New York is Revel. They ran the electric rideshare service here and shut it down on August eleventh, 2025, to focus on their fast-charging hubs — five in New York at the time, one in San Francisco.
[00:34:15] Luis Ortega (Amperlane): And then in May, Vulture and Revel announced —
[00:34:21] Luis Ortega (Amperlane): — Voltera. Voltera, not vulture. The transcript is having a day. Although some days… [laughs]
[00:34:30] Mark Feldman (Intellias): [laughs] We'll fix that one before it goes anywhere.
[00:34:36] Luis Ortega (Amperlane): Please. Voltera and Revel announced a combination on May twenty-sixth. They say the combined company expects a thousand-plus stalls, operating or in development, across eleven US metros, focused on fleet and autonomous charging.
[00:34:53] Kyrylo Shvedov (Intellias): Competitor or supplier for you?
[00:34:57] Luis Ortega (Amperlane): Could be either. Supply partner — a thousand stalls built for fleets is exactly the inventory we want bookable. Or they build their own booking and go direct to fleets. I've had one conversation with someone there. Friendly. Non-committal.
[00:35:17] Dana Whitfield (Amperlane): And to be clear, it's announced. I don't know where the deal stands, I'm not saying it closed.
[00:35:28] Kyrylo Shvedov (Intellias): We'll keep it at "announced". And regulation — Green Rides, twenty-five percent this year. Is the industry going to make it?
[00:35:39] Dana Whitfield (Amperlane): In March — the seventeenth, I think — TLC testified the industry average was twenty-two point seven percent against the twenty-five percent target for 2026. They called the companies "on track". And it goes up twenty points a year from here, so the pressure only grows. That's our tailwind.
[00:36:04] Kyrylo Shvedov (Intellias): On track, but behind. And LA — the same kind of push?
[00:36:12] Dana Whitfield (Amperlane): That's the honest risk. California has CARB's Clean Miles Standard — thirty percent electric miles in 2026. But in June, CPUC staff recommended a three-year pause, because they expect the companies to miss the 2026 targets. So the LA mandate is… wobbly.
[00:36:33] Luis Ortega (Amperlane): Which is why the LA case is about utilisation, not regulation. Those stations are full at peak with or without the rule.
[00:36:45] Kyrylo Shvedov (Intellias): Okay. New York: mandate as tailwind. LA: uncertain, rely on utilisation. I'll note it as a phase-two risk.
[00:36:56] Ravi Menon (Amperlane): Sorry — I have to drop for two minutes, my other — no, never mind. I muted them. Go on.
[00:37:07] Mark Feldman (Intellias): [laughs] We'll take that as a compliment.
[00:37:12] Kyrylo Shvedov (Intellias): Dana, at the start you said, "it's very manual, we'll get to it". I'd like to get to it. What does a day look like for your ops team?
[00:37:27] Dana Whitfield (Amperlane): So, four people on driver support and ops, bilingual. The text comes in, they check the slot grid — a Google Sheet per site — log it through a Retool screen Priya built, and reply to the driver. Then for Gowanus, sometimes they can do the hold in the system, sometimes they call the site. JFK, they call. LIC, they call the garage attendant, who puts up the sign. And for the cones, someone on site has to physically walk out and put it on the stall.
[00:38:10] Kyrylo Shvedov (Intellias): How many phone calls a day, roughly?
[00:38:15] Dana Whitfield (Amperlane): Normal day? Dozens. On a bad day, when a charger goes down —
[00:38:23] Luis Ortega (Amperlane): Oh, the charger-down day.
[00:38:27] Dana Whitfield (Amperlane): Charger goes down at Gowanus at one PM. Everybody booked on that stall for the afternoon — ops has to figure out who they are, text each one, find another stall or site, call that site, call the attendant. All by hand. And meanwhile the four-PM cab wave is coming.
[00:38:52] Kyrylo Shvedov (Intellias): So the ops team needs things that aren't in the deck at all. A manual hold — book on behalf of a driver. Overrides — "let him in, he's twelve minutes late, it's fine". Mass rebooking when a charger goes down. And disputes — the driver says "I was there, the stall was blocked", the station says "no-show".
[00:39:22] Dana Whitfield (Amperlane): All of those. Disputes are new, but they're coming the moment we charge no-show fees. Every day.
[00:39:31] Luis Ortega (Amperlane): Every single one. I would dispute it too.
[00:39:37] Kyrylo Shvedov (Intellias): So the ops console isn't a nice-to-have admin panel. It's a core product, for the four people currently holding the pilot together.
[00:39:49] Dana Whitfield (Amperlane): When you put it like that — it's not even in the architecture slide.
[00:39:57] Olena Marchuk (Intellias): Sorry, I was on mute — sorry. One light question. The cones and signs — with the platform, do you expect the physical part to stay, or every charger to know about the booking?
[00:40:15] Luis Ortega (Amperlane): Realistically some physical part stays. At some sites, for a while. The garage attendant isn't going anywhere.
[00:40:25] Olena Marchuk (Intellias): Then the platform must tell the humans on site what to do, not only the chargers. Important design input. The rest, again, with Ravi and Priya.
[00:40:39] Ravi Menon (Amperlane): You keep saying that. I'm starting to feel like I owe you a very long meeting.
[00:40:48] Olena Marchuk (Intellias): You do. [laughs] Ninety minutes would be nice, I'll take sixty.
[00:40:55] Luis Ortega (Amperlane): Add another one for her list — the previous movie runs over. Someone's still on your stall when you arrive. Ops calls them "sleepers". Car's at a hundred percent and the guy's asleep.
[00:41:13] Olena Marchuk (Intellias): [laughs] Sleepers. I'll remember this word. Next week.
[00:41:18] Dana Whitfield (Amperlane): Investors love the cinema-seat metaphor, by the way. But after this call — it's more like cinema seats where a fifth of the audience shows up late and someone's asleep in your seat. [laughs]
[00:41:36] Kyrylo Shvedov (Intellias): Most honest pitch I've heard this year.
[00:41:41] Dana Whitfield (Amperlane): Please don't put it on a slide.
[00:41:46] Mark Feldman (Intellias): And the integrations wishlist in the deck — Uber, Lyft, Tesla, the big CSMS names. Anything there you'd call a must for March?
[00:41:59] Ravi Menon (Amperlane): Honest answer: I don't know yet which are real for March, and I suspect some aren't possible at all. That's exactly the tech session. I'd rather not commit to a list today and walk it back.
[00:42:18] Kyrylo Shvedov (Intellias): Fair. We'll treat the wishlist as a wishlist until then.
[00:42:24] Kyrylo Shvedov (Intellias): One supply question on the ten thousand. From eighteen-fifty with three sites — do you have the supply lined up? Rough is fine.
[00:42:37] Luis Ortega (Amperlane): Not fully. Our three sites plus three or four new ones — possible, but tight. And every prospect says "call us when it's real".
[00:42:50] Dana Whitfield (Amperlane): And demand-side, Borough Green has four-twenty cars and only about a hundred and sixty drivers in the pilot. Room to grow just there. Plus two more fleets we're talking to.
[00:43:06] Kyrylo Shvedov (Intellias): So March isn't just a tech launch — it's what unlocks supply. Chicken and egg.
[00:43:15] Dana Whitfield (Amperlane): It's always chicken and egg. Marketplaces.
[00:43:19] Kyrylo Shvedov (Intellias): And the station contracts — what do you sign with them today?
[00:43:27] Luis Ortega (Amperlane): Today it's basically a pilot letter, two, three pages. For launch we have a draft partner agreement template — capacity commitment, no-show terms, payment terms. Still being negotiated, but I can share it.
[00:43:44] Kyrylo Shvedov (Intellias): That'd be gold. A lot of the platform rules — caps, grace period, fees — will literally come from that contract.
[00:43:56] Luis Ortega (Amperlane): I'll send it with a big "DRAFT" watermark. And stations' first questions are never about the app, by the way. It's "who's liable when a stall is blocked" and "how fast do I get paid". They want money faster than monthly.
[00:44:17] Kyrylo Shvedov (Intellias): And fleets pay net-thirty. So if you're merchant of record, that's a cash-flow gap you're sitting in the middle of. Flagging, not solving.
[00:44:29] Ravi Menon (Amperlane): My nightmare. [laughs] I've got a page and a half of notes on it.
[00:44:38] Kyrylo Shvedov (Intellias): And pilot data — could we get an export of pilot bookings? Anonymised is fine. Sites, times, no-shows, late arrivals. It'd help us see the real shape of demand, the four-PM wave.
[00:44:55] Dana Whitfield (Amperlane): Yes. Ravi, Priya can pull that?
[00:44:59] Ravi Menon (Amperlane): She can. We'll strip names and phone numbers. Give us a few days.
[00:45:07] Kyrylo Shvedov (Intellias): And the driver survey behind the thirty-one versus six minutes?
[00:45:14] Dana Whitfield (Amperlane): Two hundred and twelve drivers answered. Self-reported, so grain of salt, but yes.
[00:45:22] Kyrylo Shvedov (Intellias): Self-reported is fine as long as we label it.
[00:45:28] Mark Feldman (Intellias): Okay. Kyrylo, want to run through what we heard and what's open?
[00:45:35] Kyrylo Shvedov (Intellias): Sure, quickly. Interrupt if anything's wrong. Users: five types — fleet manager, driver as independent contractor, station operator, site staff like the attendant, and your ops team. Drivers live in Uber and Lyft and want SMS, WhatsApp and a light web page in English, Spanish and Bengali; small fleets barely want a portal; the cab shift change at four to five is the peak moment.
[00:46:07] Dana Whitfield (Amperlane): Yes.
[00:46:10] Kyrylo Shvedov (Intellias): Pilot reality: seventeen percent no-shows, twenty-two late. Stations want a ten-minute grace, auto-release and a no-show fee — mostly they want the stall back. Main cause is the forty-dollar ride, so cancelling must be effortless.
[00:46:28] Luis Ortega (Amperlane): The forty-dollar ride.
[00:46:31] Kyrylo Shvedov (Intellias): Business model: percentage from stations isn't landing; stations pay only for incremental off-peak; fleets want one invoice, net-thirty. On the table is eMSP and merchant of record, forty-two in, forty-nine out at Gowanus, plus subscription and pass-through no-show fees. Undecided — and it shapes settlement, the fleet portal, the station portal, basically everything with money in it.
[00:47:00] Ravi Menon (Amperlane): Underline that.
[00:47:03] Kyrylo Shvedov (Intellias): Twice. Capacity: thirty to fifty percent of ports at peak, per site and time window, editable by the station; NEVI sites have public-access duties. Ops: an ops console as a first-class product. Dates: New York production March first, 2027; ten thousand completed a month by June, New York only; phase one around a million through Q2; LA in Q3 2027; ten metros a 2028 ambition. And success on March second is your four sentences.
[00:47:39] Dana Whitfield (Amperlane): [laughs] I love that you kept those.
[00:47:44] Kyrylo Shvedov (Intellias): Best part of my notes. Open questions. One — the business model: percentage, spread, or both. Two — who pays no-shows, and what the driver sees. Three — what each station can actually do technically; that's next session. Four — how many new sites and fleets are realistic by June. Five — which wishlist integrations are real for March.
[00:48:14] Luis Ortega (Amperlane): Station payout frequency. Add that.
[00:48:18] Kyrylo Shvedov (Intellias): Added.
[00:48:20] Ravi Menon (Amperlane): And the pilot history. I don't want to lose a year of bookings when we move.
[00:48:30] Kyrylo Shvedov (Intellias): Pilot data migration — added, for the tech session.
[00:48:36] Dana Whitfield (Amperlane): Can I ask one thing back? The deck says MVP in twelve weeks. Is that crazy?
[00:48:45] Kyrylo Shvedov (Intellias): [pause] Not crazy as a wish. But I won't give you a number before the technical session — it depends on what the stations can do and what the money flow looks like. March first is the real constraint, and we'll plan backwards from it, including time to test with real drivers.
[00:49:11] Dana Whitfield (Amperlane): That's a fair non-answer. [laughs]
[00:49:15] Kyrylo Shvedov (Intellias): An honest one. I'll give you a real answer when I can stand behind it.
[00:49:24] Olena Marchuk (Intellias): And from architecture side — the date is aggressive, but what you described today is actually more focused than the deck. One city, real users, a real ops team. That helps.
[00:49:41] Ravi Menon (Amperlane): Good to hear.
[00:49:44] Mark Feldman (Intellias): Dana, on the business model — we won't make the decision for you. But after the tech session we could run a short working session on the model specifically, showing what each option means for the platform and the timeline. Useful?
[00:50:05] Dana Whitfield (Amperlane): Very. I need someone to break the tie between the three of us.
[00:50:13] Ravi Menon (Amperlane): Not break. Inform.
[00:50:16] Dana Whitfield (Amperlane): Inform. [laughs] Fine. Inform the tie.
[00:50:21] Mark Feldman (Intellias): We'll inform the tie. Okay, action items. Amperlane: one, the anonymised pilot data export plus the driver survey. Ravi, that's Priya?
[00:50:32] Ravi Menon (Amperlane): Priya. I own it, she does it. By Monday the fifth.
[00:50:39] Mark Feldman (Intellias): Monday, October fifth. Two, Luis — the draft station partner agreement template.
[00:50:47] Luis Ortega (Amperlane): This week. Thursday.
[00:50:50] Mark Feldman (Intellias): Thursday the first. And us: we schedule the technical deep-dive with Ravi and Priya. Olena leads, Kyrylo joins, and we bring our payments and integrations lead, because — clearly — money.
[00:51:06] Ravi Menon (Amperlane): Please bring him. Or her.
[00:51:10] Mark Feldman (Intellias): Him. Andriy. He'll enjoy your page and a half.
[00:51:16] Olena Marchuk (Intellias): How is Thursday, October eighth, eleven AM your time? I'd like the data and the contract template before, so we come prepared.
[00:51:29] Ravi Menon (Amperlane): Let me check — [inaudible] — yeah, the eighth at eleven works. Priya's in. Sixty minutes?
[00:51:38] Olena Marchuk (Intellias): Sixty. I'll send the invite with a short agenda: current tooling, station integrations, booking logic, vehicle data, payments and settlement, non-functional requirements, data migration.
[00:51:51] Luis Ortega (Amperlane): Can I crash part of it? For the station stuff. I know which sites can do what.
[00:52:01] Olena Marchuk (Intellias): Please. We'll put station integrations early, you join for twenty minutes or so.
[00:52:09] Kyrylo Shvedov (Intellias): And I'll send a written summary with the open questions by tomorrow, so you can correct anything we got wrong — especially the business model. Every number gets a source.
[00:52:25] Dana Whitfield (Amperlane): Love that. Yes please.
[00:52:28] Mark Feldman (Intellias): Let me close properly for the record. Amperlane: pilot data export and survey by Monday the fifth, via Ravi and Priya; station agreement template from Luis by Thursday the first. Intellias: Olena sends the invite for Thursday the eighth, eleven Eastern, with Andriy; Kyrylo sends the summary and open questions tomorrow, Wednesday the thirtieth; then we propose the business-model working session. Missed anything?
[00:53:00] Ravi Menon (Amperlane): Pilot data migration on the tech agenda.
[00:53:05] Olena Marchuk (Intellias): It's on.
[00:53:08] Luis Ortega (Amperlane): Payout frequency.
[00:53:10] Kyrylo Shvedov (Intellias): On the open questions.
[00:53:14] Dana Whitfield (Amperlane): Then we're good.
[00:53:17] Kyrylo Shvedov (Intellias): Just a thank you, then. Thank you for showing the no-show numbers in the first meeting. A lot of founders hide those until the third. It makes our job easier and the platform better.
[00:53:35] Dana Whitfield (Amperlane): [laughs] Well, you asked. And if we build for the deck and not for reality, we find out on March second anyway.
[00:53:47] Luis Ortega (Amperlane): From Kinship. On the phone. About cones.
[00:53:52] Mark Feldman (Intellias): [laughs] Let's avoid that call. Luis — is the Model Y still on stall six?
[00:54:01] Luis Ortega (Amperlane): It left. Two minutes over its session. Not a sleeper. A good citizen.
[00:54:09] Mark Feldman (Intellias): A happy ending.
[00:54:12] Ravi Menon (Amperlane): Okay, I have to run back into the lawyers. Olena, see you on the eighth. Bring your hard questions.
[00:54:23] Olena Marchuk (Intellias): All of them. Bye, Ravi.
[00:54:27] Ravi Menon (Amperlane): Bye all.
[00:54:29] Kyrylo Shvedov (Intellias): Thanks everyone. Coffee number four is calling.
[00:54:35] Olena Marchuk (Intellias): Bye everyone.
[00:54:37] Luis Ortega (Amperlane): Bye from Gowanus!
[00:54:40] Dana Whitfield (Amperlane): Bye! Thank you all.
00:55:03  ·  Recording stopped. Transcription ended.
