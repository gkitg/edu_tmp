import collections


n = int(input("Введите количество предприятий для расчета прибыли: "))
d = {}
for a, _ in enumerate(range(n), start=1):
    name = input("Введите название предприятия: ")
    pr = input("через пробел введите прибыль данного предприятия\nза каждый квартал(Всего 4 квартала): ")
    profit = pr.split(" ")
    d[name] = profit
    print()

fab = collections.Counter(d)

sc = []
b = 0
t = 0
for i, value in fab.items():
    summ = sum(int(j) for j in value)
    fab[i] = summ
    t += summ
    b += 1
sec = t / b

print(f"Средняя годовая прибыль всех предприятий: {str(sec)}")
bigger = []
smaller = []
for i, value_ in fab.items():
    if int(value_) >= sec:
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