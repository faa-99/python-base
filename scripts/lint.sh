#!/usr/bin/env bash

set -e
set -x

mypy ./*.py ./**/*.py
flake8 ./*.py ./**/*.py
black ./*.py ./**/*.py --check --diff
isort ./*.py ./**/*.py --check-only