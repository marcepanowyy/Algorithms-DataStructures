# 9.Cyfra jednokrotna to taka, która występuje w danej liczbie
# dokładnie jeden raz. Cyfra wielokrotna to taka, która w liczbie
# występuje więcej niż jeden raz.
#
# Mówimy, że liczba naturalna A jest ładniejsza od liczby
# naturalnej B, jeżeli w liczbie A występuje więcej cyfr
# jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo
# to ładniejsza jest ta liczba, która posiada mniej cyfr
# wielokrotnych. Na przykład: liczba 123 jest ładniejsza od 455,
# liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są
# jednakowo ładne.
#
# Dana jest tablica T zawierająca liczby naturalne. Proszę
# zaimplementować funkcję: pretty_sort(T), która sortuje elementy
# tablicy T od najładniejszych do najmniej ładnych. Użyty algorytm
# powinien być możliwie jak najszybszy. Proszę w rozwiązaniu
# umieścić 1-2 zdaniowy opis algorytmu oraz proszę oszacować
# jego złożoność czasową.

# zamieniamy liczbę na liczbę dwucyfrowa, pierwsza cyfra oznacza ilosc liczb jednokrotnych, druga cyfra oznacza 9-x,
# gdzie x to wystapienia cyfr wielokrotnych

import math

def dig_num(a):
    return math.floor((math.log10(a)))+1

def swap(a):
    d = dig_num(a)
    S = []
    B = [0] * 10
    f = 0               # first digit
    s = 0               # second digit
    while a > 0:
        S += [a%10]
        a //= 10
    for j in range(d):
        B[S[j]] += 1
    for k in range(10):
        if B[k] == 1:
            f += 1
        elif B[k] > 1:
            s += 1
    return f*10 + 9-s

# zmodyfikowany countsort

def count_sort(A, k):   # k - zakres liczb od 0 do k
    C = [0] * k                                                         # dla A=[1,3,2,4,0,4,2]
    B = [0] * len(A)                                                    # C=[1,1,2,2,1], bo 0 wystepuje raz, 1 wystepuje raz itp.
    for i in range(len(A)): # albo { for x in A
        C[A[i][1]] += 1        # C[x] += 1 }
    for i in range(1, k):   # ile liczb jest mniejszych
        C[i] += C[i-1]      # lub rownych i                            # C=[1,2,4,6,7]
    for i in range(len(A)-1, -1, -1):                                  # przegladam tablice od tylu
        C[A[i][1]] -= 1                                                # dla "2": 2 jest wieksza lub rowna od 4 liczb
        B[C[A[i][1]]] = A[i]                                           # wiec odejmuje 1 dostaje 3 (C = [1,2,3,6,7])
    for i in range(len(A)):                                            # i umieszczam na 3 pozycji dwojke w tablicy B itp.
        A[i] = B[i]

def pretty_sort(T):
    n = len(T)
    for i in range(n):
        T[i] = (T[i], swap(T[i]))

    count_sort(T, 110) # 110 bo najpiekniejsza liczba tyle wynosi xD
    S = []
    for i in range(n):
        S += [T[i][0]]
    return S

# T = [12, 525, 72, 902, 424, 567, 5775211, 561, 382, 5010]
# print(pretty_sort(T))