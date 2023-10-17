from matched import match

def test_match():
    assert match(1, 2, 3) == 0
    assert match(1, 1, 1) == 3
    assert match(1, 1, 3) == 2
    assert match(-1, 2, 3) == 0
    assert match(-1, -1, 3) == 2
