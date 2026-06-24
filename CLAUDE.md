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
*Mirrors the `APPS` dict in app.py (the source of truth). Update both together.*

| App | Port | Folder | Type |
|-----|------|--------|------|
| 5i (flagship) | 5562 | ~/5i | web |
| Kalshi Konnektor | 5555 | ~/kalshi-edge | web |
| StreamFader | 5556 | ~/streamfader | web |
| Represented | 5567 | ~/represented | web |
| EmpathyBot | 5564 | ~/empathybot | web |
| DK Konnektor | 5563 | ~/dk-konnektor | web |
| TrackTracks | — | ~/track_cpu_monitor | gui (auto-launches with Ableton) |
| DAW Doctor | — | ~/ableton-diagnostics | cli |

## Port
5554

## GitHub
https://github.com/papjamzzz/launcher — live, public

---
*Last updated: 2026-06-24 — Apps Registered table synced to APPS; Represented added after StreamFader*
