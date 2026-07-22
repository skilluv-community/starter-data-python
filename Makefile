.PHONY: dev test lint fmt clean help lab

help:
	@echo "Targets: dev / lab / test / lint / fmt / clean"

dev: lab

lab:
	docker compose up --build

test:
	uv run pytest -q

lint:
	uv run ruff check .
	uv run mypy src

fmt:
	uv run ruff format .

clean:
	rm -rf .venv .pytest_cache .ruff_cache .mypy_cache
