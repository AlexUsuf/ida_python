import math
def get_min_value(a, b, c):
    array = [a, b, c]
    min = math.inf
    for count in array:
        if min > count:
            min = count
    return min



# Решение сайта
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# if num2 >= num1 <= num3:
#     print(num1)
# elif num1 >= num2 <= num3:
#     print(num2)
# else:
#     print(num3)
