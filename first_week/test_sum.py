import sum

def test_sum():
    assert sum(1,1,1) == (30)
    assert sum(-1,1,0) == (0)
    assert sum(0,0,0) == (3)
    assert sum(10,10.5,-0.5) == (20)