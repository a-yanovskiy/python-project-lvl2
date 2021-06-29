from gendiff.open_files import open_files
from gendiff.get_diff_json import get_diff_json
from gendiff.get_diff_yaml import get_diff_yaml


def extract_and_sort_all_keys(file_1, file_2):
    merge_files = {**file_1, **file_2}
    all_keys = list(merge_files.keys())
    all_keys.sort()
    return all_keys


def gendiff(first_file, second_file):

    files = open_files(first_file, second_file)
    file_1 = files[0]
    file_2 = files[1]
    file_type = files[2]
    all_keys = extract_and_sort_all_keys(file_1, file_2)

    if file_type == '.yaml' or file_type == '.yml':
        print(
            get_diff_yaml(file_1, file_2, all_keys)
        )
    elif file_type == '.json':
        print(
            get_diff_json(file_1, file_2, all_keys)
        )
