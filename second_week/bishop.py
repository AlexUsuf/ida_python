def is_possible_move_of_the_bishop(a1, b1, a2, b2):
    if abs(a2 - a1) == abs(b2 - b1):
        return True
    else:
        return False

# Для сайта
# a1 = int(input())
# b1 = int(input())
# a2 = int(input())
# b2 = int(input())
#
# if(abs(a2 - a1) == abs(b2 -b1)):
#     print("YES")
# else:
#     print("NO")
