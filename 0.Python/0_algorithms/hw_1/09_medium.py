# -*- coding: utf-8 -*-

__author__ = 'gkitg'


# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)

print('Введите три разных числа: ')
a = int(input('1-е: '))
b = int(input('2-е: '))
c = int(input('3-е: '))

if b < a < c or c < a < b:
    print('Среднее:', a)
elif a < b < c or c < b < a:
    print('Среднее:', b)
else:
    print('Среднее:', c)