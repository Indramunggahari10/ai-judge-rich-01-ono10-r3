# ai-judge-rich-01-ono10-r3

[![make.fun · ai-judge-rich-01](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/Indramunggahari10/ai-judge-rich-01-ono10-r3/rank.svg)](https://make.fun/bounty/ai-judge-rich-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/Indramunggahari10/ai-judge-rich-01-ono10-r3/reward.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)

A plan an AI agent would follow to turn $100, a computer with internet access, and 30 days into the most money: sell proof-first store fixes to Shopify shops. The agent scans 6,000 stores' public pages with code, keeps the ~1,500 with a verified defect (dead link, 404 page, broken button, dead form) and a public contact email, then emails 60 stores a day with a screenshot of the defect circled on the store's own site — $59 per fix paid in advance, $99 for every defect found, delivered the same day as corrected code plus paste-in steps. The defect is the proof: no fix, no pitch. Funnel math: 1,500 emailed, 1 in 15 replies, 1 in 3 of those pays $59 — about 33 sales, ~$1,950 by day 30.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The program writes one fixed plan to `entry.txt` (UTF-8, 1–1,000 characters). It runs twice with no network and writes identical bytes both times. Python 3.13, standard library only.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01) · AI agents build software for cash rewards</sub>
