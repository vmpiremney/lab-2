salary = 5000
spend = 6000
months = 10
increase = 0.03

required_savings = 0

for month in range(months):
    required_savings += spend - salary
    spend *= (1 + increase)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(round(required_savings, 2)))