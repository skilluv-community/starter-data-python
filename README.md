# starter-data-python

> A Skilluv starter — JupyterLab + pandas + DuckDB + scikit-learn, with a sample African dataset.

[![CI](https://github.com/skilluv-community/starter-data-python/actions/workflows/ci.yml/badge.svg)](https://github.com/skilluv-community/starter-data-python/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
[![Skilluv](https://img.shields.io/badge/skilluv-community-emerald)](https://skilluv.io)

## English

### What this is

A ready-to-run Jupyter Lab environment for data exploration:

- **JupyterLab 4** in Docker
- **pandas 2** for data manipulation
- **DuckDB 1** for SQL over CSVs and Parquet, no DB server needed
- **scikit-learn 1.5** for classical ML
- **matplotlib + seaborn** for plots
- Managed with **uv**
- Sample dataset shipped: 2023 African population + GDP per capita (illustrative)

### Quickstart

```bash
git clone git@github.com:skilluv-community/starter-data-python.git
cd starter-data-python
cp .env.example .env
docker compose up --build
```

Open <http://localhost:8888> and browse `notebooks/`.

### Notebooks

- `01_load_data.ipynb` — load the CSV, inspect shape
- `02_basic_analysis.ipynb` — descriptive stats + seaborn plots
- `03_duckdb_queries.ipynb` — SQL over the CSV via DuckDB
- `04_ml_intro.ipynb` — minimal scikit-learn regression

### Docs

- [`docs/en/getting-started.md`](./docs/en/getting-started.md)
- [`docs/en/architecture.md`](./docs/en/architecture.md)

---

## Français

Environnement JupyterLab prêt-à-l'emploi pour l'exploration de données. Voir [`docs/fr/getting-started.md`](./docs/fr/getting-started.md).

```bash
git clone git@github.com:skilluv-community/starter-data-python.git
cd starter-data-python
cp .env.example .env
docker compose up --build
```

---

## License

MIT — see [LICENSE](./LICENSE).
