# Getting started — starter-data-python

## Prerequisites

- Docker + Docker Compose 2.24+
- (Optional, local dev) Python 3.12+, [uv](https://docs.astral.sh/uv/)

## First run

```bash
git clone git@github.com:skilluv-community/starter-data-python.git
cd starter-data-python
cp .env.example .env
docker compose up --build
```

Open <http://localhost:8888>. **Warning**: the container disables Jupyter's auth
token for developer convenience. Never expose this port to the public internet
without adding a token/password.

## Running notebooks

The `notebooks/` folder is mounted from your host, so any changes you make in Jupyter Lab are saved locally.

## Testing utility code

```bash
uv sync
uv run pytest -q
```

Tests live under `tests/`; helpers under `src/`. Notebooks should stay thin — they orchestrate, they don't hold logic.

## Working with real datasets

The shipped CSV is a small illustrative sample. See `data/README.md` for real sources (World Bank, UN, Africa Open Data, data.gouv.bj).
