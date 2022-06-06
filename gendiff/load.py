import json
from os import path

import yaml


def check_extension(filepath):
    extensions_list = ['.json', '.yaml', '.yml']
    extension = path.splitext(filepath)[1]
    if extension in extensions_list:
        return extension
    else:
        raise ValueError('Wrong extension!')


def load_file(filepath):
    file_extension = check_extension(filepath)
    if file_extension == '.json':
        return json.load(open(filepath))
    if file_extension == '.yaml' or file_extension == '.yml':
        return yaml.safe_load(open(filepath))
