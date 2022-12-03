#!/usr/bin/env bash

set -e
set -x

black ./*.py ./**/*.py
isort ./*.py ./**/*.py