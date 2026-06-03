from messy_project.config_loader import load_config
from messy_project.helpers import greet


def main(config_path="config.yaml"):
    cfg = load_config(config_path)
    return greet(cfg.get("name", "world"))


if __name__ == "__main__":
    print(main())
