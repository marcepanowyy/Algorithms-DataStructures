# Otrzymujemy na wejsciu liste par ludzi ktore sie wzajemnie znaja. Osoby sa
# reprezentowane przez liczby od 0 do n-1. Dnia pierwszego osoba 0 przekazuje pewna
# wiadomosc wszystkim swoim znajomym. Dnia drugiego kazdy ze znajomych przekazuje te
# wiadomosc wszystkim swoim znajomym, kotrzy jej jeszcze nie znali i tak dalej
# Napisz algorytm, ktory zwroci dzien, w ktorym najwiecej osob poznalo wiadomosc oraz
# ilosc osob ktore tego dnia ja otrzymaly

from queue import Queue

def bfs(graph, s):

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

    return distance

# graph = [[1,2,3,4], [0,5], [0,5,7], [0,6], [0,8], [1,2,6], [3,5,7,8,9,11,12],[2,6,10], [4,6,9], [6,8,10], [7,9], [6],[6,13], [12,14], [13]]
# print(bfs(graph, 0))