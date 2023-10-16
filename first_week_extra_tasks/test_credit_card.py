from credit_card import maskify

def test_maskify():
    assert maskify('') == ''
    assert maskify('123') == '123'
    assert maskify('SF$SDfgsd2eA') == '########d2eA'
