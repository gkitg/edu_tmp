# -*- coding: utf-8 -*-

__author__ = 'gkitg'


# Функция Аккермана
# принимает два неотрицательных целых числа
# возвращает натуральное число

import sys

sys.setrecursionlimit(10000)

def akk(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return akk(m - 1, 1)
    else:
        return akk(m - 1, akk(m, n - 1))


x = int(input('x = '))
y = int(input('y = '))
z = akk(x, y)
print(z)