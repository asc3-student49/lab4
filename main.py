import os
import sys
import types


_SRC_DIR = os.path.join(os.path.dirname(__file__), "src")
if _SRC_DIR not in sys.path:
    sys.path.insert(0, _SRC_DIR)

if "old_utils" not in sys.modules:
    from messy_project.config_loader import load_config as _load_config

    _shim = types.ModuleType("old_utils")
    _shim.load_config = _load_config
    sys.modules["old_utils"] = _shim

from helpers import greet
from old_utils import load_config


def main(config_path="config.yaml"):
    cfg = load_config(config_path)
    return greet(cfg.get("name", "world"))


if __name__ == "__main__":
    print(main())
