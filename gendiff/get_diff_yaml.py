def change_value(key, value, sign='    '):

    if sign == '+':
        sign = '  + '
    elif sign == '-':
        sign = '  - '

    return str(sign + str(key) + ': ' + str(value) + '\n')


def get_diff_yaml(file_1, file_2, all_keys):

    result = ''

    for key in all_keys:
        if key in file_1 and key in file_2:
            if file_1[key] == file_2[key]:
                result += change_value(key, file_1.get(key))
            else:
                result += change_value(key, file_1.get(key), '-')
                result += change_value(key, file_2.get(key), '+')
        else:
            if key in file_1:
                result += change_value(key, file_1.get(key), '-')
            if key in file_2:
                result += change_value(key, file_2.get(key), '+')
    result = '{\n' + result + '}\n'
    return result
