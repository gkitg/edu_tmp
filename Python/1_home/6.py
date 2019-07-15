# -*- coding: utf-8 -*-

__author__ = 'gkitg'


# Описать декоратор для функции, выводящий название функции,
# переданные ей аргументы и время её выполнения.

import time


def doc_deco(func):
    def wrap(*args, **kwargs):
        t_start = time.time()
        print('Имя функции:', func.__name__)
        print('Кортеж аргументов:', args)
        print('Словарь аргументов:', kwargs)
        result = func(*args, **kwargs)
        print('Результат:', result)
        t_stop = time.time()
        print('Время выполнения:', t_stop - t_start, 'ms')
        return result
    return wrap


@doc_deco
def add_int(a, b):
    return a + b


add_int(5, 9)