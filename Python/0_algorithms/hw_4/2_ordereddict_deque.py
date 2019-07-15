"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import OrderedDict, deque

HEX_NUMS = '0123456789ABCDEF'


def hex_to_decimal(num):
    hex_number = OrderedDict()

    for key, value in enumerate(HEX_NUMS):
        hex_number[value] = key

    return sum([hex_number[j] * (16 ** i) for i, j in enumerate(num)])


def decimal_to_hex(num):
    dec_number = OrderedDict()

    for key, value in enumerate(HEX_NUMS):
        dec_number[key] = value

    lst = []

    while num > 0:
        lst.append(num % 16)
        num = num // 16

    return [dec_number[i] for i in lst[::-1]]


first_num = deque((input('Введите первое шестнадцатеричное число: ')).upper())
second_num = deque((input('Введите второе шестнадцатеричное число: ')).upper())

first_num.reverse()
second_num.reverse()

first_num_int = hex_to_decimal(first_num)
second_num_int = hex_to_decimal(second_num)

hex_summ = decimal_to_hex(first_num_int + second_num_int)
hex_multi = decimal_to_hex(first_num_int * second_num_int)

print(f'Сумма введенных чисел: {hex_summ}')
print(f'Произведение: {hex_multi}')