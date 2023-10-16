from min_value import get_min_value

def test_get_max_value():
    assert get_min_value(2, 4) == 2
    assert get_min_value(4, 4) == 4
    assert get_min_value(0, -1) == -1
    assert get_min_value(-2, -1) == -2
