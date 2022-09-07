# 1. Niech G = (V, E) będzie pewnym grafem nieskierowanym a U ⊆ V pewnym podzbiorem jego
# wierzchołków. Grafem indukowanym G|U nazywamy graf powstały z G przez usunięcie
# wszystkich wierzchołków spoza U. Proszę podać i zaimplementować wielomianowy algorytm,
# który mając na wejściu graf G = (V, E) (reprezentacja przez listy sąsiedztwa) oraz liczbę
# naturalną k, znajduje maksymalny co do rozmiaru zbiór U ⊆ V taki, że wszystkie wierzchołki
# w G|U mają stopień większy lub równy k. Proszę oszacować czas działania algorytmu.

# 1) usun wszystkie wierzcholki ktore maja stopien mniejszy od k

G1 = [[1,3],
     [0,2,3,5,6],
     [1,4,5,6,8],
     [0,1,6,7,8],
     [2,5,8],
     [1,2,4],
     [1,2,3,8],
     [3,8],
     [2,3,4,6,7]]

def count_vertex_degree(G):                                 # zwroc tablice stopni wszystkich wierzcholkow

    n = len(G)
    degree = [0] * n

    for u in range(n):
        degree[u] = len(G[u])

    return degree

def delete_vertex(G, u, degrees):                               # usun konkretny wierzcholek "u"

    n = len(G)
    degrees = count_vertex_degree(G)
    new_G = [[] for _ in range(n)]

    for s in range(n):
        if s != u:
            for v in G[s]:
                if v != u:
                    new_G[s].append(v)

        degrees[s] = len(new_G[s])

    return new_G, degrees


def delete_vertices(G, k):

    degrees = count_vertex_degree(G)
    n = len(G)
    U = []

    while True:                                                # petla while, dlatego ze po usunieciu ostatniego wierzcholka ktorego stopien byl mniejszy od k moze zepsuc stopnie reszty wierzcholkow

        counter = 0

        for v in range(n):                                      # usuwam wierzcholki, ktore maja stopien mniejszy od k, aktualizuje polaczenia w grafie oraz stopnie wierzcholkow po usunieciu
            if degrees[v] < k:
                G, degrees = delete_vertex(G, v, degrees)

        for v in range(n):                                     # sprawdzam czy stopnie wierzcholkow sa wyzerowane lub wieksze badz rowne k
            if degrees[v] == 0 or degrees[v] >= k:             # jezeli tak, zwiekszam licznik
                counter += 1

        if counter == n:                                       # sprawdzam czy wszystkie stopnie wierzcholkow sa wyzeorowane lub wieksze badz rowne k
            for v in range(n):
                if degrees[v] != 0:                            # jezeli to zachodzi, to podzbior U spelniajacy warunki  zadania
                    U.append(v)

            if len(U) > 0: return U, degrees
            return False


G2 = [[1,2,3],
      [0,2,6,5,7],
      [0,1,3,6],
      [0,6,2,4,5],
      [3,5],
      [4,3,6,1,7],
      [2,1,3,5],
      [1,5]]

G3 = [[1],
      [0,2,3],
      [1,5,3],
      [2,1,4],
      [3],
      [2],
      [8,7],
      [6,8],
      [6,7]]

# print(delete_vertices(G1, 3))
# print(delete_vertices(G2, 3))
# print(delete_vertices(G3, 2))


