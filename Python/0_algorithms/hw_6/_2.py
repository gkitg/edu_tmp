"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""

import random

def merge_sort(alist):

    if len(alist) <= 1:
        return
    mid = len(alist)//2
    lefthalf = alist[:mid]
    righthalf = alist[mid:]

    merge_sort(lefthalf)
    merge_sort(righthalf)

    i=0
    j=0
    k=0
    while i<len(lefthalf) and j<len(righthalf):
        if lefthalf[i]<righthalf[j]:
            alist[k]=lefthalf[i]
            i += 1
        else:
            alist[k]=righthalf[j]
            j += 1
        k=k+1

    while i<len(lefthalf):
        alist[k]=lefthalf[i]
        i += 1
        k=k+1

    while j<len(righthalf):
        alist[k]=righthalf[j]
        j += 1
        k=k+1


n = int(input("Введите число элементов: "))
alist = [random.random()*50 for _ in range(n)]
print(alist)
merge_sort(alist)
print(alist)