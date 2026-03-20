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


def make_tab(replacer, spaces_count, depth):
    spaces_depth = spaces_count * depth
    TAB = f'{replacer * spaces_depth}'
    CLOSE_TAB = f'{replacer * (spaces_depth - spaces_count)}' + '}'
    return TAB, CLOSE_TAB


def format_value(val):
    if isinstance(val, bool):
        return str(val).lower()
    if val is None:
        return 'null'
    return str(val)


def format_plain_val(value):
    val = f"'{value}'" if isinstance(value, str) else format_value(value)
    return '[complex value]' if isinstance(value, dict) else val

