# Dane jest n punktow na osi liczbowej jednowymiarowej. Napisz
# algorytm, ktory stwierdzi, w ktorym z nim nalezy wybudowac dom, tak
# aby suma euklidesowych odleglosc od tego punktu do wszystkich pozostalych
# byla minimalna. Nalezy zwrocic rowniez te sume. Algorytm powinien byc
# jak najszybszy.

# szukamy mediany

import math

def Med(A):
    n = len(A)
    if n % 2 == 0:
        return (A[n//2-1] + A[n//2])/2
    else:
        return A[n//2]

A = [2,3,4,7,8,9,4]
print(Med(A))