import os
import sys


_SRC_DIR = os.path.join(os.path.dirname(__file__), "src")
if _SRC_DIR not in sys.path:
	sys.path.insert(0, _SRC_DIR)

from messy_project.helpers import format_output, greet

__all__ = ["greet", "format_output"]
