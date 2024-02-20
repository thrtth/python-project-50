from gendiff.modules.get_formatter import get_formatter
from gendiff.modules.file_parser import parse_file
from gendiff.modules.get_diff import get_diff


def generate_diff(file_path1, file_path2, format_name='stylish'):
    formatter = get_formatter(format_name)
    file_data1 = parse_file(file_path1)
    file_data2 = parse_file(file_path2)
    return formatter(get_diff(file_data1, file_data2)).strip('\n')
