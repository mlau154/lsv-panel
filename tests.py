import os

import numpy as np
import pytest

import lsv_panel


@pytest.fixture
def data_dir() -> str:
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


def test_n0012(data_dir):
    pass


def test_n63412(data_dir):
    file_name = os.path.join(data_dir, "n63412-il.txt")
    coords = np.loadtxt(file_name, skiprows=1)
    _, _, cl = lsv_panel.solve(coords, 5.0)
    assert pytest.approx(cl, 0.01) == 0.95


def test_nlf0414(data_dir):
    pass
