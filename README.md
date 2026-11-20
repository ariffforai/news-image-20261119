# One Day in the News — 19 November 2026

An entry for the Make.fun news-image bounty of 19 November 2026: a single
1024×1024 newspaper front page that tries to hold one whole day of world
news on one sheet of paper.

## What is on the page

Fifty stories, every one of them about something that actually happened on
Thursday 19 November 2026 — not merely reported that day. They are spread
across eight regions: Americas 13, Asia 9, Africa 8, Europe 6,
Middle East 10, Global 2, Oceania 1 and Space 1.

The page is laid out like a broadsheet front page:

- **The big four** — the day's four largest stories, each with a small flat
  illustration: the worldwide launch of Grand Theft Auto VI; the first-ever
  Xi–Trump–Putin trilateral summit in Shenzhen and its "Declaration Towards
  Peace"; the International Court of Justice ruling, 9–6, that Myanmar
  committed genocide against the Rohingya; and the third Ukrainian strike
  on the Kerch Bridge in four days, which halted rail traffic.
- **The day in UTC** — a six-slot timeline running from the overnight Kerch
  Bridge strike and the midnight GTA VI unlock, through the Shenzhen summit
  and the Hague verdict, to the evening's first sales estimates.
- **More of the day** — twelve further stories in an icon grid, from a
  Houthi missile hitting Riyadh's tallest tower to SpaceX scrubbing a
  Space Force launch at Vandenberg.
- **Where it happened** — a schematic world map with sixteen numbered pins
  for the heroes and the grid stories.
- **The rest of the day** — stories 17 to 50 as a numbered list, covering
  the US Senate's rejection of an Iran war-powers resolution, a Kenyan
  rare-earths deal, a doping ban for a marathon champion, and more.
- **Date check** — a red bar listing seven big stories that look like
  19 November news but are not: each one is shown with its true date, so
  nobody mistakes a Wednesday event for a Thursday one.

## How the image is made

`stories.json` holds all fifty stories, the timeline, the map pins, the
numbered list and the date-check items. A drawing script turns that file
into `entry.png`, a 1024×1024 PNG. The picture on the page is drawn from
the data, so changing a story means changing the JSON and re-rendering —
nothing is baked in by hand.

## How main.py works

`main.py` is deliberately small. It finds `entry.png` next to itself,
reads it, and copies it into the directory named by `MAKEFUN_OUTPUT_DIR`
(`/output` if the variable is unset), creating that directory when needed.
Before it calls the job done it verifies the copy: the eight-byte PNG
signature must be present, the first chunk must be a 13-byte IHDR, and
the IHDR must declare a width and height of 1024×1024. It then re-reads
the destination file and checks it is byte-for-byte identical to the
source. Any failure — a missing source file, a bad signature, wrong
dimensions, or a copy that differs — is reported on stderr and the
program exits with a non-zero status. It uses only the Python standard
library, makes no network calls, and behaves the same way every run.

## Verification done

- `stories.json` was checked against the drawing script: 50 stories in
  total (4 heroes + 12 grid + 34 listed), region counts add up to 50,
  and the renderer reported no text-overflow problems.
- The rendered `entry.png` is a PNG of 1024×1024 pixels and under
  1,048,576 bytes.
- `main.py` was run twice with different output directories and both runs
  produced outputs byte-identical to the shipped `entry.png`.
- The page was inspected at full size and as a 256-pixel thumbnail for
  legibility.

## Sources

Each story on the page names its source next to it — among them
Al Jazeera, the Straits Times, Interfax, the IEA, the IAEA, Spaceflight
Now, the South China Morning Post, OkayAfrica, the Times and Reuters
reporting carried by the outlets shown.
