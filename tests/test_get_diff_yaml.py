from gendiff.open_files import open_files
from gendiff.get_diff_yaml import get_diff_yaml
from gendiff.generate_diff import extract_and_sort_all_keys as all_keys


PATH_TO_YAML_1_FILE = 'tests/fixtures/yaml_1_test_file.yaml'
PATH_TO_YAML_2_FILE = 'tests/fixtures/yaml_2_test_file.yaml'
PATH_TO_YAML_RESULT_1_2_FILES = 'tests/fixtures/yaml_result_1-2_files.txt'


def test_get_diff_yaml_1_2_files():
    files = open_files(
        PATH_TO_YAML_1_FILE,
        PATH_TO_YAML_2_FILE
    )

    path_1 = files[0]
    path_2 = files[1]

    diff_result = get_diff_yaml(
        path_1,
        path_2,
        all_keys(path_1, path_2)
    )

    f = open(PATH_TO_YAML_RESULT_1_2_FILES)

    result_from_yaml_file = f.read()

    assert diff_result == result_from_yaml_file


PATH_TO_YAML_3_FILE = 'tests/fixtures/yaml_3_test_file.yaml'
PATH_TO_YAML_4_FILE = 'tests/fixtures/yaml_4_test_file.yaml'
PATH_TO_YAML_RESULT_3_4_FILES = 'tests/fixtures/yaml_result_3-4_files.txt'


def test_get_diff_yaml_3_4_files():
    files = open_files(
        PATH_TO_YAML_3_FILE,
        PATH_TO_YAML_4_FILE
    )

    path_3 = files[0]
    path_4 = files[1]

    diff_result = get_diff_yaml(
        path_3,
        path_4,
        all_keys(path_3, path_4)
    )

    f = open(PATH_TO_YAML_RESULT_3_4_FILES)

    result_from_yaml_file = f.read()

    assert diff_result == result_from_yaml_file
