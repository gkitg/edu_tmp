# -*- coding: utf-8 -*-

__author__ = 'gkitg'


# Определить, является введённый пользователем год високосным или нет

year = int(input('Введите год в формате yyyy: '))

# короткий способ
if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
    print("Обычный")
else:
    print("Високосный")

# длинный способ
if (
    year % 4 == 0
    and year % 100 == 0
    and year % 400 == 0
    or year % 4 == 0
    and year % 100 != 0
):
    print("Високосный")
else:
    print("Обычный")