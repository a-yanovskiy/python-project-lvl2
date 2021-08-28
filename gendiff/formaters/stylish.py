def make_value(diff) -> str:
    if diff is None:
        return 'null'

    if isinstance(diff, bool):
        string = str(diff)
        return string.lower()

    if isinstance(diff, int):
        return str(diff)

    if isinstance(diff, str):
        return diff

    return diff


def stylish(diff):

    # def inner(diff):

    result = '{'

    if not isinstance(diff, dict):
        return result + make_value(diff)

    keys = diff.keys()

    statuses = {
        'added': '  + ',
        'deleted': '  - ',
        'unchanged': '    ',
        'changed': '    ',
    }

    for key in keys:
        status = diff[key]['status']

        if status in statuses:


        if status == 'replaced':
            status = 'deleted'
            indent = status[key]
        key = 'added'
        indent = status[key]

        def
        for key in status.keys():
            indent = status[key]
            --> рекурсия
