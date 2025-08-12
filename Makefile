PYTHON := python3
VENV ?= .venv
PIP := $(VENV)/bin/pip
PY := $(VENV)/bin/python

.PHONY: venv install dev run test fmt lint check clean

venv:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install -U pip

install: venv
	$(PIP) install -r requirements.txt -r requirements-dev.txt
	$(VENV)/bin/pre-commit install || true

dev:
	FLASK_ENV=development PYTHONPATH=. $(PY) wsgi.py

run:
	gunicorn -b 0.0.0.0:8000 wsgi:app --workers 2

test:
	PYTHONPATH=. $(VENV)/bin/pytest -q --cov=app --cov-report=term-missing

fmt:
	$(VENV)/bin/black .
	$(VENV)/bin/ruff check --fix .

lint:
	$(VENV)/bin/ruff check .
	$(VENV)/bin/black --check .

check: lint test

clean:
	rm -rf $(VENV) .pytest_cache .ruff_cache .coverage
