INDENT = 4
ADDED_SIGN = '+'
REMOVED_SIGN = '-'


class UnknownStylishType(Exception):
    pass


def to_stylish(list_of_dicts, depth=0):
    result = '{\n'
    for item in list_of_dicts:
        item_type = item['type']
        match item_type:
            case 'unchanged':
                value = value_to_stylish(item["value"], depth)
                result += f'{get_indent(depth)}{item["key"]}: {value}\n'

            case 'changed':
                old_value = value_to_stylish(item["old_value"], depth)
                new_value = value_to_stylish(item["new_value"], depth)
                result += (f'{get_indent(depth, REMOVED_SIGN)}'
                           f'{item["key"]}: {old_value}\n')
                result += (f'{get_indent(depth, ADDED_SIGN)}'
                           f'{item["key"]}: {new_value}\n')

            case 'added':
                new_value = value_to_stylish(item["new_value"], depth)
                result += (f'{get_indent(depth, ADDED_SIGN)}'
                           f'{item["key"]}: {new_value}\n')

            case 'removed':
                old_value = value_to_stylish(item["old_value"], depth)
                result += (f'{get_indent(depth, REMOVED_SIGN)}'
                           f'{item["key"]}: {old_value}\n')

            case 'nested':
                result += (f'{get_indent(depth)}{item["key"]}:'
                           f' {to_stylish(item["value"], depth + INDENT)}\n')

            case _:
                raise UnknownStylishType(f'Unknown type for '
                                         f'stylish formatter: {item_type}')

    result += ' ' * depth + '}'
    return result


def value_to_stylish(value, depth):
    if isinstance(value, dict):
        return dict_to_str(value, depth + INDENT)
    return bool_and_none_to_str(value)


def dict_to_str(some_dict, depth):
    result = '{\n'
    dict_keys = some_dict.keys()
    for key in dict_keys:
        if isinstance(some_dict[key], dict):
            result += (f'{get_indent(depth)}{key}:'
                       f' {dict_to_str(some_dict[key], depth + INDENT)}\n')
        else:
            value = value_to_stylish(some_dict[key], depth)
            result += f'{get_indent(depth)}{key}: {value}\n'
    result += ' ' * depth + '}'
    return result


def bool_and_none_to_str(val):
    if val is False:
        return 'false'
    elif val is True:
        return 'true'
    elif val is None:
        return 'null'
    return val


def get_indent(depth, sign=' '):
    return f'{" " * depth}{" " * (INDENT - 2)}{sign} '
