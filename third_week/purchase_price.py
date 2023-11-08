a = int(input())
b = int(input())
n = int(input())
rubles = a * n
penny = b * n
while penny >= 100:
    rubles += 1
    penny -= 100

print(rubles, penny)
