import json

import yaml


def load_file(file, ext):
    if ext == '.json':
        file = json.load(open(file))
    elif ext == '.yaml' or ext == '.yml':
        file = yaml.safe_load(open(file))
    else:
        raise ValueError('Wrong extension!')
    return file
