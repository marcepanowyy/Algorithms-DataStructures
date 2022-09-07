# Zadanie 2: Dostarczanie przesyłek
# Bajtocja jest krainą zawierającą N miast, N-1 dwukierunkowych dróg i układ dróg tworzy graf spójny. Mając
# listę K miast do których musimy dostarczyć przesyłki i mogąc wystartować i zakończyć trasę w dowolnym
# mieście, podaj minimalny dystans, który musimy przebyć, że zrealizować to zadanie.

# BRAK CYKLI

# mozemy zaczac w punkcie A i skonczyc w B

### Implementacja #1
#### Dla grafu nieważonego
##### Z usuwaniem gałęzi, których nie będziemy odwiedzać, jadąc do miast (mapujemy graf do takiej postaci, aby w liściach znalazły się zawsze miasta, do których chemy pojechać)

def undirected_graph_list(E: 'array of edges', n: 'number of vertices'):
    G = [[] for _ in range(n)]
    for edge in E:
        G[edge[0]].append(edge[1])
        G[edge[1]].append(edge[0])
    return G


def map_graph(G: 'graph represented by adjacency lists', C: 'array of cities to visit'):
    n = len(G)
    k = len(C)

    visits = [0] * n
    for i in range(k):
        visits[C[i]] = 2  # Mark cities which will be visited

    def dfs(u):
        found_to_visit = visits[u] == 2
        visits[u] = 1
        for v in G[u]:
            if visits[v] == 0 or visits[v] == 2:
                if dfs(v):
                    found_to_visit = True

        if not found_to_visit:
            visits[u] = -1

        return found_to_visit

    dfs(C[0])

    for u in range(n):
        if visits[u] == -1:
            G[u] = []
        else:
            # We must also remove edges which join cities
            # on a path with unvisited cities
            edges = []
            for v in G[u]:
                if visits[v] == 1:
                    edges.append(v)
            G[u] = edges


def diameter_helper(G, begin_u):
    n = len(G)
    visited = [False] * n
    max_u = max_dist = 0

    def dfs(u, dist):
        nonlocal max_u, max_dist
        if dist > max_dist:
            max_dist = dist
            max_u = u

        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs(v, dist + 1)
        return dist

    dfs(begin_u, 0)

    return max_dist, max_u


def tree_diameter(G: 'graph represented by adjacency lists'):
    n = len(G)
    for u in range(n):
        if G[u]: break
    _, u = diameter_helper(G, u)
    diam, v = diameter_helper(G, u)
    return diam, u, v


def min_dist(G: 'graph represented by adjacency lists', C: 'array of cities to visit'):
    n = len(G)

    map_graph(G, C)

    total_dist = 0
    for u in range(n):
        total_dist += len(G[u])

    diam, begin_city, end_city = tree_diameter(G)
    total_dist -= diam

    return total_dist, begin_city, end_city