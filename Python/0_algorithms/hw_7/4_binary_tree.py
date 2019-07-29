from binarytree import tree, bst, Node


class MyNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


a = tree(height=4, is_perfect=False)
print(a)
b = bst(height=3, is_perfect=True)
print(b)

root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.right.right = Node(50)
root.left.left = Node(2)
print(root)

print('*' * 50)
c = tree(height=5, is_perfect=False)
print(c)
num = int(input('Какое число найти: '))


def search(bin_tree, number, path=''):
    if bin_tree.value == number:
        return f'Число {number} найдено по следующему пути:\nКорень{path}'
    if number < bin_tree.value and bin_tree.left is not None:
        return search(bin_tree.left, number, path=f'{path}\nШаг влево')
    if number > bin_tree.value and bin_tree.right is not None:
        return search(bin_tree.right, number, path=f'{path}\nШаг вправо')
    return f'Число {number} отсутсвует'


print(search(c, num))
