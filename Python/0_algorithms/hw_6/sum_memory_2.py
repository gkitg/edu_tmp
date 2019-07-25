# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# (в рамках первых трех уроков)

import sys


def sum_memory(objects):
    sum_mem = 0
    unique_id = set()
    for key, value in objects.items():
        if key.startswith('__'):
            # убираем "магию"
            continue
        elif hasattr(value, '__call__'):
            # убираем функции
            continue
        elif hasattr(value, '__loader__'):
            # убираем модули
            continue
        elif id(value) in unique_id:
            # убираем объекты (переменные), которые уже попали в сумму
            continue
        else:
            unique_id.add(id(value))
            sum_mem += sys.getsizeof(value)
            print(f'переменная {key} класса {type(value)} хранит {value} '
                  f'и занимает {sys.getsizeof(value)} байт')

    return sum_mem
