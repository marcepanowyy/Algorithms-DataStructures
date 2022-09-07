# Sciezka w drzewie

# to samo co na kolosie jakims XD

# Dane jest drzewo ukorzenione T, gdzie kazdy wierzcholek v
# ma potencjalnie ujemna wartosc value(v). Prosze zaproponowac
# algorytm, ktory znajduje wartosc najbardziej wartosciowej
# sciezki w drzewie T

# aint my solution

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path(root):
    global_max = float('-inf')

    def recur(node):
        if not node: return 0
        nonlocal global_max

        left_max = recur(node.left)
        right_max = recur(node.right)
        global_max = max(global_max, node.val + left_max + right_max)
        # No forks of a path are allowed (as a current path, treat only a path
        # which is a single line because as a final result we will take only
        # the a path which is a single line)
        curr_max = max(0, node.val + max(left_max, right_max))
        return curr_max

    recur(root)

    return global_max