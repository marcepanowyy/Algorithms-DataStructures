from egzP3btesty import runtests 
from queue import PriorityQueue

def get_sum(G):

    sum_ = 0
    n = len(G)

    for u in range(n):
        for v, w in G[u]:
            sum_ += w

    return sum_//2

def lufthansa(G: 'graph represented by adjacency lists'):

    n = len(G)
    parents = [-1] * n
    weights = [float("-inf")] * n
    processed = [False] * n
    pq = PriorityQueue()
    pq.put((0, 0))
    max_ST = 0
    flag = True

    while not pq.empty():
        u_weight, u = pq.get()
        u_weight *= (-1)
        if processed[u]:
            if flag == True:
                flag = False
                pass
            else: continue
        processed[u] = True
        max_ST += u_weight
        for v, e_weight in G[u]:
            if not processed[v] and e_weight > weights[v]:
                parents[v] = u
                weights[v] = e_weight
                pq.put((-e_weight, v))

    return get_sum(G) - max_ST



runtests ( lufthansa, all_tests=True )