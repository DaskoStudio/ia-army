# IA-ARMY

> Architecture skeleton of a multi-agent system built around Solana: market monitoring, decision support and prediction markets, coordinated by an orchestrator.

![Status](https://img.shields.io/badge/status-showcase-38f0c0?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Solana](https://img.shields.io/badge/Solana-9945FF?style=flat-square&logo=solana&logoColor=white)

> **ℹ️ Showcase repository.** Only the architecture is public. Strategies, integrations, keys and every agent implementation are private and **not included**.

---

## Table of contents

- [Concept](#concept)
- [Architecture](#architecture)
- [What this repository contains](#what-this-repository-contains)
- [Getting started](#getting-started)
- [Project structure](#project-structure)
- [Tech stack](#tech-stack)

## Concept

IA-ARMY splits a complex workflow into small, specialised agents instead of one monolithic bot. An orchestrator registers agents, routes work between them and exposes the whole system through a single API. The private version targets Solana market monitoring and prediction-market use cases.

## Architecture

```text
┌────────────┐     ┌─────────────────────────┐     ┌───────────────┐
│ Dashboard  │────►│  Backend (FastAPI)      │────►│ Orchestrator  │
│ (React)    │     │  health · API           │     │ agent registry│
└────────────┘     └─────────────────────────┘     └───────┬───────┘
                                                           │
                          ┌────────────────┬───────────────┤
                          ▼                ▼               ▼
                     ┌─────────┐     ┌──────────┐    ┌──────────┐
                     │ Agent A │     │ Agent B  │    │ Agent …  │
                     │ (Agent) │     │ (Agent)  │    │ (Agent)  │
                     └─────────┘     └──────────┘    └──────────┘
```

Each agent implements the same abstract `Agent.run()` contract, which keeps the orchestrator independent from what the agents actually do.

## What this repository contains

| Component | Status |
|---|---|
| `GET /health` | ✅ Returns `{"status":"ok"}` |
| `Agent` abstract class (`run`) | ⛔ Contract only |
| `Orchestrator.register(name, agent)` | ⛔ Signature only — raises `NotImplementedError` |
| Generic prompt example (`config/prompts/example.md`) | ✅ No external action |
| Frontend | Minimal React manifest, no interface |
| Trading agents, Solana connections, notifications, dashboard | ❌ Not included |

## Getting started

**Prerequisites:** Python 3.11+. Node.js/npm is only needed for the frontend manifest.

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --host 127.0.0.1
```

```bash
curl http://127.0.0.1:8000/health      # {"status":"ok"}
```

Interactive API docs: <http://127.0.0.1:8000/docs>. No secret is required. The frontend has no start command — only its React dependency is declared (`cd frontend && npm install`).

## Project structure

```text
backend/main.py           API and health check
backend/agents/base.py    Abstract Agent class
backend/orchestrator.py   register() signature (not implemented)
config/prompts/           Generic prompt example
frontend/package.json     Minimal React manifest
core/ agents/ deploy/     Reserved placeholders
```

## Tech stack

Python · FastAPI · Uvicorn · React (manifest). Solana integration and advanced coordination are target architecture only.

---

**Author** — Konaté Adama · [github.com/DaskoStudio](https://github.com/DaskoStudio)
