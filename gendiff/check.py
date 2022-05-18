from gendiff.load import load_files_by_ext


def check_ext(first_file, second_file):
    first_file_extension = first_file[first_file.rfind('.'):][1:]
    second_file_extension = second_file[second_file.rfind('.'):][1:]

    if first_file_extension != second_file_extension:
        raise Exception('Files have different formats')
    else:
        return load_files_by_ext(first_file, second_file, first_file_extension)
