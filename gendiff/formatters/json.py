import json


def get_json(diff):
    diff = str(diff)
    diff = diff.replace("\'", "\"")
    diff = diff.replace("True", "true")
    diff = diff.replace("False", "false")
    diff = diff.replace("None", "null")

    result = json.loads(diff)
    result = json.dumps(result, indent=2, sort_keys=True)
    return result
