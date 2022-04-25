from re import S
from gendiff.generate_diff import generate_diff
import ast
import pytest


PATH_TO_JSON_1_FILE = "tests/fixtures/json_1_test_file.json"
PATH_TO_JSON_2_FILE = "tests/fixtures/json_2_test_file.json"

PATH_TO_JSON_3_FILE = "tests/fixtures/json_3_test_file.json"
PATH_TO_JSON_4_FILE = "tests/fixtures/json_4_test_file.json"

PATH_TO_YAML_1_FILE = "tests/fixtures/yaml_1_test_file.yaml"
PATH_TO_YAML_2_FILE = "tests/fixtures/yaml_2_test_file.yaml"

PATH_TO_YAML_3_FILE = "tests/fixtures/yaml_3_test_file.yaml"
PATH_TO_YAML_4_FILE = "tests/fixtures/yaml_4_test_file.yaml"

PATH_TO_STYLISH_FIRST_RESULT = "tests/fixtures/stylish_first_result.txt"
PATH_TO_STYLISH_SECOND_RESULT = "tests/fixtures/stylish_second_result.txt"
PATH_TO_PLAIN_FIRST_RESULT = "tests/fixtures/plain_first_result.txt"
PATH_TO_PLAIN_SECOND_RESULT = "tests/fixtures/plain_second_result.txt"


@pytest.mark.parametrize("first_file, second_file, result_file, formater",
                         [
                             (PATH_TO_JSON_1_FILE, PATH_TO_JSON_2_FILE, PATH_TO_STYLISH_FIRST_RESULT, "stylish"),
                             (PATH_TO_JSON_3_FILE, PATH_TO_JSON_4_FILE, PATH_TO_STYLISH_SECOND_RESULT, "stylish"),
                             (PATH_TO_YAML_1_FILE, PATH_TO_YAML_2_FILE, PATH_TO_STYLISH_FIRST_RESULT, "stylish"),
                             (PATH_TO_YAML_3_FILE, PATH_TO_YAML_4_FILE, PATH_TO_STYLISH_SECOND_RESULT, "stylish"),
                             (PATH_TO_JSON_1_FILE, PATH_TO_JSON_2_FILE, PATH_TO_PLAIN_FIRST_RESULT, "plain"),
                             (PATH_TO_JSON_3_FILE, PATH_TO_JSON_4_FILE, PATH_TO_PLAIN_SECOND_RESULT, "plain"),
                             (PATH_TO_YAML_1_FILE, PATH_TO_YAML_2_FILE, PATH_TO_PLAIN_FIRST_RESULT, "plain"),
                             (PATH_TO_YAML_3_FILE, PATH_TO_YAML_4_FILE, PATH_TO_PLAIN_SECOND_RESULT, "plain"),
                         ]
                         )
def test_generate_diff(first_file, second_file, result_file, formater):

    diff = generate_diff(first_file, second_file, formater)

    with open(result_file, 'r') as f:
        result = f.read()

    assert diff == result
