from twttr import shorten

def test_vowels_only():
    assert shorten("ooo") == ""
    assert shorten("AEIOUaeiou") == ""

def test_combination():
    assert shorten("How") == "Hw"
    assert shorten("Greetings") == "Grtngs"

def test_consonants():
    assert shorten("HCHKRDTN") == "HCHKRDTN"

def test_punct():
    assert shorten("Hello.") == "Hll."

def test_number():
    assert shorten("Hello1") == "Hll1"
