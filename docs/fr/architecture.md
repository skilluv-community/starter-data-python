# Architecture — starter-data-python

## Choix opinionated

### 1. Logique dans `src/`, orchestration dans les notebooks

Les fonctions de transformation vivent dans `src/utils.py` où elles peuvent être testées. Les notebooks les importent et se concentrent sur le récit.

### 2. DuckDB pour du SQL ad-hoc

DuckDB lit CSV / Parquet / JSON directement, sans serveur DB. Le plus rapide pour répondre à "à quoi ressemblent ces données".

### 3. uv plutôt que pip

- Lockfile unique, install rapide, envs reproductibles.
- `uv sync --frozen` en CI.

### 4. Ruff + mypy strict

Config unique, linter + formatter.

### 5. Jupyter Lab en Docker, notebooks montés depuis l'hôte

Env cohérent entre contributeurs, `.ipynb` dans le repo.

## Limites

- Pas de lakehouse (Iceberg / Delta / Hudi).
- Pas de tracking d'expériences (MLflow, W&B) — ajouter au-delà des modèles jouets.
- Pas de framework de dashboard — le notebook est le dashboard.
