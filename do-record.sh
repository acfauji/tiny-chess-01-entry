#!/usr/bin/env bash
cd /root/makefun-work/tiny-chess-01-entry
./mf record --competition tiny-chess-01 --source /root/makefun-work/tiny-chess-01-entry -- opencode run -m opencode/big-pickle "$(cat PROMPT.txt)" 2>&1