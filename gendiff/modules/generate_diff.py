import json
from os import path
import yaml


INDENT = 4


def bool_and_none_to_str(val):
    if val is False:
        return 'false'
    elif val is True:
        return 'true'
    elif val is None:
        return 'null'
    return val


def parse_file(file_path):
    extension = path.splitext(file_path)[1]
    file_data = None
    if extension == '.json':
        file_data = json.load(open(file_path))
    elif extension == '.yml' or extension == '.yaml':
        file_data = yaml.safe_load(open(file_path))
    return file_data


def generate_diff(file_path1, file_path2, output_format):
    formater = globals()[output_format]
    file_data1 = parse_file(file_path1)
    file_data2 = parse_file(file_path2)
    return formater(get_diff(file_data1, file_data2))


def is_dict(node):
    return type(node) is dict


def get_diff(dict1, dict2):
    result = []
    sorted_keys = sorted(set(list(dict1.keys()) + list(dict2.keys())))
    for key in sorted_keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)
        if key not in dict1:
            result.append({'key': key,
                           'type': 'added',
                           'new_value': value2})

        elif key not in dict2:
            result.append({'key': key,
                           'type': 'removed',
                           'old_value': value1})

        elif is_dict(value1) and is_dict(value2):
            children = get_diff(value1, value2)
            result.append({'key': key,
                           'type': 'nested',
                           'value': children})

        elif value1 == value2:
            result.append({'key': key,
                           'type': 'unchanged',
                           'value': value1})

        elif value1 != value2:
            result.append({'key': key,
                           'type': 'changed',
                           'old_value': value1,
                           'new_value': value2})

    return result


def stylish(list_of_dicts, depth=0):
    result = '{\n'
    for item in list_of_dicts:
        item_type = item['type']
        if item_type == 'unchanged':
            value = value_to_str(item["value"], depth)
            result += f'{" " * depth}    {item["key"]}: {value}\n'

        elif item_type == 'changed':
            old_value = value_to_str(item["old_value"], depth)
            new_value = value_to_str(item["new_value"], depth)
            result += f'{" " * depth}  - {item["key"]}: {old_value}\n'
            result += f'{" " * depth}  + {item["key"]}: {new_value}\n'

        elif item_type == 'added':
            new_value = value_to_str(item["new_value"], depth)
            result += f'{" " * depth}  + {item["key"]}: {new_value}\n'

        elif item_type == 'removed':
            old_value = value_to_str(item["old_value"], depth)
            result += f'{" " * depth}  - {item["key"]}: {old_value}\n'

        elif item_type == 'nested':
            result += (f'{" " * depth}    {item["key"]}:'
                       f' {stylish(item["value"], depth + INDENT)}\n')

    result += ' ' * depth + '}'
    return result


def dict_to_str(some_dict, depth):
    result = '{\n'
    dict_keys = some_dict.keys()
    for key in dict_keys:
        if is_dict(some_dict[key]):
            result += (f'{" " * depth}    {key}:'
                       f' {dict_to_str(some_dict[key], depth + INDENT)}\n')
        else:
            value = value_to_str(some_dict[key], depth)
            result += f'{" " * depth}    {key}: {value}\n'
    result += ' ' * depth + '}'
    return result


def value_to_str(value, depth):
    if is_dict(value):
        return dict_to_str(value, depth + INDENT)
    return bool_and_none_to_str(value)
