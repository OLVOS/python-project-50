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


def format_plain_val(value):
    val = f"'{value}'" if isinstance(value, str) else format_value(value)
    return '[complex value]' if isinstance(value, dict) else val


def render_value(replacer=' ', spaces=4, frmt=format_value):

    def make_render(data, depth=1, end=''):
        (TAB, CLOSE_TAB), res = make_tab(replacer, spaces, depth), ['{']

        if not isinstance(data, dict):
            return '' if data == '' else frmt(data)

        for index, (k, v) in enumerate(data.items()):
            if frmt.__name__ == 'dumps':
                end = ',' if index < len(data) - 1 else ''
            res.append(
                f'{TAB}{frmt(k)}: {make_render(v, depth=depth + 1)}{end}')

        res.append(CLOSE_TAB)
        return '\n'.join(res)

    return make_render
