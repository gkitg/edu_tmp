#-------------------------------------------------------------------------------
# Name:       
# Purpose:
#
# Author:      
#
# Created:     
# Copyright:   (c)
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import timeit


#2. Написать два алгоритма нахождения i-го по счёту простого числа.
#Без использования «Решета Эратосфена»;
#Используя алгоритм «Решето Эратосфена»
import timeit
from memory_profiler import profile


# Вариант 1 (простой)
@profile
def simple(i):
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


# Вариант 2 (решето Эратосфена)
@profile
def eratosfen(i):
    n = 2
    l = 10000
    sieve = [x for x in range(l)]
    sieve[1] = 0
    while n < l:
        if sieve[n] != 0:
            m = n*2
            while m < l:
                sieve[m] = 0
                m += n
        n += 1
    return [p for p in sieve if p != 0][i-1]

i = int(input('Введите порядковый номер искомого простого числа:'))
print(simple(i))
print(eratosfen(i))
#print(timeit.timeit("simple(i)", setup="from __main__ import simple,i", number=100))
#print(timeit.timeit("eratosfen(i)", setup="from __main__ import eratosfen,i", number=100))

"""
Время работы алгоритмов для поиска 10-го простого числа 100 раз:
- простой - 0.002
- решето - 0.391
Время работы алгоритмов для поиска 100-го простого числа 100 раз:
- простой - 0.257
- решето - 0.384
Время работы алгоритмов для поиска 1000-го простого числа 100 раз:
- простой - 43.141
- решето - 0.430
Алгоритм решета Эратосфена эффективен для поиска простого числа с большим порядковым номером.
Сложность простого алгоритма O(n^2)
Сложность решета Эратосфена O(n log(log n))
"""
'''

Line #    Mem usage    Increment   Line Contents
================================================
    19     40.2 MiB     40.2 MiB   @profile
    20                             def simple(i):
    21     40.2 MiB      0.0 MiB       count = 1
    22     40.2 MiB      0.0 MiB       n = 2
    23     40.2 MiB      0.0 MiB       while count <= i:
    24     40.2 MiB      0.0 MiB           t = 1
    25     40.2 MiB      0.0 MiB           is_simple = True
    26     40.2 MiB      0.0 MiB           while t <= n:
    27     40.2 MiB      0.0 MiB               if n % t == 0 and t != 1 and t != n:
    28     40.2 MiB      0.0 MiB                   is_simple = False
    29     40.2 MiB      0.0 MiB                   break
    30     40.2 MiB      0.0 MiB               t += 1
    31     40.2 MiB      0.0 MiB           if is_simple:
    32     40.2 MiB      0.0 MiB               if count == i:
    33     40.2 MiB      0.0 MiB                   break
    34     40.2 MiB      0.0 MiB               count += 1
    35     40.2 MiB      0.0 MiB           n += 1
    36     40.2 MiB      0.0 MiB       return n


Line #    Mem usage    Increment   Line Contents
================================================
    39     40.2 MiB     40.2 MiB   @profile
    40                             def eratosfen(i):
    41     40.2 MiB      0.0 MiB       n = 2
    42     40.2 MiB      0.0 MiB       l = 10000
    43     40.8 MiB      0.1 MiB       sieve = [x for x in range(l)]
    44     40.8 MiB      0.0 MiB       sieve[1] = 0
    45     40.8 MiB      0.0 MiB       while n < l:
    46     40.8 MiB      0.0 MiB           if sieve[n] != 0:
    47     40.8 MiB      0.0 MiB               m = n*2
    48     40.8 MiB      0.0 MiB               while m < l:
    49     40.8 MiB      0.0 MiB                   sieve[m] = 0
    50     40.8 MiB      0.0 MiB                   m += n
    51     40.8 MiB      0.0 MiB           n += 1
    52     40.9 MiB      0.1 MiB       return [p for p in sieve if p != 0][i-1]
'''
