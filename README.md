# Messy Project

A small application now organized in a conventional src layout.

## Current Layout

```text
messy_project/
├── README.md
├── main.py
├── src/
│   └── messy_project/
│       ├── __init__.py
│       ├── main.py
│       ├── helpers.py
│       └── old_utils.py
├── test_main.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── test_helpers.py
├── config/
│   └── app.yaml
├── data/
│   ├── sample.json
│   └── data_loader.yaml
├── scripts/
│   ├── deploy.sh
│   ├── deploy_helpers.py
│   └── run_tests.sh
├── conftest.py
└── requirements.txt
```

## Running

```bash
uv venv --seed --python=3.13
.\.venv\Scripts\activate
pip install -r requirements.txt
PYTHONPATH=src python -m messy_project.main
pytest
```

## Notes

1. The application config is config/app.yaml.
2. The data loader settings file is data/data_loader.yaml.
3. The script helper module is scripts/deploy_helpers.py and remains separate from src/messy_project/helpers.py.
4. old_utils.py is retained because it is still imported by the application.
