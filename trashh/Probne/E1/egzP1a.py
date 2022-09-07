from egzP1atesty import runtests 

# M - tablica zawierajaca wszystkie oznaczenia
# W - string w jezyku naturalnym
# D - tablica indeksow rozpoznawalnych

def ConvertToMorse(word, M):
    result = ""
    for letter in word:
        ind = ord(letter) - ord("A")
        result += M[ind][1]
    return result

def titanic(W, M, D):
    d = {}
    for ind in D:
        morse = M[ind][1]
        if morse not in d: d[morse] = 1

    searched = ConvertToMorse(W, M)
    n = len(searched)
    dp = [i+1 for i in range(n)]

    for start in range(n):
        for iter in range(4):

            if start + iter < n and searched[start:start+iter+1] in d:
                if start - 1 >= 0 and dp[start+iter] > dp[start-1] + 1: dp[start+iter] = dp[start-1] + 1
                elif start == 0: dp[start+iter] = 1

    return dp[-1]

W = 'SOS'
D = [0, 4, 13, 19, 25]
M = [('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'), ('E', '.'), ('F', '..-.'),
('G', '--.'), ('H', '....'), ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
('M', '--'), ('N', '-.'), ('O', '---'), ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),
('S', '...'), ('T', '-'), ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'),
('Y', '-.--'), ('Z', '--..')]

titanic(W, M, D)

# runtests ( titanic, recursion=False )