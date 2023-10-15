from even_or_odd import even_odd

def test_even_odd():
    assert even_odd(20) == "Even"
    assert even_odd(21) == "Odd"

def test_type_values():
    assert even_odd([]) == "Error type"
