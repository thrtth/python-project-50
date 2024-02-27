import json
from os import path
import yaml


class NotSupportedExt(Exception):
    pass


def parse_file(file_path):
    extension = path.splitext(file_path)[1]
    file = open(file_path)
    return parse(file, extension)


def parse(file, extension):
    if extension == '.json':
        file_data = json.load(file)
    elif extension == '.yml' or extension == '.yaml':
        file_data = yaml.safe_load(file)
    else:
        raise NotSupportedExt(f'File format not supported: {extension}')
    return file_data
