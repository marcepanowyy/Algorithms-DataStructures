# tworze tablice wypelniona n wartosciami (magazyny). Nastepnie rozmieszczam wegiel po kolei do magazynow
# w zaleznosci od tego ktory moze przyjac okreslona wartosc. Szukamy ostatniego indeksu magazynu k, w ktorym mozemy
# rozmiescic ostatnia porcje.



# n**2

from egz2atesty import runtests


def coal(A, T):

    n = len(A)
    buckets = [T for _ in range(n)]

    for idx, value in enumerate(A):
        k = 0
        while buckets[k] < value:
            k += 1
        else:
            buckets[k] -= value

    return k


runtests( coal, all_tests = True )

# probowalem rowniez rozwiazac zadanie uzywajac drzewa bst. Jesli od obecnego node'a mozemy odjac wartosc val z tablicy A
# to to robimy, aktualizujemy pojemnosc i ustawiamy end_index (wartosc ktora nas interesuje).
# jesli nie mozemy, to rozpatrujemy 2 mozliwosci. jesli tree.capacity > T - val to znaczy, ze po odjeciu,
# mniejsza wartosc bedzie na lewo od obecnego node'a (dlatego drzewo BST), a jesli wieksza, to na prawo.
# niestety program nie prezchodzi wszystkich testow


# class Node:
#     def __init__(self, capacity, id):
#         self.capacity = capacity
#         self.id = id
#         self.right = None
#         self.left = None
#
#
#
# def create_tree(A, T):
#
#     tree = Node(T, 0)
#
#     def insert(tree, val):
#
#         nonlocal T, idx, end_idx
#
#         if tree.capacity >= val:
#             tree.capacity -= val
#             end_idx = tree.id
#
#         else:
#
#             if tree.capacity > T - val:
#
#                 if tree.left:
#                     tree = tree.left
#                     insert(tree, val)
#                 else:
#                     new_node = Node(T, idx + 1)
#                     idx += 1
#                     tree.left = new_node
#                     tree = tree.left
#                     insert(tree, val)
#
#             else:
#                 if tree.right:
#                     tree = tree.right
#                     insert(tree, val)
#
#                 else:
#                     new_node = Node(T, idx+1)
#                     idx += 1
#                     tree.right = new_node
#                     tree = tree.right
#                     insert(tree, val)
#
#     idx = 0
#     end_idx = 0
#
#     for val in A:
#         insert(tree, val)
#
#     return end_idx
#
# runtests( create_tree, all_tests = True )


