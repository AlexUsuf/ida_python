array_type_values = [float, int]
def even_odd(num):
    if type(num) not in array_type_values:
        return "Error type"
    elif num % 2 == 0:
        return "Even"
    return "Odd"
