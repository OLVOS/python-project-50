import argparse

from gendiff.generate_diff import generate_diff
from gendiff.parser import parsing


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',

    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='stylish',
                        help='set format of output')

    args = parser.parse_args()
    diff = generate_diff(
        parsing(args.first_file),
        parsing(args.second_file),
        args.format
    )
    print(diff)


if __name__ == '__main__':
    main()
