from pathlib import Path

import pytest

from gendiff import generate_diff
from gendiff.parser import parsing


@pytest.fixture
def get_path():
    def inner(test_filename):
        return parsing(Path(__file__).parent / 'test_data' / test_filename)
    return inner


@pytest.fixture
def expected():
    def inner(expected_file):
        path = Path(__file__).parent / 'test_data' / expected_file
        return path.read_text()
    return inner


def test_gendiff_input_file_types(get_path, expected):
    f1_json, f2_json = get_path('file1.json'), get_path('file2.json')
    f1_yaml, f2_yaml = get_path('filepath1.yml'), get_path('filepath2.yml')
    expected_result = expected('expected_stylish.txt')

    assert generate_diff(f1_json, f2_json) == expected_result
    assert generate_diff(f1_yaml, f2_yaml) == expected_result


def test_gendiff_format_plain(get_path, expected):
    f1, f2 = get_path('filepath1.yml'), get_path('filepath2.yml')
    expected_result = expected('expected_plain.txt')

    assert generate_diff(f1, f2, 'plain') == expected_result


def test_gendiff_format_json(get_path, expected):
    f1, f2 = get_path('filepath1.yml'), get_path('filepath2.yml')
    expected_result = expected('expected_json.txt')

    assert generate_diff(f1, f2, 'json') == expected_result
