import json
from pathlib import Path

import yaml

""" MAIN """


def parsing(path):
    with open(path) as f:
        end = Path(path).suffix

        if end == '.json':
            return json.load(f)
        if end == '.yml' or '.yaml':
            return yaml.safe_load(f)


def format_value(val):
    if isinstance(val, bool):
        return str(val).lower()
    if val is None:
        return 'null'
    return str(val)


""" STYLISH """


def make_tab_status(status: str, tab):
    prefix = tab[:-2]
    tab_status = {
        'unchanged': f'{prefix}  ', 'added': f'{prefix}+ ',
        'removed': f'{prefix}- ', 'nested': tab,
        'changed': {'old': f'{prefix}- ', 'new': f'{prefix}+ '}}.get(status)
    if status == 'changed':
        return tab_status['old'], tab_status['new']
    return tab_status


def render_value(data, replacer=' ', spaces_count=4, depth=1):
    spaces_depth = spaces_count * depth
    TAB = f'{replacer * spaces_depth}'
    CLOSE_TAB = f'{replacer * (spaces_depth - spaces_count)}' + '}'
    res = [' {']

    if not isinstance(data, dict):
        if data == '':
            return ''
        return ' ' + format_value(data)

    for k, v in data.items():
        res.append(f'{TAB}{k}:{render_value(v, depth=depth + 1)}')

    res.append(CLOSE_TAB)
    return '\n'.join(res)


def stylish(data, replacer=' ', spaces_count=4, depth=1):
    spaces_depth = spaces_count * depth
    TAB = f'{replacer * spaces_depth}'
    CLOSE_TAB = f'{replacer * (spaces_depth - spaces_count)}' + '}'
    res = ['{']

    for i in data:
        status, key = i['status'], i['key']

        if status == 'changed':
            tab_old, tab_new = make_tab_status(status, TAB)
            res.append(
                f'{tab_old}{key}:{render_value(i["old"], depth=depth + 1)}\n'
                f'{tab_new}{key}:{render_value(i["new"], depth=depth + 1)}')
        elif status == 'nested':
            res.append(f'{make_tab_status(status, TAB)}{key}:'
                       f' {stylish(i["children"], depth=depth + 1)}')
        else:
            res.append(f'{make_tab_status(status, TAB)}{key}:'
                       f'{render_value(i["value"], depth=depth + 1)}')

    res.append(CLOSE_TAB)
    return '\n'.join(res)
