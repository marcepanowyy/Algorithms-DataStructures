class Node():
    def __init__(self):
        self.next = None
        self.value = None

# Funkcja, ktora przerabia tablice na liste jednokierunkowa

def tab2list(A):
    head = Node()
    tail = head
    for i in range(len(A)):
        x = Node()
        x.value = A[i]
        tail.next = x
        tail = x
    return head.next

# Funkcja, ktora wypisuje liste jednokierunkowa

def print_list(L):
    while L != None:
        print(L.value, "->", end=" ")
        L = L.next
    print("|")

# T = [9, 6, 0, 15]
# K = tab2list(T)
# print_list(K)


# Scalanie jednokierunkowych list i sortowanie list jednokierunkowych

def merge(K1, K2):
    head = Node()
    tail = head
    while K1 != None and K2 != None:
        if K1.value <= K2.value:
            tail.next = K1
            K1 = K1.next
        else:
            tail.next = K2
            K2 = K2.next

        tail = tail.next

    if K1 == None: tail.next = K2
    if K2 == None: tail.next = K1
    while tail.next != None: tail = tail.next

    return head.next, tail


# MergeSort na listach jednokierunkowych

def cut_list(L):
    if L is None:
        return None
    while L.next != None and L.next.get_value >= L.value:
        L = L.next

    H = L.next
    L.next = None
    return H

# dla 3->1->2->6->2->7>|
# L: 3->|
# H: 1->2->6->2->7->|

# T = [3, 1, 2, 6, 2, 7]
# L = tab2list(T)
# print_list(L)
# H = cut_list(L)
# print_list(L)
# print_list(H)

def merge_sort1(L): # O(n^2)
    if L is None:
        return None
    tail = cut_list(L)
    S = L
    L = tail
    while L != None:
        tail = cut_list(L)
        S, _ = merge(S, L)
        L = tail
    return S

def merge_sort2(L): # O(nlogn)

    # [1 7] [2 3 5] [1 2] [1]
    # zawsze startujemy od poczatku
    # znajdujemy pierwswza serie poczatkowa i druga
    # serie poczatkowa i je laczymy, powstaje:
    # [1 2 3 5 7], potem szukamy kolejnyhc dwoch serii
    # powstaje: [1 1 2]
    # potem [1 1 1 2 2 3 5 7]

    while True:
        NH = None
        NT = None
        while True:
            if L == None:
                L = NH
                break
            A = L
            L, T = cut_list(L)

            if NT == None and L == None:
                return A

            if L == None:
                NT.next = A
                L = NH
                break

            B = L
            L, _ = cut_list(L)

            X, T = merge(A, B)

            if NH == None:
                NH = X
            else:
                NT.next = X
            NT = T

# Dana jest tablica A, n elementowa, posortowana, liczba x
# Podaj algorytm znajdujacy indeksy i,j takie, ze A[i] + A[j] = x
# lub stwierdzajacy ze ich nie ma

def suma(t,x):
    i = 0
    j = len(t) - 1

    while i < j:

        if t[i] + t[j] == x:
            return True, i, j

        elif t[i] + t[j] < x:
            i += 1

        else:
            j -= 1

    return False


# Pojemniki z woda
# Dane prostokaty, nie nachodza na siebie, powierzchnia wody (2D)
# Dla danej powierzchni wody A
# Ile pojemnikow zostalo zapelnionych w calosci

T = [[[3,7], [5, 0]], [[6,1], [7,0]], [[0,1], [1,0]]]

def areaInTotal(T):                               # calculating the area of all the rectangles
    n = len(T)
    W = [0] * n
    total = 0
    for i in range(n):
        W[i] = abs(T[i][0][0] - T[i][1][0]) * abs(T[i][0][1]-T[i][1][1])
    for i in range(n):
        total += W[i]
    return total

def width(T):                                     # looking for the width of each rectangle in the array
    n = len(T)
    W = [0] * n
    for i in range(n):
        W[i] = abs(T[i][0][0] - T[i][1][0])
    return W

def howMany(T, A):        # T - opposite cords array, A - amount of water

    n = len(T)
    wid = width(T)        # wid - array of width
    t = areaInTotal(T)    # t - sum of all the rectangles' areas
    c, lvl = 0, 0         # counter = 0, level = 0

    if t >= A:

        while A > 0:

            for i in range(n):

                if T[i] != None:

                    if lvl == T[i][1][1]:
                        A -= wid[i]
                        T[i][1][1] += 1

            for i in range(n):

                if T[i]!= None:

                    if T[i][0][1] == T[i][1][1] and A >= 0:
                        c += 1
                        T[i] = None

            lvl += 1
    else:
        return n

    return c


x = (howMany(T, 4))
print(x)


# lider

def find_leader(arr):
    # Look for a hypothetic leader
    counter = 0
    candidate = None
    for val in arr:
        if not counter:
            counter = 1
            candidate = val
        elif val == candidate:
            counter += 1
        else:
            counter -= 1

    # If a counter is equal to 0 (or lower than 0), there must be no leader
    if counter <= 0:
        return None
    # Check if a leader candidate is a leader
    counter = 0
    for val in arr:
        if val == candidate:
            counter += 1
    if counter > len(arr) // 2:
        return candidate
    return None


def has_leader(arr):
    return find_leader(arr) is not None

