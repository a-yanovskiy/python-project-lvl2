from gendiff.formatters.plain import get_plain
import ast
import pytest

PATH_TO_DIFF_FIRST_RESULT = "fixtures/diff_first_result.txt"
PATH_TO_PLAIN_FIRST_RESULT = "fixtures/plain_first_result.txt"

PATH_TO_DIFF_SECOND_RESULT = "fixtures/diff_second_result.txt"
PATH_TO_PLAIN_SECOND_RESULT = "fixtures/plain_second_result.txt"


@pytest.mark.parametrize("path_to_diff_file, path_to_plained_file",
    [
        (PATH_TO_DIFF_FIRST_RESULT, PATH_TO_PLAIN_FIRST_RESULT),
        (PATH_TO_DIFF_SECOND_RESULT, PATH_TO_PLAIN_SECOND_RESULT),
    ]
)
def test_get_plain(path_to_diff_file, path_to_plained_file):

    with open(path_to_diff_file, 'r') as unformatted:
        unformatted_file = unformatted.read()
        unformatted_file = ast.literal_eval(unformatted_file)
    with open(path_to_plained_file, 'r') as formatted:
        formatted_file = formatted.read()

    formatted_by_plain = get_plain(unformatted_file)

    assert formatted_by_plain == formatted_file
