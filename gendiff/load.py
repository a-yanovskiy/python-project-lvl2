import json
from os import path

import yaml


def load_file(filepath):
    file_extension = path.splitext(filepath)[1]
    if file_extension == '.json':
        file = json.load(open(filepath))
    elif file_extension == '.yaml' or file_extension == '.yml':
        file = yaml.safe_load(open(filepath))
    else:
        raise ValueError('Wrong extension!')
    return file
