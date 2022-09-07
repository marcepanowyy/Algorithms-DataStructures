# Srednica Drzewa. Srednica drzewa nazywamy odleglosc miedzy jego najbardziej oddalonymi od siebie
# wierzcholkami. Napisz algorytm, ktory pryzjmujac na wejsciu drzewo (niekoniecznie binarne)
# w postaci listy krawedzi zwroci jego srednice

# MOJE ROZWIAZANIE <3333 

def find_max_path(graph, s):     # or tree diameter

    # zaczynajac od wierzcholka s, szukamy najdluzszej sciezki z s do wierzcholka x. (interesuje nas rowniez
    # indeks wierzcholka x). Tradycyjnie dfs z tablica parentow zeby znac odleglosci

    visited = [False] * len(graph)
    parent = [None] * len(graph)
    dist = [float("inf")] * len(graph)
    parent[s] = None
    dist[s] = 0

    def dfs_visit(u):
        nonlocal graph, visited, parent, dist
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                dist[v] = dist[parent[v]]+1
                dfs_visit(v)

    dfs_visit(s)

    # szukamy wierzcholka z ktorego odl jest najwieksza
    index_max = max(range(len(dist)), key = dist.__getitem__)

    # zerujemy wszystkie dotychczasowe wartosci parent oraz dist i visited

    visited = [False] * len(graph)
    parent = [None] * len(graph)
    dist = [float("inf")] * len(graph)
    dist[index_max] = 0

    # wywolujemy kolejny raz dfs_visit zaczynajac od wierzcholka o indeksie znalezionym linijke wczesniej

    dfs_visit(index_max)

    # szukamy indeksu ktory ma najwieksza odleglosc (drugi raz). Jest to poczatek naszej przykladowej najdluzszej sciezki
    index_max = index_max = max(range(len(dist)), key = dist.__getitem__)

    res = []

    def get_solution(parent, index_max):
        nonlocal res
        if parent[index_max] != None:
            get_solution(parent, parent[index_max])
        res.append(index_max)

    get_solution(parent, index_max)

    return res  # jezeli interesuje nas srednica to wystarczy nalozyc funkcje len na res

# G = [[1,2,3,4],[0,5],[0,7],[0],[0,8,9],[1,6],[5],[2],[4],[4]]
# print(find_max_path(G, 0))

# Rozw Matiego

def undirected_graph_list(E: 'array of edges'):
    # Find a number of vertices in a graph
    n = 0
    for edge in E:
        n = max(n, edge[0], edge[1])
    n += 1

    G = [[] for _ in range(n)]
    for edge in E:
        G[edge[0]].append(edge[1])
        G[edge[1]].append(edge[0])
    return G


def tree_diameter(E: 'array of edges'):
    # Create a graph representation using adjacency lists
    G = undirected_graph_list(E)
    # Look for the longest path
    return max_path(G)


def max_path(G: 'graph represented using adjacency lists'):
    n = len(G)
    global_max = 0
    visited = [False] * n

    def recur(u):

        nonlocal global_max
        visited[u] = True

        max_paths = [-1, -1]
        for v in G[u]:
            if not visited[v]:
                v_max = recur(v)
                update_max_paths(max_paths, v_max)

        # If entered a node which has only one node connected
        # (is a leaf), store length of the current path equal to 0
        if len(G[u]) == 1:
            curr_max = 0
        # ELse, increase a length of the longest path by 1
        else:
            curr_max = max(max_paths) + 1

        # If found both paths, compare the length of them both increased by 2
        # with the globally longest path
        if max_paths[0] >= 0 and max_paths[1] >= 0:
            global_max = max(global_max, sum(max_paths) + 2)
        # Else, we must have found only one path (or no paths), so the other one is -1
        # Therefore, we have to choose the longest one and compare its length increased
        # by 1 to the global max
        else:
            global_max = max(global_max, max(max_paths) + 1)

        return curr_max

    recur(0)  # This doesn't matter where we start

    return global_max


def update_max_paths(max_paths, child_max):
    # Try to replace the lower value at first (we want to
    # maximize a sum of both paths' values so we have to get rid
    # of the lower one at first)
    if max_paths[0] > max_paths[1] and child_max > max_paths[1]:
        max_paths[1] = child_max
    elif child_max > max_paths[0]:
        max_paths[0] = child_max



