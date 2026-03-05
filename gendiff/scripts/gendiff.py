import argparse
from gendiff.utils import parsing


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',

    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    data1 = parsing(args.first_file)
    data2 = parsing(args.second_file)
    print(data1)
    print(data2)


if __name__ == '__main__':
    main()
