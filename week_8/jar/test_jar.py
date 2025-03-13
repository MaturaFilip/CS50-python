from jar import Jar
import pytest


def test_init():
    with pytest.raises(ValueError):
        jar = Jar(-1)

    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    jar = Jar(12)
    assert jar.capacity == 12
    assert jar.size == 0

def test_str():
    jar = Jar()
    jar.deposit(2)
    assert str(jar) == "🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2

def test_withdraw():
    jar = Jar()
    jar.deposit(3)
    jar.withdraw(2)
    assert jar.size == 1
