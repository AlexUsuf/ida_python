from next_and_prev import get_values

def test_get_values():
    assert get_values(1) == ['next value for 1 is 2', 'prev value for 1 is 0']

def test_values():
    assert get_values([]) == 'Type error'
