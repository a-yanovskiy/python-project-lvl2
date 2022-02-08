from gendiff.formaters.stylish import get_stylish
from gendiff.formaters.plain import get_plain


def formater(diff, formater_str):

    formaters = {
        'stylish': get_stylish,
        'plain': get_plain,
    }

    return formaters[formater_str](diff)
