from chess_board import is_one_color

def test_is_one_color():
    assert is_one_color(1,1,1,1) == 'YES'
    assert is_one_color(0,0,0,0) == 'YES'
    assert is_one_color(10,1,1,1) == 'NO'
