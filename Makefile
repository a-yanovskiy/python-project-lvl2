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

run-json-files12:
	poetry run gendiff tests/fixtures/json_1_test_file.json tests/fixtures/json_2_test_file.json

run-json-files34:
	poetry run gendiff tests/fixtures/json_3_test_file.json tests/fixtures/json_4_test_file.json

run-yaml-files12:
	poetry run gendiff tests/fixtures/yaml_1_test_file.yaml tests/fixtures/yaml_2_test_file.yaml

run-yaml-files34:
	poetry run gendiff tests/fixtures/yaml_3_test_file.yaml tests/fixtures/yaml_4_test_file.yaml

.PHONY: install test test-coverage lint selfcheck check build run-json-files12 run-json-files34 run-yaml-files12 run-yaml-files34
