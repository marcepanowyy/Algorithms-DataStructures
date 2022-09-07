# Złożoność
#
# Obliczeniowa
# O(n * log(n)) - budowanie drzewa przedziałowego (sortowanie końców przedziałów odbywa się w tym czasie),
# O(log(n)) - wstawianie pojedynczego przedziału do drzewa,
# O(log(n) + k) - wypisywanie wszystkich przedziałów, w których zawiera się wskazana liczba, gdzie - liczba węzłów w drzewie, - liczba
# przedziałów, jakie otrzymamy jako rezultat,
#
# Pamięciowa
# O(n * log(n)) - w drzewie maksymalnie znajdzie się kopii każdego z przedziałów, a więc łącznie będzie tyle przedziałów
# n - liczba węzłów w drzewie


class ITNode:
    def __init__(self, key, span):
        self.key = key
        self.span = span
        self.parent = None
        self.intervals = []
        self.left = self.right = None

class IntervalTree:
    def __init__(self, spans, insert_spans=False):
        self.root = self.build_tree(self.get_coordinates(spans))
        if insert_spans:
            for span in spans:
                self.insert(span)

    def insert(self, span):
        l, r = span
        is_valid = True
        nodes_list = []

        def recur(node):
            # If a node represents a span which is contained in the inserted
            # span, we will add this span to a node's intervals list
            if l <= node.span[0] and node.span[1] <= r:
                nodes_list.append(node)
            # If the span inserted is no valid span
            elif node.key is None:
                nonlocal is_valid
                is_valid = False
                return
            # If the current node's key value splits inserted span, we have
            # to go left and right in a tree
            elif l < node.key < r:
                recur(node.left)
                recur(node.right)
            # If the current node's key is on the right side of the inserted
            # span, we have to go left
            elif r <= node.key:
                recur(node.left)
            # If the current node's key is on the left side, we have to go
            # right
            elif node.key <= l:
                recur(node.right)

        recur(self.root)

        if not is_valid:
            raise ValueError(f"Span '{span}' cannot be inserted")
        for node in nodes_list:
            node.intervals.append(span)

    def query(self, val):
        intervals = []

        def recur(node):
            if node.span[0] <= val <= node.span[1]:
                if node.key:
                    if val <= node.key: # change to < if want sharp inequality
                        recur(node.left)
                    elif val >= node.key: # change to > if want sharp inequality
                        recur(node.right)
                intervals.extend(node.intervals)

        recur(self.root)
        return intervals

    @staticmethod

    def build_tree(values):
        inf = float('inf')
        l = r = inf

        def recur(i, j, l=-inf, r=inf, parent=None):
        # Create a leaf node
            if i > j:
                node = ITNode(None, (l, parent.key) if l != parent.key else (parent.key, r))
                node.parent = parent
                return node

            mid = (i + j) // 2
            root = ITNode(values[mid], (l, r))
            root.parent = parent
            root.left = recur(i, mid - 1, l, values[mid], root)
            root.right = recur(mid + 1, j, values[mid], r, root)

            return root

        return recur(0, len(values) - 1)

    @staticmethod
    def get_coordinates(spans):
        # Create an array of sorted begin-end spans coordinates
        A = [c for span in spans for c in span]
        A.sort()
        # Filter out repeated values
        B = [A[0]]
        for i in range(1, len(A)):
            if A[i] != A[i - 1]:
                B.append(A[i])
        return B

# pomocniczy kod:

def binary_tree_string(tree_root, *, fn=lambda node: node.val):
    if not tree_root: return ''

    # Store data from a tree
    data = []
    lvl_nodes = [tree_root]
    just = 1

    while True:
        if not lvl_nodes: break

        curr_row = []
        branches = []
        next_nodes = []

        if not any(lvl_nodes):
            break

        for node in lvl_nodes:
            if not node:
                curr_row.append('')
                branches.extend([' ', ' '])
                next_nodes.extend([None, None])
            else:
                val = str(fn(node))
                just = max(len(val), just)
                curr_row.append(val)
            if node.left:
                next_nodes.append(node.left)
                branches.append('/')
            else:
                next_nodes.append(None)
                branches.append(' ')
            if node.right:
                next_nodes.append(node.right)
                branches.append('\\')
            else:
                next_nodes.append(None)
                branches.append(' ')

        data.append((curr_row, branches))
        lvl_nodes = next_nodes

    begin_sep = sep = 3 if just % 2 else 2
    data_iter = iter(data[::-1])
    result = [''] * (len(data) * 2 - 1)
    result[-1] = (' ' * sep).join(val.center(just) for val in next(data_iter)[0])

    # Format the tree string
    for i, (values, branches) in enumerate(data_iter):
        mul = 2 * i + 1
        # Values
        indent = (2 ** (i + 1) - 1) * (just + begin_sep) // 2
        sep = 2 * sep + just
        result[-(mul + 2)] = f"{' ' * indent}{(' ' * sep).join(val.center(just) for val in values)}"
        # Branches
        branch_indent = (3 * indent + just) // 4
        branches_row = []
        d_indent = indent - branch_indent
        branches_sep = ' ' * (2 * (d_indent - 1) + just)
        for i in range(0, len(branches), 2):
            branches_row.append(f"{branches[i]}{branches_sep}{branches[i + 1]}")
        result[-(mul + 1)] = f"{' ' * branch_indent}{(' ' * (sep - 2 * d_indent)).join(branches_row)}"
    return '\n'.join(result)





S = [[0, 10], [5, 20], [7, 12], [10, 15]]
it = IntervalTree(S, True)
# print(binary_tree_string(it.root, fn=lambda node: node.key))
# print(binary_tree_string(it.root, fn=lambda node: node.span))



# Problem sumy podprzedzialow

# Obliczeniowa
# O(n) - budowanie drzewa przedziałowego (tym razem nie sortujemy nic),
# O(log(n)) - znajdowanie sumy podprzedziału,
# O(log(n)) - modyfikacja pojedynczej wartości z przedziału (konieczne jest naprawienie sum w odpowiednich węzłach w czasie ),

# Pamięciowa
# O(n) - w drzewie znajdzie się maksymalnie elementów - na każdym poziomie wyżej razy mniej niż na poprzednim, a na ostatnim
# będzie dokładnie elementów, gdzie - liczba wartości w całym przedziale (otrzymujemy więc złożoność O(2 * n) = O(n))

class SegmentTree:
    def __init__(self, values):
        self.n = len(values)
        self.tree = self._create_tree(values)

    def __repr__(self):
        return f'SegmentTree({self.tree[self.n:]})'

    def update(self, idx, value):
        i = self.n + idx
        diff = value - self.tree[i]
        # Update all parents sums
        while i: # Root has 1 index so we can loop till an index is non-zero
            self.tree[i] += diff
            i //= 2 # Move to the parent's node

    def get_sum(self, a: 'first number index', b: 'last number index'):
        total = 0

        def recur(idx=1, i=0, j=self.n-1):
            if a <= i and j <= b:
                nonlocal total
                total += self.tree[idx]
            else:
                mid = (i + j) // 2
                if mid < a:
                    recur(2 * idx + 1, mid + 1, j)
                elif mid >= b:
                    recur(2 * idx, i, mid)
                else:
                    recur(2 * idx + 1, mid + 1, j)
                    recur(2 * idx, i, mid)

        recur()
        return total

    def _create_tree(self, values):
        n = len(values)
        arr = [None] * (2 * n)

        for i in range(n):
            arr[n + i] = values[i]

        for i in range(n - 1, 0, -1):
            arr[i] = arr[2 * i] + arr[2 * i + 1]

        return arr

A = [1, 7, 2, 3, 6, 1, 3, 4]
st = SegmentTree(A)
# print(st.tree)
# print(st.get_sum(2, 5))
# print(st.get_sum(5, 5))
# print(st.get_sum(1, 5))

