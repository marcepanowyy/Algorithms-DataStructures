# from edge representation [(v1, v2, weight), ...] to matrix representation

def convert1(E):

    n = len(E)
    max_ = 0

    for i in range(n):
        max_ = max(max_, E[i][0], E[i][1])

    new_G = [[0] * (max_+1) for _ in range(max_+1)]

    for i in range(n):
        v1 = E[i][0]
        v2 = E[i][1]
        w = E[i][2]
        new_G[v1][v2] = w
        new_G[v2][v1] = w

    return new_G

# from matrix representation to [[[v1,weight1], ...]...]

def convert2(G):

    n = len(G)
    new_G = [[] for _ in range(n)]

    for u in range(n):
        for v in range(n):
            if G[u][v]:
                new_G[u].append([v, G[u][v]])

    return new_G

# E = [(0,1,4), (0,2,3), (1,2,8), (2,3,6), (1,4,1), (4,3,22), (4,5,2), (3,6,5), (5,6,8)]
# G = convert1(E)
# G = convert2(G)
# print(G)

# from adjecency list to matrix representation

def convert3(G):

    n = len(G)
    new_G = [[0] * n for _ in range(n)]

    for u in range(n):
        for v, weight in G[u]:
            new_G[u][v] = weight

    return new_G

G = [[[1,4], [4,3]],
     [[2,2], [4,2]],
     [[3,4]],
     [],
     [[2,2], [5,2]],
     [[3,5]]]

G = convert3(G)
x = 2