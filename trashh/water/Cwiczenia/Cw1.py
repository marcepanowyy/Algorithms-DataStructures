# Sortowanie w czasie O(n^2)

def selection_sort(T):
    n = len(T)
    for i in range(n):
        minIndex = i
        for j in range(i+1, n):
            if T[minIndex] > T[j]:
                minIndex = j
        T[minIndex], T[i] = T[i], T[minIndex]
    return T

# T = [9, 3, -2, 15, -10]
# print(selectionSort(T))

# Implementacja wstawianie Node'a do posortowanej
# listy jednokierunkowej

class Node:
    def __init__(self):
        self.next = None
        self.value = None

def insert_to_node(node, L):
    start = L
    while L.next != None and L.next.get_value < node.get_value:
        L = L.next

    node.next = L.next
    L.next = node


# Implementacja wypisywanie listy jednokierunkowej

def print_List(L):
    if L is not None:
        print(L.get_value, end=" ")
        print_List(L.next)
    else:
        print()

# L = Node()
# nnode = Node()
# nnode.value = 2
# L.next = nnode
# nn = Node()
# nn.value = 5
# nnode.next = nn
# print_List(L)
# a = Node()
# a.value = 1
# insert_to_node(a, L)
# print_List(L)
# b = Node()
# b.value = 3
# insert_to_node(b, L)
# print_List(L)
# c = Node()
# c.value = 7
# insert_to_node(c, L)
# print_List(L)

# Implementacja usuwania z listy jednokierunkowej
# najwiekszej liczby

def delMax(L):
    m = L.next
    m_prev = L
    prev = L
    L=L.next

    while prev.next != None:
        if prev.next.get_value > m.get_value:
            m_prev = prev
            m = prev.next
        prev = prev.next

    m_prev.next = m.next
    return L

# Funkcja odwracajaca kolejnosc wezlow w liscie

def reverse(L):
    if L is None:
        return

    prev = None
    nxt = L.next

    while L:
        L.next = prev
        prev = L
        L = nxt
        if nxt != None:
            nxt = nxt.next

    return prev


# Funkcja znajdujaca minimum i maksimum w tablicy o
# dl. n, wykonujaca 3/2n + C porownan

def min_max(T):
    l = len(T)
    minimal = float('inf')
    maximal = float('-inf')
    for i in range(0, l-1, 2):
        if T[i] < T[i+1]:
            T[i], T[i+1] = T[i+1], T[i]
        if T[i] > maximal:
            maximal = T[i]
        if T[i+1] < minimal:
            minimal = T[i+1]
    return maximal, minimal

# T = [1, 8, 12, -1, 10]
# print(min_max(T))


# Implementacja wyszukiwania binarnego w posortowanej
# tablicy, znajdujace najmniejszy indeks z dana wartoscia

def binary_search(T, b, e, x): # begin, end
    if b > e: return None
    c = (b + e) // 2
    if T[c] == x:
        res = binary_search(T, b, c-1, x)
        if res == None: return c
        return res
    if T[c] > x:
        return binary_search(T, b, c-1, x)
    else:
        return binary_search(T, c+1, e, x)


# T1 = [0, 5, 5, 5, 5, 5, 5, 5, 7, 8]
# print(binary_search(T1, 0, len(T1)-1, 5))

# for i in range(len(T1)):
#     print(i, binary_search(T1, 0, len(T1), T1[i]))





