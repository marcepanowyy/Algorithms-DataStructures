# Krasnoludy i Trolle. Wyobrazmy sobie podziemy labirynt zl0ozony z ogormych jaskin
# polaczonych waskimi korytarzami. W jedenj z jaskin kransoludy zbudowaly swoja osade a
# w kazdej z pozostalych jaskin mieszna znana krasnoludom ilosc trolli. Krasnoludy chca
# zaplanowac swoja obrone na wypadek ataku ze strony trolli. Zamierzaja w tym celu
# zakrasc sie i podlozyc ladunek wybuchowy pod jeden z korytarzy, tak, aby trolle mieszkajace
# za tym korytarzem nie mialy zadnej sciezki, ktora moglyuby dotrzec do osady krasnolodow
# ktory korytarz nalezy wysadzic w powietrze, aby odciac dostep do krasnoludzkiej osady
# najwiekszej liczbie trolli?

# trzeba wysadzic most

# potrzebujemy mosty znajdujace sie najblizej krasnoludzkiej osady

def undirected_graph_list(E: 'array of edges', n: 'number of vertices'):
    G = [[] for _ in range(n)]
    for edge in E:
        G[edge[0]].append(edge[1])
        G[edge[1]].append(edge[0])
    return G


def bridges(G: 'graph represented by adjacency lists'):
    n = len(G)
    low = [0] * n
    times = [0] * n
    time = 0

    def dfs(u, parent):
        nonlocal time
        time += 1
        low[u] = times[u] = time

        for v in G[u]:
            # when there is no visit time, a vertex hasn't been yet visited
            if not times[v]:
                dfs(v, u)
                # If we have a cycle, we must update the low value of the parent vertex
                if low[v] < low[u]: low[u] = low[v]
            # v cannot be a parent of u as it's obvious it will always be visited before
            # and connected to the vertex u which doesn't imply that we have a trailing edge
            elif v != parent:
                # We have a back edge (we try to enter a vertex which was entered before)
                if times[v] < low[u]: low[u] = times[v]

    # I assume that dwarfs' cave is in the 0 vertex
    dfs(0, -1)



    return times, low


def blow_up_bridge(G: 'graph represented by adjacency lists', C: 'counts of trolls in caves'):
    # We will check if there is a bridge for each vertex
    times, low = bridges(G)
    n = len(G)
    visited = [False] * n
    best_count = 0
    best_bridge = None

    # Define the first DFS function which will look for the closest bridges
    def dfs_bridge(u):
        visited[u] = True
        # Check each neighbour if there is a bridge or not (if it hasn't been yet visited)
        for v in G[u]:
            # A visited array guarantees that we will always start from the closest bridge
            # if there are some later (the first bridge on a particular path)
            if not visited[v]:
                # Check if there is a bridge. If it does so, start another DFS algorithm
                if low[v] == times[v]:  # There is a bridge between (from u to v)
                    nonlocal best_bridge, best_count
                    # Start a DFS (can be BFS, it doesn't matter now) in the subgraph
                    # on the other side of a bridge (from a vertex v)
                    # (We are sure this algorithm will visit only such vertices which are
                    # in a part of a graph which will become disconnected after blowing up
                    # the u-v bridge as there is only one way to get back to the grap - via
                    # this bridge which has already been visited)
                    curr_count = dfs_count(v)
                    if curr_count > best_count:
                        best_count = curr_count
                        best_bridge = (u, v)
                # If there is no bridge, just continue searching for a bridge (or another bridge
                # which will result in disconnectiong more trolls)
                else:
                    dfs_bridge(v)

    # A DFS function which counts a number of trolls
    def dfs_count(u):
        visited[u] = True
        total = C[u]
        for v in G[u]:
            if not visited[v]:
                total += dfs_count(v)
        return total

    # Start looking for the closest bridges from dwarfs' cave
    dfs_bridge(0)

    # Return the result
    return best_bridge, best_count



# E = [(0,1),(0,3),(4,3),(3,2),(2,1),(1,5)]
# G = undirected_graph_list(E,6)
# T = [0,3,5,1,8,5]
# print(blow_up_bridge(G,T))