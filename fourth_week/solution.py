# Задача №1
# Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно.
a = int(input())
b = int(input())
for i in range(a, b + 1):
    print(i)

# Задача №2
# Даны два целых числа A и В. Выведите все числа от A до B включительно,
# в порядке возрастания, если A < B, или в порядке убывания в противном случае.
a = int(input())
b = int(input())
if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print(i)

# Задача №3
# Даны два целых числа A и В, A>B
# . Выведите все нечётные числа от A до B включительно, в порядке убывания.
# В этой задаче можно обойтись без инструкции if.
a = int(input())
b = int(input())
if(a % 2 != 0):
    for i in range(a, b - 1 , -2):
        print(i)
else:
    for i in range(a - 1, b - 1, -2):
        print(i)
# Задача № 4
# Дано 10 целых чисел. Вычислите их сумму. Напишите программу, использующую наименьшее число переменных.
result = 0
for i in range(10):
    result += int(input())
print(result)

# Задача №5
# Дано несколько чисел. Вычислите их сумму.
# Сначала вводите количество чисел N, затем вводится ровно N целых чисел. Какое наименьшее число переменных нужно для решения этой задачи?
result = 0
for i in range(int(input())):
    result += int(input())
print(result)

# Задача №6
# По данному натуральному n вычислите сумму 13+23+33+...+n3.
result = 0
n = int(input())
for i in range(n+1):
    result += i**3
print(result)
# Задача №7
# Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!.
# По данному натуральному n вычислите значение n!. Пользоваться математической библиотекой math в этой задаче запрещено.
n = int(input())
def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1
print(factorial(n))

# Задача № 8
# По данному натуральном n
# вычислите сумму 1!+2!+3!+...+n!
# В решении этой задачи можно использовать только один цикл.
# Пользоваться математической библиотекой math в этой задаче запрещено.
n = int(input())
temp = 0;
factorial_count = 1
for i in range(1, n + 1):
    factorial_count *= i
    temp += factorial_count
print(temp)

# Задача №9
# Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел.
# Подсчитайте количество нулей среди введенных чисел и выведите это количество.
# Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр.

n = int(input())
def get_count_zeroes(n):
    count = 0
    for i in range(n):
        temp = int(input())
        if temp == 0:
            count += 1
    return count
print(get_count_zeroes(n))

# Задача №10
# По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов.

n = int(input())
prev = ''
for i in range(1, n + 1):
    prev += str(i)
    print(prev)

# Задача №11
# Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась. Найдите ее, зная номера оставшихся карточек.
# Дано число N, далее N − 1 номер оставшихся карточек (различные числа от 1 до N). Программа должна вывести номер потерянной карточки.
#
# Для самых умных: массивами и аналогичными структурами данных пользоваться нельзя.
n = int(input())
result = 0
for i in range(1, n + 1):
    result += i
for i in range(n - 1):
    temp = int(input())
    result -= temp
print(result)