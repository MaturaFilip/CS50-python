from fuel import convert, gauge
import pytest

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(24) == "24%"

def test_convert():
    assert convert("1/4") == 25
    assert convert("0/10") == 0

    with pytest.raises(ValueError):
        convert("A/4")
        convert("4/A")

    with pytest.raises(ValueError):
        convert("5/2")
        convert("1.5/6")
        convert("1:5")

    with pytest.raises(ZeroDivisionError):
        convert("1/0")
