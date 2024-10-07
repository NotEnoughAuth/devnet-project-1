import yaml
import json
import xml.etree.ElementTree as ET

def parseYaml(yamlFile):
    with open(yamlFile, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            return None
          
def parseJson(jsonFile):
    with open(jsonFile) as f:
        data = json.load(f)
    return data

def parseXml(xmlFile):
    #parse an xml file to python dict
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    return root
    

