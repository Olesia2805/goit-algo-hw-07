"""Завдання 1

Напишіть алгоритм (функцію), який знаходить найбільше значення у двійковому дереві пошуку 
або в AVL-дереві. Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.

Завдання 2

Напишіть алгоритм (функцію), який знаходить найменше значення у двійковому дереві пошуку 
або в AVL-дереві. Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.

Завдання 3

Напишіть алгоритм (функцію), який знаходить суму всіх значень у двійковому дереві пошуку 
або в AVL-дереві. Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела."""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def print_tree(root, level=0, prefix=""):
    if root is None:
        return
    print_tree(root.right, level + 1, "R:")
    print(" " * 4 * level + prefix + str(root.val))
    print_tree(root.left, level + 1, "L:")

# Task 1. Finds the maximum value in the binary tree
def max_value(root):
    current = root
    while current.right:
        current = current.right
    return current.val

# Task 2. Finds the minimum value in the binary tree
def min_value(root):
    current = root
    while current.left:
        current = current.left
    return current.val

# Task 3. Finds the sum value in the binary tree
def sum_value(root):
    if root is None:
        return 0
    
    sum = root.val
    sum += sum_value(root.left)
    sum += sum_value(root.right)
    return sum

# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

max = max_value(root)
min = min_value(root)
sum = sum_value(root)

print("Binary Tree:")
print_tree(root)

print(f"Max value: {max};\nMin value: {min};\nSum value: {sum}")