from area_of_triangle import *

def test_area_triangle():
    assert area_triangle(1,2) == 1.0
    assert area_triangle(1, 100) == 50
    assert area_triangle(1.5, 2) == 1.5

def test_values():
    assert area_triangle(-1, -100) == "Not a triangle"
    assert area_triangle('2', 100) == "Type error"
    assert area_triangle([1.2,3,4], 100) == "Type error"
    assert area_triangle(None, 100) == "Type error"

if __name__ == '__main__':
    test_area_triangle()
    print('OK')
