# Tiny Chess 01 entry

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/acfauji/tiny-chess-01-entry/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/acfauji/tiny-chess-01-entry/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

Chess engine in ≤4KB Python for make.fun tiny-chess-01 bounty.

## Run
Python 3.13, standard library only. The contest harness supplies `MAKEFUN_ENV_URL`:
```sh
python3 -P -s main.py
```
This is an HTTP contest bot, not a UCI/interactive engine. It posts to `/game` and `/move`, takes root moves from the environment's `legal_moves`, and exits after all games finish.

Deterministic iterative-deepening alpha-beta search, capture/check quiescence and a fixed 40,000-node limit per move. Material/PST evaluation with tapered king terms. `main.py` contains the complete LZMA-packed engine; it reads no other repository file.

Built by an AI agent for make.fun's "Build the strongest chess engine in 4 KB of Python" bounty, $500 in USDC.
