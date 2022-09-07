# Dane sa dwa zbiory liczb, reprezentowane jako tablice rozmiarow
# m i n, gdzie m jest znacznie mniejsze od n. Zaproponuj algorytm,
# ktory sprawdzi czy zbiory sa rozlaczne

# sortujemy tablice n: nlogn
# wyszukiwanie binarne: m logn (bo dla m elementow)
# wiec zlozonosc nlogn, bo n>m

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


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)

# from random import randint
#
# A = [randint(1, 1000) for i in range(100)]
# B = [randint(1, 1000) for i in range(10)]
#
# print(A)
# print(B)

def algorithm(A, B):
    n = len(A)
    m = len(B)
    quick_sort(A, 0, n - 1)
    for i in range(m):
        if binary_search(A,0,n-1,B[i]) != None:
            return False, B[i]
    return True

# print(algorithm(A,B))
