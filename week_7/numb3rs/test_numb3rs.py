from numb3rs import validate
import pytest

def test_validate():
    assert validate("1.1.1.1") == True
    assert validate("275.1.42.92") == False
    assert validate("192.10.1") == False
    assert validate("127.0.0.1") == True
    assert validate("140.247.235.144") == True
    assert validate("1") == False
    assert validate("ip_address") == False
    assert validate("275.275.300.920") == False
    assert validate("23.275.92.1") == False

