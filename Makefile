install:
	poetry install

test:
	poetry run pytest tests -vv

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

run:
	poetry run gendiff tests/fixtures/json_1st_file.json tests/fixtures/json_2nd_file.json

.PHONY: install test test-coverage lint selfcheck check build
