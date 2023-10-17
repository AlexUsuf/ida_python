from chocolate import chocolate

def test_chocolate():
    assert chocolate(4, 2, 6) == True
    assert chocolate(2, 10, 7) == False
    assert chocolate(5, 7, 1) == False
    assert chocolate(7, 4, 21) == False
