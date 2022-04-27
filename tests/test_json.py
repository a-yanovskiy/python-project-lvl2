from gendiff.formaters.json import get_json
import ast
import pytest

PATH_TO_DIFF_FIRST_RESULT = "fixtures/diff_first_result.txt"
PATH_TO_JSON_FIRST_RESULT = "fixtures/json_first_result.json"

PATH_TO_DIFF_SECOND_RESULT = "fixtures/diff_second_result.txt"
PATH_TO_JSON_SECOND_RESULT = "fixtures/json_second_result.json"


@pytest.mark.parametrize("path_to_diff_file, path_to_jsoned_file",
                         [
                             (PATH_TO_DIFF_FIRST_RESULT, PATH_TO_JSON_FIRST_RESULT),
                             (PATH_TO_DIFF_SECOND_RESULT, PATH_TO_JSON_SECOND_RESULT),
                         ]
                         )
def test_json(path_to_diff_file, path_to_jsoned_file):
    with open(path_to_diff_file, 'r') as unformated:
        unformated_file = unformated.read()
        unformated_file = ast.literal_eval(unformated_file)
    with open(path_to_jsoned_file, 'r') as formated:
        formated_file = formated.read()

    formated_by_json = get_json(unformated_file)

    assert formated_by_json == formated_file
