from os import path

from gendiff.load import load_file


def compare_ext(first_file, second_file):
    first_file_extension = path.splitext(first_file)[1]
    second_file_extension = path.splitext(second_file)[1]

    if first_file_extension != second_file_extension:
        raise Exception('Files have different formats')
    else:
        file_1 = load_file(first_file, first_file_extension)
        file_2 = load_file(second_file, second_file_extension)
        return file_1, file_2
