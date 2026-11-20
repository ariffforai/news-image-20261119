# THE WORLD IN ONE DAY — Thursday 19 November 2026

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/ariffforai/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/ariffforai/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image summing up the world news of **Thursday 19 November 2026**, built for [make.fun](https://make.fun/bounty/news-image-20261119)'s "Sum up 19 November's world news in one image" bounty ($250).

## The day in 50 stories

The front page is drawn in code from `stories.json`: a masthead stating the count (50 stories · 8 regions), the giant date, a UTC timeline of the day, four illustrated hero stories, a twelve-story grid with icons, a world map with numbered pins and a region legend, a numbered one-line list for stories 17–50, a DATE CHECK bar naming what was deliberately left out, and a footer stating the date rule and the sources.

**The big four**

1. **GTA VI is out — 13 years later** — the game unlocks at midnight local time around the world, with a 99 on Metacritic; 6.38 million people watched the launch in its first 90 minutes.
2. **Trump, Xi and Putin meet — a first** — the first-ever trilateral of the three leaders, at Kylin Villa in Shenzhen, ends with a joint pledge that a nuclear war cannot be won and must never be fought.
3. **Court: Myanmar committed genocide** — the International Court of Justice rules 9–6 that Myanmar's 2017 crackdown on the Rohingya was genocide, the first time the court has held a state responsible for the crime.
4. **Kerch Bridge hit a third time** — Ukrainian Neptune missiles strike the bridge linking Russia and Crimea for the third time in four days, halting rail traffic.

**More of the day** — COP31's draft drops all fossil-fuel language; Anthropic's $1.5 trillion IPO debuts at $83 and closes at $97; Wall Street slumps 2% in its longest slide since April 2024; Bangladesh locks down under 3,000 paramilitary troops; the FCC lets prisons jam contraband phones; Mongolia's president quits; three tankers hit mines off Hormuz; the IEA calls the Hormuz crisis the greatest threat to energy security ever; and potatoes grow in simulated moon soil.

Every story is tagged CLAIM or CONFIRMED with its source, and every story happened or was first reported on 19 November 2026. Seven near-misses were checked and moved to the DATE CHECK bar instead of the front page: the Van Gogh record sale, the Pew report on Islam passing Christianity by 2035, Jeffries being named speaker-designate, the US–Venezuela military deal, Musk's "pretty foolish" midterm-spending regret and the Ethiopia–Eritrea troop buildup all belong to Wednesday 18 November; the UK–EU summit and the COP31 final deal are both due Friday 20 November.

The image is an original front page drawn with PIL from the story data in `stories.json`: masthead, timeline, heroes, grid, map, list, date check and footer, with simple flat illustrations drawn in code. No photograph, character or artwork belonging to anyone else is used.

## How it works

`main.py` (Python 3.13, standard library only) copies the shipped `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`). It is deterministic — both runs write identical bytes — and needs no network.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The output is a 1024×1024 PNG, 193,369 bytes — inside the 1 MiB and 1024×1024 limits.
