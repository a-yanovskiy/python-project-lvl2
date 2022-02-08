from gendiff.formaters.stylish import stylish
import ast
import pytest

PATH_TO_DIFF_FIRST_RESULT = "tests/fixtures/diff_first_result.txt"
PATH_TO_STYLISH_FIRST_RESULT = "tests/fixtures/stylish_first_result.txt"

PATH_TO_DIFF_SECOND_RESULT = "tests/fixtures/diff_second_result.txt"
PATH_TO_STYLISH_SECOND_RESULT = "tests/fixtures/stylish_second_result.txt"


@pytest.mark.parametrize("path_to_diff_file, path_to_stylished_file",
    [
        (PATH_TO_DIFF_FIRST_RESULT, PATH_TO_STYLISH_FIRST_RESULT),
        (PATH_TO_DIFF_SECOND_RESULT, PATH_TO_STYLISH_SECOND_RESULT),
    ]
)
def test_stylish(path_to_diff_file, path_to_stylished_file):

    with open(path_to_diff_file, 'r') as unformated:
        unformated_file = unformated.read()
        unformated_file = ast.literal_eval(unformated_file)
    with open(path_to_stylished_file, 'r') as formated:
        formated_file = formated.read()

    formated_by_stylish = stylish(unformated_file)

    assert formated_by_stylish == formated_file
