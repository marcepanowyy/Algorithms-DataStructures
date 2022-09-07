# Dana jest nieskonczona tablica A, gdzie pierwsze n pozycji zawiera poosrtowane
# liczby naturalne, a reszta tablicy ma wartosci None
# Nie jest dana wartosc n. Przedstaw algorytm, ktory dla danej
# liczby naturalnej x znajdzie indeks w tablicy, pod ktorym znajduje
# sie wartosc x. Jezeli nie ma jje w tablicy nalezy zwrocic None

# skaczemy od 2^i potegi, zaczynajac od indeksu 0, jezeli A[2^i] bedzie wieksze od x to wyszukujemy binarnie

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

