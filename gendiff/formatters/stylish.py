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
    types = {
        "added": "+ ",
        "deleted": "- ",
        "unchanged": "  ",
        "changed": "  ",
    }

    def inner(node, depth):

        if not isinstance(node, dict):
            return make_value(node)

        nonlocal types
        result = "{"
        indent = "  " * depth

        keys = node.keys()

        for key in keys:
            type = node[key]["type"]
            body1 = node[key]["body1"]

            if type == "replaced":
                result += ("\n" + indent + types["deleted"] + key + ": "
                           + inner(body1, depth + 2))

                body2 = node[key]["body2"]
                result += ("\n" + indent + types["added"] + key + ": "
                           + inner(body2, depth + 2))
            else:
                result += ("\n" + indent + types[type] + key + ": "
                           + inner(body1, depth + 2))

        return result + "\n" + indent[:-2] + "}"

    return inner(diff, 1)
