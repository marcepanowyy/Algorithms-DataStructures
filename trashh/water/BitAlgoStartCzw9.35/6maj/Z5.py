# Zadanie 5: Ścieżki w DAGu
# Otrzymujemy na wejściu w postaci listy krawędzi skierowany graf acykliczny (DAG - Directed Acyclic Graph)
# oraz parę wierzchołków s i t. Naszym zadaniem jest obliczyć, ile jest możliwych ścieżek między s i t.

# BFS z modyfikacja proste jak drut

# albo tak:

def count_all_paths(G, s, t):
    n = len(G)
    visited = [False] * n
    counts = [0] * n
    counts[t] = 1

    def dfs(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs(v)
            counts[u] += counts[v]

    dfs(s)

    return counts[s]


def dag_list(E: 'array of graph edges'):
    n = max(u for edge in E for u in edge) + 1
    G = [[] for _ in range(n)]
    for u, v in E:
        G[u].append(v)
    return G


####################################### lub tak

from queue import Queue


def restore_paths(parents, s, t):
    n = len(parents)
    result = []

    def recur(u, curr=[]):
        if u == s:
            result.append([u] + curr)
        else:
            for v in parents[u]:
                recur(v, [u] + curr)

    recur(t)

    return result


def get_all_paths(G, s, t):
    n = len(G)
    q = Queue()
    q.put(s)
    parents = [[] for _ in range(n)]

    while not q.empty():
        i = q.get()
        for j in G[i]:
            if not parents[j]:
                q.put(j)
            parents[j].append(i)

    return restore_paths(parents, s, t)

def paths(G, s, t):
    print(f'All paths from {s} to {t}')
    print(*(f'{i+1:<3} {path}' for i, path in enumerate(map(lambda arr: ' -> '.join(map(str, arr)), get_all_paths(G, s, t)))),sep ='\n')


E = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (2, 6), (1, 6), (6, 3), (6, 9), (9, 10), (6, 7), (7, 10),
     (7, 8), (10, 11), (11, 8), (8, 4)]

G = dag_list(E)

paths(G, 0, 5)