import yaml

def parseYaml(yamlFile):
    with open(yamlFile, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            return None
        

print(parseYaml('test.yaml'))