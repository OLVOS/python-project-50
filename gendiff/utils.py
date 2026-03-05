import json
from pathlib import Path


def parsing(path):
    path = Path(path)
    if not path.exists():
        path = path = Path('tests/test_data') / path

    with open(path) as f:
        return json.load(f)


def hello():
    print('hello')
