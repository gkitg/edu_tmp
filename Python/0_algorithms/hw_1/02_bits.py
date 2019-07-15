# -*- coding: utf-8 -*-

__author__ = 'gkitg'


# Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат

a = 5
print(f'{a} = {bin(a)}')
b = 6
print(f'{b} = {bin(b)}')
# AND
print(f'{a} and {b} = {a & b} ({bin(a & b)})')
# OR
print(f'{a} or {b} = {a | b} ({bin(a | b)})')
# XOR
print(f'{a} xor {b} = {a ^ b} ({bin(a ^ b)})')

print(f'{a} >> 3 = {a >> 3} ({bin(a >> 3)})') # 5 // 2**3
print(f'{a} << 3 = {a << 3} ({bin(a << 3)})') # 5 * 2**3

print(f'not {a} = {~a} ({bin(~a)})')