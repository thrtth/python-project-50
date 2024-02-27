from gendiff.formatters.stylish import to_stylish
from gendiff.formatters.plain import to_plain
from gendiff.formatters.json import to_json


class WrongFormat(Exception):
    pass


def get_formatter(format_name):
    if format_name == 'plain':
        formatter = to_plain
    elif format_name == 'stylish':
        formatter = to_stylish
    elif format_name == 'json':
        formatter = to_json
    else:
        raise WrongFormat(f'Wrong format: {format_name}')
    return formatter
