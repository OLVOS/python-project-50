from gendiff.const import TAB_STATUSES
from gendiff.utils import make_tab, render_value


def make_tab_status(status: str, tab):
    prefix = tab[:-2]
    if status == 'changed':
        return f'{prefix}{TAB_STATUSES[status]["old"]}', \
               f'{prefix}{TAB_STATUSES[status]["new"]}'
    return f'{prefix}{TAB_STATUSES[status]}'


def stylish(data, replacer=' ', spaces=4, depth=1):
    (TAB, CLOSE_TAB), res = make_tab(replacer, spaces, depth), ['{']
    render = render_value(replacer, spaces)

    for node in data:
        status, key, val = node['status'], node['key'], ''

        if status in ('added', 'removed', 'both'):
            val = render(node["value"], depth=depth + 1)

        elif status == 'nested':
            val = stylish(node["children"], depth=depth + 1)

        elif status == 'changed':
            tab_old, tab_new = make_tab_status(status, TAB)
            res.append(
                f'{tab_old}{key}: {render(node["old"], depth=depth + 1)}\n'
                f'{tab_new}{key}: {render(node["new"], depth=depth + 1)}')
            continue

        res.append(f'{make_tab_status(status, TAB)}{key}: {val}')

    res.append(CLOSE_TAB)
    return '\n'.join(res)
