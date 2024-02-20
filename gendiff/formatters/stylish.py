from gendiff.formatters.common import bool_and_none_to_str

INDENT = 4


def to_stylish(list_of_dicts, depth=0):
    result = '{\n'
    for item in list_of_dicts:
        item_type = item['type']
        match item_type:
            case 'unchanged':
                value = value_to_stylish(item["value"], depth)
                result += f'{" " * depth}    {item["key"]}: {value}\n'

            case 'changed':
                old_value = value_to_stylish(item["old_value"], depth)
                new_value = value_to_stylish(item["new_value"], depth)
                result += f'{" " * depth}  - {item["key"]}: {old_value}\n'
                result += f'{" " * depth}  + {item["key"]}: {new_value}\n'

            case 'added':
                new_value = value_to_stylish(item["new_value"], depth)
                result += f'{" " * depth}  + {item["key"]}: {new_value}\n'

            case 'removed':
                old_value = value_to_stylish(item["old_value"], depth)
                result += f'{" " * depth}  - {item["key"]}: {old_value}\n'

            case 'nested':
                result += (f'{" " * depth}    {item["key"]}:'
                           f' {to_stylish(item["value"], depth + INDENT)}\n')

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
            result += (f'{" " * depth}    {key}:'
                       f' {dict_to_str(some_dict[key], depth + INDENT)}\n')
        else:
            value = value_to_stylish(some_dict[key], depth)
            result += f'{" " * depth}    {key}: {value}\n'
    result += ' ' * depth + '}'
    return result
