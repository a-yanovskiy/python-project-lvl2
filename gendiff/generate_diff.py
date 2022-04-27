from gendiff.open_files import open_files
from gendiff.make_diff import make_diff
from gendiff.formaters.formaters import formater


def generate_diff(first_file, second_file, format='stylish'):

    files = open_files(first_file, second_file)
    file_1 = files[0]
    file_2 = files[1]

    diff = make_diff(file_1, file_2)

    return formater(diff, format)
