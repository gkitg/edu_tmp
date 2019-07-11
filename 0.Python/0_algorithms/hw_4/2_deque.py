"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque

x = deque(input("Введите первое число: "))
y = deque(input("Введите второе число: "))


def hex_sum(x, y):
    x = "".join([i for i in x])
    y = "".join([i for i in y])
    s = hex((int(float.fromhex(x) + float.fromhex(y))))
    s = deque(s[2::].upper())
    print("Сумма:", s)


def hex_mul(x, y):
    x = "".join([i for i in x])
    y = "".join([i for i in y])
    s = hex((int(float.fromhex(x) * float.fromhex(y))))
    s = deque(s[2::].upper())
    print("Произведение:", s)


hex_sum(x, y)
hex_mul(x, y)