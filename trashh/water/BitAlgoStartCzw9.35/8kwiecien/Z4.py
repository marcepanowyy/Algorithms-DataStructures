# Dostajemy tablicę M na N wypelniona wartosciami (kosztem wejscia)
# Mamy znalezc minimalmy koszt potrzebny do dostania sie z pozycji
# [0][0] do pozycji [M-1][N-1]
# zakladamy, ze mozemy sie poruszac tylko w bok i dol
# oraz wszystkie koszty sa dodatnie


# zakladamy ze w bok znaczy w prawo

def grid_traveler(i,j):
    if i == 1 and j == 1: return 1
    if i == 0 or j == 0: return 0
    return grid_traveler(i-1, j) + grid_traveler(i, j-1)


print(grid_traveler(3,3))