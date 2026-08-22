from gendiff.formatters import json, plain, stylish

FORMATTERS = {'stylish': stylish, 'plain': plain, 'json': json}


def generate_diff(data1, data2, format_name='stylish'):

    def build_diff(d1, d2):
        nodes, keys = [], sorted(set(d1.keys()) | set(d2.keys()))

        for k in keys:
            if is_added(k, d1, d2):
                nodes.append(added_format(k, d2))

            elif is_removed(k, d1, d2):
                nodes.append(removed_format(k, d1))

            elif is_nested(k, d1, d2):
                nodes.append(nested_format(k, d1, d2, build_diff))

            elif is_changed(k, d1, d2):
                nodes.append(changed_format(k, d1, d2))

            elif is_both(k, d1, d2):
                nodes.append(both_format(k, d2))

        return nodes

    return FORMATTERS[format_name](build_diff(data1, data2))


def is_both(key, data1, data2): return (
        key in data1 and key in data2)
def is_added(key, data1, data2): return (
        key in data2 and key not in data1)
def is_removed(key, data1, data2): return (
        key not in data2 and key in data1)
def is_changed(key, data1, data2): return (
        is_both(key, data1, data2) and data1[key] != data2[key])
def is_nested(key, data1, data2): return (
        is_both(key, data1, data2)
        and isinstance(data1[key], dict) and isinstance(data2[key], dict))


def both_format(k, f2): return {
    'status': 'both', 'key': k, 'value': f2[k]}
def added_format(k, f2): return {
    'status': 'added', 'key': k, 'value': f2[k]}
def removed_format(k, f1): return {
    'status': 'removed', 'key': k, 'value': f1[k]}
def changed_format(k, f1, f2): return {
    'status': 'changed', 'key': k, 'old': f1[k], 'new': f2[k]}
def nested_format(k, f1, f2, make_tree): return {
    'status': 'nested', 'key': k, 'children': make_tree(f1[k], f2[k])}
