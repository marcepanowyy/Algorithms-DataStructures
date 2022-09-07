# MergeSort

# Python program for implementation of MergeSort
def merge_sort(t):
    if len(t) > 1:
        # Finding the mid of the array
        mid = len(t) // 2
        # Dividing the array elements
        L = t[:mid]
        # into 2 halves
        R = t[mid:]
        # Sorting the first half
        merge_sort(L)
        # Sorting the second half
        merge_sort(R)
        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                t[k] = L[i]
                i += 1
            else:
                t[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            t[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            t[k] = R[j]
            j += 1
            k += 1


# T = [1, 9, 12, 99, 12, 9, 12, 19, 16, 14, 2, 0, 15]
# merge_sort(T)
# print(T)

# QuickSort

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)


# T = [1, 9, 12, 99, 12, 9, 12, 19, 16, 14, 2, 0, 15]

# quick_sort(T, 4, len(T)-1)
# print(T)

# HeapSort

def heapify(A, n, i):
    l = 2 * i + 1
    r = 2 * i + 2
    m = i
    if l < n and A[l] > A[m]: m = l
    if r < n and A[r] > A[m]: m = r
    if m != i:
        A[i], A[m] = A[m], A[i]
        heapify(A, n, m)

def parent(i):
    return (i-1)//2

def build_heap(A):
    n = len(A)
    for i in range(parent(n-1), -1, -1): # zaczynamy od rodzica ostatniego elementu
        heapify(A, n, i)

def heap_sort(A):
    n = len(A)
    build_heap(A)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)

# T = [1, 9, 12, 99, 12, 9, 12, 19, 16, 14, 2, 0, 15]
# heap_sort(T)
# print(T)

