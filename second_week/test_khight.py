from knight import is_possible_move_of_the_knight
def test_is_possible_move_of_the_knight():
    assert is_possible_move_of_the_knight(2, 4, 3, 2) == True
    assert is_possible_move_of_the_knight(5, 2, 4, 4) == True
    assert is_possible_move_of_the_knight(5, 1, 4, 3) == True
    assert is_possible_move_of_the_knight(1, 1, 1, 4) == False
    assert is_possible_move_of_the_knight(1, 1, 8, 8) == False
    assert is_possible_move_of_the_knight(2, 8, 3, 5) == False
