# Implementacja Qsorta tak, by zawsze uzywal
# najwyzej O(logn) dod. pamieci

from random import randint

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quicksort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        if q - p < r - q:         #sprawdzamy ktora czesc po wybraniu piwota jest dluzsza
            quicksort(A, p, q-1)
            p = q + 1
        else:
            quicksort(A, q+1, r)
            r = q - 1

def qs(A, p, r):
    pivot = partition(A, p, r)
    if p < r:
        qs(A, p, pivot-1)
        qs(A, pivot+1, r)

# T = [1, 9, 2, 2, 9, 10, 2, 7, 4]
# qs(T, 0, len(T)-1)
# print(T)

# S(n) = S(n/2) + c = S(n/4) + 2c = c*logn

# n = 11
# T = [randint(0, 20) for i in range(n)]
# print(T)
# quicksort(T, 0, len(T)-1)
# print(T)


# Prosze zaimplementowac jak najszybszy algorytm
# sortujacy n elementowa tablice, zawierajaca
# liczby ze zbioru [0, 1, 2, .., n^2 -1]


# Implementacja funkcji wstawiajacej dowolny
# element do kopca binarnego

def parent(i):
    return (i-1)//2

def ins(T, key, n):
    T[n] = key                                  # wstawiam element do ostatniej komorki
    i = n
    while i > 0 and T[i] > T[parent(i)]:        # naprawiamy kopiec
        T[i], T[parent(i)] = T[parent(i)], T[i]
        i = parent(i)

# Qsort iteracyjnie
# S = []
# S.append(x) <-- push
# S.pop(x) <-- pop
# len(S) == 0 <-- is empty

def it_qsort(T):
    S = []
    p = 0
    r = len(T) - 1
    S.append((p, r))
    while len(S) > 0:
        (p,r) = S.pop()
        if p < r:
            q = partition(T,p,r)
            if q - p > r - q:
                S.append((p,q-1))
                S.append((q+1, r))
            else:
                S.append((q+1,r))
                S.append((p,q-1))

from random import randint

# T = [randint(1, 10) for i in range(10)]
# print(T)
# it_qsort(T)
# print(T)

# Dana jest tablica n liczb. Proszę
# zaimplementować algorytm czy pewna
# liczba występuje w ciągu więcej niż n/2 razy
# 1, 7, 2, 7, 7

def leader(T):
    c = 1
    l = T[0]
    for i in range(1, len(T)):
        if l == T[i]:
            c += 1
        else:
            if c > 0:
                c -= 1
            else:
                l = T[i]
                c = 1
    c = 0
    for i in range(len(T)):
        if T[i] == l:
            c += 1

    if c > len(T) // 2:
        return l
    return None

# x = leader([2,3,2,4,5,2,2,2,5,2])
# print(x)

# Najwiekszy przedzial
# Dany ciag przedzialow [a1, b1],...,[an, bn]
# Proszę zaproponowac algorytm, który znajduje
# przedział zawierający najwięcej pozostałych
# przedziałów

# f(x) = liczba przedzialow, ktore zaczynaja
# sie na pozycji x lub wczesniej
# g(x) = liczba przedzialow, ktora konczy
# sie na pozycji x lub wczesniej


# Proszę zaproponować strukturę danych
# która realizuje nastepujace operacje
# w czasie O(logn):
# a) insert, remove_min, remove_max  2 kopce min i max
# struktur apowinna trzymac wartosc i indeks w tym drugim kopcu z kopca max wskaznik na elementy w kopcu min
# b) insert, remove_median




