# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

SIZE = 3
MIN_ITEM = 0
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)] for _ in range(SIZE)]

for line in matrix:
    print(*line, sep='\t')


max_ = None

for j in range(len(matrix[0])):
    min_ = matrix[0][j]

    for i in range(len(matrix)):
        if matrix[i][j] < min_:
            min_ = matrix[i][j]

    if max_ is None or max_ < min_:
        max_ = min_

print(f'Max in min = {max_}')

