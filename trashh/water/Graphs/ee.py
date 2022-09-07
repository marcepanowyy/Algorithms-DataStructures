# Eulerian Path/Circuit algorithm (Hierholzer's algorithm) for directed graphs

# Step 1 to finding an Eulerian path is determining if there even exists
# an Eulerian path

# Recall that for an Eulerian path to exist at most one vertex has
# (outdegree) - (indegree) = 1 and at most one vertex has
# (indegree) - (outdegree) = 1 and all other vertices have equal
# in and out degrees

# list adjecency representation (works for directed graphs as well :) )

# DAG

def condition(IN, OUT):

    n = len(IN)
    c1, c2 = 0, 0

    for i in range(n):
        if IN[i] - OUT[i] == 1:
            c1 += 1
            end_node = i                         # tam gdzie wchodza
        if OUT[i] - IN[i] == 1:
            c2 += 1
            start_node = i

    if c1 > 1 or c2 > 1:
        return None

    if c1 == 0 and c2 == 0:

        min_value = float("inf")
        start_node = None

        for i in range(n):
            if IN[i] != 0 and IN[i] < min_value:
                start_node = i
                min_value = IN[i]

    for i in range(n):
        if i != end_node and i != start_node and IN[i] != OUT[i]:
            return None

    return start_node

def count_degrees(G):

    n = len(G)
    IN, OUT = [0] * n, [0] * n

    for u in range(n):
        for v in G[u]:
            OUT[u] += 1
            IN[v] += 1

    return conditionEulerianPath(IN, OUT)


class Vertex:
    def __init__(self):
        self.id = None
        self.next = None


def create(G):

    n = len(G)
    modified_G = []
    edges = 0

    for u in range(n):
        head = Vertex()
        tail = head
        for v in G[u]:
            new_vertex = Vertex()
            new_vertex.id = v
            tail.next = new_vertex
            tail = tail.next
            edges += 1
        modified_G.append(head.next)

    return modified_G, edges


def eulerian_path(G):

    start_node = count_degrees(G)
    if start_node == None: return start_node
    solution_path = []

    modified_G, no_edges = create(G)

    def dfs_visit(modified_G, u):

        while modified_G[u] != None:

            v = modified_G[u].id
            modified_G[u] = modified_G[u].next
            dfs_visit(modified_G, v)

        solution_path.append(u)

    dfs_visit(modified_G, start_node)

    if len(solution_path) != no_edges+1: return False               # graf nie byl spojny
    return solution_path

G1 = [[], [3,2], [4,4,2], [5,2,1], [6,3], [6], [3]]

# print(eulerian_path(G2))
