# rekurencyjne schody Amazona
# Dana jest tablica A zawierajaca liczby naturalne nie mniejsze od 1
# Poczatkowo stoimy na pozycji 0, wartosc A[i] informuje nas jaka jest
# maksymalna dlugosc skoku na nastepna pozycje

# Przyklad A = {1, 3, 2, 1, 0}

# z poycji 0 moge przejsc na pozycje 1. z pozycji 1 moge przejsc
# na pozycje 2,3,4

# na ile roznych sposobow mozna przejsc z pozycji 0 na pozycje n-1

# f(i) - ilosc sposobow na ktore mozemy przejsc od 0 do i
# f(n-1) = suma(f(i), ze mozemy przejsc od i do n-1)

