import json


def get_json(diff):
    str_diff = str(diff)
    replaced_quotes = str_diff.replace("\'", "\"")
    replaced_bools = (
        replaced_quotes.replace("True", "true")).replace("False", "false")
    replaced_nulls = replaced_bools.replace("None", "null")

    json_loads = json.loads(replaced_nulls)
    json_dumps = json.dumps(json_loads, indent=2, sort_keys=True)
    return json_dumps
