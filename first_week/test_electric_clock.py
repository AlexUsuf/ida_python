from electric_clock import get_time

def test_get_time():
    assert get_time(150) == [2, 30]
    assert get_time(1441) == [0, 1]
    assert get_time(444) == [7, 24]

def test_values():
    assert get_time(None) == "Type error"
    assert get_time('str') == "Type error"
    assert get_time([1, 32]) == "Type error"
