from plates import is_valid

def test_01():
    assert is_valid("01") == False

def test_shorter():
    assert is_valid("L") == False

def test_correct():
    assert is_valid("CS50") == True

def test_longer():
    assert is_valid("Hello, world") == False

def test_num():
    assert is_valid("1") == False

def  test_blank():
    assert is_valid("") == False

def test_punct():
    assert is_valid("CS!!") == False

def test_alpha():
    assert is_valid("CSF") == True

def test_num_placement():
    assert is_valid("CS50P") == False

def test_zero_placement():
    assert is_valid("CS05") == False

def without_alpha_start():
    assert is_valid("123456") == False
    assert is_valid("111k") == False

def test_is_v():
    assert is_valid("123456") == False
    assert is_valid("PI3.14") == False


