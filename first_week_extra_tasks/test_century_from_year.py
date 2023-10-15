from century_from_year import century

def test_century():
    assert century(1705) == 18
    assert century(1900) == 19
    assert century(89) == 1
