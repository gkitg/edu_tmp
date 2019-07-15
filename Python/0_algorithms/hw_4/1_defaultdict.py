#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Администратор
#
# Created:     26.01.2019
# Copyright:   (c) Администратор 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
чья прибыль ниже среднего.
"""

import collections

c_count = int(input("Введите кол-во компаний: "))

companies = collections.defaultdict()
for i in range(c_count):
    name = input("Введите наименование %d-й компании: " % (i+1))
    income = [float(input("Введите прибыль за %d квартал: " % (j+1))) for j in range(4)]
    companies[name] = sum(income)
print(companies)

avg = sum(companies.values())/c_count
print("Средняя прибыль всех компаний за год: %.0f" % avg)

print("Компании с прибылью выше средней: ")
for c in companies:
    print(c)
    if companies[c] >= avg:
        print("%s (%.0f)" % (c, companies[c]))

print("Компании с прибылью ниже средней: ")
for c in companies:
    if companies[c] < avg:
        print("%s (%.0f)" % (c, companies[c]))

