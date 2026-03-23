from json import dumps

from gendiff.utils import make_tab, render_value


def json(data, replacer=' ', spaces=2, depth=1):
    TAB, CLOSE_TAB = make_tab(replacer, spaces, depth)
    render = render_value(replacer, spaces, frmt=dumps)
    res = ['{']

    for index, node in enumerate(data):
        value, end = '', ',' if index < len(data) - 1 else ''
        if node['status'] in ('added', 'both'):
            value = render(node["value"], depth=depth + 1)
        elif node['status'] == 'changed':
            value = render(node["new"], depth=depth + 1)
        elif node['status'] == 'nested':
            value = json(node["children"], depth=depth + 1)
        elif node['status'] == 'removed':
            continue

        res.append(f'{TAB}{render(node["key"])}: {value}{end}')

    res.append(CLOSE_TAB)
    return '\n'.join(res)

