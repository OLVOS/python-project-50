from gendiff.utils import parsing


def generate_diff(path1, path2):
    file1, file2 = parsing(path1), parsing(path2)
    keys = sorted(set(file1.keys()) | set(file2.keys()))

    line = ['{']
    for k in keys:
        val1, val2 = file1.get(k), file2.get(k)

        if k in file2 and k in file1:
            if file2[k] != file1[k]:
                line.append(f'  - {k}: {val1}')
                line.append(f'  + {k}: {val2}')
            else:
                line.append(f'    {k}: {val2}')

        elif k in file2 and k not in file1:
            line.append(f'  + {k}: {val2}')
        elif k not in file2 and k in file1:
            line.append(f'  - {k}: {val1}')

    line.append('}')

    return '\n'.join(line)
