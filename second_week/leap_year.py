def is_leap_year(year):
    if year % 4 == 0:
        if(year % 100 != 0 or year % 400 == 0):
            return True
    return False










# Решение сайта
# year = int(input())
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("YES")
# else:
#     print("NO")
