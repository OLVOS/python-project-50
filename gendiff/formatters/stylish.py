from gendiff.const import TAB_STATUSES
from gendiff.utils import make_tabs, render_value


def make_tab_status(status: str, tab):
    prefix = tab[:-2]
    if status == 'changed':
        return f'{prefix}{TAB_STATUSES[status]["old"]}', \
               f'{prefix}{TAB_STATUSES[status]["new"]}'
    return f'{prefix}{TAB_STATUSES[status]}'


def stylish(data, replacer=' ', spaces=4, depth=1):
    (tab, close_tab), res = make_tabs(replacer, spaces, depth), ['{']

    for node in data:
        status, key, val = node['status'], node['key'], ''

        if status in ('added', 'removed', 'both'):
            val = render_value(node["value"], depth=depth + 1)

        elif status == 'nested':
            val = stylish(node["children"], depth=depth + 1)

        elif status == 'changed':
            tab_old, tab_new = make_tab_status(status, tab)
            val_old = render_value(node["old"], depth=depth + 1)
            val_new = render_value(node["new"], depth=depth + 1)
            res.append(f'{tab_old}{key}: {val_old}\n'
                       f'{tab_new}{key}: {val_new}')
            continue

        res.append(f'{make_tab_status(status, tab)}{key}: {val}')

    res.append(close_tab)
    return '\n'.join(res)
