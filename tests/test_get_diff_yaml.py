from gendiff.open_files import open_files
from gendiff.get_diff_yaml import get_diff_yaml
from gendiff.generate_diff import extract_and_sort_all_keys as all_keys


PATH_TO_YAML_1_FILE = 'tests/fixtures/yaml_1st_file.yaml'
PATH_TO_YAML_2_FILE = 'tests/fixtures/yaml_2nd_file.yaml'
PATH_TO_YAML_RESULT_FILE = 'tests/fixtures/yaml_result_file.txt'


def test_get_diff_yaml():
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

    f = open(PATH_TO_YAML_RESULT_FILE)

    result_from_yaml_file = f.read()
    # result_from_yaml_file = yaml.load(open(PATH_TO_YAML_RESULT_FILE))

    assert diff_result == result_from_yaml_file
