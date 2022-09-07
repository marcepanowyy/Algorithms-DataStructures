# Sortowanie tablicy n liczb ze zbioru {0, 1, ..., n^2 -1}

# word = "kot%211"
# print(word)
# for i in range(len(word)):
#     print(ord(word[i]))

def sortsquare(T):
    n = len(T)
    B = [0] * n
    C = [0] * n
    for i in range(n):
        C[T[i]%n] += 1
    for i in range(1, n):
        C[i] += C[i-1]
    for i in range(n-1, -1, -1):
        C[T[i]%2] -= 1
        B[C[T[i]%n]] = T[i]
    C = [0] * n
    D = [0] * n
    for i in range(n):
        C[B[i]//n] += 1
    for i in range(1, n):
        C[i] += C[i-1]
    for i in range(n-1, -1, -1):
        C[B[i]//n] -= 1
        D[C[B[i]//n]] = B[i]
    for i in range(n):
        T[i] = D[i]
    return T


# Sortowanie tablicy rozmiaru n zawierającej logn roznych
# wartosci

# Mamy dane dwa slowa, a i b. Prosze podac alogrytm
# sprawdzający czy sa anagramami (NAD UNICODEM 2^16 znakow)
# kot, tok - anagramy
# kot, kat - nieanagramy


from random import *

def alloc(n):
    return [randint(0, 10**9) for i in range(n)]

def check_anagrams(word1, word2):

    if len(word1) != len(word2):
        return False

    counters = alloc(2**16)

    for i in range(len(word1)):
        counters[ord(word1[i])] = 0

    for i in range(len(word1)):
        counters[ord(word1[i])] += 1
        counters[ord(word2[i])] -= 1

    for i in range(len(word1)):
        if counters[ord(word1[i])] != 0:
            return False

    return True

# word1 = "FA()LI1$22!wski%"
# word2 = "2LA(I%1i$2sk)!wF"
# print(check_anagrams(word1, word2))

# A - tablica zawierajaca n parami roznych liczb
# (wszystkie liczby sa inne), tablica A jest
# nieposortowana
# Prosze znalezc liczby A[i], A[j], takie ze
# A[i] - A[j] jest jak najwieksze oraz nie ma takiej
# liczby A[t]: A[i] > A[t] > A[j]




# A - n elementowa tablica, gdzie A[i] to nr
# koloru. A[i] nalezy {0, 1, ..., k-1} (mamy
# k-1 kolorow)
# Znalezc indeksy i<j takie ze j-i jest jak
# najmniejsze oraz w prezdziale A[i], A[i+1], ..., A[j]
# pojawiaja sie wszystkie k kolory


# Generowane sa ciagi liczb ze zbioru {0, 1, .., 10**9}
# Chcemy zaprojektowac strukture danych z operacjami:
# a) insert(x) - wstaw x
# b) count() - ile roznych liczb wstawiono
# c) reset() - usuniecie ze struktury danych
# Wszystkie operacje musza dzialac w czasie stalym O(1)