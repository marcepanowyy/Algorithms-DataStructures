def partition(tab, left, right):
    n = len(tab)
    piv = tab[right // n][right % n]
    i = left - 1
    for j in range(left, right):
        if tab[j // n][j % n] < piv:
            i += 1
            tab[j // n][j % n], tab[i // n][i % n] = tab[i // n][i % n], tab[j // n][j % n]
    i += 1
    tab[right // n][right % n], tab[i // n][i % n] = tab[i // n][i % n], tab[right // n][right % n]
    return i


def quickselect(tab, left, right, k):
    if k > 0 and k <= right - left + 1:
        piv = partition(tab, left, right)

        if piv - left == k - 1:
            n = len(tab)
            return tab[piv // n][piv % n]

        if piv - left > k - 1:
            return quickselect(tab, left, piv - 1, k)
        return quickselect(tab, piv + 1, right, k - piv + left - 1)

    return float("inf")

T = [[5, 12, 5],
     [7, 3, 66],
     [41, 2, 61]]

x = quickselect(T, 0, len(T)-1, 3)
print(x)
n = len(T)
for i in range(n):
    print(T[i])