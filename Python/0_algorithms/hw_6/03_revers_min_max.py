# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

from sum_memory_2 import sum_memory


SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

idx_min = 0
idx_max = 0
for i in range(len(array)):
    if array[i] < array[idx_min]:
        idx_min = i
    elif array[i] > array[idx_max]:
        idx_max = i

array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
print(array)

print(locals())     # пример того как выглядит "локальный 'словарь'"
print('*' * 50)
print(sum_memory(locals()))

