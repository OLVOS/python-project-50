from gendiff.CONST import tab_status
from gendiff.utils import format_value, make_tab


def make_tab_status(status: str, tab):
    prefix = tab[:-2]
    if status == 'changed':
        return f'{prefix}{tab_status[status]["old"]}', \
               f'{prefix}{tab_status[status]["new"]}'
    return f'{prefix}{tab_status[status]}'


def render_value(data, replacer=' ', spaces_count=4, depth=1):
    (TAB, CLOSE_TAB), res = make_tab(replacer, spaces_count, depth), [' {']

    if not isinstance(data, dict):
        return '' if data == '' else ' ' + format_value(data)

    for k, v in data.items():
        res.append(f'{TAB}{k}:{render_value(v, depth=depth + 1)}')

    res.append(CLOSE_TAB)
    return '\n'.join(res)


def stylish(data, replacer=' ', spaces_count=4, depth=1):
    (TAB, CLOSE_TAB), res = make_tab(replacer, spaces_count, depth), ['{']

    for i in data:
        status, key = i['status'], i['key']
        if status == 'changed':
            tab_old, tab_new = make_tab_status(status, TAB)
            res.append(
                f'{tab_old}{key}:{render_value(i["old"], depth=depth + 1)}\n'
                f'{tab_new}{key}:{render_value(i["new"], depth=depth + 1)}')

        elif status == 'nested':
            value = f' {stylish(i["children"], depth=depth + 1)}'
            res.append(f'{make_tab_status(status, TAB)}{key}:{value}')

        else:
            value = f'{render_value(i["value"], depth=depth + 1)}'
            res.append(f'{make_tab_status(status, TAB)}{key}:{value}')

    res.append(CLOSE_TAB)
    return '\n'.join(res)
