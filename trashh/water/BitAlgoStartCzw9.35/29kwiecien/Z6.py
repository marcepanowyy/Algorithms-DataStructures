# Rozmiary poddrzew. Dostajemy na wejsciu liste krawedzi drzewa (niekoniecznie binarnego) oraz
# wyrozniony wierzcholek - korzen. Kazdy wierzcholek tworzy swoje wlasne poddrzewo. Dla kazdego
# wierzcholka wyznacz ilosc wierzcholkow w jego poddrzewie

def subtrees_sizes(T: 'tree represented with adjacency lists', root: 'root vertex'):
    n = len(T)
    sizes = [0] * n
    parents = [None] * n

    def recur(u):
        if not sizes[u]:
            count = 1
            for v in T[u]:
                if v != parents[u]:
                    parents[v] = u
                    count += recur(v)
            sizes[u] = count
        return sizes[u]

    recur(root)

    return sizes