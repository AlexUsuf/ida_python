from bishop import is_possible_move_of_the_bishop
def test_is_possible_move_of_the_bishop():
    assert is_possible_move_of_the_bishop(4, 4, 5, 5) == True
    assert is_possible_move_of_the_bishop(4, 4, 5, 3) == True
    assert is_possible_move_of_the_bishop(4, 4, 3, 3) == True
    assert is_possible_move_of_the_bishop(1, 1, 1, 7) == False
    assert is_possible_move_of_the_bishop(1, 8, 8, 8) == False
    assert is_possible_move_of_the_bishop(4, 4, 4, 6) == False
