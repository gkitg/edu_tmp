import collections


n = int(input("Введите количество предприятий для расчета прибыли: "))
d = dict()
a = 1
for i in range(n):
    name = input("Введите название предприятия: ")
    pr = input("через пробел введите прибыль данного предприятия\nза каждый квартал(Всего 4 квартала): ")
    profit = pr.split(" ")
    d[name] = profit
    a += 1
    print()

fab = collections.Counter(d)

sc = []
b = 0
t = 0
for i in fab:
    summ = 0
    for j in fab[i]:
        summ += int(j)
    fab[i] = summ
    t += summ
    b += 1
sec = t / b

print("Средняя годовая прибыль всех предприятий: " + str(sec))
bigger = []
smaller = []
for i in fab:
    if int(fab[i]) >= sec:
        bigger.append(i)
    else:
        smaller.append(i)
print("Предприятия, с прибылью выше среднего значения: ", end = "")
for i in bigger:
    print(i, end = " ")
print()
print()
print("Предприятия, с прибылью ниже среднего значения: ", end = "")
for i in smaller:
    print(i, end = " ")
print()