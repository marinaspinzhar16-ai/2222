class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Функція пошуку мінімального значення
def find_min(root):
    if root is None:
        return None  # Дерево порожнє

    current = root
    while current.left is not None:
        current = current.left

    return current.key

# Приклад дерева
root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)

print("Найменше значення:", find_min(root))
