# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

SIZE = 10
MIN_ITEM = -800
MAX_ITEM = -750
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

index = -100500
for i in range(len(array)):   # или for i in range(len(array)):
    if array[i] < 0 and index == -100500:
        index = i
    elif 0 > array[i] > array[index]:
        index = i
if index != -100500:
    print(f'Максимальное отрицательное число {array[index]} '
          f'находится в ячейке {index}')

# вариант 2
num = float('-inf')
for i, item in enumerate(array):
    if 0 > item > num:
        num = item
        index = i

if num != float('-inf'):
    print(f'Максимальное отрицательное число {num} '
          f'находится в ячейке {index}')
