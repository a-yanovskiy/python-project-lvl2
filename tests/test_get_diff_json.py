from gendiff.open_files import open_files
from gendiff.get_diff_json import get_diff_json
from gendiff.generate_diff import extract_and_sort_all_keys as all_keys


PATH_TO_JSON_1_FILE = 'tests/fixtures/json_1_test_file.json'
PATH_TO_JSON_2_FILE = 'tests/fixtures/json_2_test_file.json'
PATH_TO_JSON_RESULT_FILE = 'tests/fixtures/json_result_1-2_files.txt'


def test_get_diff_json_1_2_files():
    files = open_files(
        PATH_TO_JSON_1_FILE,
        PATH_TO_JSON_2_FILE
    )

    path_1 = files[0]
    path_2 = files[1]

    diff_result = get_diff_json(
        path_1,
        path_2,
        all_keys(path_1, path_2)
    )

    f = open(PATH_TO_JSON_RESULT_FILE)

    result_from_json_file = f.read()

    assert diff_result == result_from_json_file


PATH_TO_JSON_3_FILE = 'tests/fixtures/json_3_test_file.json'
PATH_TO_JSON_4_FILE = 'tests/fixtures/json_4_test_file.json'
PATH_TO_JSON_RESULT_FILE = 'tests/fixtures/json_result_3-4_files.txt'


def test_get_diff_json_3_4_files():
    files = open_files(
        PATH_TO_JSON_3_FILE,
        PATH_TO_JSON_4_FILE
    )

    path_3 = files[0]
    path_4 = files[1]

    diff_result = get_diff_json(
        path_3,
        path_4,
        all_keys(path_3, path_4)
    )

    f = open(PATH_TO_JSON_RESULT_FILE)

    result_from_json_file = f.read()

    assert diff_result == result_from_json_file
