from gendiff.open_files import open_files
from gendiff.make_diff import make_diff


PATH_TO_JSON_1_FILE = "tests/fixtures/json_1_test_file.json"
PATH_TO_JSON_2_FILE = "tests/fixtures/json_2_test_file.json"
PATH_TO_JSON_3_FILE = "tests/fixtures/json_3_test_file.json"
PATH_TO_JSON_4_FILE = "tests/fixtures/json_4_test_file.json"
PATH_TO_JSON_FIRST_RESULT = "tests/fixtures/json_diff_first_result.txt"
PATH_TO_JSON_SECOND_RESULT = "tests/fixtures/json_diff_second_result.txt"

PATH_TO_YAML_1_FILE = "tests/fixtures/yaml_1_test_file.yaml"
PATH_TO_YAML_2_FILE = "tests/fixtures/yaml_2_test_file.yaml"
PATH_TO_YAML_3_FILE = "tests/fixtures/yaml_3_test_file.yaml"
PATH_TO_YAML_4_FILE = "tests/fixtures/yaml_4_test_file.yaml"
PATH_TO_YAML_FIRST_RESULT = "tests/fixtures/yaml_diff_first_result.txt"
PATH_TO_YAML_SECOND_RESULT = "tests/fixtures/yaml_diff_second_result.txt"


def check_make_diff(path_1, path_2, result):
    files = open_files(
        path_1,
        path_2,
    )

    file1 = files[0]
    file2 = files[1]

    diff_result = str(make_diff(file1, file2))

    with open(result, 'r') as file:
        result_from_file = file.read().replace('\n', '')

    return diff_result, result_from_file


def test_make_diff_json_1():

    result = check_make_diff(
        PATH_TO_JSON_1_FILE,
        PATH_TO_JSON_2_FILE,
        PATH_TO_JSON_FIRST_RESULT,
    )
    assert result[0] == result[1]


def test_make_diff_json_2():

    result = check_make_diff(
        PATH_TO_JSON_3_FILE,
        PATH_TO_JSON_4_FILE,
        PATH_TO_JSON_SECOND_RESULT,
    )
    assert result[0] == result[1]



def test_make_diff_yaml_1():

    result = check_make_diff(PATH_TO_YAML_1_FILE, PATH_TO_YAML_2_FILE, PATH_TO_YAML_FIRST_RESULT)
    assert result[0] == result[1]


def test_make_diff_yaml_2():

    result = check_make_diff(
        PATH_TO_YAML_3_FILE,
        PATH_TO_YAML_4_FILE,
        PATH_TO_YAML_SECOND_RESULT,
    )
    assert result[0] == result[1]
