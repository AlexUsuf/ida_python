from division_apple import division

def test_division():
    assert division(50, 6) == f"Каждый съел: 8. Яблок в корзине: 2"
    assert division(10, 1) == f"Каждый съел: 10. Яблок в корзине: 0"
def test_values():
    assert division([], '') == "Type error"
    assert division(0, 3) == "Division by zero"



if __name__ == '__main__':
    test_division()
    test_values()
    print('Ok')