import json

#FILE_NAME = "C:/Users/anuno/OneDrive/Documents/ITESO/Modelos de crédito/CREDIT-RISK-2020B/src/exams/flatten-json/ex-5.json"


def to_dict(file: str):
    with open(file, "r") as f:
        json_file = json.load(f)
    return json_file


def flatten_dict(file: dict):
    result = {}

    def flatten(file: dict, name=''):
        if isinstance(file, dict):
            for key in file.keys():
                flatten(file[key], name + key + '.')

        elif isinstance(file, list):
            count = 0
            for i in file:
                flatten(i, name + str(count) + '.')
                count += 1
        else:
            result[name[:-1]] = file

    flatten(file)
    return json.dumps(result, indent=3, sort_keys=True)
