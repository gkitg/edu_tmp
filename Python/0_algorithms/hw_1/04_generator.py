# -*- coding: utf-8 -*-

__author__ = 'gkitg'


# Написать программу, которая генерирует в указанном пользователем диапазоне:
#   случайное целое число,
#   случайное вещественное число,
#   случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Если надо получить случайный символ от 'a' до 'f', вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random


#   случайное целое число
print('Случайное целое число')
num_start = int(input('Начало диапазона: '))
num_end = int(input('Конец диапазона: '))
# result = int(random.random() * (num_end - num_start + 1)) + num_start
result = random.randint(num_start, num_end)
print(result)

#   случайное вещественное число
print('Случайное вещественное число')
num_start = float(input('Начало диапазона: '))
num_end = float(input('Конец диапазона: '))
# result = random.random() * (num_end - num_start) + num_start
result = random.uniform(num_start, num_end)
print(round(result, 3))

#   случайный символ
print('Случайный символ')
num_start = ord(input('Начало диапазона: '))
num_end = ord(input('Конец диапазона: '))
# result = int(random.random() * (num_end - num_start + 1)) + num_start
result = random.randint(num_start, num_end)
print(chr(result))