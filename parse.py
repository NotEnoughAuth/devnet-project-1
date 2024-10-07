import yaml
import json

def parseYaml(yamlFile):
    with open(yamlFile, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            return None
          
def parse_json(jsonFile):
    with open(jsonFile) as f:
        data = json.load(f)
    return data
        

print(parseYaml('test.yaml'))

