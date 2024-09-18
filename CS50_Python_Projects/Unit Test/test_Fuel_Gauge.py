from Fuel_Gauge import gauge, convert 
import pytest

def test_valid_fractions():
    assert gauge(5,10) == "50%"
    assert gauge(3,10) == "30%"
    assert gauge(3.33333333333,10) == "33%"

def test_invalid_fractions():
    with pytest.raises(TypeError):
        gauge("a", 10)
    with pytest.raises(TypeError):
        gauge("Hej")
    with pytest.raises(TypeError):
        gauge(8, "bums")
    with pytest.raises(ZeroDivisionError):
        gauge(80,0)

def test_special_fractions():
    assert gauge(0,100) == "Empty"
    assert gauge(100,100) == "Full"
    with pytest.raises(ZeroDivisionError):
        gauge(0,0)
