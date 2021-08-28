import json
import yaml


def open_files(first_file, second_file):

    first_file_extension = first_file[first_file.rfind('.'):]
    second_file_extension = second_file[second_file.rfind('.'):]

    if first_file_extension != second_file_extension:
        raise Exception('У файлов разные форматы')
    else:
        if first_file_extension == '.json':
            file_1 = json.load(open(first_file))
            file_2 = json.load(open(second_file))
        elif first_file_extension == '.yaml' or first_file_extension == '.yml':
            file_1 = yaml.safe_load(open(first_file))
            file_2 = yaml.safe_load(open(second_file))
        return file_1, file_2
