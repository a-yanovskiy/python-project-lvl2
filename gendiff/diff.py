from gendiff.formatters.formatters import format_diff
from load import load_file


def make_diff(dict1, dict2=None):
    if not isinstance(dict1, dict):
        return dict1

    if dict2 is None:
        dict2 = dict1

    keys_set_1 = set(dict1.keys())
    keys_set_2 = set(dict2.keys())

    all_keys = sorted(list(keys_set_1 | keys_set_2))
    added = list(keys_set_2 - keys_set_1)
    deleted = list(keys_set_1 - keys_set_2)

    result = {}

    for key in all_keys:
        if key in added:
            result[key] = {'type': 'added', 'body1': make_diff(dict2[key])}
        elif key in deleted:
            result[key] = {'type': 'deleted', 'body1': make_diff(dict1[key])}
        else:
            if dict1[key] == dict2[key]:
                result[key] = {
                    'type': 'unchanged',
                    'body1': make_diff(dict1[key])
                }
            elif not isinstance(dict1[key], dict) or not isinstance(
                    dict2[key], dict):
                result[key] = {
                    'type': 'replaced',
                    'body1': make_diff(dict1[key]),
                    'body2': make_diff(dict2[key])
                }
            else:
                result[key] = {
                    'type': 'changed',
                    'body1': make_diff(dict1[key], dict2[key])
                }
    return result


def generate_diff(first_file, second_file, format='stylish'):
    file_1 = load_file(first_file)
    file_2 = load_file(second_file)
    diff = make_diff(file_1, file_2)
    return format_diff(diff, format)
