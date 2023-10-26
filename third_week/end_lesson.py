n = int(input())
n = ((n + 1) // 2 - 1) * 15 + n * 45 + (n // 2) * 5
print(n // 60 + 9, n % 60)
