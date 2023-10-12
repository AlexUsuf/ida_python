from sum import array_type_values
def get_values(n):
    if type(n) not in array_type_values:
        return "Type error"
    return [f"next value for {n} is {n+1}", f"prev value for {n} is {n-1}"]


print(get_values(3))
