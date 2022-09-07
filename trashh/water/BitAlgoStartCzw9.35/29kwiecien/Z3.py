# Jeziora. Dana jest dwuwymiarowa tablica N na N w ktorje kazda komorka ma wartossc
# W - reprezentujaca Wode lub L - lad. Grupe komorek wody polaczonych ze soba brzegami
# nazywamy jeziorem.
# a) Policz ile jezior jest w tablicy
# a') Ile komorek zajmuje najwieksze jezioro
# b) Zakladajac ze pola o indeksach [0][0] i [n-1][n-1] sa ladem sprawdz czy da sie przejsc
# droga ladowa z pola [0][0] do pola [n-1][n-1]. Mozna chodzic na boki, nie na ukos.
# c) znajdz najrktosza sciezke iedzy tymi punktami. Wypisz po kolei indeksy pol w tej sciezce

# a)

def count_lakes(M: 'square matrix representing terrain'):
    n = len(M)
    visited = [[False] * n for _ in range(n)]
    counter = 0

    def visit_lake(i, j):
        visited[i][j] = True
        if i > 0 and M[i - 1][j] and not visited[i - 1][j]:
            visit_lake(i - 1, j)
        if i < n - 1 and M[i + 1][j] and not visited[i + 1][j]:
            visit_lake(i + 1, j)
        if j > 0 and M[i][j - 1] and not visited[i][j - 1]:
            visit_lake(i, j - 1)
        if j < n - 1 and M[i][j + 1] and not visited[i][j + 1]:
            visit_lake(i, j + 1)

    for i in range(n):
        for j in range(n):
            if M[i][j] and not visited[i][j]:
                visit_lake(i, j)
                counter += 1

    return counter

M = [list(map(int, line)) for line in '''
01000000
01011000
00011010
01111010
00110000
01000011
11011010
00010000
'''.strip().splitlines()]

# print(*M, sep='\n')
# print('Number of lakes:', count_lakes(M))

# a') Liczba komórek, jakie zawiera największe jezioro


def visit_lake(M, i, j, visited):
    n = len(M)
    counter = 0

    def dfs_visit(i, j):
        nonlocal counter
        counter += 1
        visited[i][j] = True
        if i > 0 and M[i - 1][j] and not visited[i - 1][j]:
            dfs_visit(i - 1, j)
        if i < n - 1 and M[i + 1][j] and not visited[i + 1][j]:
            dfs_visit(i + 1, j)
        if j > 0 and M[i][j - 1] and not visited[i][j - 1]:
            dfs_visit(i, j - 1)
        if j < n - 1 and M[i][j + 1] and not visited[i][j + 1]:
            dfs_visit(i, j + 1)

    dfs_visit(i, j)

    return counter


def largest_lake(M: 'square matrix representing terrain'):
    n = len(M)
    visited = [[False] * n for _ in range(n)]
    largest = 0

    for i in range(n):
        for j in range(n):
            if M[i][j] and not visited[i][j]:
                largest = max(largest, visit_lake(M, i, j, visited))

    return largest

# b)

def is_path(M: 'matrix representing terrain',
            begin: 'coordinates of beginning point',
            target: 'coordiantes of target point'):
    # If begin field or target field is water, return False as we cannot go through water
    if M[begin[0]][begin[1]] or M[target[0]][target[1]]:
        return False

    n = len(M)
    visited = [[False] * n for _ in range(n)]

    def dfs_visit(i, j):
        visited[i][j] = True
        if i == target[0] and j == target[1]:
            return True
        if i > 0 and not M[i - 1][j] and not visited[i - 1][j]:
            if dfs_visit(i - 1, j): return True
        if i < n - 1 and not M[i + 1][j] and not visited[i + 1][j]:
            if dfs_visit(i + 1, j): return True
        if j > 0 and not M[i][j - 1] and not visited[i][j - 1]:
            if dfs_visit(i, j - 1): return True
        if j < n - 1 and not M[i][j + 1] and not visited[i][j + 1]:
            if dfs_visit(i, j + 1): return True
        return False

    return dfs_visit(*begin)


M = [list(map(int, line)) for line in '''
01000000
01011000
00011010
01111010
00110000
01000011
11011010
00010000
'''.strip().splitlines()]

n = len(M)
# print(*M, sep='\n')
# print('Does path exist?:', is_path(M, (0, 0), (n - 1, n - 1)))
# print('Does path exist?:', is_path(M, (n - 1, 0), (n - 1, n - 1)))
# print('Does path exist?:', is_path(M, (4, 1), (5, 3)))
# print('Does path exist?:', is_path(M, (4, 2), (5, 3)))

# d)

from queue import Queue


def shortest_path(M: 'matrix representing terrain',
                  begin: 'coordinates of beginning point',
                  target: 'coordiantes of target point'):
    # If begin field or target field is water, return -1 as we cannot go through water
    if M[begin[0]][begin[1]] or M[target[0]][target[1]]:
        return None

    n = len(M)
    parent = [[()] * n for _ in range(n)]  # Array to hold where we came from
    parent[begin[0]][begin[1]] = begin
    q = Queue()
    q.put(begin)
    found_path = False

    while not q.empty():
        i, j = q.get()
        if i == target[0] and j == target[1]:
            found_path = True
            break
        if i > 0 and not M[i - 1][j] and not parent[i - 1][j]:
            q.put((i - 1, j))
            parent[i - 1][j] = (i, j)
        if i < n - 1 and not M[i + 1][j] and not parent[i + 1][j]:
            q.put((i + 1, j))
            parent[i + 1][j] = (i, j)
        if j > 0 and not M[i][j - 1] and not parent[i][j - 1]:
            q.put((i, j - 1))
            parent[i][j - 1] = (i, j)
        if j < n - 1 and not M[i][j + 1] and not parent[i][j + 1]:
            q.put((i, j + 1))
            parent[i][j + 1] = (i, j)

    parent[begin[0]][begin[1]] = None

    # Restore path (a path will be stored in a reversed order)
    if found_path:
        i, j = target
        path = [(i, j)]
        while parent[i][j]:
            i, j = parent[i][j]
            path.append((i, j))

        n = len(path)
        for i in range(n // 2):
            path[i], path[n - i - 1] = path[n - i - 1], path[i]
        return path

    return None


M = [list(map(int, line)) for line in '''
01000000
01011000
00011010
01111010
00110000
01000011
11011010
00010000
'''.strip().splitlines()]

n = len(M)
# print(*M, sep='\n')
# print('Shortest path:', shortest_path(M, (0, 0), (n - 1, n - 1)))
# print('Shortest path:', shortest_path(M, (n - 1, 0), (n - 1, n - 1)))
# print('Shortest path:', shortest_path(M, (4, 1), (5, 3)))
# print('Shortest path:', shortest_path(M, (4, 2), (5, 3)))