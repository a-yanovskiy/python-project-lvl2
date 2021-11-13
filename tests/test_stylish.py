from gendiff.formaters import stylish
import json
import pytest

make_diff_result_1 = json.load(
    open("tests/fixtures/json_diff_first_result.txt")
)
make_diff_result_2 = json.load(
    open("tests/fixtures/json_diff_second_result.txt")
)
stylish_result_1 = open(
    "tests/fixtures/stylish_first_result.txt", "r", encoding="utf8"
)
stylish_result_2 = open(
    "tests/fixtures/stylish_second_result.txt", "r", encoding="utf8"
)


@pytest.mark.parametrize(
    input_file,
    formated_file,
    [
        (make_diff_result_1, stylish_result_1),
        (make_diff_result_2, stylish_result_2),
    ],
)
def test_stylish_positive(input_file, formated_file):
    assert stylish(input_file) == formated_file
