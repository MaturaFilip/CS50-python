from um import count
import pytest

def test_convert():
    assert count("yummy") == 0
    assert count("um, thanks um...") == 2
    assert count("Um") == 1

