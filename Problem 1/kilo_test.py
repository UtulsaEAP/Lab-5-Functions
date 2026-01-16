from kilo_to_pounds import kilo_to_pounds
import pytest

def test_kilo_to_pounds():
    assert kilo_to_pounds(0) == 0
    assert kilo_to_pounds(1) == pytest.approx(2.20462, rel=1e-3)
    assert kilo_to_pounds(10) == pytest.approx(22.0462, rel=1e-3)
    assert kilo_to_pounds(50) == pytest.approx(110.231, rel=1e-3)
    assert kilo_to_pounds(100) == pytest.approx(220.462, rel=1e-3)

def test_kilo_to_pounds_negative():
    assert kilo_to_pounds(-1) == pytest.approx(-2.20462, rel=1e-3)
    assert kilo_to_pounds(-10) == pytest.approx(-22.0462, rel=1e-3)

def test_kilo_to_pounds_float():
    assert kilo_to_pounds(1.5) == pytest.approx(3.30693, rel=1e-3)
    assert kilo_to_pounds(2.5) == pytest.approx(5.51155, rel=1e-3)
