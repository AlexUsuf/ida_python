from sum import *
def area_triangle(a, b):
    if (type(a) not in array_type_values or type(b) not in array_type_values):
        return "Type error"
    elif (a <= 0 or b <= 0):
        return "Not a triangle"
    else:
        return a * b / 2