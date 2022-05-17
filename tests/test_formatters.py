import ast

import pytest

from gendiff.formatters.json import get_json
from gendiff.formatters.plain import get_plain
from gendiff.formatters.stylish import get_stylish

PATH_TO_DIFF_FIRST_RESULT = "tests/fixtures/diff_first_result.txt"
PATH_TO_DIFF_SECOND_RESULT = "tests/fixtures/diff_second_result.txt"

PATH_TO_STYLISH_FIRST_RESULT = "tests/fixtures/stylish_first_result.txt"
PATH_TO_STYLISH_SECOND_RESULT = "tests/fixtures/stylish_second_result.txt"

PATH_TO_PLAIN_FIRST_RESULT = "tests/fixtures/plain_first_result.txt"
PATH_TO_PLAIN_SECOND_RESULT = "tests/fixtures/plain_second_result.txt"

PATH_TO_JSON_FIRST_RESULT = "tests/fixtures/json_first_result.json"
PATH_TO_JSON_SECOND_RESULT = "tests/fixtures/json_second_result.json"


@pytest.mark.parametrize("path_to_diff_file, path_to_formatted_file, formatter",
                         [
                             (PATH_TO_DIFF_FIRST_RESULT, PATH_TO_STYLISH_FIRST_RESULT, get_stylish),
                             (PATH_TO_DIFF_SECOND_RESULT, PATH_TO_STYLISH_SECOND_RESULT, get_stylish),
                             (PATH_TO_DIFF_FIRST_RESULT, PATH_TO_PLAIN_FIRST_RESULT, get_plain),
                             (PATH_TO_DIFF_SECOND_RESULT, PATH_TO_PLAIN_SECOND_RESULT, get_plain),
                             (PATH_TO_DIFF_FIRST_RESULT, PATH_TO_JSON_FIRST_RESULT, get_json),
                             (PATH_TO_DIFF_SECOND_RESULT, PATH_TO_JSON_SECOND_RESULT, get_json),
                         ]
                         )
def test_formatters(path_to_diff_file, path_to_formatted_file, formatter):
    with open(path_to_diff_file, 'r') as unformatted:
        unformatted_file = unformatted.read()
        unformatted_file = ast.literal_eval(unformatted_file)
    with open(path_to_formatted_file, 'r') as formatted:
        formatted_file = formatted.read()

    formatted = formatter(unformatted_file)
    assert formatted == formatted_file
