# CountSort
# Chcemy posortowac pewna tablice rozmiaru n zawierajaca liczby od 0 do k-1 (dla liczb naturalnych)
# zachowuje stablinosc, O(n+k)

def count_sort(A, k):   # k - zakres liczb od 0 do k
    C = [0] * k                                                         # dla A=[1,3,2,4,0,4,2]
    B = [0] * len(A)                                                    # C=[1,1,2,2,1], bo 0 wystepuje raz, 1 wystepuje raz itp.
    for i in range(len(A)): # albo { for x in A
        C[A[i]] += 1        # C[x] += 1 }
    for i in range(1, k):   # ile liczb jest mniejszych
        C[i] += C[i-1]      # lub rownych i                            # C=[1,2,4,6,7]
    for i in range(len(A)-1, -1, -1):                                  # przegladam tablice od tylu
        C[A[i]] -= 1                                                   # dla "2": 2 jest wieksza lub rowna od 4 liczb
        B[C[A[i]]] = A[i]                                              # wiec odejmuje 1 dostaje 3 (C = [1,2,3,6,7])
    for i in range(len(A)):                                            # i umieszczam na 3 pozycji dwojke w tablicy B itp.
        A[i] = B[i]


T = [1, 9, 12, 0, 1, 14, 15, 2]
(count_sort(T, 16))
print(T)

# wyznaczyc element, ktory po posortowaniu tablicy
# znalalzby sie na pozycji k-tej

# przyklady elementarne
# k = 0 - min
# k = n-1 -> max

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def select(A, p, r, k):   # dziala w czasie liniowym
    if p == r:
        return A[p]
    q = partition(A, p, r)
    if q == k:
        return A[q]
    elif k<q:
        return select(A, p, q-1, k)
    else:
        return select(A, q+1, r, k)


