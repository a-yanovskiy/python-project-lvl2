from gendiff.formatters.json import get_json
import ast
import pytest

PATH_TO_DIFF_FIRST_RESULT = "tests/fixtures/diff_first_result.txt"
PATH_TO_JSON_FIRST_RESULT = "tests/fixtures/json_first_result.json"

PATH_TO_DIFF_SECOND_RESULT = "tests/fixtures/diff_second_result.txt"
PATH_TO_JSON_SECOND_RESULT = "tests/fixtures/json_second_result.json"


@pytest.mark.parametrize("path_to_diff_file, path_to_jsoned_file",
                         [
                             (PATH_TO_DIFF_FIRST_RESULT, PATH_TO_JSON_FIRST_RESULT),
                             (PATH_TO_DIFF_SECOND_RESULT, PATH_TO_JSON_SECOND_RESULT),
                         ]
                         )
def test_get_json(path_to_diff_file, path_to_jsoned_file):
    with open(path_to_diff_file, 'r') as unformatted:
        unformatted_file = unformatted.read()
        unformatted_file = ast.literal_eval(unformatted_file)
    with open(path_to_jsoned_file, 'r') as formatted:
        formatted_file = formatted.read()

    formatted_by_json = get_json(unformatted_file)

    assert formatted_by_json == formatted_file
