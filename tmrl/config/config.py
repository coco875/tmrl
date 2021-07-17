import yaml
import pprint

with open("example.yaml") as f:
    yaml_content = dict(yaml.load_all(f, Loader=yaml.Loader))

pprint.pprint(yaml_content['calling-birds'])
