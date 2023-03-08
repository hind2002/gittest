
import pytest


def test_soustraction():
    assert 4 - 2 == 2

def test_soustraction_negative():
    assert 2 - 4 == -2

def test_soustraction_decimal():
    assert 0.3 - 0.2 == pytest.approx(0.1)
