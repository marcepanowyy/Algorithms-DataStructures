# Sejf. Dostales sejf ktory odblokowuje sie czterosyfrowym pinem (0000-9999). Pod wyswietlaczem znajduje sie kilka
# przyciskow z liczbami od 1 do 9999 - prykladowo (13, 223, 782, 3902). Sejf ten dziala inaczej niz normalny
# wcisniecie przycisku z liczba powoduje dodanie liczby z przycisku do liczby na wyswietlaczu. Jezeli suma jest wieksza niz
# 9999 to pierwsza cyfra zostaje obcieta. Jest tobie znany PIN oraz cyfry, ktore sa aktualnie wyswietlane. Znajdz najrkotsza
# sekwencje nacisniec przyciskow, ktora pozwoli ci odblokowac sejf. Jezeli taka sekwencja nie istnieje, zwroc None

# np mamy akutalnie cyfry 9001, PIN do 2000 i pod wysiwteltaczem mamy cyfry
# 13, 223, 782, 3402.

# rozw. Mamy 1000 wierzcholkow 9001 laczymy z 9001+13, 9001+223 itp
# i bfs. Jezeli wierzcholek zostal juz odwiedzony to nie wchodzimy do niego

from queue import Queue


def shortest_unlock_sequence(target, current, buttons, *, num_digits=1):
    limit = 10 ** num_digits
    visited = [False] * limit
    parent = [None] * limit

    q = Queue()
    q.put(current)
    parent[current] = -1

    found_seq = False

    # Treat every step as an edge of a graph and a resulting number
    # as a vertex of a graph (use BFS algorithm)

    while not q.empty():
        u = q.get()
        if u == target:
            found_seq = True
            break
        for button in buttons:
            v = (u + button) % limit
            if not parent[v]:
                parent[v] = u
                q.put(v)

    # Return None if no unlocking sequence was found
    if not found_seq:
        return None

    # Else, restore pressed buttons sequence
    result = []
    v = target
    while v != current:
        result.append((v - parent[v]) % limit)  # This can be negative, thus we use modulo
        v = parent[v]

    return result


# buttons = [2, 8, 5]
# target = 3
# current = 2
#
# print(shortest_unlock_sequence(target, current, buttons))


