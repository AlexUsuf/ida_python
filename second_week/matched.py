def match(a, b, c):
    if (a == b and b == c and a == c):
        return 3
    elif (a == b or b == c or a == c):
        return 2
    else:
        return 0


#
# решение для сайта
# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
# if (n1 == n2 and n2 == n3 and n1 == n3):
#     print(3)
# elif (n1 == n2 or n2 == n3 or n1 == n3):
#     print(2)
# else:
#     print(0)
