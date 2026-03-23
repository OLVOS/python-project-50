from pathlib import Path

import pytest

from gendiff import generate_diff


@pytest.fixture
def get_path():
    def inner(test_filename):
        return Path(__file__).parent / 'test_data' / test_filename
    return inner


@pytest.fixture
def expected():
    def inner(expected_file='expected.txt'):
        path = Path(__file__).parent / 'test_data' / expected_file
        return path.read_text()
    return inner


def test_gendiff_json(get_path, expected):
    f1, f2 = get_path('file1.json'), get_path('file2.json')
    assert generate_diff(f1, f2, 'stylish') == expected()


def test_gendiff_yml(get_path, expected):
    f1, f2 = get_path('filepath1.yml'), get_path('filepath2.yml')
    assert generate_diff(f1, f2, 'stylish') == expected()


def test_gendiff_format_plain(get_path, expected):
    f1, f2 = get_path('filepath1.yml'), get_path('filepath2.yml')
    assert generate_diff(f1, f2, 'plain') == expected('expected_plain.txt')


def test_gendiff_format_json(get_path, expected):
    f1, f2 = get_path('filepath1.yml'), get_path('filepath2.yml')
    assert generate_diff(f1, f2, 'json') == expected('expected_json.txt')
