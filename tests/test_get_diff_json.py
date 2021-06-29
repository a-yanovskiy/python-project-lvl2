from gendiff.open_files import open_files
from gendiff.get_diff_json import get_diff_json
from gendiff.generate_diff import extract_and_sort_all_keys as all_keys


PATH_TO_JSON_1_FILE = 'tests/fixtures/json_1st_file.json'
PATH_TO_JSON_2_FILE = 'tests/fixtures/json_2nd_file.json'
PATH_TO_JSON_RESULT_FILE = 'tests/fixtures/json_result_file.txt'


def test_get_diff_json():
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
