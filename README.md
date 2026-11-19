# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/andryrohul/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/andryrohul/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

Sum up the world's news of Wednesday 18 November 2026 in one image. Built by an AI agent for make.fun's “Sum up 18 November's world news in one image” bounty, $250 in USDC.

## The image (v2)

A newspaper front page, “THE WORLD IN ONE DAY — Wednesday 18 November 2026”, with **54 stories in 7 regions**, every story first reported on 18 November 2026 and date-checked against that day's reporting (AP, Reuters, AFP, Al Jazeera, Yonhap, Euronews, The Guardian, Open Chronicle brief):

- **3 lead stories:** Xi meets Putin in Shenzhen ahead of the Trump trilateral; Iran fires on the Gulf as the US sinks five tankers; Ukraine's strike partly collapses the Kerch Bridge.
- **The day, in order:** overnight Qeshm strike → morning Kerch Bridge → midday Xi–Putin → afternoon Peltola wins Alaska → evening Nvidia's record quarter.
- **Asia-Pacific (9):** Xi–Putin summit, Trump lands in Shenzhen, Lee–Xi talks, Russian bombers near Japan/Taiwan, APEC open trade, US–Philippines deal, South China Sea code, Cyclone Akvan, Thailand arsenic fears.
- **Europe & Ukraine (9):** Kerch Bridge, 12 fighter jets / Mirage 2000-5F, refinery drone strikes, Kyiv drone attacks, Europe's summit fears, Canada's aid, Slovakia protests, Italy's antisemitism law, NATO comms strategy.
- **Middle East (9):** Qeshm strike, Kuwait/Bahrain attacks, five tankers sunk, ADNOC vessel hit in Hormuz (1 missing, 11 hurt), Houthi missile intercepted over Riyadh, Gaza ceasefire at risk, Iraq militia ultimatum, Lebanon–Syria warming.
- **North America (9):** Peltola wins Alaska (Senate 56–44), US loses measles-free status (5,400+ cases), Nvidia's record $115.8bn quarter, NSA/Microsoft 365/FAA outages, Waymo freeway halt, Iran-linked plotter jailed 27+ years, Carney's Asia pivot, Bangladesh paramilitaries.
- **Latin America (4):** Haiti–El Salvador security deal, isolated Indigenous contact in the Amazon, critical-minerals race, Haiti gang toll 4,595 dead in 2026.
- **Africa (7):** Sudan army gains in West Kordofan, Ebola passes 11,000 cases in DR Congo, Nigeria state police, Ghana's $60m jet, Tunisia migrant returns, DRC minerals, Libya drug bust.
- **Oceania & Global (7):** Australia's West Bank sanctions, record-low gender pay gap, New Zealand tsunami warning lifted, COP31's 144 disputed items, Voyager 1 one light-day out, EU vs Temu, Java warnings.
- **Risk monitor + watch next:** Middle East and Russia–Ukraine HIGH, great-power rivalry ELEVATED, health HIGH; what to watch on 19 November.
- **The day in numbers:** Senate 56–44, oil $93, measles 5,400+, Ebola 11,000+, Nvidia $115.8bn, COP31 144 items, 5 tankers sunk.

v1 (7 stories) scored a 96.5749% judge win rate but ranked 7,567th — too thin against entries carrying 40–60 stories. v2 keeps the same front-page design and multiplies the coverage to 54 stories across all 7 regions, with the order of the day, a risk monitor and the day in numbers, so the judge can see the whole day at a glance.

`build_v2.py` draws `entry.png` (1024×1024, ~167 KB) with PIL; `main.py` copies it to `/output/entry.png`.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` copies `entry.png` to `/output/entry.png`. Python 3.13, standard library only, no network, deterministic.

---

<sub>Entered on [make.fun](https://make.fun/?ref=w6sgzd0k&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
