from gendiff.formaters.stylish import stylish
import ast


def load_files(path_to_unformated_file, path_to_formated_file):

    with open(path_to_unformated_file, 'r') as unformated:
        unformated_file = unformated.read()
        unformated_file = ast.literal_eval(unformated_file)
    with open(path_to_formated_file, 'r') as formated:
        formated_file = formated.read()

    formated_by_stylish = stylish(unformated_file)

    return formated_by_stylish, formated_file


def test_stylish_json_1():

    loaded = load_files("tests/fixtures/json_diff_first_result.txt", "tests/fixtures/json_stylish_first_result.txt")
    stylished_file = loaded[0]
    formated_file = loaded[1]

    assert stylished_file == formated_file


def test_stylish_json_2():

    loaded = load_files("tests/fixtures/json_diff_second_result.txt", "tests/fixtures/json_stylish_second_result.txt")
    stylished_file = loaded[0]
    formated_file = loaded[1]

    assert stylished_file == formated_file
