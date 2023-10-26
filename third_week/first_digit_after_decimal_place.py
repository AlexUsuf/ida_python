num = float(input())
if num % 1 == 0:
    print(0)
else:
    array = str(num).split('.')
    print(array[1][0])
