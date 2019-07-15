# -*- coding: utf-8 -*-

__author__ = 'gkitg'


# Найти сумму и произведение цифр введённого пользователем трехзначного числа

num = input('Введите трёхзначное число: ')

# решение через долнительные переменные
num = int(num)
a = num // 100
b = num % 100 // 10
c = num % 10
summa = a + b + c
# mult = a * b * c
print(f'Сумма = {summa}')
print(f'Произведение = {a * b * c}')

# решение через цикл
num = str(num)
summa = 0
mult = 1
for i in num:
    summa += int(i)
    mult *= int(i)
print(f'Сумма = {summa}')
print(f'Произведение = {mult}')