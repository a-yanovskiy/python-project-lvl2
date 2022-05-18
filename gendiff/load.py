import json

import yaml


def load_files_by_ext(file_1, file_2, ext='json'):
    if ext == 'json':
        file_1 = json.load(open(file_1))
        file_2 = json.load(open(file_2))
    elif ext == 'yaml' or ext == 'yml':
        file_1 = yaml.safe_load(open(file_1))
        file_2 = yaml.safe_load(open(file_2))
    return file_1, file_2
