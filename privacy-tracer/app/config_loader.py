import yaml


def load_services_config(path="config/services.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)["services"]
