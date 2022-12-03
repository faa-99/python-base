import csv
from pathlib import Path
from typing import List


def write_csv(data: List, file_path: Path):
    with open(file_path, "w") as f:
        writer = csv.writer(f)
        writer.writerows(data)


def read_csv(file_path: Path):
    with open(file_path, newline="") as f:
        reader = csv.reader(f, delimiter=",")
        data = [row for row in reader]
    return data
