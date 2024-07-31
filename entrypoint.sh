#!/bin/bash

echo 'Rodando as Migrations!'
poetry run alembic update head

echo 'Rodando projeto!'
poetry run uvicorn --host 0.0.0.0 focofitness.app:app