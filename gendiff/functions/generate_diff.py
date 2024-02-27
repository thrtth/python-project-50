from gendiff.functions.get_formatter import get_formatter
from gendiff.functions.file_parser import parse_file
from gendiff.functions.get_diff import get_diff
from gendiff.functions.file_parser import NotSupportedExt
from gendiff.functions.get_formatter import WrongFormat
from gendiff.formatters.stylish import UnknownStylishType
from gendiff.formatters.plain import UnknownPlainType


def generate_diff(file_path1, file_path2, format_name='stylish'):
    try:
        formatter = get_formatter(format_name)
        file_data1 = parse_file(file_path1)
        file_data2 = parse_file(file_path2)
        return formatter(get_diff(file_data1, file_data2)).strip('\n')
    except (NotSupportedExt,
            WrongFormat,
            UnknownStylishType,
            UnknownPlainType) as error:
        print(error)
