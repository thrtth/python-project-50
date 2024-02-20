import json
from os import path
import yaml


def parse_file(file_path):
    extension = path.splitext(file_path)[1]
    file_data = None
    if extension == '.json':
        file_data = json.load(open(file_path))
    elif extension == '.yml' or extension == '.yaml':
        file_data = yaml.safe_load(open(file_path))
    return file_data
