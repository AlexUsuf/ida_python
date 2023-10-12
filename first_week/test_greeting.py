from greeting import greeting

def test_greeting():
    assert greeting("Alex") == "Hello, Alex!"
    assert greeting("Mr. Dumbledore") == "Hello, Mr. Dumbledore!"

def test_values():
    assert greeting([]) == "Type error"
    assert greeting(1234) == "Type error"
