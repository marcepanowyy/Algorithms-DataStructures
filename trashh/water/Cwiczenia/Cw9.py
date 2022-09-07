# Ćwiczenia 9: Zastosowania DFS i najkrótsze ścieżki
# Zadania obowiązkowe
# Zadanie 1. Proszę zaimplementować algorytm Dijkstry (dla wybranej przez prowadzącego reprezentacji
# grafu).

# DONE

# Zadanie 2. Proszę zaimplementować wybrany przez siebie algorytm obliczania minimalnego drzewa roz-
# pinającego dla wybranej przez prowadzącego reprezentacji grafu.

# KRUSKAL DONE

# Zadania standardowe

# Zadanie 1. (ścieżka Hamiltona w DAGu) Ścieżka Hamiltona to ścieżka przechodząca przez wszystkie
# wierzchołki w grafie, przez każdy dokładnie raz. W ogólnym grafie znalezienie ścieżki Hamiltona jest pro-
# blemem NP-trudnym. Proszę podać algorytm, który stwierdzi czy istnieje ścieżka Hamiltona w acyklicznym
# grafie skierowanym.

def topological_sort(G: 'graph represented using adjacency lists'):
    n = len(G)
    visited = [False] * n
    result = [None] * n
    idx = n

    def dfs(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs(v)
        nonlocal idx
        idx -= 1
        result[idx] = u

    for u in range(n):
        if not visited[u]:
            dfs(u)

    return result


def has_hamiltonian_path(G: 'DAG'):
    t_sorted = topological_sort(G)
    for i in range(len(t_sorted) - 1):
        u = t_sorted[i]
        for v in G[u]:
            # If we found a desired edge wich connects
            # the u vertex with the next topologically
            # sorted vertex
            if t_sorted[i + 1] == v:
                break
        # If a loop wasn't broken, there is no desired edge
        else:
            return False
    return True

# G = [[1,2],[2],[3],[]]
# res = has_hamiltonian_path(G)
# print(res)

# Zadanie 2. (dobry początek) Wierzchołek v w grafie skierowanym nazywamy dobrym początkiem jeśli
# każdy inny wierzchołek można osiągnąć scieżką skierowaną wychodzącą z v. Proszę podać algorytm, który
# stwierdza czy dany graf zawiera dobry początek.

def happy_beginnin(graph):

    def dfs_visit(u):
        nonlocal graph, visited
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs_visit(v)

    for v in range(len(graph)):
        visited = [False] * len(graph)
        dfs_visit(v)
        flag = 1
        for i in range(len(graph)):
            if visited[i] == False:
                flag = 0
                break
        if flag == 1:
            return True, v
    return False

# G = [[1,4],[2,3],[],[],[5],[],[4]]
# print(happy_beginnin(G))



# Zadanie 3. (najkrósze ścieżki w DAGu) Jak znaleźć najkrótsze ścieżki z wierzchołka s do wszystkich
# innych w acyklicznym grafie skierowanym?

def topological_sort(G: 'DAG represented by adjacency lists'):
    n = len(G)
    visited = [False] * n
    result = [None] * n
    idx = n

    def dfs(u):
        visited[u] = True
        for v, _ in G[u]:
            if not visited[v]:
                dfs(v)
        nonlocal idx
        idx -= 1
        result[idx] = u

    for u in range(n):
        if not visited[u]:
            dfs(u)

    return result


def shortest_paths(G: 'DAG represented by adjacency lists'):
    n = len(G)
    inf = float('inf')
    weights = [inf] * n
    t_sorted = topological_sort(G)
    weights[t_sorted[0]] = 0

    # Relax each neighbour of a vertex
    for u in t_sorted:
        for v, weight in G[u]:
            if weights[u] + weight < weights[v]:
                weights[v] = weights[u] + weight

    return weights


# Zadanie 4. (logarytmy) Mamy dany graf G = (V, E) z wagami w∶ E → N−{0} (dodatnie liczby naturalne).
# Chcemy znalezc scieżkę z wierzchołka u do v tak, by iloczyn wag był minimalny. Omówic rozwiązanie (bez
# implementacji)

# nakladamy logarytm na kazda krawedz, korzystamy z monotonicznosci tej funkcji. wi1, wi2, ..., win to szukane krawedzie
# minimalny iloczyn to wi1*wi2* ...*win. Po nalozeniu logarytmu dostajemy log(wi1*wi2* ...*win) = logwi1 + logwi2 + ... + logwin
# przeprowadzamy algorytm Dijkstry

import math

from queue import PriorityQueue


def dijkstra(G: 'graph represented by adjacency lists', s: 'source', t: 'target'):
    n = len(G)
    inf = float('inf')
    weights = [inf] * n
    parents = [None] * n
    pq = PriorityQueue()
    pq.put((0, s, None))

    while not pq.empty():
        min_w, u, parent = pq.get()
        # We will find the minimum total weight path only once so the
        # code below this if statement will be executed only once
        if min_w < weights[u]:
            weights[u] = min_w
            parents[u] = parent
            # Break a loop if we found a shortest path to the specified
            # target
            if u == t: break
            # Add all the neighbours of the u vertex to the priority queue
            for v, weight in G[u]:
                if weights[v] == inf:
                    pq.put((weights[u] + weight, v, u))

    return parents, weights

def get_path(parents, t):
    path = []

    while t is not None:
        path.append(t)
        t = parents[t]

    path.reverse()

    return path


def map_graph(G: 'graph represented by adjacency lists'):
    n = len(G)
    G2 = [[] for _ in range(n)]

    for u in range(n):
        for v, weight in G[u]:
            G2[u].append((v, math.log(weight)))

    return G2


def lowest_product_path(G: 'graph represented by adjacency lists', s: 'start vertex', t: 'target vertex'):
    G2 = map_graph(G)
    parents, weights = dijkstra(G2, s, t)

    if weights[t] == float('inf'):
        return -1, []

    # Reund a number as a product will always be int
    # because we have integer edges weights
    product = int(math.e ** weights[t] + 0.5)
    return product, get_path(parents, t)


# Zadanie 5. (problem przewodnika turystycznego) Przewodnik chce przewieźć grupę K turystów z
# miasta A do miasta B. Po drodze jest jednak wiele innych miast i między różnymi miastami jeżdzą autobusy o
# różnej pojemności. Mamy daną listę trójek postaci (x, y, c), gdzie x i y to miasta między którymi bezpośrednio
# jeździ autobus o pojemności c pasażerów.
# Przewodnik musi wyznaczyć wspólną trasę dla wszystkich tursytów i musi ich podzielić na grupki tak,
# żeby każda grupka mogła przebyć trasę bez rodzielania się. Proszę podać algorytm, który oblicza na ile
# (najmniej) grupek przewodnik musi podzielić turystów (i jaką trasą powinni się poruszać), źeby wszyscy
# dostali się z A do B.




# Zadanie 6. (dwóch kierowców) Dana jest mapa kraju w postaci grafu G = (V, E), gdzie wierzchołki to
# miasta a krawędzie to drogi łączące miasta. Dla każdej drogi znana jest jej długość (wyrażona w kilometrach
# jako liczba naturalna). Alicja i Bob prowadzą (na zmianę) autobus z miasta x ∈ V do miasta y ∈ V , zamienia-
# jąc się za kierownicą w każdym kolejnym mieście. Alicja wybiera trasę oraz decyduje, kto prowadzi pierwszy.
# Proszę zapropnować algorytm, który wskazuje taką trasę (oraz osobę, która ma prowadzić pierwsza), żeby
# Alicja przejechała jak najmniej kilometrów. Algorytm powinien być jak najszybszy (ale przede wszystkim
# poprawny).

from queue import PriorityQueue

def dijkstra(G: 'graph represented by adjacency lists', s: 'source', t: 'target'):

    n = len(G)
    inf = float('inf')
    weights = [[inf] * 2 for _ in range(n)]
    parents = [[None] * 2 for _ in range(n)]
    pq = PriorityQueue()

    # We will store in a pq queue tuples as follows:
    # (<Alice's distance>, <current vertex>, <parent vertex>, <flag indicating if
    # the last person who drives is Alice or Bob>)

    pq.put((0, s, None, 0))  # 0 - Alice starts
    pq.put((0, s, None, 1))  # 1 - Bob starts

    while not pq.empty():

        min_dist, u, parent, driver = pq.get()

        if min_dist < weights[u][driver]:
            weights[u][driver] = min_dist
            parents[u][driver] = (parent, int(not driver))
            # Break a loop if we found a shortest path to the specified
            # target
            if u == t: break
            # Add all the neighbours of the u vertex to the priority queue
            for v, weight in G[u]:
                # Add a path only if there hasn't been the shortest path yet
                # If the last was Alice and there is no shortest path to the v
                # vertex on which the last driver was Bob
                if driver == 0 and weights[v][1] == inf:
                    # Now Bob drives, so Alice's distance isn't updated
                    pq.put((min_dist, v, u, 1))
                # The last driver was Bob and there is no shortest path to
                # the v vertex on which Alice drives last
                elif weights[v][0] == inf:
                    # Now Alice drives, so distance is updated
                    pq.put((min_dist + weight, v, u, 0))

    return parents, weights

def get_path(parents, t, last_driver):
    path = []

    prev_driver = last_driver
    while t is not None:
        path.append(t)
        t, prev_driver = parents[t][prev_driver]

    path.reverse()

    return path, prev_driver


def drive_bus(G: 'graph represented by adjacency lists', s: 'source', t: 'target'):
    # Let's say that we return ALice as there is noting to drive
    if s == t: return 'Alice', -1, []
    parents, weights = dijkstra(G, s, t)
    inf = float('inf')
    last_driver = 0 if weights[t][0] < inf else 1
    # Check if there is a path from s to t
    if weights[t][last_driver] == inf:
        return '', -1, []
    path, first_driver = get_path(parents, t, last_driver)
    return 'Alice' if not first_driver else 'Bob', weights[t][last_driver], path

def directed_weighted_graph_list(E: 'array of edges'):
    # Find a number of vertices
    n = 0
    for e in E:
        n = max(n, e[0], e[1])
    n += 1
    # Create a graph
    G = [[] for _ in range(n)]
    for e in E:
        G[e[0]].append((e[1], e[2]))
        G[e[1]].append((e[0], e[2]))
    return G


E1 = [(0, 1, 8), (0, 2, 15), (0, 5, 12), (0, 10, 10), (0, 12, 30), (1, 4, 15), (1, 2, 4), (2, 3, 7), (3, 1, 10),
     (3, 4, 13), (4, 7, 14), (5, 6, 20), (5, 3, 18), (6, 4, 11), (6, 7, 8), (8, 7, 4), (9, 8, 12), (10, 5, 19),
     (10, 11, 25), (10, 7, 10), (11, 9, 60), (12, 11, 32), (9, 10, 25)]

E2 = [(0,1,1),(0,5,2),(5,2,1),(1,2,3),(2,3,6),(2,6,11),(6,4,1),(4,3,3),(6,7,2),(7,8,1)]

G = directed_weighted_graph_list(E2)
# for i in range(len(G)):
#     print(G[i])

print(drive_bus(G, 0, 8))



# Zadanie 7. (problem stacji benzynowych na grafie) Pewien podróżnik chce przebyć trasę z punktu A
# do punktu B. Niestety jego samochód spala dokładnie jeden litr paliwa na jeden kilometr trasy. W baku mieści
# się dokładnie D litrów paliwa. Trasa jest reprezentowana jako graf, gdzie wierzchołki to miasta a krawędzie to
# łączące je drogi. Każda krawędź ma długość w kilometrach (przedstawioną jako licza naturalna). W każdym
# wierzchołku jest stacja benzynowa, z daną ceną za litr paliwa. Proszę podać algorytm znajdujący trasę z
# punktu A do punktu B o najmniejszym koszcie. Proszę uzasadnić poprawność algorytmu.


