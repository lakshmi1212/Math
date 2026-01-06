import pytest
from src.math_operations import subtract

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 1) == -1
    assert subtract(-1, -1) == 0
    assert subtract(2.5, 1.5) == 1.0
