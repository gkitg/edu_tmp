from collections import Counter, deque


def haffman_tree(s):
    # Считаем уникальные символы.
    count = Counter(s)
    # Сортируем по возрастанию количества повторений.
    sorted_elements = deque(sorted(count.items(), key=lambda item: item[1]))
    # Проверка если строка состоит из одного повторяющего символа.
    if len(sorted_elements) != 1:
        # Цикл для построения дерева
        while len(sorted_elements) > 1:
            # цикл объединяет два крайне левых элемента
            # Вес объединенного элемента
            weight = sorted_elements[0][1] + sorted_elements[1][1]
            # Словарь из 2 крайне левых элементов, попутно вырезаем их
            # из "sorted_elements".
            comb = {0: sorted_elements.popleft()[0],
                    1: sorted_elements.popleft()[0]}
            # Ищем место для вставки объединенного элемента
            for i, _count in enumerate(sorted_elements):
                if weight > _count[1]:
                    continue
                # Вставляем объеденный элемент
                sorted_elements.insert(i, (comb, weight))
                break
            else:
                # Добавляем объеденный корневой элемент после
                # завершения работы цикла
                sorted_elements.append((comb, weight))
    else:
        # приравниваемыем значение 0 к одному повторяющему символу
        weight = sorted_elements[0][1]
        comb = {0: sorted_elements.popleft()[0], 1: None}
        sorted_elements.append((comb, weight))
    return sorted_elements[0][0]


code_table = {}


def haffman_code(tree, path=''):
    # Если элемент не словарь. Заносим его, а так же его код в словарь
    # для кодировке. Если элемент словарь. Рекурсивно спускаемся вниз по
    # первому и второму значению.
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


s = "beep boop beer!"

haffman_code(haffman_tree(s))

for i in s:
    print(code_table[i], end=' ')
print()