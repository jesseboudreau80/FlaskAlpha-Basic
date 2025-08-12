# FlaskAlpha-Basic

A minimal, production-ready Flask starter with app factory, blueprints, CORS, security headers, Prometheus metrics, tests, Docker, and CI.

## Purpose
Jumpstart new Flask services with consistent structure, tooling, and deployability.

## My Role
Template author/maintainer. Use as a base for microservices or prototypes.

## Technologies Used
Flask · Gunicorn · python-dotenv · Flask-CORS · Flask-Talisman · Prometheus Exporter · Pytest · Ruff · Black · Docker · GitHub Actions

## Local Dev (Crostini / Linux)
```bash
cd /mnt/chromeos/removable/Chromeb_L/FlaskAlpha-Basic
make install
make dev
# open http://localhost:8000

