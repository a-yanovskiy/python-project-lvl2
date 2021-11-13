from gendiff.open_files import open_files
from gendiff.make_diff import make_diff

PATH_TO_JSON_1_FILE = 'tests/fixtures/json_1_test_file.json'
PATH_TO_JSON_2_FILE = 'tests/fixtures/json_2_test_file.json'
PATH_TO_JSON_FIRST_RESULT = 'tests/fixtures/json_diff_first_result.txt'


def test_make_diff_json_first():
    files = open_files(
        PATH_TO_JSON_1_FILE,
        PATH_TO_JSON_2_FILE,
    )

    file1 = files[0]
    file2 = files[1]

    diff_result = make_diff(file1, file2)

    result_file = open(PATH_TO_JSON_FIRST_RESULT)

    result_from_json_file = result_file.read()

    assert diff_result == result_from_json_file


PATH_TO_JSON_3_FILE = 'tests/fixtures/json_3_test_file.json'
PATH_TO_JSON_4_FILE = 'tests/fixtures/json_4_test_file.json'
PATH_TO_JSON_SECOND_RESULT = 'tests/fixtures/json_diff_second_result.txt'


# TODO FileNotFoundError исправить. почему не видит файлы?
def test_make_diff_second():
    files = open_files(
        PATH_TO_JSON_3_FILE,
        PATH_TO_JSON_4_FILE,
    )

    file3 = files[0]
    file4 = files[1]

    diff_result = make_diff(file3, file4)

    f = open(PATH_TO_JSON_SECOND_RESULT)

    result_from_json_file = f.read()

    assert diff_result == result_from_json_file
