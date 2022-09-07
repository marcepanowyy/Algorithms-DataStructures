# zaproponuj klase reprezentujaca str danych, kotra w kosntruktorze
# dostaje tablice liczb naturlanych dlugosci n o zakresie wartosci [0, k]
# ma ona posiadac metode count_num_in_range(a,b) - ma ona zwracac
# informacje o tym, ile liczb w zakresie [a, b] bylo w tablicy, ma dzialac
# w czasie O(1). Mozna zalozyc, ze zawsze a >= 1 i b <= k

def count_sort(A, k):
    C = [0] * k
    B = [0] * len(A)
    for i in range(len(A)):
        C[A[i]] += 1
    for i in range(1, k):
        C[i] += C[i-1]
    for i in range(len(A)-1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
    for i in range(len(A)):
        A[i] = B[i]

from random import randint

def random_tab_generator(n, k):
    T = []
    for i in range(n):
        T += [randint(0, k)]
    return T


def count_identical(T, k):

    n = len(T)
    count_sort(T, k+1)

    for i in range(n):
        T[i] = [T[i], 1]

    i = 1
    while i < len(T):
        if T[i-1][0] == T[i][0]:
            T[i-1][1] += 1
            T.pop(i)
        else:
         i+= 1

def how_many(T, k, a, b):
    count_identical(T, k)
    n = len(T)
    counter, i, = 0, 0
    while i < n:
        if T[i][0] >= a and T[i][0] <= b:
            counter += T[i][1]

        i += 1

    return counter

T = random_tab_generator(25, 15)
res = how_many(T, 15, 5, 7)
print(res)