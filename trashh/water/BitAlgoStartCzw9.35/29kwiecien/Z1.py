# napisz algorytm sprawdzajacy czy graf nieskierowany posiada cykl

from queue import Queue

def bfs(graph, s):

    queue = Queue()
    visited = [False] * len(graph)
    parent = [None] * len(graph)

    queue.put(s)
    visited[s] = True

    while not queue.empty():
        u = queue.get()
        for v in graph[u]:
            if visited[v]:
                if v == parent[u]:
                    continue
                else:
                    print("Mamy cykl")
                    return
            else:
                visited[v] = True
                queue.put(v)
                parent[v] = u

# g = [[1], [0,2,4], [1,3], [2,4], [1,3]]
# wierzchloek 0 ma krawedz z 1, wierzcholek 1 ma krawedz z 2 i 4 itp.
# bfs(g, 0)

