import json


def bool_to_lowercase(val):
    if val is False:
        return 'false'
    elif val is True:
        return 'true'
    return val


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    json_keys = sorted(set(list(file1.keys()) + list(file2.keys())))
    result_str = '{\n'
    for key in json_keys:
        val1 = bool_to_lowercase(file1.get(key))
        val2 = bool_to_lowercase(file2.get(key))
        if val1 is not None and val2 is not None:
            if val1 == val2:
                result_str += f'    {key}: {val1}\n'
            else:
                result_str += f'  - {key}: {val1}\n'
                result_str += f'  + {key}: {val2}\n'
        else:
            if val2 is None:
                result_str += f'  - {key}: {val1}\n'
            else:
                result_str += f'  + {key}: {val2}\n'
    result_str += '}'
    return result_str
