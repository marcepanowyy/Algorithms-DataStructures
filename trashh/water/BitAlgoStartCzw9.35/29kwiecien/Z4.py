# Sklejanie przedzialow. Dany jest ciag przedzialow postaci [ai, bi]. Dwa przedzialy
# mozna skleic, jesli maja dokladnie jeden punkt wspolny. Podaj algorytm, ktory sprawdza, czy da sie uzyskac
# przedzial [a,b] poprzez sklejenie przedzialow

# tworzymy graf
# przedzial [0,3] wierzcholek 0 i 3 polaczone krawedzia

def binary_search(A: 'sorted array', val: 'searched value'):
    n = len(A)
    l = 0
    r = n - 1
    while l <= r:
        m = (l + r) // 2
        if A[m] < val:
            l = m + 1
        else:
            r = m - 1
    return l if l < n and A[l] == val else -1


def map_spans(S: 'array of spans'):
    # Unpack all coordinates to one array and sort them in a non-decreasing order
    n = len(S)
    A = [0] * (2 * n)
    for i in range(n):
        A[2 * i] = S[i][0]
        A[2 * i + 1] = S[i][1]
    A.sort()

    # Filter out repeated values
    B = [A[0]]
    for i in range(1, 2 * n):
        if A[i - 1] == A[i]:
            continue
        B.append(A[i])

    # Map spans (change their coordiantes to natural numbers)
    for i in range(n):
        S[i][0] = binary_search(B, S[i][0])
        S[i][1] = binary_search(B, S[i][1])

    # Return array of sorted coordinates with no repetitions
    return B


def create_spans_graph(S: 'array of spans'):
    A = map_spans(S)
    n = len(A)  # There will be as many vertices as the number of unique coordinates
    G = [[] for _ in range(n)]

    for span in S:
        G[span[0]].append(span[1])  # It's important that a graph is directed

    return G, A


def get_path(parents, t, A):
    path = []
    while parents[t] is not None:
        path.append([A[parents[t]], A[t]])
        t = parents[t]
    path.reverse()
    return path


def get_spans_to_merge(G: 'graph represended using adjacency lists',
                       A: 'array of sorted coordinates with no repetitions',
                       s: 'begin vertex',
                       t: 'end vertex'):
    n = len(G)
    parents = [None] * n
    parents[s] = s

    def dfs(u):
        if u == t:
            return True
        for v in G[u]:
            if parents[v] is None:
                parents[v] = u
                if dfs(v):
                    return True
        return False

    parents[s] = None

    return get_path(parents, t, A) if dfs(s) else []


def merge_spans_init(S: 'array of spans'):
    G, A = create_spans_graph(S)

    def merge_spans(target: 'target span from merged spans'):
        begin_i = binary_search(A, target[0])
        end_i = binary_search(A, target[1])
        # If there is no span which has a coordinate the same as the target, return False
        if begin_i < 0 or end_i < 0:
            return []
        # Otherwise, using a DFS algorithm, search for the path between begin_i and end_i
        return get_spans_to_merge(G, A, begin_i, end_i)

    return merge_spans

A = [[1, 10], [12, 15], [30, 40], [10, 18], [18, 30]]

