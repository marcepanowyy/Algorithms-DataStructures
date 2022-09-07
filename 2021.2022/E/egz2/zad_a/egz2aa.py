
def update(buckets, new_capacity, idx):   # find new index and insert new bucket after subtracting

    b, e = 0, len(buckets)-1

    while b <= e:

        mid = (b+e) // 2
        if buckets[mid][0] < new_capacity:
            b = mid + 1
        else:
            e = mid-1

    buckets.insert(b, [new_capacity, idx])
    return idx

def binary_search(buckets, value, T):

    n = len(buckets)
    b, e = 0, n-1

    while b <= e:
        mid = (b + e) // 2

        if buckets[mid][0] < value:
            b = mid + 1
        else:
            e = mid - 1

    if b > n-1:
        buckets.append([T-value, n]) # create new bucket with n index
        buckets.pop(b)
        return update(buckets, T-value, b)

    elif buckets[b][0] >= value:
        new_capacity = buckets[b][0] - value
        buckets.pop(b)
        return update(buckets, new_capacity, b)



A = [1, 6, 2, 10, 8, 7, 1]
T = 10



# def coal( A, T ):
#     # tu prosze wpisac wlasna implementacje
#
#     buckets = []
#
#     for value in A:
#         x = binary_search(buckets, value, T)
#
#     # return x
#
# coal(A, T)

from egz2atesty import runtests



# tworze tablice wypelniona n wartosciami (magazyny). Nastepnie rozmieszczam wegiel po kolei do magazynow
# w zaleznosci od tego ktory moze przyjac okreslona wartosc. Szukamy ostatniego indeksu magazynu k, w ktorym mozemy
# rozmiescic ostatnia porcje.

def coal(A, T):

    n = len(A)
    buckets = [T for _ in range(n)]

    for idx, value in enumerate(A):
        k = 0
        while buckets[k] < value:
            k += 1
        else:
            buckets[k] -= value

    return k


# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( coal, all_tests = False )

coal(A, T)