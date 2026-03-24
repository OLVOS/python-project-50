import json
from pathlib import Path

import yaml


def parsing(path):
    with open(path) as f:
        end = Path(path).suffix

        if end == '.json':
            return json.load(f)
        if end in ('.yml', '.yaml'):
            return yaml.safe_load(f)


def make_tab(replacer=' ', spaces=4, depth=1):
    spaces_depth = spaces * depth
    TAB = f'{replacer * spaces_depth}'
    CLOSE_TAB = f'{replacer * (spaces_depth - spaces)}' + '}'
    return TAB, CLOSE_TAB


def format_value(val):
    if isinstance(val, bool):
        return str(val).lower()
    if val is None:
        return 'null'
    return str(val)


def format_plain(value):
    if isinstance(value, dict):
        return '[complex value]'
    return f"'{value}'" if isinstance(value, str) else format_value(value)


def render_value(replacer=' ', spaces=4, frmt=format_value):

    def make_render(data, depth=1):
        (TAB, CLOSE_TAB), res = make_tab(replacer, spaces, depth), ['{']

        if not isinstance(data, dict):
            return frmt(data)

        for k, v in data.items():
            value = make_render(v, depth=depth + 1)
            res.append(f'{TAB}{k}: {value}')

        res.append(CLOSE_TAB)
        return '\n'.join(res)

    return make_render
