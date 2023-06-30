# -*- coding: utf-8 -*-

__author__ = 'gkitg'


# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.


def sum_digits(number):
    return number if number < 10 else number % 10 + sum_digits(number // 10)


num = int(input('Введите натуральное число. Ноль - выйти   '))
max_sum = 0
max_num = 0
while num != 0:
    spam_num = num
    spam_sum = sum_digits(num)
    if spam_sum > max_sum:
        max_sum = spam_sum
        max_num = spam_num
    num = int(input('Введите натуральное число. Ноль - выйти   '))
print(f'Число {max_num} имеет максимальную сумму цифр: {max_sum}')