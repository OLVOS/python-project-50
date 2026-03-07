import json


def parsing(path):
    with open(path) as f:
        return json.load(f)


def is_added(key, data): return key in data
def is_removed(key, data): return key not in data
def is_unchanged(key, data1, data2): return key in data1 and key in data2


def json_format(val): return json.dumps(val)
