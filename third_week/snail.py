import math
h = int(input())
a = int(input())
b = int(input())
result = math.ceil((h - a) / (a - b)) + 1
print(result)
