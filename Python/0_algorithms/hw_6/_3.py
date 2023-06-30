"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


from memory_profiler import profile


length = 900

@profile
def recursion(length):
    def sum_series_numbers(n, elem=1):
        return 0 if n <= 0 else elem + sum_series_numbers(n - 1, -elem/2)

    print(f'Сумма последовательности из {length} элементов равна {sum_series_numbers(length)}')


@profile
def for_in(length):
    elem = 1
    amount = 0
    for _ in range(length):
        amount += elem
        elem = -elem / 2
    print(f'Сумма последовательности из {length} элементов равна {amount}')


'''
Line #    Mem usage    Increment   Line Contents
================================================
    18     27.4 MiB     27.4 MiB   @profile
    19                             def for_in(length):
    20     27.4 MiB      0.0 MiB       elem = 1
    21     27.4 MiB      0.0 MiB       amount = 0
    22     27.4 MiB      0.0 MiB       for i in range(length):
    23     27.4 MiB      0.0 MiB           amount += elem
    24     27.4 MiB      0.0 MiB           elem = -elem / 2
    25     27.4 MiB      0.0 MiB       print(f'Сумма последовательности из {length} элементов равна {amount}')

Сумма последовательности из 900 элементов равна 0.6666666666666666

Line #    Mem usage    Increment   Line Contents
================================================
    11     27.4 MiB     27.4 MiB   @profile
    12                             def recursion(length):
    13     28.8 MiB      0.0 MiB       def sum_series_numbers(n, elem=1):
    14     28.8 MiB      0.0 MiB           if n <= 0:
    15     28.8 MiB      0.0 MiB               return 0
    16     28.8 MiB      0.0 MiB           return elem + sum_series_numbers(n - 1, -elem/2)
    17     28.8 MiB      0.0 MiB       print(f'Сумма последовательности из {length} элементов равна {sum_series_numbers(length)}')
'''
