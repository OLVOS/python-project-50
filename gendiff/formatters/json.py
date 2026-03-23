from json import dumps


def json(data, spaces=2):

    def build_dict(n):
        res = {}

        for node in n:
            key, status = node['key'], node['status']
            if status in ('added', 'both'):
                res[key] = node['value']
            elif status == 'changed':
                res[key] = node['new']
            elif status == 'nested':
                res[key] = build_dict(node['children'])
            elif status == 'removed':
                continue

        return res

    return dumps(build_dict(data), indent=spaces)
