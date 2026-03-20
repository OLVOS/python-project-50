from gendiff.utils import format_plain_val


def plain(data, path=''):
    res = []

    for i in data:
        curr_path = path + i['key']
        value = format_plain_val(i['value']) if 'value' in i else ''

        if i['status'] == 'nested':
            res.append(plain(i['children'], path=f'{path + i["key"]}' + '.'))

        elif i['status'] == 'added':
            res.append(f"Property '{curr_path}' was added with value: {value}")

        elif i['status'] == 'removed':
            res.append(f"Property '{curr_path}' was removed")

        elif i['status'] == 'changed':
            old, new = format_plain_val(i['old']), format_plain_val(i['new'])
            res.append(
                f"Property '{curr_path}' was updated. From {old} to {new}")

    return '\n'.join(res)
