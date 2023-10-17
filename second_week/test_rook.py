from rook import is_possible

def test_is_possible():
    assert is_possible(1,1,2,2) == False
    assert is_possible(4,4,5,4) == True
    assert is_possible(1,1,1,2) == True
    assert is_possible(4,4,4,3) == True
    assert is_possible(1,8,8,8) == True
