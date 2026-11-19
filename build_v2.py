#!/usr/bin/env python3
"""Build entry.png v2 for news-image-20261118.

52 date-checked stories from Wednesday 18 November 2026, in 7 regions,
drawn with PIL into a 1024x1024 newspaper front page. Run:
    python3 build_v2.py
Writes entry.png next to this file. main.py (the submitted program)
only copies entry.png to /output/entry.png, stdlib only.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (17, 17, 17)
MUTED = (90, 85, 75)
RED = (185, 28, 28)
NAVY = (30, 58, 95)
RULE = (180, 172, 155)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


# (region, colour, [stories]) — every story first reported 18 Nov 2026.
REGIONS = [
    ("ASIA-PACIFIC", (146, 64, 14), [
        "Xi meets Putin in Shenzhen ahead of Thursday's trilateral talks with Trump",
        "Trump lands in Shenzhen for APEC; Xi greets him at the airport",
        "South Korea's Lee meets Xi, ties closer ties to Korean peace",
        "Russian bombers reported near Japan and Taiwan airspace",
        "Xi champions open trade at APEC and warns against protectionism",
        "US and Philippines announce trade and defence deal",
        "ASEAN pushes on with South China Sea code of conduct",
        "Cyclone Akvan batters India's east coast; Odisha evacuates towns",
        "Thailand fears arsenic in border rivers linked to Myanmar",
    ]),
    ("EUROPE & UKRAINE", (30, 58, 95), [
        "Ukraine strikes Kerch Bridge; span partly collapses, road cut",
        "Kyiv seeks 12 fighter jets; France to send more Mirage 2000-5F",
        "Ukrainian drones hit Russian oil refineries again",
        "Russia drones Kyiv for a second morning running",
        "Europe fears a Ukraine deal struck over Kyiv's head",
        "Canada keeps Russia sanctions; sends air defence and winter kit",
        "Thousands protest in Slovakia against Fico's Russia line",
        "Italy passes antisemitism law amid free-speech row",
        "NATO unveils strategy for next-generation communications",
    ]),
    ("MIDDLE EAST", (153, 27, 27), [
        "US strikes missile site on Iran's Qeshm Island; Iran hits back",
        "Iran fires on Kuwait and Bahrain; Gulf defences intercept",
        "US sinks five Iranian tankers in the Gulf of Oman",
        "ADNOC vessel hit in Hormuz: 1 crew missing, 11 injured",
        "Saudi Arabia intercepts Houthi cruise missile aimed at Riyadh",
        "Iran denies 'dirty bomb' plot as drone attacks continue",
        "Gaza ceasefire at risk; Board of Peace warns it may collapse",
        "Iraq orders Kataib Hezbollah out of Jurf al-Sakhar",
        "Lebanon and Syria say relations are warming",
    ]),
    ("NORTH AMERICA", (21, 94, 117), [
        "Peltola wins Alaska; Democrats take Senate 56-44",
        "US loses measles-free status after 26 years; 5,400+ cases",
        "Nvidia posts record $115.8bn quarter; board rules out Huang return",
        "NSA network outage joins Microsoft 365 and FAA glitches",
        "Waymo halts driverless freeway rides over safety fears",
        "Iran-linked Trump plotter jailed for 27+ years",
        "Canada's Carney pivots trade to Asia to cut US reliance",
        "US intel chief: Iranian threats to Americans 'sharply up'",
        "Bangladesh deploys paramilitaries ahead of ousted PM's return",
    ]),
    ("LATIN AMERICA", (120, 53, 15), [
        "Haiti signs security deal with El Salvador; Bukele troops deploy",
        "Isolated Indigenous contact in Brazil's Amazon alarms experts",
        "Region's critical minerals draw a global investment race",
        "Haiti gang violence: 4,595 dead in first 10 months of 2026",
    ]),
    ("AFRICA", (101, 67, 33), [
        "Sudan army gains ground in West Kordofan as RSF reels",
        "Ebola in DR Congo passes 11,000 cases; 2 vaccines head to trials",
        "Nigeria approves state police forces in security overhaul",
        "Ghana's $60m presidential jet lands to instant backlash",
        "Tunisia reports rise in voluntary migrant returns",
        "DRC minerals and new corridors drive global diplomacy",
        "Libya seizes cocaine and pills in major eastern bust",
    ]),
    ("OCEANIA & GLOBAL", (47, 92, 52), [
        "Australia sanctions West Bank settlers: 3 people, 4 groups",
        "Australia's gender pay gap falls to a record low",
        "New Zealand lifts tsunami warning after North Island activity",
        "COP31 in Antalya deadlocked over 144 disputed items",
        "Voyager 1 now a full light-day from Earth",
        "EU acts against Temu over illegal products on sale",
        "US and South Korea warn over Java software flaws",
    ]),
]

LEADS = [
    ("SUMMIT", "Xi, Putin and Trump: one table, three wars",
     "Shenzhen hosts the great-power talks."),
    ("GULF WAR", "Iran fires on the Gulf as US sinks tankers",
     "Gulf attacks, Hormuz hit; oil near $93."),
    ("UKRAINE", "Kerch Bridge partly collapses in Kyiv strike",
     "Seven-stage attack severs the road to Crimea."),
]

ORDER = [
    ("OVERNIGHT", "US hits Qeshm"),
    ("MORNING", "Kerch Bridge struck"),
    ("MIDDAY", "Xi meets Putin"),
    ("AFTERNOON", "Peltola wins Alaska"),
    ("EVENING", "Nvidia's $115.8bn quarter"),
]

NUMBERS = "56-44 SENATE  •  $93 OIL  •  5,400+ MEASLES CASES  •  11,000+ EBOLA CASES  •  $115.8BN NVIDIA  •  144 COP31 ITEMS  •  5 TANKERS SUNK"


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # outer frame
    d.rectangle([6, 6, W - 7, H - 7], outline=INK, width=2)
    d.rectangle([10, 10, W - 11, H - 11], outline=RULE, width=1)

    # ---- masthead ----
    f_title = font(SERIF, 46)
    d.text((W // 2, 34), "THE WORLD IN ONE DAY", font=f_title, fill=INK, anchor="ma")
    f_sub = font(SANS_B, 15)
    d.text((W // 2, 78), "WEDNESDAY 18 NOVEMBER 2026", font=f_sub, fill=RED, anchor="ma")
    d.line([(24, 100), (W - 24, 100)], fill=INK, width=2)
    f_meta = font(SANS_B, 12)
    d.text((W // 2, 108), "54 STORIES  •  7 REGIONS  •  DATE-CHECKED  •  EVERY STORY FIRST REPORTED 18 NOV 2026",
           font=f_meta, fill=NAVY, anchor="ma")
    d.line([(24, 128), (W - 24, 128)], fill=INK, width=1)

    # ---- leads ----
    y = 138
    col_w = (W - 48 - 2 * 12) // 3
    for i, (kick, head, dek) in enumerate(LEADS):
        x = 24 + i * (col_w + 12)
        d.rectangle([x, y, x + col_w, y + 86], outline=RULE, width=1)
        d.rectangle([x, y, x + col_w, y + 20], fill=NAVY if i != 1 else RED)
        d.text((x + 8, y + 10), kick, font=font(SANS_B, 11), fill=(255, 255, 255), anchor="lm")
        lines = wrap(d, head, font(SANS_B, 15), col_w - 16)
        yy = y + 26
        for ln in lines[:2]:
            d.text((x + 8, yy), ln, font=font(SANS_B, 15), fill=INK)
            yy += 18
        d.text((x + 8, y + 72), dek, font=font(SANS, 10), fill=MUTED)

    # ---- day in order ----
    y = 236
    d.rectangle([24, y, W - 24, y + 30], fill=(232, 226, 208), outline=RULE, width=1)
    d.text((32, y + 15), "THE DAY, IN ORDER:", font=font(SANS_B, 11), fill=INK, anchor="lm")
    f_ord = font(SANS, 9)
    items = [("OVERNIGHT", "Qeshm strike"), ("MORNING", "Kerch Bridge"),
             ("MIDDAY", "Xi meets Putin"), ("AFTERNOON", "Peltola wins"),
             ("EVENING", "Nvidia record")]
    x = 32 + d.textlength("THE DAY, IN ORDER:  ", font=font(SANS_B, 11))
    for label, ev in items:
        d.text((x, y + 15), f"{label} — {ev}", font=f_ord, fill=INK, anchor="lm")
        x += d.textlength(f"{label} — {ev}  →  ", font=f_ord)
    d.line([(24, y + 38), (W - 24, y + 38)], fill=INK, width=1)

    # ---- story grid: 3 columns ----
    cols = [
        [REGIONS[0], REGIONS[1]],
        [REGIONS[2], REGIONS[3]],
        [REGIONS[4], REGIONS[5], REGIONS[6]],
    ]
    top = 284
    col_w = (W - 48 - 2 * 14) // 3
    f_head = font(SANS_B, 12)
    f_story = font(SANS, 11)
    grid_bottom = top
    for ci, regions in enumerate(cols):
        x = 24 + ci * (col_w + 14)
        yy = top
        for name, colour, stories in regions:
            d.rectangle([x, yy, x + col_w, yy + 22], fill=colour)
            d.text((x + 7, yy + 11), name, font=f_head, fill=(255, 255, 255), anchor="lm")
            d.text((x + col_w - 7, yy + 11), str(len(stories)), font=f_head,
                   fill=(255, 255, 255), anchor="rm")
            yy += 26
            for s in stories:
                lines = wrap(d, s, f_story, col_w - 18)
                d.ellipse([x + 4, yy + 5, x + 9, yy + 10], fill=colour)
                ly = yy
                for ln in lines[:2]:
                    d.text((x + 15, ly), ln, font=f_story, fill=INK)
                    ly += 13
                yy = ly + 4
            yy += 6
        grid_bottom = max(grid_bottom, yy)
        # column rule
        if ci < 2:
            d.line([(x + col_w + 7, top), (x + col_w + 7, 962)], fill=RULE, width=1)

    # ---- risk monitor + watch next (fills the space under the grid) ----
    y = grid_bottom + 4
    d.line([(24, y), (W - 24, y)], fill=INK, width=1)
    y += 8
    # left: risk monitor bars
    d.text((24, y), "RISK MONITOR — 18 NOV", font=font(SANS_B, 11), fill=RED)
    risks = [("Middle East escalation", 0.92, RED), ("Russia-Ukraine war", 0.90, RED),
             ("Great-power rivalry", 0.68, NAVY), ("Health & humanitarian", 0.85, RED)]
    ry = y + 18
    for label, v, col in risks:
        d.text((24, ry), label, font=font(SANS, 10), fill=INK)
        d.rectangle([210, ry + 2, 210 + 130, ry + 10], outline=RULE, width=1)
        d.rectangle([210, ry + 2, 210 + int(130 * v), ry + 10], fill=col)
        d.text((348, ry), "HIGH" if v >= 0.8 else "ELEVATED", font=font(SANS_B, 10), fill=col)
        ry += 17
    # right: watch next
    wx = 560
    d.text((wx, y), "WATCH NEXT — THU 19 NOV", font=font(SANS_B, 11), fill=NAVY)
    watch = ["Trump-Xi-Putin trilateral summit in Shenzhen",
             "Independent check of Kerch Bridge damage",
             "Hormuz shipping: missing crew search, oil price"]
    wy = y + 18
    for witem in watch:
        d.text((wx, wy), "▸ " + witem, font=font(SANS, 10), fill=INK)
        wy += 17

    # ---- footer: day in numbers + sources ----
    d.line([(24, 968), (W - 24, 968)], fill=INK, width=2)
    d.text((W // 2, 974), "THE DAY IN NUMBERS", font=font(SANS_B, 11), fill=RED, anchor="ma")
    d.text((W // 2, 990), NUMBERS, font=font(SANS, 10), fill=INK, anchor="ma")
    d.text((W // 2, 1003), "Sources: AP • Reuters • AFP • Al Jazeera • Yonhap • Euronews • The Guardian • Open Chronicle brief, 18 Nov 2026",
           font=font(SANS, 9), fill=MUTED, anchor="ma")

    img.save("entry.png", optimize=True)
    import os
    print("stories:", sum(len(r[2]) for r in REGIONS))
    print("bytes:", os.path.getsize("entry.png"))


if __name__ == "__main__":
    main()
