


# Problem plecakowy
# algorytm wielomianowy wzgl liczby przedmiotow
# i sumy ich profitow

# f(i,p) = min waga z przedmiotow 0,..., osiagajacych profit = p

# f(i,p) = f(i-1, p) dla p < P[i]
# f(i,p) = min(f(i-1,p), f(i-1, p-P[i] + W[i])



# Dane są ciągi a1, ..., an
# b1, ..., bn. prosze zaimplementowac algorytm
# znajdujacy ich najdluzszy wspolny podciag
# A: 1 7 3 2
# B: 7 2 4 2 3
# ODP: 7 3

# Problem wydawania monet
# x - kwota
# m1, ... mn - nominaly monet
# prosze podac algorytm wydajacy kwote x uzywajac
# jak najmniej monet
# np. x = 15
# nominaly: 1, 5, 8
# 15 -> 3x5
# 9 -> 1, 8

# f(x) = minimalna liczba monet do wydania x
# f(0) = 0
# f(x) = min(f(x-mj) + 1
#        po j od(1, n)

def coins(x, M):
    T = [x+1 for _ in range(x+1)]
    T[0] = 0
    for y in range(x+1):
        for m in M:
            if y >= m:
                T[y] = min(T[y], T[y-m]+1)
    print(T)
    return x

M = [1, 2, 5]
x = coins(13, M)

# wedrowka po tablicy
# tablica A dwuwymiarowa
# dojscie do prawego dolnego rogu
# koszt - suma pol
# prosze podac algorytm znajdujacy koszt najtanszego
# przejscia z lewego gornego rogu do prawego dolnego

def min_cost1(cost, row, col):

    for i in range(1, row):
        cost[i][0] += cost[i - 1][0]

    for j in range(1, col):
        cost[0][j] += cost[0][j - 1]

    for i in range(1, row):
        for j in range(1, col):
            cost[i][j] += (min(cost[i - 1][j], cost[i][j - 1]))

    return cost[row - 1][col - 1]

# Mamy ciag liczb: 5, 2, 7, 1, 6, 3, 8, 4, 2, 7
# k - liczba robotnikow
# chcemy zeby podzial pracy byl jak najbardziej sprawiedliwy
# wartosc podzialu - najmniejsza suma elementow w spojnym
# podciagu
# prosze podac algorytm znajdujacy podzial o max wartosci



# Prosze podac algorytm znajdujacy najdluzszy podciag rosnacy w czasie O(nlogn)



# Prosze pokazac jak przy pomocy algorytmu znajdujacego najdluzszy wspolny podciag rozwiazac problem najdluzszego podciagu rosnacego