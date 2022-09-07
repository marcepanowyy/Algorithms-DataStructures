# Domy i sklepy. Mamy mape miasteczka w ktorym sa domy i sklepy. Na mapie sa rowniez drogi
# kazda dlugosci 1, ktore lacza dom z domem albo dom ze sklepem. Naszym zadaniem jest dla kazdego domu
# znalezc odleglosc najblizszego sklepu

# wykonac bfs dla kazdego ze sklepu (od razu do kolejki dodac wszystkie wierzcholki,
# ktore sa sklepami i aktualizowac odleglosci)

from queue import Queue


def shortest_way_to_shop(G: 'graph representing connections between shops and houses',
                         shops: 'array of shops vertices indices'):
    n = len(G)
    visited = [False] * n
    result = [float('inf')] * n  # Infinity means no path
    q = Queue()
    for shop in shops:
        visited[shop] = True
        result[shop] = 0
        q.put(shop)

    while not q.empty():
        i = q.get()
        for j in G[i]:
            if not visited[j]:
                result[j] = result[i] + 1
                visited[j] = True
                q.put(j)
    return result