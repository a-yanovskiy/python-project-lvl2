from gendiff.formatters.stylish import get_stylish
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
def test_get_stylish(path_to_diff_file, path_to_stylished_file):
    with open(path_to_diff_file, 'r') as unformatted:
        unformatted_file = unformatted.read()
        unformatted_file = ast.literal_eval(unformatted_file)
    with open(path_to_stylished_file, 'r') as formatted:
        formatted_file = formatted.read()

    formatted_by_stylish = get_stylish(unformatted_file)

    assert formatted_by_stylish == formatted_file
