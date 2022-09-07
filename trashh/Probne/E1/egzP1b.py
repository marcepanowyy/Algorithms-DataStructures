from egzP1btesty import runtests 
from queue import PriorityQueue

def convert(edges):

    n = 0
    for u, v, _ in edges:
        n = max(u, v)

    n += 1
    graph = [[] for _ in range(n)]

    for u, v, w in edges:
        graph[u].append([v, w])
        graph[v].append([u, w])

    return graph

def dijkstra(G, s, t):

    n = len(G)
    dist = [[float("inf")] * 5 for _ in range(n)]
    pq = PriorityQueue()
    pq.put((0, s, 0))

    while not pq.empty():
        min_w, u, stops = pq.get()
        if min_w < dist[u][stops]:
            dist[u][stops] = min_w

            if u == t and dist[t][4] != float("inf"): return min_w
            for v, weight in G[u]:

                if stops >= 4: continue

                if dist[v][stops+1] == float("inf"):
                    pq.put((dist[u][stops] + weight, v, stops+1))

    return float("inf")


G = [
(0, 1, 9), (0, 2, 1),
(1, 2, 2), (1, 3, 8),
(1, 4, 3), (2, 4, 7),
(2, 5, 1), (3, 4, 7),
(4, 5, 6), (3, 6, 8),
(4, 6, 1), (5, 6, 1)
]
D = 0
L = 6

def turysta( G, D, L ):

    graph = convert(G)
    return dijkstra(graph, D, L)

# print(turysta(G, D, L))
# runtests (turysta)