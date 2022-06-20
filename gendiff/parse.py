import json

import yaml


def parse(data, format):
    if format == '.json':
        return json.load(data)
    if format == '.yaml' or format == '.yml':
        return yaml.safe_load(data)
