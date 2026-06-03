from .helpers import greet
from .old_utils import load_config


def main(config_path="config/app.yaml"):
    cfg = load_config(config_path)
    name = cfg.get("name", "world") if isinstance(cfg, dict) else "world"
    return greet(name)


if __name__ == "__main__":
    print(main())
