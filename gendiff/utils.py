import json


def parsing(path):
    with open(path) as f:
        return json.load(f)


def hello():
    print('hello')
