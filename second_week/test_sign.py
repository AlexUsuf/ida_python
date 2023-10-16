from sign import get_singn

def test_get_sign():
    assert get_singn(100) == 1
    assert get_singn(-10) == -1
    assert get_singn(0) == 0
    assert get_singn(-0) == 0
