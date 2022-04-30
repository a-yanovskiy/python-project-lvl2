from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import get_plain
from gendiff.formatters.json import get_json


def formatter(diff, formatter_str):

    formatters = {
        'stylish': get_stylish,
        'plain': get_plain,
        'json': get_json,
    }

    return formatters[formatter_str](diff)
