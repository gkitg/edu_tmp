# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

N = 10
MIN_ITEM = -800
MAX_ITEM = -750
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(N)]
print(array)

# 1 вариант
idx_min = 0
idx_max = 0
for i in range(len(array)):
    if array[i] < array[idx_min]:
        idx_min = i
    elif array[i] > array[idx_max]:
        idx_max = i

array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
print(array)

print('=' * 20)

# 2 вариант как пример асимптотической сложности
# O(n) против O(n) * (1 + 1 + 0.5 + 0.5)
min_num = min(array)
max_num = max(array)
idx_min = array.index(min_num)
idx_max = array.index(max_num)
array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
print(array)
