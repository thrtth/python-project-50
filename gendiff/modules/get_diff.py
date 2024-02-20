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
