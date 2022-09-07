# Zadanie 4: Domino
# Mamy pewien układ klocków domino. Otrzymujemy go w postaci listy par [a, b]: Jeżeli przewrócimy klocek a,
# to klocek b też się przewróci. Chcemy znaleźć minimalną liczbę klocków, które trzeba przewrócić ręcznie, aby
# wszystkie domina były przewrócone.

# szukamy silnych skladowych

def directed_graph_list(E: 'array of edges', n: 'number of vertices'):
    G = [[] for _ in range(n)]
    for edge in E:
        G[edge[0]].append(edge[1])
    return G


def get_process_times(G: 'directed graph represented using adjacency lists'):
    n = len(G)
    times = [0] * n
    visited = [False] * n
    time = 0

    def dfs(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs(v)
        nonlocal time
        time += 1
        times[u] = time

    for u in range(n):
        if not visited[u]:
            dfs(u)

    return times

x = get_process_times(G)

def get_transposed_graph(G: 'directed graph represented using adjacency lists'):
    n = len(G)
    G2 = [[] for _ in range(n)]

    for u in range(n):
        for v in G[u]:
            G2[v].append(u)

    return G2

def get_vertices_order(times):
    n = len(times)
    order = [-1] * n
    for i in range(n):
        order[n - times[i]] = i
    return order

def find_coherent_components(G: 'directed graph represented using adjacency lists'):
    n = len(G)
    # Get processing time of each vertex
    times = get_process_times(G)
    # Create transposed graph
    G = get_transposed_graph(G)
    # Get order of vertices in which DFS will be started from such vertices
    order = get_vertices_order(times)
    # Create an array in which a result will be stored (each number will refer
    # to the other coherent component of a graph)
    result = [-1] * n  # This array will also be used to check if a vertex was visited
    num = 0

    def dfs(u):
        result[u] = num
        for v in G[u]:
            if result[v] < 0:
                dfs(v)

    # Start dfs from vertices of the highest processing time
    for i in range(n):
        u = order[i]
        if result[u] < 0:
            dfs(u)
            num += 1

    return result, num



def coherent_components_graph(G: 'directed graph represented using adjacency lists'):
    components, n2 = find_coherent_components(G)
    n = len(G)
    G2 = [[] for _ in range(n2)]

    for u in range(n):
        for v in G[u]:
            u2 = components[u]
            v2 = components[v]
            if v2 != u2:
                G2[u2].append(v2)

    return G2



def count_vertices_without_ingoing_edges(G: 'directed graph represented using adjacency lists'):
    count = n = len(G)
    has_ingoing_edge = [False] * n
    for u in range(n):
        for v in G[u]:
            if not has_ingoing_edge[v]:
                has_ingoing_edge[v] = True
                count -= 1
    return count


def count_dominoes_to_knock(E: 'array of dominoes pairs'):
    # Get a number of domino pieces
    n = 0
    for edge in E:
        n = max(n, edge[0], edge[1])
    n += 1
    # Create a DAG based on domino pieces
    G = directed_graph_list(E, n)
    # Create a graph of coherent components
    G2 = coherent_components_graph(G)
    # Count a number of vertices with no ingoing edges
    return count_vertices_without_ingoing_edges(G2)


# E = [(0, 1), (1, 2), (3, 2), (2, 4), (4, 1), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 6),
#      (4, 7), (4, 6), (5, 9), (10, 0), (15, 14), (15, 11), (15, 11), (11, 13), (14, 13), (5, 13),
#      (16, 8), (0, 12), (12, 3)]
#
# print(count_dominoes_to_knock(E))