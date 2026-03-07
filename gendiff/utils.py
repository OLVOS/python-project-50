import json
from pathlib import Path

import yaml


def parsing(path):
    with open(path) as f:
        end = Path(path).suffix

        if end == '.json':
            return json.load(f)
        if end == '.yml' or '.yaml':
            return yaml.safe_load(f)


def is_added(key, data): return key in data
def is_removed(key, data): return key not in data
def is_unchanged(key, data1, data2): return key in data1 and key in data2


def set_format(val): return json.dumps(val)
