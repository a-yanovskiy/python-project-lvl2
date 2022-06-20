from os import path


def load_file(filepath):
    extensions_list = ['.json', '.yaml', '.yml']
    extension = path.splitext(filepath)[1]
    if extension in extensions_list:
        return open(filepath), extension
    else:
        raise ValueError('Wrong extension!')
