from sum import array_type_values

def division(n, k):
    if (type(n) not in array_type_values or type(k) not in array_type_values):
        return "Type error"
    elif n == 0 or k == 0:
        return "Division by zero"
    else:
        total_apples = n // k
        basket_apples = n % k
        return f"Каждый съел: {total_apples}. Яблок в корзине: {basket_apples}"




print(division(50,3))