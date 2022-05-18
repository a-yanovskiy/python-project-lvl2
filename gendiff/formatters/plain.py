def get_plain(diff):
    return make_plain(diff)[:-1]


def make_value(diff) -> str:
    if isinstance(diff, dict):
        return '[complex value]'

    if diff is None:
        return "null"

    if isinstance(diff, bool):
        string = str(diff)
        return string.lower()

    if isinstance(diff, int):
        return str(diff)

    if isinstance(diff, str):
        return f"'{diff}'"

    return diff


def make_plain(diff):
    def inner(node, save_key):

        if not isinstance(node, dict):
            return make_value(node)

        property = ""

        keys = node.keys()

        for key in keys:
            type = node[key]["type"]
            body1 = node[key]["body1"]

            if type == "changed":

                save_key += str(key) + '.'
                property += inner(body1, save_key)
                if key in save_key.split('.'):
                    save_key = save_key.replace(f'{key}.', "")
                else:
                    save_key = ""

            else:
                body1 = make_value(body1)
                if type == 'replaced':
                    body2 = node[key]["body2"]
                    body2 = make_value(body2)
                    property += f"Property '{save_key}{key}' \
was updated. From {body1} to {body2}\n"

                elif type == 'added':
                    property += f"Property '{save_key}{key}' \
was added with value: {body1}\n"

                elif type == 'deleted':
                    property += f"Property '{save_key}{key}' was removed\n"

                else:
                    continue

        return property

    return inner(diff, save_key="")
