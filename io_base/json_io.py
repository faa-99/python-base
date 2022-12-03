import json
from pathlib import Path
from typing import Dict


def write_json(data: Dict, file_path: Path):
    with open(file_path, "w") as outfile:
        json.dump(data, outfile)


def read_json(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
    return data
