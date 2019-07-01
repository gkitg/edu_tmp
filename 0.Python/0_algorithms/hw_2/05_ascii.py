# -*- coding: utf-8 -*-

__author__ = 'gkitg'


# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

START = 32
STOP = 127

for i in range(START, STOP + 1):
    print(f'\t{i}-{chr(i)}', end='')
    if i % 10 == 1:
        print()