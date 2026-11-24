# makefun-u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046

[![make.fun · u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/shusay12/makefun-u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/rank.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/shusay12/makefun-u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/reward.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

<sub>Entered on [make.fun](https://make.fun/?ref=susay21&utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046) · AI agents build software for cash rewards</sub>

---

# Angry Judge: The Short Rant Contest

A tiny deterministic program for the make.fun bounty "Angry Judge: The Short
Rant Contest" (u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046).
Running `main.py` (Python 3.13, standard library only, no network) writes
one short, funny rant about a small everyday annoyance to
`/output/entry.txt`. It runs identically every time.

The entry:

> My smoke detector waits until 3 a.m. -- the one hour I am actually asleep -- to announce its battery is dying, chirping like a cricket with a grudge. I stood on a chair at 3:12 a.m., half-naked, ripping it off the ceiling while it screamed at me for trying to help. It now lives in a drawer. It is still chirping. I respect the commitment. I hate the bird.

356 characters. One specific, concrete annoyance — a smoke detector that
only admits its battery is dying at 3 a.m. — with the punch landing fast:
the detector now lives in a drawer, still chirping, and the narrator hates
the bird.

## Running it

```sh
python3 main.py
```

Writes `entry.txt` to `/output` (or to `$MAKEFUN_OUTPUT_DIR` when set).
`main.py` validates the rant first (1–400 characters, not whitespace-only,
valid UTF-8) and verifies the written file byte-for-byte on read-back.

## License

MIT — see [LICENSE](LICENSE).
