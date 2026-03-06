from gendiff.utils import (
    is_added,
    is_removed,
    is_unchanged,
    json_format,
    parsing,
)


def generate_diff(path1, path2):
    file1, file2 = parsing(path1), parsing(path2)
    keys = sorted(set(file1.keys()) | set(file2.keys()))
    line = ['{']

    for k in keys:
        val1, val2 = json_format(file1.get(k)), json_format(file2.get(k))

        if is_unchanged(k, file1, file2):
            if file2[k] != file1[k]:
                line.append(f'  - {k}: {val1}')
                line.append(f'  + {k}: {val2}')
            else:
                line.append(f'    {k}: {val2}')

        elif is_added(k, file2):
            line.append(f'  + {k}: {val2}')

        elif is_removed(k, file2):
            line.append(f'  - {k}: {val1}')

    line.append('}\n')
    return '\n'.join(line)
