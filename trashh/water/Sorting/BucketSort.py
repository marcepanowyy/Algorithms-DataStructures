import random

# Sortowanie kubełkowe - bucket sort

# Sortujemy tablicę n liczb pochodzących z rozkładu
# jednostajnego nad przedziałem [0,1)

# 0.42, 0.13, 0.07, 0.21, 0.91, 0.13, 0.37

# Tworzymy n kubełkow (kubelek - lista jednokier.)

# w naszym przypadku 7 kubelkow

# przedzialy to 1/n

# [0.15), [0.15, 0.30), ..., (0.90, 1)

# rozdzielam liczby do odpowiednich kubełków

# sortujemy kazdy kubelek osobno

# Sortujemy przez wybieranie/wstawianie

# kopiujemy kolejno liczby z kubełków do
# tablicy wyjściowej

# jak przydzielić liczbę do kubełka?
# jesli x nalezy do [0,1)
# to x laduje w kubelku podloga z x*n

# liczba kubelkow musi zalezec od rozmiaru danych
# i musi zalezec liniowo
# (najprostrza rzecz - tyle kubelkow co rozmiar tablicy)

# jesli spelnione zalozenia oczekiwany - O(n)

import math

class Node:
    def __init__(self):
        self.next = None
        self.value = None

def tab_to_list(tab):
    if tab is None or tab == []:
        return None
    head = curr = Node(tab[0])
    for i in range(1, len(tab)):
        curr.next = Node(tab[i])
        curr = curr.next
    return head

# T = [random.randint(1, 99)/100 for i in range(13)]
# print(T)

# def InsertionSort(A):
#     n = len(A)
#     for i in range(1, n):
#         key = A[i]
#         j = i - 1
#         while j >= 0 and A[j] > key:
#             A[j+1] = A[j]
#             j = j - 1
#         A[j+1] = key

# def bucket_sort(A):
#     n = len(A)
#     B = [[] for i in range(n)]
#     C = []
#     for i in range(n):
#         B[math.floor((A[i])*n)] += [A[i]]
#     # print(B)
#     for i in range(n):
#         if len(B[i]) > 1:
#             InsertionSort(B[i])
#     for i in range(n):
#         C += B[i]
#
#     return C

# bucket_sort(T)


# drugi bucketsort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]


def bucket_sort(arr, k):
    n = len(arr)
    buckets = [[] for _ in range(n)]
    interval = k / n
    for elem in arr:
        buckets[int(elem // interval)].append(elem)
    i = 0
    for bucket in buckets:
        bubble_sort(bucket)
        for elem in bucket:
            arr[i] = elem
            i += 1

# T = [1.12, 1.43, 1.91, 1.42, 1.52, 1.77]
# bucket_sort(T, )


# T = [0.7, 0.1, 0.4, 0.9, 0.1, 0.8, 0.4, 0.4, 0.1]

# print(bucket_sort(T, 0.9))

def bucket_sort2(arr):
    n = len(arr)
    k = max(arr)
    buckets = [[] for _ in range(n)]
    interval = k / n
    for elem in arr:
        buckets[int(elem // interval)].append(elem)
    i = 0
    for bucket in buckets:
        bubble_sort(bucket)
        for elem in bucket:
            arr[i] = elem
            i += 1

# A = [0.3, 0.21, 0.11, 0.08, 0.32, 0.67, 0.53, 0.876, 0.9]
# bucket_sort2(A)
# print(A)


# T = [1.12, 1.43, 1.91, 1.42, 1.52, 1.77]
# bucket_sort2(T)


def bucketsort(A):
    n = len(A)
    if n <= 1:
        return A
    high = max(A)
    low = min(A)
    interval = high - low   #zakladamy rownomierny rozklad wartosci na danym przedziale
    buckets = [ [] for _ in range(n+1)]

    for elem in A:
        key = int(n*((elem-low)/interval))
        buckets[key].append(elem)
    for bucket in buckets:
        bucketsort(bucket)
    A = []
    for i in range(n+1):
        A += buckets[i]
    return A

A = [7.84, 6.42, 2.42, 4.52, 3.26]

# ////////////////////////


def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key

    return A


def find_bucket(val, n, _min, _max):
    i = int((val - _min) / (_max - _min) * n)
    if i == n: i -= 1
    return i


def bucket_sort3(A):

    n = len(A)
    _min, _max = min(A), max(A)
    B = [[] for _ in range(n)]

    for i in range(n):
        B[find_bucket(A[i], n, _min, _max)].append(A[i])

    for i in range(n):
        insertion_sort(B[i])

    i = 0

    for j in range(n):
        for k in range(len(B[j])):
            A[i] = B[j][k]
            i += 1

    return A


A1 = [0, 100, 20, 80, 30, 60, 40, 50, 50]
# print(bucket_sort3(A1))