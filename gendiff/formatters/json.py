import json


def get_json(diff):
    return json.dumps(diff, indent=2, sort_keys=True)
