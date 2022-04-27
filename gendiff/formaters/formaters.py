from gendiff.formaters.stylish import get_stylish
from gendiff.formaters.plain import get_plain
from gendiff.formaters.json import get_json


def formater(diff, formater_str):

    formaters = {
        'stylish': get_stylish,
        'plain': get_plain,
        'json': get_json,
    }

    return formaters[formater_str](diff)
