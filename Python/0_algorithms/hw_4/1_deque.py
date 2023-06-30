from collections import deque


n = int(input("Введите количество предприятий: "))

org_lst = []
for i in range(n):
    new_org = dict(name=input(f"Введите наименование предприятия {i+1}: "), qp=deque(), q_sum=0.0)
    for qn in range(1, 5):
        new_org['qp'].append(float(input(f"Введите доход предприятия {i+1} за {qn} квартал: ")))
    new_org['q_sum'] = sum(new_org['qp'])
    org_lst.append(new_org)
    print("-" * 5)

avg = sum(i.get('q_sum', 0.0) for i in org_lst) / n
print(f"Предприятия с общей прибылью выше среднего (среднее = {avg:.2f}):",
      ", ".join([f"{i.get('name')} ({i.get('q_sum')})" for i in org_lst if i.get('q_sum', 0.0) > avg]))

print(f"Предприятия с общей прибылью ниже среднего (среднее = {avg:.2f}):",
      ", ".join([f"{i.get('name')} ({i.get('q_sum')})" for i in org_lst if i.get('q_sum', 0.0) < avg]))