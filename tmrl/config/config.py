import yaml
import pprint

def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)


yaml_content = read_yaml("example.yaml")
pprint.pprint(yaml_content)