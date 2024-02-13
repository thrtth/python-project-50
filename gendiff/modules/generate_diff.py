import json
from os import path
import yaml
from gendiff.formatters.formatters import to_stylish
from gendiff.formatters.formatters import to_plain
from gendiff.formatters.formatters import to_json


def parse_file(file_path):
    extension = path.splitext(file_path)[1]
    file_data = None
    if extension == '.json':
        file_data = json.load(open(file_path))
    elif extension == '.yml' or extension == '.yaml':
        file_data = yaml.safe_load(open(file_path))
    return file_data


def generate_diff(file_path1, file_path2, format_name):
    formatter = get_formatter(format_name)
    file_data1 = parse_file(file_path1)
    file_data2 = parse_file(file_path2)
    return formatter(get_diff(file_data1, file_data2)).strip('\n')


def get_formatter(format_name):
    formatter = to_stylish
    if format_name == 'plain':
        formatter = to_plain
    elif format_name == 'json':
        formatter = to_json
    return formatter


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

        elif isinstance(value1, dict) and isinstance(value2, dict):
            children = get_diff(value1, value2)
            result.append({'key': key,
                           'type': 'nested',
                           'value': children})

        elif value1 == value2:
            result.append({'key': key,
                           'type': 'unchanged',
                           'value': value1})

        else:
            result.append({'key': key,
                           'type': 'changed',
                           'old_value': value1,
                           'new_value': value2})

    return result
