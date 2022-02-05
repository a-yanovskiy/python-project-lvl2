from gendiff.formaters.plain import plain
import ast
import pytest

PATH_TO_DIFF_FIRST_RESULT = "tests/fixtures/diff_first_result.txt"
PATH_TO_PLAIN_FIRST_RESULT = "tests/fixtures/plain_first_result.txt"

PATH_TO_DIFF_SECOND_RESULT = "tests/fixtures/diff_second_result.txt"
PATH_TO_PLAIN_SECOND_RESULT = "tests/fixtures/plain_second_result.txt"


@pytest.mark.parametrize("path_to_diff_file, path_to_plained_file",
    [
        (PATH_TO_DIFF_FIRST_RESULT, PATH_TO_PLAIN_FIRST_RESULT),
        (PATH_TO_DIFF_SECOND_RESULT, PATH_TO_PLAIN_SECOND_RESULT),
    ]
)
def test_plain(path_to_diff_file, path_to_plained_file):

    with open(path_to_diff_file, 'r') as unformated:
        unformated_file = unformated.read()
        unformated_file = ast.literal_eval(unformated_file)
    with open(path_to_plained_file, 'r') as formated:
        formated_file = formated.read()

    formated_by_plain = plain(unformated_file)

    assert formated_by_plain, formated_file
