from queen import is_possible_move_of_the_queen

def test_is_possible_move_of_the_queen():
    assert is_possible_move_of_the_queen(1, 1, 2, 2) == True
    assert is_possible_move_of_the_queen(3, 3, 1, 1) == True
    assert is_possible_move_of_the_queen(7, 6, 5, 2) == False
    assert is_possible_move_of_the_queen(1, 2, 3, 1) == False
    assert is_possible_move_of_the_queen(2, 7, 4, 6) == False
    assert is_possible_move_of_the_queen(5, 2, 5, 8) == True
