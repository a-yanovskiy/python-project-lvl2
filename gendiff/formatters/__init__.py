"""__init__.py."""
from gendiff.formatters.json import get_json
from gendiff.formatters.plain import get_plain
from gendiff.formatters.stylish import get_stylish


def format_diff(diff, formatter_str):
    formatters = {
        'stylish': get_stylish,
        'plain': get_plain,
        'json': get_json,
    }

    return formatters[formatter_str](diff)
