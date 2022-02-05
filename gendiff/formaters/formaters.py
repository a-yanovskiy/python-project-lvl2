from gendiff.formaters import stylish


def formater(diff, formater_str):

    formater = getattr(stylish, formater_str)

    return formater(diff)
