#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Администратор
#
# Created:     26.01.2019
# Copyright:   (c) Администратор 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import collections
import functools

nums = collections.defaultdict(list)
for d in range(2):
    n = input("Введите %d-е натуральное шестнадцатиричное число: " % (d+1))
    nums[f"{d + 1}-{n}"] = list(n)
print(nums)

sum = sum(int(''.join(i), 16) for i in nums.values())
print("Сумма: ", list('%X' % sum))

mult = functools.reduce(lambda a, b: a * b, [int(''.join(i), 16) for i in nums.values()])
print("Произведение: ", list('%X' % mult))
