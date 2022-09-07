# Zadanie 3: Szach i goniec (II kolokwium 2020)

# Algocja leży na wielkiej pustyni i składa się z miast oraz oaz połączonych drogami. Każde miasto jest otoczone
# murem i ma tylko dwie bramy. Z każdej bramy prowadzi dokładnie jedna droga do jednej oazy (ale do danej
# oazy może dochodzić dowolnie wiele dróg; oazy mogą też być połączone drogami między sobą). Prawo Algocji
# wymaga, że jeśli ktoś wjechał do miasta jedną bramą, to musi go opuścić drugą.
# Szach Algocji postanowił wysłać gońca, który w każdym mieście kraju odczyta zakaz formułowania zadań “o
# szachownicy” (obraza majestatu). Szach chce, żeby goniec odwiedził każde miasto dokładnie raz (ale nie ma
# ograniczeń na to ile razy odwiedzi każdą z oaz). Goniec wyjeżdża ze stolicy Algocji, miasta x, i po odwiedzeniu
# wszystkich miast ma do niej wrócić.
# Proszę przedstawić (bez implementacji) algorytm, który stwierdza czy odpowiednia trasa gońca istnieje. Proszę
# uzasadnić poprawność algorytmu oraz oszacować jego złożoność czasową.


# interesuje nas sciezka eulera (sciezka ktora przechodzi przez wszystkie krawedzie w grafie). Interesuja nas
# krawedzie, ktore zawieraja miasta. W wierczholkach miast mamy krawedzie wychodzace i wchodzace

# tworzymy nowy graf - oazy to wierzcholki, krawedzie to drogi z oazy do miasta lub drogi z oazy do oazy
# scalamy wierzcholki ktore lacza oazy


def create_graph(E: 'array of edges', C: 'array of cities indices'):
    # Find a number of vertices
    n = 0
    for edge in E:
        n = max(n, edge[0], edge[1])
    n += 1
    # Create an array which will represent a graph
    G = [[False, []] for _ in range(n)]
    for edge in E:
        G[edge[0]][1].append(edge[1])
        G[edge[1]][1].append(edge[0])
    # Mark vertices which are cities
    for city in C:
        G[city][0] = True
    return G


def cities_to_edges(G: 'graph'):
    n = len(G)
    new_oasis_indices = [-1] * n  # Helper array to map indices of oasis in the new graph

    idx = 0
    for i in range(n):
        if not G[i][0]:
            new_oasis_indices[i] = idx
            idx += 1

    # Create a new graph
    new_n = idx
    new_G = [[0, []] for _ in range(new_n)]
    visited = [False] * n

    for i in range(n):
        # Continue if mapped a city before
        if visited[i]: continue
        # Mark the current vertex as visited
        visited[i] = True
        # If it is a city (it must have 2 neighbours - always)
        if G[i][0]:
            # Get its neighbours
            u = G[i][1][0]
            v = G[i][1][1]
            # While at least one of the neighbours is a city, loop till we reach an oasis
            prev_u = prev_v = i
            while G[u][0]:
                visited[u] = True
                u, prev_u = G[u][1][0] if G[u][1][0] != prev_u else G[u][1][1], u
            while G[v][0]:
                visited[v] = True
                v, prev_v = G[v][1][0] if G[v][1][0] != prev_v else G[v][1][1], v
            # When both vertices are now oasis, we can add an edge representing
            # all the cities on a way (we have to visit them all at once)
            new_u = new_oasis_indices[u]
            new_v = new_oasis_indices[v]
            new_G[new_u][1].append((True, new_v))  # True means this edge is a city
            new_G[new_v][1].append((True, new_u))  # True means this edge is a city
            # Increment a number of connected city edges (edges which are cities) to the oasis
            new_G[new_u][0] += 1
            new_G[new_v][0] += 1
            # If it's an oasis
        else:
            # An oasis can have multiple neighbours but cities will be covered in the case above,
            # so we will add only edges between oasis in here
            new_u = new_oasis_indices[i]
            for v in G[i][1]:
                if not G[v][0]:  # If is also an oasis
                    new_v = new_oasis_indices[v]
                    # Add only one edge as the remaining ones will be added from the other oasis
                    new_G[new_u][1].append((False, new_v))  # False means this edge connects two oasis
    return new_G


def degree_after_oasis_merge(G, oasis_u, visited):
    deg = 0

    def dfs(u):
        visited[u] = True
        # If u is a vertex which has at least one city edge connected, all the city
        # edges will be linked to the beginning vertex, so its degree will be increased
        # by the number of city edges outgoing from the u edge
        if G[u][0]:
            nonlocal deg
            deg += G[u][0]

        for i in range(len(G[u][1])):
            # If hasn't been visited yet and is not a city edge
            v = G[u][1][i][1]
            is_city_edge = G[u][1][i][0]
            if not visited[v] and not is_city_edge:
                dfs(v)

    dfs(oasis_u)

    return deg


def does_path_exist(E: 'array of edges', C: 'array of cities indices'):
    G = create_graph(E, C)
    if len(C) == len(G): return True  # We have a cycle - no oasis there
    G = cities_to_edges(G)
    n = len(G)
    visited = [False] * n

    print(*G, sep='\n')

    for u in range(n):
        if not visited[u]:
            # Check if the resulting graph will be Eulerian or not
            # (if found a vertex of odd degree, return False)
            deg = degree_after_oasis_merge(G, u, visited)

            print(u, deg)

            if deg % 2:
                return False
    return Truei

