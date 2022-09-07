# Dana jest tablica A oraz liczba k. Znalezc liczbe
# roznych par elementow z tablicy A o roznicy rownej k
# Przyklad: dla tablicy [7,11,3,7,3,9,5] oraz k =4
# odp to 3, bo (7,11), (7,3), (9,5)

# zakladam ze liczby calkowite

# zaczynamy jak przy countsorcie
# szukam par a nie wyniku :))

T = [10, 12, 4, 2, 22, 9]

def find(A, k):
    n = len(A)
    x = max(A)
    C = [0] * (x+1)
    S = []
    for i in range(n):
        C[A[i]] += 1
    a, b = 0, k
    for i in range(x-k+1):
        if C[a] > 0 and C[b] > 0:
            S += [(a, b)]
        a += 1
        b += 1

    return S

# A = [7, 11, 3, 7, 3, 9, 5]
# print(find(A, 4))


# jesli niecalkowite to mozna robic buckesortem
