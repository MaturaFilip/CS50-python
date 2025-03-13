from seasons import get_valid_input
import pytest

def test_get_valid_input():
    assert get_valid_input("1999-01-01") == [1999, 1, 1]

