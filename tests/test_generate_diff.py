from re import S
from gendiff.generate_diff import generate_diff
import ast
import pytest


PATH_TO_JSON_1_FILE = "tests/fixtures/json_1_test_file.json"
PATH_TO_JSON_2_FILE = "tests/fixtures/json_2_test_file.json"
PATH_TO_JSON_STYLISH_FIRST_RESULT = "tests/fixtures/json_stylish_first_result.txt"

PATH_TO_JSON_3_FILE = "tests/fixtures/json_3_test_file.json"
PATH_TO_JSON_4_FILE = "tests/fixtures/json_4_test_file.json"
PATH_TO_JSON_STYLISH_SECOND_RESULT = "tests/fixtures/json_stylish_second_result.txt"

PATH_TO_YAML_1_FILE = "tests/fixtures/yaml_1_test_file.yaml"
PATH_TO_YAML_2_FILE = "tests/fixtures/yaml_2_test_file.yaml"
PATH_TO_YAML_STYLISH_FIRST_RESULT = "tests/fixtures/yaml_stylish_first_result.txt"

PATH_TO_YAML_3_FILE = "tests/fixtures/yaml_3_test_file.yaml"
PATH_TO_YAML_4_FILE = "tests/fixtures/yaml_4_test_file.yaml"
PATH_TO_YAML_STYLISH_SECOND_RESULT = "tests/fixtures/yaml_stylish_second_result.txt"


@pytest.mark.parametrize("first_file, second_file, result_file",
    [
        (PATH_TO_JSON_1_FILE, PATH_TO_JSON_2_FILE, PATH_TO_JSON_STYLISH_FIRST_RESULT),
        (PATH_TO_JSON_3_FILE, PATH_TO_JSON_4_FILE, PATH_TO_JSON_STYLISH_SECOND_RESULT),
        # (PATH_TO_YAML_1_FILE, PATH_TO_YAML_2_FILE, PATH_TO_YAML_STYLISH_FIRST_RESULT),
        # (PATH_TO_YAML_3_FILE, PATH_TO_YAML_4_FILE, PATH_TO_YAML_STYLISH_SECOND_RESULT),
    ]
)
def test_generate_diff(first_file, second_file, result_file):

    diff = generate_diff(first_file, second_file, "stylish")

    with open(result_file, 'r') as f:
        result = f.read()

    assert diff == result
