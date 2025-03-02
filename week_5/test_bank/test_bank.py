from bank import value

def test_hello():
    assert value("Hello") == 0

def test_hi():
    assert value("Hi") == 20

def test_no_greetings():
    assert value("Dog") == 100