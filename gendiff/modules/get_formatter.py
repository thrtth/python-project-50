from gendiff.formatters.stylish import to_stylish
from gendiff.formatters.plain import to_plain
from gendiff.formatters.json import to_json


def get_formatter(format_name):
    formatter = to_stylish
    if format_name == 'plain':
        formatter = to_plain
    elif format_name == 'json':
        formatter = to_json
    return formatter
