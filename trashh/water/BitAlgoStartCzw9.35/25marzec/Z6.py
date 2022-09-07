# Dana jest posortowana rosnaco tablica A wielkosci n zawierajaca
# parami rozne liczby naturalne. Podaj algorytm, ktory sprawdzi
# czy jest taki indeks i, ze A[i] == i. Co zmieni sie, jezeli liczby
# beda po prostu calkowite, niekoniecznie naturalne?

# jesli A[0] > 0 to nie istnieje taki indeks
# jesli A[0] = 0 to i = 0  o(1)
# jesli A[0] < 0 robimy binary search O(logn)
