from gendiff.open_files import open_files
from gendiff.make_diff import make_diff


def check_make_diff(path_1, path_2, result):
    files = open_files(
        path_1,
        path_2,
    )

    file1 = files[0]
    file2 = files[1]

    diff_result = make_diff(file1, file2)

    result_file = open(result)

    result_from_file = result_file.read()

    return diff_result, result_from_file


def test_make_diff_json_1():

    PATH_TO_1_FILE = "tests/fixtures/json_1_test_file.json"
    PATH_TO_2_FILE = "tests/fixtures/json_2_test_file.json"
    PATH_TO_FIRST_RESULT = "tests/fixtures/json_diff_first_result.txt"

    check_make_diff(
        PATH_TO_1_FILE,
        PATH_TO_2_FILE,
        PATH_TO_FIRST_RESULT,
    )
    assert check_make_diff[0] == check_make_diff[1]


def test_make_diff_json_2():

    PATH_TO_3_FILE = "tests/fixtures/json_3_test_file.json"
    PATH_TO_4_FILE = "tests/fixtures/json_4_test_file.json"
    PATH_TO_SECOND_RESULT = "tests/fixtures/json_diff_second_result.txt"

    check_make_diff(
        PATH_TO_3_FILE,
        PATH_TO_4_FILE,
        PATH_TO_SECOND_RESULT,
    )
    assert check_make_diff[0] == check_make_diff[1]


def test_make_diff_yaml_1():

    PATH_TO_3_FILE = "tests/fixtures/yaml_1_test_file.yaml"
    PATH_TO_4_FILE = "tests/fixtures/yaml_2_test_file.yaml"
    PATH_TO_SECOND_RESULT = "tests/fixtures/yaml_diff_first_result.txt"

    check_make_diff(
        PATH_TO_3_FILE,
        PATH_TO_4_FILE,
        PATH_TO_SECOND_RESULT,
    )
    assert check_make_diff[0] == check_make_diff[1]


def test_make_diff_yaml_2():

    PATH_TO_3_FILE = "tests/fixtures/yaml_3_test_file.yaml"
    PATH_TO_4_FILE = "tests/fixtures/yaml_4_test_file.yaml"
    PATH_TO_SECOND_RESULT = "tests/fixtures/yaml_diff_second_result.txt"

    check_make_diff(
        PATH_TO_3_FILE,
        PATH_TO_4_FILE,
        PATH_TO_SECOND_RESULT,
    )
    assert check_make_diff[0] == check_make_diff[1]
