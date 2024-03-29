import pytest

from gendiff.diff import make_diff
from gendiff.load import load_file
from gendiff.parse import parse

PATH_TO_JSON_1_FILE = "tests/fixtures/json_1_test_file.json"
PATH_TO_JSON_2_FILE = "tests/fixtures/json_2_test_file.json"
PATH_TO_JSON_FIRST_RESULT = "tests/fixtures/diff_first_result.txt"

PATH_TO_JSON_3_FILE = "tests/fixtures/json_3_test_file.json"
PATH_TO_JSON_4_FILE = "tests/fixtures/json_4_test_file.json"
PATH_TO_JSON_SECOND_RESULT = "tests/fixtures/diff_second_result.txt"

PATH_TO_YAML_1_FILE = "tests/fixtures/yaml_1_test_file.yaml"
PATH_TO_YAML_2_FILE = "tests/fixtures/yaml_2_test_file.yaml"
PATH_TO_YAML_FIRST_RESULT = "tests/fixtures/diff_first_result.txt"

PATH_TO_YAML_3_FILE = "tests/fixtures/yaml_3_test_file.yaml"
PATH_TO_YAML_4_FILE = "tests/fixtures/yaml_4_test_file.yaml"
PATH_TO_YAML_SECOND_RESULT = "tests/fixtures/diff_second_result.txt"


@pytest.mark.parametrize("path_1, path_2, result",
                         [
                             (PATH_TO_JSON_1_FILE, PATH_TO_JSON_2_FILE, PATH_TO_JSON_FIRST_RESULT),
                             (PATH_TO_JSON_3_FILE, PATH_TO_JSON_4_FILE, PATH_TO_JSON_SECOND_RESULT),
                             (PATH_TO_YAML_1_FILE, PATH_TO_YAML_2_FILE, PATH_TO_YAML_FIRST_RESULT),
                             (PATH_TO_YAML_3_FILE, PATH_TO_YAML_4_FILE, PATH_TO_YAML_SECOND_RESULT),
                         ]
                         )
def test_make_diff(path_1, path_2, result):
    data_1, format_1 = load_file(path_1)
    data_2, format_2 = load_file(path_2)
    file_1 = parse(data_1, format_1)
    file_2 = parse(data_2, format_2)

    diff_result = str(make_diff(file_1, file_2))

    with open(result, 'r') as file:
        result_from_file = file.read().replace('\n', '')

    assert diff_result == result_from_file
