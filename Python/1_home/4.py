# -*- coding: utf-8 -*-

__author__ = 'gkitg'


# Даны три  пары точек:
#   1.	A1(xa1, ya1), A2(xa2, ya2)
#   2.	B1(xb1, yb1), B2(xb2, yb2)
#   3.	С1(xс1, yс1), С2(xс2, yс2)
# Через данные пары точек проходят прямые a, b, c соответственно.
# Определить отношение между  прямыми (три прямые параллельны; две прямые параллельны; три прямые пересекаются и т.д.).
# Если три прямые пересекаются, более чем в одной точке, то они образуют треугольник.
# Вычислить площадь этого треугольника.
# Входные данные
# Шесть пар чисел типа float по четыре числа в строке — координаты точек, через которые проходят прямые.
# Вывод
# В первой строке вывести отношение между прямыми.
# Варианты:
# "a || b || c", если три прямые параллельны
# "a || b" или "a || с" или "b || с", если только две прямые параллельны
# "a /\ b /\ c", если три прямые пересекаются
# Во второй строке вывести площадь треугольника, если три прямые пересекаются, более чем в одной точке.
# В остальных случаях вывести 0.


def get_area(a, b, c):
    """
    Вычисление площади треугольника
    """
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def length_segment(x1: float, y1: float, x2: float, y2: float):
    """
    Вычисление длины отрезка
    """
    return (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5


def equation_straight_line(x1: float, y1: float, x2: float, y2: float):
    """
    Уравнение прямой
    """
    try:
        k = (y1 - y2) / (x1 - x2)
        b = y2 - k * x2
        return k, b
    except ZeroDivisionError:
        print('На 0 делить нельзя!')


def run(coords=None):
    try:
        if not coords:
            xa1, xa2, ya1, ya2 = list(
                map(float, input('Введите координаты прямой a четыре числа float через пробел: ').split(' ')))
            xb1, xb2, yb1, yb2 = list(
                map(float, input('Введите координаты прямой b четыре числа float через пробел: ').split(' ')))
            xc1, xc2, yc1, yc2 = list(
                map(float, input('Введите координаты прямой c четыре числа float через пробел: ').split(' ')))
        else:
            xa1, xa2, ya1, ya2 = coords[0]
            xb1, xb2, yb1, yb2 = coords[1]
            xc1, xc2, yc1, yc2 = coords[2]
    except ValueError:
        print('Вы ввели некорректные данные, введите координаты прямой типа float')
        return

    line_a = equation_straight_line(xa1, xa2, ya1, ya2)
    line_b = equation_straight_line(xb1, xb2, yb1, yb2)
    line_c = equation_straight_line(xc1, xc2, yc1, yc2)

    if line_a[0] == line_b[0] == line_c[0]:
        print("a || b || c")
    elif line_a[0] == line_b[0]:
        print("a || b")
        print(0)
    elif line_a[0] == line_c[0]:
        print("a || с")
        print(0)
    elif line_b[0] == line_c[0]:
        print("b || с")
        print(0)
    else:
        print("a /\ b /\ c")
        # пересечение line_a и line_b
        # line_a[0] * x + line_a[1] = line_b[0] * x + line_b[1]
        x1 = (line_b[1] - line_a[1]) / (line_a[0] - line_b[0])
        y1 = line_a[0] * x1 + line_a[1]
        # пересечение line_a и line_c
        x2 = (line_c[1] - line_a[1]) / (line_a[0] - line_c[0])
        y2 = line_a[0] * x2 + line_a[1]
        # пересечение line_b и line_c
        x3 = (line_b[1] - line_c[1]) / (line_c[0] - line_b[0])
        y3 = line_b[0] * x3 + line_b[1]

        a = length_segment(x1, y1, x2, y2)
        b = length_segment(x1, y1, x3, y3)
        c = length_segment(x2, y2, x3, y3)

        area = get_area(a, b, c)
        print(area)


run()