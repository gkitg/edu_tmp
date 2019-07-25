"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

import random
import timeit

# Стандартнный подход
def bubble_sort(orig_list):
    n = 1
    #k = 0
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
        n +=1
    return orig_list


# Доработанный подход
# если за проход по списку не совершается ни одной сортировки
# то функция прекращает свою работу
def bubble_sort_upd(orig_list):
    n = 1
    k = 0
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
                k = 1
        if k == 0:
            break
        n +=1
    return orig_list


orig_list = [random.randint(-100, 100) for i in range(10)]

print(timeit.timeit("bubble_sort(orig_list)", setup="from __main__ import bubble_sort, orig_list", number=1000000))
print(timeit.timeit("bubble_sort_upd(orig_list)", setup="from __main__ import bubble_sort_upd, orig_list", number=1000000))


