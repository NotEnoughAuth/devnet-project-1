import json

def parse_json(jsonFile):
    with open(jsonFile) as f:
        data = json.load(f)
    return data

