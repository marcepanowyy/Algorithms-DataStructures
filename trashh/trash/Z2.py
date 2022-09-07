
from zad2testy import runtests


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None
        self.counter = 0

def add_to_tree(Tree, char):

    for letter in char:

        if letter == '0':
            if Tree.left is None:
                new_node = Node()
                new_node.value = 0
                new_node.counter = 1
                Tree.left = new_node
                Tree = Tree.left
            else:
                Tree = Tree.left
                Tree.counter += 1

        else:
            if Tree.right is None:
                new_node = Node()
                new_node.value = 1
                new_node.counter = 1
                Tree.right = new_node
                Tree = Tree.right
            else:
                Tree = Tree.right
                Tree.counter += 1


def double_prefix(L):
    Tree = Node()
    for char in L:
        add_to_tree(Tree, char)

    res = []

    def get_solution(Tree, new_char = ''):

        if Tree.right is not None and Tree.right.i >= 2:
            new_char += '1'
            Tree.right.i -= 1
            return get_solution(Tree.right, new_char)

        if Tree.left is not None and Tree.left.i >= 2:
            new_char += '0'
            Tree.left.i -= 1
            return get_solution(Tree.left, new_char)

        return new_char



    while Tree.left.i >= 2 or Tree.right.i >= 2:
        res.append(get_solution(Tree))

    return res

# L = ['0100', '0110', '1010', '1']






runtests(double_prefix)