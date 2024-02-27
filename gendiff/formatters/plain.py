class UnknownPlainType(Exception):
    pass


def to_plain(list_of_dicts, path_to_value=''):
    result = ''
    for item in list_of_dicts:
        item_type = item['type']
        new_path = (path_to_value + "." + item["key"]).strip('.')
        match item_type:
            case 'changed':
                result += (f"Property '{new_path}' was updated. "
                           f"From {value_to_plain(item['old_value'])} "
                           f"to {value_to_plain(item['new_value'])}\n")

            case 'added':
                result += (f"Property '{new_path}' "
                           f"was added with value: "
                           f"{value_to_plain(item['new_value'])}\n")

            case 'removed':
                result += f"Property '{new_path}' was removed\n"

            case 'nested':
                result += to_plain(item["value"], new_path)

            case 'unchanged':
                pass

            case _:
                raise UnknownPlainType(f'Unknown type for '
                                       f'plain formatter: {item_type}')
    return result


def value_to_plain(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool) or value is None:
        return bool_and_none_to_str(value)
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return value


def bool_and_none_to_str(val):
    if val is False:
        return 'false'
    elif val is True:
        return 'true'
    elif val is None:
        return 'null'
    return val
