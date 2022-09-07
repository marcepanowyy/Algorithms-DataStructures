# [2pkt.]Zadanie3.
#
# Dana jest tablica A zawierająca n = len(A) liczb naturalnych. Dodatkowo wiadomo, że A w sumie zawiera k różnych liczb (należy
# założyć, że k jest dużo mniejsze niż n).Proszę zaimplementować funkcję Longestincomplete(A, k), która zwraca długość
# najdłuższego spójnego ciągu elementów tablicy A, w którym nie występuje wszystkie k liczb.
# (Można założyć, że podana wartość k jest zawsze prawidłowa.)
#
# Przykład Dla tablicy A = [1, 100, 5, 100, 1, 5, 1, 5]
# wartością wywołania longest_inconplete(A, 3) powinno być
# 4 (ciąg 1, 5, 1, 5 z końca tablicy).

def Longestincomplete(A, k):
    n = len(A)
    max = 0
    C = []

    for i in range(n):
        if A[i] not in C:
            C += [A[i]]

    for num in range(k):
        c = 0
        for i in range(n):
            if A[i] == C[num]:
                c = 0
            else:
                c += 1

            if c > max:
                max = c

    return max

T = [1, 100, 5, 100, 1, 5, 1, 5]
print(Longestincomplete(T, 3))

