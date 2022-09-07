# Dziwne oplaty

# Komunikacja miejska w pewnym miescie jest dosc dziwnie zorganizowana.
# Za przejechanie kazdego odcinka miedzy dwiema stacjami obowiazujae osobna
# oplata. Od tej kwoty jest jednak odejmowany calkowity koszt poniosiony od poczatku
# podrozy (jesli jest ujemny, po prostu nic sie nie placi)

# na trasie 1-2-3-5 oplaty wyniosa kolejno 60+20+0, a na trasie 1-4-5 bedzie to 120+30


# [0] ----- 60 ----- [1] -----80-----[2]-------70-----[4]
#   \                                                /
#    \120                                           /
#     \                                            /
#      [3]-------------------150------------------/


G = [[[1,60], [3,120]],
     [[0,60], [2,80]],
     [[1,80], [4,70]],
     [[0,120], [4,150]],
     [[2,70], ]]

from queue import PriorityQueue

def dijkstra2(G, s, t):

    n = len(G)
    weights = [float("inf")] * n
    parents = [None] * n
    pq = PriorityQueue()
    pq.put((0, s, None, None))

    while not pq.empty():
        min_w, u, parent, prev_edge = pq.get()

        if min_w < weights[u]:
            weights[u] = min_w
            parents[u] = parent

            # if u == t: break

            for v, weight in G[u]:
                if weights[v] == float("inf"):
                    if weight - prev_edge < 0:
                        pq.put((0, v, u, weight))
                    else:
                        pq.put((weight - weights[u], v, u, weight))


    return parents, weights


