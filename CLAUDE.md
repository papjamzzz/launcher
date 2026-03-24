# Launcher — Re-Entry File
*Re-entry: Launcher*

## What This Is
Central hub for all Creative Konsoles tools. One click to launch, open, or monitor any app. Shows live status (online/offline) for every project.

## Re-Entry Phrase
"Re-entry: Launcher"

## Current Status
Live. All apps registered. Runs on port 5554.

## File Structure
```
launcher/
├── app.py              ← Flask, port 5554
├── templates/index.html
├── static/logo.png     ← JP paintball character
├── requirements.txt
├── Makefile
└── CLAUDE.md
```

## How to Run
```bash
cd ~/launcher
make setup   # first time only
make run     # starts on http://127.0.0.1:5554
```

## Apps Registered
| App | Port | Folder |
|-----|------|--------|
| 5i | 5562 | ~/5i |
| Kalshi Konnektor | 5555 | ~/kalshi-edge |
| StreamFader | 5556 | ~/streamfader |
| Track Tracks | 5557 | ~/track_cpu_monitor |
| DAW Doctor | 5558 | ~/ableton-diagnostics |
| KK Trader | 5559 | ~/kalshi-trader |
| Kode Keeper | 5560 | ~/kodekeeper |
| Pipeline | 5561 | ~/pipeline |

## Port
5554

## GitHub
https://github.com/papjamzzz/launcher — live, public

---
*Last updated: 2026-03-23*
