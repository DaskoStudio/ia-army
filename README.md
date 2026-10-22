> ℹ️ Dépôt vitrine — code de base / architecture ; fonctionnalités clés privées.

# IA-ARMY

Socle d’architecture pour un système multi-agents autour de Solana ; stratégies et intégrations privées non incluses.

## ✨ Fonctionnalités

- API FastAPI avec `GET /health`.
- Contrat abstrait `Agent.run()` et signature d’enregistrement d’un orchestrateur.
- Exemple de prompt générique, sans action externe.

L’orchestrateur reste un stub et lève `NotImplementedError`. Aucun agent de trading, connexion Solana, notification ni tableau de bord fonctionnel n’est livré.

## 🧱 Structure

```text
backend/main.py            API et santé
backend/agents/base.py     Classe abstraite Agent
backend/orchestrator.py    Signature register() non implémentée
config/prompts/example.md  Prompt générique
frontend/package.json      Manifeste React minimal (sans interface)
core/, agents/, deploy/    Emplacements réservés
```

## 🚀 Lancer

Prérequis : Python 3.11+ ; Node.js/npm uniquement pour le manifeste frontend.

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --host 127.0.0.1
```

Vérifier : `curl http://127.0.0.1:8000/health`. Documentation : `http://127.0.0.1:8000/docs`.
Aucun secret requis. Le frontend ne propose pas de commande de démarrage : seule sa dépendance React est déclarée (`cd frontend && npm install`).

## 🛠️ Stack

Python · FastAPI · Uvicorn · React (manifeste). Solana et coordination avancée : architecture cible uniquement.

## 👤 Auteur

Konaté Adama (@DaskoStudio) — Ynov Campus
