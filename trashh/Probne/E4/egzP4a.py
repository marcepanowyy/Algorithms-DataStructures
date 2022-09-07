from egzP4atesty import runtests 

def can_extend(b1, b2):
    if b1[0] < b2[0] and b1[1] < b2[1]: return True
    return False

def mosty(C):

    n = len(C)
    C.sort(key=lambda x: x[1])
    C.sort(key=lambda x: x[0])

    T = [1] * n
    for i in range(n):
        for j in range(i):
            if can_extend(C[j], C[i]) and T[i] < T[j] + 1:
                T[i] = T[j] + 1

    # print(max(T))
    return max(T)

runtests ( mosty, all_tests=True )