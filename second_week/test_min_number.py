from min_number import get_min_value


def test_get_min_value():
    assert get_min_value(1,2,3) == 1
    assert get_min_value(10,2,3) == 2
    assert get_min_value(10,20,3) == 3
    assert get_min_value(10,20,-3) == -3
    assert get_min_value(2,2,3) == 2
