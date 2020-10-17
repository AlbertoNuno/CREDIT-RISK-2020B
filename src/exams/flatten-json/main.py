import json
from .utils import *


class Main:

    @staticmethod
    def show(file: str = FILE_NAME) -> str:
        with open(file, "r") as f:
            data = json.load(f)
        return json.dumps(data)
    @staticmethod
    def flatten(file: str = FILE_NAME) -> str:
        flattened_file = to_dict(file)
        new_file = flatten_dict(flattened_file)
        return new_file


