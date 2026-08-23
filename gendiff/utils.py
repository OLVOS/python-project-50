

def make_tabs(replacer=' ', spaces=4, depth=1):
    spaces_depth = spaces * depth
    tab = replacer * spaces_depth
    close_tab = replacer * (spaces_depth - spaces) + '}'
    return tab, close_tab


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


def render_value(data, replacer=' ', spaces=4, depth=1, frmt=format_value):
    (tab, close_tab), res = make_tabs(replacer, spaces, depth), ['{']

    if not isinstance(data, dict):
        return frmt(data)

    for k, v in data.items():
        value = render_value(v, depth=depth + 1)
        res.append(f'{tab}{k}: {value}')

    res.append(close_tab)
    return '\n'.join(res)

