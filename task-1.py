money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05

months = 1

while money_capital >= spend:
    money_capital += salary - spend
    spend *= (1 + increase)
    months += 1

print("Количество месяцев, которое можно протянуть без долгов:", months)