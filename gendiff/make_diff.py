def diff_keys(dict1, dict2):
    """[summary]

    Args:
        dict1 ([type]): [description]
        dict2 ([type]): [description]

    Returns:
        [type]: [description]
    """
    keys_set_1 = set(dict1.keys())
    keys_set_2 = set(dict2.keys())

    all_keys_sorted = sorted(list(keys_set_1 | keys_set_2))
    added_keys = list(keys_set_2 - keys_set_1)
    deleted_keys = list(keys_set_1 - keys_set_2)
    return all_keys_sorted, added_keys, deleted_keys


def make_diff(dict1, dict2=None):

    if not isinstance(dict1, dict):
        return dict1

    if dict2 is None:
        dict2 = dict1

    all_keys = diff_keys(dict1, dict2)[0]
    added = diff_keys(dict1, dict2)[1]
    deleted = diff_keys(dict1, dict2)[2]

    result = {}

    for key in all_keys:
        if key in added:
            result[key] = {
                'status': 'added',
                'body1': make_diff(dict2[key])
            }
        elif key in deleted:
            result[key] = {
                'status': 'deleted',
                'body1': make_diff(dict1[key])
            }
        else:
            if dict1[key] == dict2[key]:
                result[key] = {
                    'status': 'unchanged',
                    'body1': dict1[key]}
            elif not isinstance(
                dict1[key], dict
            ) or not isinstance(
                dict2[key], dict
            ):
                result[key] = {
                    'status': 'replaced',
                    'body1': make_diff(dict1[key]),
                    'body2': make_diff(dict2[key])
                }
            else:
                result[key] = {
                    'status': 'changed',
                    'body1': make_diff(dict1[key], dict2[key])
                }
    return result
