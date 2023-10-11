array_type_values = [int, float]
def sum(a, b, c):
    if(type(a) not in array_type_values or type(b) not in array_type_values or type(c) not in array_type_values):
        return "Type error"
    return a + b + c
