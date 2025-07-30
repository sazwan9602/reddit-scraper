import json
from pathlib import Path
from typing import Any
import os


def write_json(file_name: str, data: Any) -> None:
    try:
        with open(Path(file_name), "w") as file:
            json.dump(data, file, indent=4)
        print("Data written successfully.")
    except (TypeError, ValueError) as e:
        print(f"Data serialization error: {e}")
    except IOError as e:
        print(f"File write error: {e}")


def read_directory(dir: str) -> list:
    return os.listdir(Path(dir))


def read_json_file(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            print("Data read successfully.")
            return data
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
    except IOError as e:
        print(f"File read error: {e}")
    return None
