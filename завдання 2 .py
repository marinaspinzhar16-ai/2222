class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Функція для обчислення суми всіх значень у дереві
def sum_tree(root):
    if root is None:
        return 0

    return root.key + sum_tree(root.left) + sum_tree(root.right)

# Приклад дерева
root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)

print("Сума всіх значень:", sum_tree(root))
