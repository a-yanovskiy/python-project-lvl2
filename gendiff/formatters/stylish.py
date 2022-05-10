def make_value(diff) -> str:
    if diff is None:
        return "null"

    if isinstance(diff, bool):
        string = str(diff)
        return string.lower()

    if isinstance(diff, int):
        return str(diff)

    if isinstance(diff, str):
        return diff

    return diff


def get_stylish(diff):
    statuses = {
        "added": "+ ",
        "deleted": "- ",
        "unchanged": "  ",
        "changed": "  ",
    }

    def inner(node, depth):

        if not isinstance(node, dict):
            return make_value(node)

        nonlocal statuses
        result = "{"
        indent = "  " * depth

        keys = node.keys()

        for key in keys:
            status = node[key]["status"]
            body1 = node[key]["body1"]

            if status == "replaced":
                result += ("\n" + indent + statuses["deleted"] + key + ": "
                           + inner(body1, depth + 2))

                body2 = node[key]["body2"]
                result += ("\n" + indent + statuses["added"] + key + ": "
                           + inner(body2, depth + 2))
            else:
                result += ("\n" + indent + statuses[status] + key + ": "
                           + inner(body1, depth + 2))

        return result + "\n" + indent[:-2] + "}"

    return inner(diff, 1)
