from gendiff.utils import format_plain


def plain(data, path=''):
    res = []

    for node in data:
        curr_path = path + node['key']
        value = format_plain(node['value']) if 'value' in node else ''

        if node['status'] == 'nested':
            res.append(plain(node['children'], path=f'{curr_path}.'))

        elif node['status'] == 'added':
            res.append(f"Property '{curr_path}' was added with value: {value}")

        elif node['status'] == 'removed':
            res.append(f"Property '{curr_path}' was removed")

        elif node['status'] == 'changed':
            old, new = format_plain(node['old']), format_plain(node['new'])
            res.append(
                f"Property '{curr_path}' was updated. From {old} to {new}")

    return '\n'.join(res)
