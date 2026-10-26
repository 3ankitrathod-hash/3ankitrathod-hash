"""Shared fixtures for the supply chain analysis tests.

The analysis script is loaded straight from its file and pointed at temporary
folders, so running the tests never writes into the repository's data or
outputs directories.
"""

import importlib.util
from pathlib import Path

import pandas as pd
import pytest

PROJECT_DIR = Path(__file__).resolve().parents[1]
SCRIPT_PATH = PROJECT_DIR / "analyze_supply_chain.py"
DATA_PATH = PROJECT_DIR / "data" / "supply_chain_orders.csv"
COMMITTED_OUTPUTS = PROJECT_DIR / "outputs"
README_PATH = PROJECT_DIR / "README.md"


@pytest.fixture(scope="session")
def module():
    """The analysis script, imported as a module."""
    spec = importlib.util.spec_from_file_location("analyze_supply_chain", SCRIPT_PATH)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


@pytest.fixture
def source_data():
    """The committed demo dataset."""
    return pd.read_csv(DATA_PATH)


@pytest.fixture
def run_analysis(module, monkeypatch, tmp_path):
    """Return a function that runs the analysis on a DataFrame and returns the output folder."""

    def _run(frame):
        input_file = tmp_path / "input" / "orders.csv"
        input_file.parent.mkdir()
        frame.to_csv(input_file, index=False)
        output_dir = tmp_path / "outputs"
        monkeypatch.setattr(module, "DATA_PATH", input_file)
        monkeypatch.setattr(module, "OUTPUT_DIR", output_dir)
        module.main()
        return output_dir

    return _run
