from leap_year import is_leap_year

def test_is_leap_year():
    assert is_leap_year(2012) == True
    assert is_leap_year(2015) == False
    assert is_leap_year(2100) == False
    assert is_leap_year(2020) == True
    assert is_leap_year(1900) == False
