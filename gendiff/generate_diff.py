import json


def generate_diff(first_file, second_file):
    file_1 = json.load(open(first_file))
    file_2 = json.load(open(second_file))

    merged_dict = {**file_1, **file_2}
    list_keys = list(merged_dict.keys())
    list_keys.sort()

    result = []

    for i in list_keys:
        if i in file_1 and i in file_2:
            if file_1[i] == file_2[i]:
                result.append(
                    str('  ' + str(i) + ': ' + file_1.get(i)))
            else:
                result.append(
                    str('- ' + str(i) + ': ' + str(file_1.get(i))))
                result.append(
                    str("+ " + str(i) + ': ' + str(file_2.get(i))))
        else:
            if i in file_1:
                result.append(
                    str('- ' + str(i) + ': ' + str(file_1.get(i))))
            if i in file_2:
                result.append(
                    str('+ ' + str(i) + ': ' + str(file_2.get(i))))
    return result
