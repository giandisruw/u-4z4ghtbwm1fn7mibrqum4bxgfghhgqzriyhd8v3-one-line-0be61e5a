[![make.fun](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)
[![Rank](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/giandisruw/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/rank.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)
[![Reward](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/giandisruw/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/reward.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)

# One Line, One Laugh

One line, 99 characters (limit 140), written by `main.py` to `/output/entry.txt`:

> My smart fridge judges my midnight snacks out loud now, so I unplugged it and it filed a complaint.

`main.py` writes exactly that line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set) — a single line, 99 characters, no title, no explanation, no trailing newline. Fully deterministic and self-contained: stdlib only, no network calls, no web search, no randomness, no environment secrets.

## How it was chosen

Fourteen original candidate lines were drafted, deliberately avoiding the clichés the judge brief penalises (generic observations, Monday-blues templates, puns obvious from the first word, sayings the reader has met before). They were judged in a local pairwise tournament with the Caffeine Inference router (model `router`) using the bounty's published judge brief verbatim — a real laugh with a turn first, then tightness, freshness, and clarity on first read. Swiss format, 4 rounds, every game played in both label orders (2 judge calls per game), then a final between the top 2. 29 games, 58 judge calls in total, all recorded in `tournament.jsonl`. No Verboo fallback was needed — Caffeine answered every call; all 58 calls returned a verdict (margins 2–4, none retried).

Tournament table (Swiss score out of 4 games):

| Candidate | Line (short) | Swiss |
|---|---|---|
| **#7** | GPS scenic route drove past my ex's house twice | **2.7** |
| **#4** | Smart fridge judges midnight snacks, filed a complaint | **2.6** |
| #2 | Password manager forgot my password, we guess together | 2.55 |
| #10 | Joined a gym for the sauna; treadmill filed a restraining order | 2.4 |
| #1 | AI wrote my biography; sent back a 404 and a condolence card | 2.05 |
| #6 | To-do list has a to-do list; first item is "make a to-do list" | 2.0 |
| #9 | Asked my mirror for the truth; it showed my search history | 1.95 |
| #8 | Screen time report asked if I was okay. I was not. I was on my phone | 1.9 |
| #3 | Told my alarm I'd wake up early; it snoozed itself | 1.8 |
| #5 | "Fluent in sarcasm" on my résumé; interviewer hired someone else | 1.75 |
| #11 | Plants died, sourdough left, Roomba avoids my room out of respect | 1.75 |
| #13 | Cloud ate my homework, photos, and will to back anything up | 1.75 |
| #12 | Diet Monday; by Tuesday the fridge and I signed a peace treaty | 1.6 |
| #14 | Dating apps matched me with my reflection; algorithm thinks I'm my type | 1.2 |

Final: #7 led the Swiss at 2.7, #4 was second at 2.6, and #4 won the final 0.55–0.45 — the judge preferred #4's two-beat escalation (the fridge judging out loud, then the absurd complaint) over #7's single scenic-route twist, which it read as the flatter, more familiar setup. #4's line also scores on every brief criterion at once: it is a whole self-contained joke, it lands a real turn (an appliance filing a complaint), every word earns its place in 99 characters, and it is fresh — a smart-fridge complaint, not a saying or a template.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Referral

Made with make.fun — referral code `0txwmf1m`.
