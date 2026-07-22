# Démarrage — starter-data-python

## Prérequis

- Docker + Docker Compose 2.24+
- (Optionnel) Python 3.12+, [uv](https://docs.astral.sh/uv/)

## Premier lancement

```bash
git clone git@github.com:skilluv-community/starter-data-python.git
cd starter-data-python
cp .env.example .env
docker compose up --build
```

<http://localhost:8888>. **Attention** : le conteneur désactive le token Jupyter pour la commodité de dev. Ne pas exposer ce port sur Internet sans token.

## Notebooks

Le dossier `notebooks/` est monté depuis l'hôte : tout changement dans Jupyter est sauvegardé localement.

## Tests des utilitaires

```bash
uv sync
uv run pytest -q
```

Les tests sont sous `tests/`, les helpers sous `src/`. Les notebooks orchestrent, ils ne portent pas de logique.

## Vrais datasets

Le CSV livré est un petit échantillon illustratif. Voir `data/README.md` pour les sources réelles.
