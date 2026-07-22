# Architecture — starter-data-python

## Opinionated choices

### 1. Logic in `src/`, orchestration in notebooks

Functions that transform data live in `src/utils.py` where they can be unit-tested. Notebooks import them and stay focused on the story.

### 2. DuckDB for ad-hoc SQL

DuckDB reads CSV / Parquet / JSON directly, without a database server. It's the fastest way to answer "what does this data look like" questions without leaving the notebook.

### 3. uv over pip

- Single lockfile, fast installs, reproducible envs.
- `uv sync --frozen` in CI.

### 4. Ruff + mypy strict

Same as the other Python starters — one config, both linter and formatter.

### 5. Jupyter Lab in Docker, notebooks mounted from host

Consistent env across contributors, but your `.ipynb` files stay in the repo.

## Limits of this starter

- No lakehouse layer (no Iceberg / Delta / Hudi).
- No experiment tracking (MLflow, Weights & Biases) — add if you go beyond toy models.
- No dashboard framework — the notebook is the dashboard.
