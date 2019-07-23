# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’]
# и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque


BASE = 16

HEX_NUMBERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
               'A', 'B', 'C', 'D', 'E', 'F')

BIN_NUMBERS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
               '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
               'C': 12, 'D': 13, 'E': 14, 'F': 15}


def sum_hex(first, second):
    """
    Изменяемые объекты передаются по ссылке
    Используем копию, чтобы не ломать оригинал
    """
    first = first.copy()
    second = second.copy()

    if len(second) > len(first):
        first, second = second, first

    second.extendleft('0' * (len(first) - len(second)))

    result = deque()
    overflow = 0
    while len(first) != 0:
        first_num = BIN_NUMBERS[first.pop()]
        second_num = BIN_NUMBERS[second.pop()]

        result_num = first_num + second_num + overflow

        if result_num >= BASE:
            overflow = 1
            result_num -= BASE
        else:
            overflow = 0

        result.appendleft(HEX_NUMBERS[result_num])

    if overflow == 1:
        result.appendleft('1')

    return result


def mult_hex(first, second):
    first = first.copy()
    second = second.copy()

    if len(second) > len(first):
        first, second = second, first

    second.extendleft('0' * (len(first) - len(second)))
    result = deque('0')

    while len(second) != 0:
        second_num = BIN_NUMBERS[second.pop()]

        spam = deque('0')
        for _ in range(second_num):
            spam = sum_hex(spam, first)

        spam.extend('0' * (len(first) - len(second) - 1))
        result = sum_hex(result, spam)

    return result


if __name__ == '__main__':
    a = deque(input('Введите первое число в hex формате (только цифры от 0 до f): ').upper())
    b = deque(input('Введите второе число в hex формате (только цифры от 0 до f): ').upper())

    print(f'{list(a)} + {list(b)} = {list(sum_hex(a, b))}')
    print(f'{a} * {b} = {mult_hex(a, b)}')  # специально убрал список, чтобы показать как хранится
