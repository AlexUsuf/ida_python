p = int(input())
x = int(input())
y = int(input())
start_money = x * 100 + y
monetary_contribution = (100 + p) * start_money // 100
monetary_in_rubbles = monetary_contribution // 100
monetary_in_peney = monetary_contribution % 100
print(monetary_in_rubbles, monetary_in_peney)
