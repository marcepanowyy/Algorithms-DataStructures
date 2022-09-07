# Masz dana tablice zawierajaca n n>= 11 liczb naturalnych w zakresie
# [0, k]. Zamieniono 10 liczb z tej tablicy na losowe liczby spoza tego zakresu
# np duzo wieksze lub ujemne. Napisz algorytm, ktory posortuje tablicę w czasie O(n)

# przechodzisz po calej tablicy
# wywalasz liczby spoza tablicy
# pozostale sortujesz countsortem
# nastpenie wywalone liczby sortuje sie
# elementy wywalone wstawiasz z powrotem



import random

def make_random(T):
    n = len(T)
    upper_limit = max(T)+1
    index_arr = random.sample(range(0, n-1), 10)
    for i in range(10):
        T[index_arr[i]] = random.randint(upper_limit, 10**9)
    return T




def count_sort(A, k):   # k - zakres liczb od 0 do k (dla 5 k = 6)
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


def sort(T, k):
    n = len(T)
    i = 0
    odd_ones = []
    while len(T) != n-10:
        if T[i] > k:
            odd_one = T.pop(i)
            odd_ones += [odd_one]
        else:
            i += 1

    count_sort(T, k+1)
    odd_ones.sort()

    for i in range(10):
        T += [odd_ones[i]]
    return T


# zakres [0, 15]
T = [1, 14, 12, 12, 3, 8, 9, 1, 12, 4, 5, 1, 5, 15, 14, 12, 5, 4, 4, 12, 4, 9]
make_random(T)
print(sort(T, 15))