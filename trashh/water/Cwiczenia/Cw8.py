# Ćwiczenia 8: Grafy, BFS i DFS

from queue import Queue

# Zadania obowiązkowe

# Zadanie 1. (Pause) Znany operator telefonii komórkowej Pause postanowił zakonczyc działalnosc w
# Polsce. Jednym z głównych elementów całej procedury jest wyłaczenie wszystkich stacji nadawczych (które
# tworza spójny graf połaczen). Ze wzgledów technologicznych urzadzenia nalezy wyłaczac pojedynczo a operatorowi
# dodatkowo zalezy na tym, by podczas całego procesu wszyscy abonenci znajdujacy sie w zasiegu
# działajacych stacji mogli sie ze soba łaczyc (czyli by graf pozostał spójny). Proszę zaproponować algorytm
# podający kolejność wyłączania stacji.


# Zadanie 2. (cykl na cztery) Dany jest graf nieskierowany G zawierający n wierzchołków. Zaproponuj
# algorytm, który stwierdza czy w G istnieje cykl składający się z dokładnie 4 wierzchołków. Zakładamy, że
# graf reprezentowany jest przez macierz sasiedztwa A.

def swap(G):
    n = len(G)
    G2 = [[] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if G[u][v]: G2[u].append(v)
    return G2

def find_cycle_of_4(graph):

    n = len(graph)
    paths = [0 for _ in range(n)]

    for v in range(n):  # O(n)

        for i in range(n):  # O(n)
            if graph[v][i]:
                for j in range(n):  # O(n)
                    if graph[i][j] and j != v:
                        paths[j] += 1

        for k in range(n):  # O(n)
            if paths[k] >= 2:
                res = [v]
                i = 2
                for q in range(n):  # O(n)
                    if graph[v][q] == graph[k][q] == 1:
                        res.append(q)
                        if i == 1:
                            res.append(k)
                        i -= 1
                    if i == 0:
                        break
                res.append(v)
                print(res)
                return True

    return False


test1 = [[0, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 0]]
# print(find_cycle_of_4(test1))


test2 =    [[0, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 1, 0]]
# print(find_cycle_of_4(test2))


# Zadania standardowe

# Zadanie 1. (DFS/BFS) Proszę zaimplementować następujące algorytmy:
# 1. Sprawdzanie czy graf jest dwudzielny (czyli zauważyć, że to 2-kolorowanie i użyć DFS lub BFS).
# 2. Policzyć liczbę spójnych składowych w grafie (implementacja przeciwna do tej z poprzedniego zadania)

# a)

def if_bipartite(graph, s):

    queue = Queue()
    visited = [False] * len(graph)
    map = [None] * len(graph)

    queue.put(s)
    visited[s] = True
    map[s] = 0

    while not queue.empty():
        u = queue.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.put(v)
                if map[u] == 0:
                    map[v] = 1
                else:
                    map[v] = 0

            if map[v] == map[u]:
                return False

    return True

# G = [[1,5,6], [0,2], [1,3, 6], [2,4], [3,5], [0,4], [0,2]]
# if_bipartite(G, 0)

# G = [[1],[0,2],[1,3],[1,2]]
# print(if_bipartite(G, 0))

G1 = [[1, 2],
     [0, 3, 4],
     [0, 3, 5],
     [1, 2],
     [1, 5],
     [2, 4]]

G2 = [[4, 6],
      [4, 5],
      [5, 6],
      [4, 6],
      [0, 1, 3],
      [1, 2],
      [0, 2, 3]]

# print(if_bipartite(G1, 0))
# print(if_bipartite(G2, 0))

# b)

def count_connected_components(G: 'graph represented using adjacency lists'):

    n = len(G)
    visited = [False] * n

    def dfs(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs(v)

    count = 0
    for u in range(n):
        if not visited[u]:
            count += 1
            dfs(u)

    return count

# G = [[1,2],[0,2],[0,1],[4],[3], [6], [5], []]
# print(count_connected_components(G))


# Zadanie 2. (uniwersalne ujście) Mówimy, że wierzchołek t w grafie skierowanym jest uniwersalnym
# ujściem, jeśli (a) z każdego innego wierzchołka v istnieje krawędź z v do t, oraz (b) nie istnieje żadna krawędź
# wychodząca z t.
# 1. Podać algorytm znajdujący uniwersalne ujście (jeśli istnieje) przy reprezentacji macierzowej (O(n2)).
# 2. Pokazać, że ten problem można rozwiazac w czasie O(n) w reprezentacji macierzowej.

# szukamy wierzcholka z ktorego nie wychodza zadne krawedzie wiec wiersz tego wierzcholka ma wartosci 0 oraz
# wszystkie pozostale wierzcholki maja krawedz wychodzaca do tego wierzcholka wiec w kolumnie wszedzie 1 poza punktem T[v][v]
# przyklad:
'''
0 1 0 0 0 0
0 0 0 0 0 0
0 1 0 0 0 0
0 1 0 0 0 0
0 1 0 0 0 0 
'''

# wierzcholek 1 jest uniwersalnym ujciem


# Zadanie 3. (BFS i najkrótsze ścieżki) Proszę zaimplementować algorytm BFS tak, żeby znajdował
# najkrótsze ścieżki w grafie i następnie, żeby dało się wypisać najkrotszą ścieżkę z zadanego punktu startowego
# do wskazanego wierzchołka.

from queue import Queue

def distance(graph, s, q):

    queue = Queue()

    visited = [False] * len(graph)
    distance = [float("-inf")] * len(graph)
    parent = [-1] * len(graph)
    parent[0] = None
    distance[0] = 0

    queue.put(s)
    visited[s] = True

    while not queue.empty():
        u = queue.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                queue.put(v)
                distance[v] = distance[u] + 1

    res = []
    res.append(q)

    while parent[q] != None:
        res.append(parent[q])
        q = parent[q]

    return distance, parent, res



# G = [[1,4,5],[0,2],[1,3],[2,6],[0,7],[0,7],[3,7],[4,5,6]]
# print(distance(G, 0, 6))


# Zadanie 4. (malejące krawędzie) Dany jest graf G = (V, E), gdzie każda krawędź ma wagę ze zbioru
# {1, . . . , ∣E∣} (wagi krawędzi są parami różne). Proszę zaproponować algorytm, który dla danych wierzchołków
# x i y sprawdza, czy istnieje ścieżka z x do y, w której przechodzimy po krawędziach o coraz mniejszych wagach.


def is_path(G: 'undirected graph represented by adjacency matrix', x: 'source', y: 'target'):
    n = len(G)

    def dfs(u, weight):
        # Return True if visited the target
        if u == y: return True
        for v in range(n):
            # If there is an edge (G[u][v] != 0) and it hasn't been
            # visited yet (G[u][v] > 0) and its weight is smaller than the
            # previous one, visit the next vertex going through this edge
            if 0 < G[u][v] < weight:
                w = G[u][v]
                G[u][v] = G[v][u] = -G[u][v]  # Mark as visited
                if dfs(v, w): return True  # Return True if a path was found
        return False

    res = False
    # Start a DFS from each vertex we can visit from the source
    for v in range(n):
        if G[x][v] > 0:  # If there is an unvisited edge
            w = G[x][v]
            G[x][v] = G[v][x] = -G[x][v]  # Mark as visited
            # If found a path, break the loop and store the result
            if dfs(v, w):
                res = True
                break

    # Fix a matrix (restore original values)
    for u in range(n):
        for v in range(n):
            G[u][v] = abs(G[u][v])

    return res


def undirected_graph_matrix(E: 'array of edges'):
    # Calculate a number of vertices
    n = 0
    for edge in E:
        n = max(n, edge[0], edge[1])
    n += 1
    # Create a graph matrix
    G = [[0] * n for _ in range(n)]  # 0 means no edge
    for edge in E:
        G[edge[0]][edge[1]] = edge[2]  # edge[2] is weight
        G[edge[1]][edge[0]] = edge[2]
    return G


M = [[0, 8, 0, 9, 0, 0],
     [8, 0, 2, 0, 3, 0],
     [0, 2, 0, 6, 0, 0],
     [9, 0, 6, 0, 3, 0],
     [0, 3, 0, 3, 0, 2],
     [0, 0, 0, 0, 2, 0]]

# print(is_path(M,1,5))

# Zadanie 5. (krawędzie 0/1) Dana jest mapa kraju w postaci grafu G = (V, E). Kierowca chce przejechać
# z miasta (wierzchołka) s do miasta t. Niestety niektóre drogi (krawędzie) są płatne. Każda droga ma taką
# samą jednostkową opłatę. Proszę podać algorytm, który znajduje trasę wymagającą jak najmniejszej liczby
# opłat. W ogólności graf G jest skierowany, ale można najpierw wskazać algorytm dla grafu nieskierowanego.

from queue import PriorityQueue


def dijkstra(G: 'graph represented by adjacency lists', s: 'source', t: 'target'):
    n = len(G)
    inf = float('inf')
    visited = [False] * n
    parents = [-1] * n
    dist = [inf] * n
    dist[s] = 0
    # Initialize a priority queue where we will store (vertex, min distance) pairs
    # sorted by the minimum priority
    pq = PriorityQueue()
    pq.put((0, s))

    while not pq.empty():
        min_dist, u = pq.get()
        visited[u] = True  # Mark as visited
        # Skip a vertex if there was already found a better distance
        if dist[u] < min_dist: continue
        # Loop over all the neighbours and check if we can update some of them
        for v, weight in G[u]:
            if visited[v]: continue
            new_dist = dist[u] + weight
            # Update the distance from source to v vertex if found a shorter path
            if new_dist < dist[v]:
                dist[v] = new_dist
                parents[v] = u
                pq.put((new_dist, v))
        # Stop a while loop if we have already found a distance to the target
        if u == t: return dist[u], parents

    # Otherwise, we cannot reach the target
    return inf, []


def restore_path(parents, s, t):
    path = [t]
    u = t
    while parents[u] != s:
        u = parents[u]
        path.append(u)
    path.append(s)
    # Reverse a path to get subsequent vertices in the right order
    return path[::-1]


def min_cost_path(G: 'graph represented by adjacency lists', s: 'source', t: 'target'):
    cost, parents = dijkstra(G, s, t)
    # Return None if there is no path from the source to the target
    if cost == float('inf'): return None
    return cost, restore_path(parents, s, t)


def undirected_graph_list(E: 'array of edges'):
    # Calculate a number of vertices
    n = 0
    for edge in E:
        n = max(n, edge[0], edge[1])
    n += 1
    # Create a graph array
    G = [[] for _ in range(n)]
    for edge in E:
        G[edge[0]].append((edge[1], edge[2]))  # edge[2] is a weight of an edge
        G[edge[1]].append((edge[0], edge[2]))  # edge[2] is a weight of an edge
    return G

# Zadanie 6. (bezpieczny przelot) Dany jest graf G = (V, E), którego wierzchołki reprezentują punkty
# nawigacyjne nad Bajtocją, a krawędzie reprezentują korytarze powietrzne między tymi punktami. Każdy
# korytarz powietrzny ei ∈ E powiązany jest z optymalnym pułapem przelotu pi ∈ N (wyrażonym w metrach).
# Przepisy dopuszczają przelot danym korytarzem jeśli pułap samolotu różni się od optymalnego najwyżej o t
# metrów. Proszę zaproponować algorytm (bez implementacji), który sprawdza czy istnieje możliwość przelotu
# z zadanego punktu x ∈ V do zadanego punktu y ∈ V w taki sposób, żeby samolot nigdy nie zmieniał pułapu.
# Algorytm powinien być poprawny i możliwie jak najszybszy. Proszę oszacować jego złożoność czasową.


# Zadanie 7. (kosztowna szachownica) Dana jest szachownica o wymiarach n × n. Każde pole (i, j)
# ma koszt (liczbę ze zbioru {1, . . . , 5}) umieszczony w tablicy A (na polu A[j][i]). W lewym górnym rogu
# szachownicy stoi król, którego zadaniem jest przejsc do prawego dolnego rogu, przechodzac po polach o
# minmalnym sumarycznym koszcie. Prosze zaimplementowac funkcje kings path(A), która oblicza koszt
# sciezki króla. Funkcja powinna byc mozliwie jak najszybsza.

from queue import PriorityQueue

def dijkstra(G: 'grid'):

    moves = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    n = len(G)
    inf = float('inf')
    visited = [[False] * n for _ in range(n)]
    parents = [[None] * n for _ in range(n)]
    cost    = [[inf] * n for _ in range(n)]
    cost[0][0] = G[0][0]
    # Initialize a priority queue where we will store (vertex, min distance) pairs
    # sorted by the minimum priority
    pq = PriorityQueue()
    pq.put((0, 0, 0))

    while not pq.empty():
        min_cost, i, j = pq.get()
        visited[i][j] = True  # Mark as visited
        # Skip a vertex if there was already found a better distance
        if cost[i][j] < min_cost: continue
        # Loop over all the neighbours and check if we can update some of them
        for d_i, d_j in moves:
            new_i = i + d_i
            new_j = j + d_j
            if 0 <= new_i < n and 0 <= new_j < n and not visited[new_i][new_j]:
                new_cost = cost[i][j] + G[new_i][new_j]
                # Update the distance from source to v vertex if found a shorter path
                if new_cost < cost[new_i][new_j]:
                    cost[new_i][new_j] = new_cost
                    parents[new_i][new_j] = (i, j)
                    pq.put((new_cost, new_i, new_j))

    # Otherwise, we cannot reach the target
    return cost[-1][-1], parents


def restore_path(parents):
    n = len(parents)
    i = j = n - 1
    result = []
    while parents[i][j]:
        result.append((i, j))
        i, j = parents[i][j]
    result.append((i, j))
    return result[::-1]


def kings_path(G: 'grid'):
    cost, parents = dijkstra(G)
    return cost, restore_path(parents)

from random import randint, seed

gen_A = lambda n: [[randint(1, 100) for _ in range(n)] for _ in range(n)]

A = gen_A(4)
# print(*A, sep='\n')
# print(kings_path(A))


#
# Jak zostanie czas i trzeba czymś wypełnić
#
# Zadanie 1. (kapitan statku, zadanie z kolokwium w 2012/13) Kapitan pewnego statku zastanawia
# się, czy może wpłynąć do portu mimo, że nastąpił odpływ. Do dyspozycji ma mapę zatoki w postaci tablicy
# M, gdzie M[y][x] to głebokość zatoki na pozycji (x, y). Jeśli jest ona większa niż pewna wartość int T
# to statek może się tam znaleźć. Początkowo statek jest na pozycji (0, 0) a port znajduje się na pozycji
# (n − 1, m − 1). Z danej pozycji statek może przepłynąć bezpośrednio jedynie na pozycję bezpośrednio obok
# (to znaczy, na pozycję, której dokładnie jedna ze współrzędnych różni się o jeden). Proszę napisać funkcję
# rozwiązującą problem kapitana.


def sail_path(G: 'grid of water depth', t: 'min depth required'):

    n = len(G)
    m = len(G[0])

    path = []

    def dfs(i, j):

        if i == n - 1 and j == m - 1: return True

        G[i][j] *= -1  # Mark this field as visited
        if i > 0 and G[i - 1][j] > t and dfs(i - 1, j):
            path.append('U')
            return True
        if i < n - 1 and G[i + 1][j] > t and dfs(i + 1, j):
            path.append('D')
            return True
        if j > 0 and G[i][j - 1] > t and dfs(i, j - 1):
            path.append('L')
            return True
        if j < m - 1 and G[i][j + 1] > t and dfs(i, j + 1):
            path.append('R')
            return True

        return False

    # Check if we are already stranded
    if G[0][0] <= t: return None

    # Check if we can reach the end from the G[0][0]
    res = dfs(0, 0)

    # Fix the grid (restore original depths)
    for i in range(n):
        for j in range(m):
            G[i][j] = abs(G[i][j])

    return None if not res else path[::-1]  # Reverse a path to get the original order

# M = [[4,2,8,6,5],[4,7,10,2,5],[1,2,3,3,5]]
# res = sail_path(M, 3)
# print(res)


# Zadanie 2. (czy nieskierowany?) Proszę podać algorytm, który mając na wejściu graf G reprezentowany
# przez listy sąsiedztwa sprawdza, czy jest nieskierowany (czyli czy dla każdej krawędzie u → v istnieje także
# krawędź przeciwna).

