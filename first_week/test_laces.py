from laces import get_value

def test_get_value():
    assert get_value(2, 1, 3, 4) == 26
    assert get_value(10, 20, 30, 40) == 2410
