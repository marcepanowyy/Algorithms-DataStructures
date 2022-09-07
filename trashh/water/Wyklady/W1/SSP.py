# Problem: Suma Spojnego Podciagu (SSP)
# Dane: A[0,...,n-1] - Tablica liczb calkowitych

from time import time
from random import seed, randint

n = int(input("podaj ilosc elem. tablicy: "))

seed(42)

def getdata(n):
    return [randint(-100000,100000) for i in range(n)]

T=getdata(n)

# O(n)

def ssp1(T):
    result = 0
    partial = 0
    for i in range(len(T)):
        partial += T[i]
        partial = max(0, partial)
        result = max(partial, result)
    return result

start = time()

# wynik = ssp1(T)
# print(wynik)

end = time()

print("czas dzaialania: %f sek" %(end-start))

