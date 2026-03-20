from gendiff.formatters import plain, stylish
from gendiff.utils import parsing


def generate_diff(path1, path2, format_name='stylish'):
    file1, file2 = parsing(path1), parsing(path2)

    def build_diff(f1, f2):
        line, keys = [], sorted(set(f1.keys()) | set(f2.keys()))

        for k in keys:
            if is_added(k, f1, f2):
                line.append(added_format(k, f2))
            elif is_removed(k, f1, f2):
                line.append(removed_format(k, f1))
            elif is_nested(k, f1, f2):
                line.append(nested_format(k, f1, f2, build_diff))
            elif is_changed(k, f1, f2):
                line.append(changed_format(k, f1, f2))
            else:
                line.append(both_format(k, f2))

        return line

    if format_name == 'stylish':
        return stylish(build_diff(file1, file2))
    if format_name == 'plain':
        return plain(build_diff(file1, file2))


def is_both(key, data1, data2): return\
        key in data1 and key in data2
def is_added(key, data1, data2): return\
        key in data2 and key not in data1
def is_removed(key, data1, data2): return\
        key not in data2 and key in data1
def is_changed(key, data1, data2): return\
        is_both(key, data1, data2) and data1[key] != data2[key]
def is_nested(key, data1, data2): return\
        isinstance(data1[key], dict) and isinstance(data2[key], dict)


def both_format(k, f2): return {
    'status': 'unchanged', 'key': k, 'value': f2[k]}
def added_format(k, f2): return {
    'status': 'added', 'key': k, 'value': f2[k]}
def removed_format(k, f1): return {
    'status': 'removed', 'key': k, 'value': f1[k]}
def changed_format(k, f1, f2): return {
    'status': 'changed', 'key': k, 'old': f1[k], 'new': f2[k]}
def nested_format(k, f1, f2, make_tree): return {
    'status': 'nested', 'key': k, 'children': make_tree(f1[k], f2[k])}
