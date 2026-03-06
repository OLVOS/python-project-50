from pathlib import Path

import pytest

from gendiff import generate_diff


@pytest.fixture
def get_path():
    def inner(filename):
        return Path(__file__).parent / 'test_data' / filename
    return inner


@pytest.fixture
def expected():
    path = Path(__file__).parent / 'test_data' / 'expected.txt'
    return path.read_text()


def test_gendiff(get_path, expected):
    f1, f2 = get_path('file1.json'), get_path('file2.json')
    assert generate_diff(f1, f2) == expected
