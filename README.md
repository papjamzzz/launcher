<p align="center">
  <img src="static/logo.png" width="120" alt="Launcher logo"/>
</p>

# Launcher — Creative Konsoles Hub

> **Everything running. One place.**

The central launchpad for the entire Creative Konsoles stack. Start, stop, and monitor every app from one dashboard — no terminal required.

---

## What It Does

- **App grid** — every project in the stack, with live online/offline status
- **One-click start/stop** — launch any app directly from the dashboard
- **Port monitor** — real-time check that each server is actually responding
- **Process tracking** — knows if a server crashed vs. never started
- **Direct links** — jump to any running app in one click

---

## Apps in the Stack

| App | What It Does | Port |
|-----|-------------|------|
| [5i](https://github.com/papjamzzz/5i) | Parallel AI synthesis — 5 models, one verdict | 5562 |
| [Kalshi Konnektor](https://github.com/papjamzzz/kalshi-konnektor) | Prediction market edge detector | 5555 |
| [KK Trader](https://github.com/papjamzzz/kalshi-trader) | Autonomous trading bot | 5559 |
| [StreamFader](https://github.com/papjamzzz/Stream-Fader) | Streaming content ranker with DJ fader | 5556 |
| [TrackTracks](https://github.com/papjamzzz/Track-Tracks) | Per-track CPU monitor for Ableton Live | 5557 |
| [DAW Doctor](https://github.com/papjamzzz/Daw-Doctor) | DAW diagnostics and session optimizer | 5558 |
| [Kode Keeper](https://github.com/papjamzzz/kodekeeper) | Claude Code mission control | 5560 |
| [Key Watcher](https://github.com/papjamzzz/key-watcher) | API key health monitor | 5563 |
| [WithYou](https://github.com/papjamzzz/empathybot) | AI voice companion — 12 support types | 5564 |

---

## Setup

```bash
git clone https://github.com/papjamzzz/launcher.git
cd launcher
make setup
make run
```

Opens at `http://127.0.0.1:5554`

Or double-click `launch.command` on Mac.

---

## Stack

Python · Flask · psutil · Vanilla JS · JetBrains Mono

No external UI frameworks. Runs local.

---

## Part of Creative Konsoles

Built by [Creative Konsoles](https://creativekonsoles.com) — tools built using thought.

**[creativekonsoles.com](https://creativekonsoles.com)** &nbsp;·&nbsp; support@creativekonsoles.com

<!-- repo maintenance: 2026-04-10 -->
