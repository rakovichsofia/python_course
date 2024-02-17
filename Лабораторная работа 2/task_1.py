money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
month_to_live = 1
all_cap = money_capital + salary - spend
while all_cap > spend:
    month_to_live += 1
    all_cap += salary - spend
    spend *= 1.05

print("Количество месяцев, которое можно протянуть без долгов:", month_to_live)
