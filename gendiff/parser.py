import json
from pathlib import Path

import yaml


def get_data(data):
    with open(data) as f:
        return f.read(), Path(data).suffix


def parse(content, data_format):
    parse_by_format = {
        '.json': json.loads,
        '.yml': yaml.safe_load,
        '.yaml': yaml.safe_load
    }
    return parse_by_format[data_format](content)


def parsing(data):
    content, data_format = get_data(data)
    result = parse(content, data_format)
    return result
