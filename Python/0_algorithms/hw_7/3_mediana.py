# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найти в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой – не больше ее.

import random


# вариант 1
def median_square(array):
    for i in range(len(array)):
        smaller = equal = bigger = 0
        for j in range(len(array)):
            if array[i] < array[j]:
                smaller += 1
            elif array[i] > array[j]:
                bigger += 1
            else:
                equal += 1
        equal -= 1

        if smaller == bigger or smaller == equal + bigger or smaller + equal == bigger:
            return array[i]


# вариант 2
def partition(array, pivot):
    smaller = []
    equally = []
    bigger = []
    for item in array:
        if item < pivot:
            smaller.append(item)
        elif item > pivot:
            bigger.append(item)
        else:
            equally.append(item)
    return smaller, equally, bigger


def top_key(array, key):
    pivot = array[random.randrange(len(array))]
    left, middle, right = partition(array, pivot)

    if len(left) == key:
        return left
    if len(left) < key <= len(left) + len(middle):
        return middle
    if len(left) > key:
        return top_key(left, key)
    return top_key(right, key - len(left) - len(middle))


def median(array):
    result_list = top_key(array, len(array) // 2 + 1)
    return max(result_list)


SIZE = 4
LIMIT = 100
data = [random.randrange(0, LIMIT) for _ in range(2 * SIZE + 1)]
print(data)
print(f'mediana_square = {median_square(data)}')
print(data)
print(f'mediana = {median(data)}')
print(data)
print(sorted(data))


# вариант 3
import statistics  # sorry за импорт внизу :-)

print('*' * 50)
print(data)
print(f'mediana = {statistics.median(data)}')
print(sorted(data))

