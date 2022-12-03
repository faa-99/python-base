from pathlib import Path
from typing import Dict

import yaml


def write_yaml(data: Dict, file_path: Path):
    with open(file_path, "w") as outfile:
        yaml.dump(data, outfile)


def read_yaml(file_path: Path):
    with open(file_path, "r") as f:
        data = yaml.load(f, yaml.SafeLoader)
    return data
