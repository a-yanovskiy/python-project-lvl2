from os import path

from gendiff.load import load_files_by_ext


def compare_ext(first_file, second_file):
    first_file_extension = path.splitext(first_file)[1]
    second_file_extension = path.splitext(second_file)[1]

    if first_file_extension != second_file_extension:
        raise Exception('Files have different formats')
    else:
        return load_files_by_ext(first_file, second_file, first_file_extension)
