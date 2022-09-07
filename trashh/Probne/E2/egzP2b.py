from egzP2btesty import runtests
from math import log10

class Node:
    def __init__(self, value, id):
        self.value = value
        self.id = id
        self.right = None
        self.left = None

def create_tree(D):

    tree = Node(0, None)

    def add_2_tree(str, tree):
        for bit in reversed(str):
            if bit == '1':
                if tree.right:
                    tree = tree.right
                    tree.value += 1
                else:
                    new_node = Node(1, '1')
                    tree.right = new_node
                    tree = tree.right

            else:
                if tree.left:
                    tree = tree.left
                    tree.value += 1
                else:
                    new_node = Node(1, '0')
                    tree.left = new_node
                    tree = tree.left

    for str in D:
        add_2_tree(str, tree)



    return tree


D = ["1100", "100", "0", "1111", "1101"]
Q = ["", "1", "11", "0", "1101"]


def kryptograf(D, Q):

    tree = create_tree(D)
    sum_ = 0
    if tree.left: sum_ += tree.left.value
    if tree.right: sum_ += tree.right.value
    tree.value = sum_
    res = 1

    def dfs(str, tree):

        for bit in reversed(str):
            if bit == '1':
                tree = tree.right
            else:
                tree = tree.left

        return tree.value


    for str in Q:
        res *= dfs(str, tree)

    return log10(res)

# kryptograf(D, Q)

# Zmień all_test na:
# 0 - Dla małych testów
# 1 - Dla złożoności akceptowalnej
# 2 - Dla złożoności dobrej
# 3 - Dla złożoności wzorcowej

runtests(kryptograf, all_tests = 3)