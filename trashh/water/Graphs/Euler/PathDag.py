# The Eulerian path is that we must visit visit every edge in that path only once

# The condition for eulerian path is that:

# For Undirected graph: Either every vertex has even degree or excatly two vertices has odd degree

# For Directed Graph: At most one vertex has indegree - outdegree = 1 and at most on vertex has
# outdegree - indegree = 1 and rest all vertix has equal outdegree and indegree

# In our case it is given that there is valid arrangment possible so it has made sure that euler path exists so
# we dont need to check that Since it is directed graph we need to follow that indegree-outdegree rule:

# Step1: Find the node that has outdegree - indegree = 1 that edge would we the start edge
# Step 2: If no such node exists you can start from any node
# Step 3: Do dfs on start node and append to our path

# eulerian path for directed graph

def condition4path(graph):

    n = len(graph)
    In, Out = [0] * n, [0] * n

    for u in range(n):
        for v in graph[u]:
            Out[u] += 1
            In[v] += 1

    c1, c2 = 0, 0

    for i in range(n):
        if In[i] - Out[i] == 1:
            c1 += 1
            end_node = i
        if Out[i] - In[i] == 1:
            c2 += 1
            start_node = i

    if c1 > 1 or c2 > 1:
        return False, None

    if c2 == 0:                             # mozemy zaczac z dowolnego wierzcholka
        for i in range(n):
            if In[i] + Out[i] != 0: return True, i

    return True, start_node


def eulerian_path(graph):

        condition, start_node = condition4path(graph)
        if not condition: return None

        route = []

        def dfs(u):

            while graph[u]:
                v = graph[u].pop()
                dfs(v)
            route.append(u)

        dfs(start_node)
        return route[::-1]

graph1 = [[1], [3, 2], [], [4], [0]]

# print(eulerian_path(graph1))

# Time complexity : O(V+E)