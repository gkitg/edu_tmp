from collections import namedtuple

n = int(input("Введите количество предприятий: "))
companies = namedtuple("Company", " name period_1 period_2 period_3 period_4")
profit_aver = {}

for _ in range(n):
    company = companies(name=input("Введите название предприятия: "),
                     period_1=int(input("Введите прибыль за первый квартал: ")),
                     period_2=int(input("Введите прибыль за второй квартал: ")),
                     period_3=int(input("Введите прибыль за третий квартал: ")),
                     period_4=int(input("Введите прибыль за четвертый квартал: ")))

    profit_aver[company.name] = (company.period_1 + company.period_2 + company.period_3 + company.period_4) / 4

total_aver = sum(profit_aver.values())
total_aver = total_aver / n

for key, value in profit_aver.items():
    if value > total_aver:
        print(key, "- прибыль выше среднего")
    elif value < total_aver:
        print(key, "- прибыль ниже среднего")
    elif value == total_aver:
        print(key, "- средняя прибыль")