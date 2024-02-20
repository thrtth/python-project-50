import json


def to_json(list_of_dicts):
    return json.dumps({'root': list_of_dicts})
