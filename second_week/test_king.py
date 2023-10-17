from king import is_possible_move_of_the_king

def test_is_possible_move_of_the_king():
    assert is_possible_move_of_the_king(4, 4, 5, 5) == True
    assert is_possible_move_of_the_king(1, 1, 5, 5) == False
    assert is_possible_move_of_the_king(1, 1, 8, 1) == False
    assert is_possible_move_of_the_king(1, 1, 5, 1) == False
    assert is_possible_move_of_the_king(5, 5, 5, 1) == False
    assert is_possible_move_of_the_king(1, 5, 5, 1) == False
    assert is_possible_move_of_the_king(4, 4, 5, 4) == True
