
n = int(input("input number of cities >> "))


D = [n*[0] for i in range(n)]

print("\nfill your array with distance \n")

for i in range(n):
    for j in range(n):
        if j>i:
            print("input the dist between city number", i, "and", j)
            x = int(input())
            D[i][j] = x
            D[j][i] = x

    D[i][i] = 0


for i in range(n):
    print(D[i])


# if 5<float('inf'):
#     print("OK")

F = [[float('inf')*n for i in range(n)]]
F[0][1] = D[0][1]

def tspf(i, j, F, D):
    if F[i][j] != float('inf'):
        return F[i][j]
    if i == j-1:
        best = float('inf')
        for k in range(j-1):
            best = min(best, tspf(k, j-1, F, D) + D[k][j])
        F[j-1][j] = best
    else:
        F[i][j] = tspf(i, j-1, F, D) + D[j-1][j]
    return F[i][j]

