def sum(a, b, c):
    array = [int, float]
    if(type(a) not in array or type(b) not in array or type(c) not in array):
        return "Type error"
        
    return a + b + c

