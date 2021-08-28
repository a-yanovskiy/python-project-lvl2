from gendiff.open_files import open_files
from gendiff.make_diff import make_diff


def generate_diff(first_file, second_file):

    files = open_files(first_file, second_file)
    file_1 = files[0]
    file_2 = files[1]

    print(make_diff(file_1, file_2))
