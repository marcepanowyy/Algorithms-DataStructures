# Prosze zaproponowac algorytm, ktory dla talicy liczb calkowitych rozstrzyga
# czy kazda liczba z tablicy jest suma dwoch innych liczb z tablicy.
# Algorytm poiwnien byc jak najszybszy. Oszacuj zlozonosc obliczeniowa

# 1) posortuj tablice (nlogn)
# 2) ustawiamy 2 wskazniki na koniec i poczatek i szukamy sumy przesuwajac sie w prawo lub w lewo (n^2)

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

def algorithm(A):

    n = len(A)
    quick_sort(A, 0, n-1)

    for i in range(n):

        b, e = 0, n - 1
        Flag = False

        for j in range(n):
                if A[i] > A[b] + A[e] and b < e:
                    b += 1
                if A[i] < A[b] + A[e] and b < e:
                    e -= 1
                if A[i] == A[b] + A[e] and b < e:
                    Flag = True
                    break

        if Flag != True:
            return False, A[i]

    return True

# from random import randint
#
# A = [randint(0, 10) for i in range(10)]
# print(A)
# print(algorithm(A))