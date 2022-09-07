# black forest to las rosnacy na osi liczbowej. Las sklada sie
# z n drzew rosnacych na pozycjach 0,..., n-1. Dla kazdego i od 0 do n-1
# znany jest zysk ci, jaki mozna osiagnac scinajac drzewo z pozycji i.
# John chce uzyskac max zysk ze scinanych drzew, ale prawo zabrania
# scinania dwoch drzew pod rzad. Prosze zaproponowac algorytm, dzieki ktoremu
# John znajdzie optymalny plan wycinki

#  f(i) = max zysk do itego drzewa
#  f(i) = max(f(i-1), f(i-2) + A[i])

def sub(A):
    n = len(A)
    A[1] = max(A[0], A[1])
    for i in range(2, n):
        A[i] = max(A[i-1], A[i-2] + A[i])

    return A[n-1]

# C = [4, 11, 5, 2, 10]
# print(sub(C))


# Kazdy klocek to przedzial postaci [a,b]. Dany jest ciag klockow
# [a1,b1], [a2,b2], ..., [an, bn]. Klocki spadaja na osc liczbowa w kolejnosci
# podanej w caigu. Prosze zaproponoiwac algorytm ktory oblicza ile klockow
# nalezy usunac z listy, tak zeby kazdy kolejny spadajacy klocek
# miescil sie w calosci w tam, ktory spadl tuz przed nim
# najdluzszy ciag klockow, z ktorych kazdy jest zawarty w poprzednim
# konczacy sie na klocku o indeksie i

# f(i) = max{f(j) +1 | klocek j zawiera klocek i}
#       0<=j<i

def bricks(T):
    n = len(T)
    F = [1] * n
    for i in range(1, n):
        for j in range(i):
            if T[i][0] >= T[j][0] and T[j][1] >= T[i][1] and F[j] + 1 > F[i]:
                F[i] = F[j] +1

    return n - max(F)

# Pewna zaba skacze po osi liczbowej. Ma sie dostac z zera do n-1, skaczac wylacznie
# w kierunku wiekszych liczb. Skok z liczby i do liczby j (j>i) kosztuja ją j-i jednostek energii
# a jej energia nigdy nie moze spasc ponizej zera. Na poczatku zaba ma 0 jednostek energii, ale na szczescie
# na niektorych liczbach takze na zerze leza przekaski o okreslonej wartosci energetycznej . Wartosc przekaski dodaje sie
# do aktualnej energii Zbigniewa. Prosze zaproponowac algorytm, ktory oblicza minimalna liczbe
# skokow na dotarcie z 0 do n-1 majac dana tablice A z wartosciami energetycznymi przekasek na kazdej z liczb

# f(i,j) = minimalna liczba skokow zeby dotrzec do itego pola i miec j jednostek energii (po zjedzeniu A[i])
# min po j z f(n-1, j) --> rozw
# f(i, j) = min po k, gdzie k nalezy [0, i) z (f(k, i-k-A[i])+1)
# f(i, -j) = inf

# ladowanie promu. Dana jest tablica A[n] z dlugosciami samochodow, ktore stoja w kolejce, zeby wjechac na prom.
# prom ma dwa pasy (lewy i prawy), oba dlugosci L. Prosze napisa program, ktory wyznacza, ktore samochodu powinny pojechac na ktory pas,
# zeby na promie zmiescilo sie jak najwiecej aut. Auta musza wjecahc w takiej kolejnosci, w jakiej sa podane w tablicy A

# f(i, g, d) =


# Mamy drzewo binarne z roznymi wartosciami na node'ach (moga byc ujemne). Znalezc dlugosc najwiekszej sciezki w tym drzewie
# f(v) - wartosc najwiekszej sciezki zaczynajacej sie w V i kierujacej sie w strone lisci
# f(i) = max{0, v.val, v.val + f(v.right), v.val + f(v.left}
# wynik =>  max po wszystkich v z (0, v.val + f(v.right) + f(v.left))        (v.val + f(v.right) + f(v.left) moze byc ujemne dlatego 0 w argumencie)


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self. lef = None
        self.f = 0

v = Node(5)
u = Node(-2)
w = Node(3)
z = Node(10)

v.lef = u
v.right = w
w.right = z

def f(v):
    if v == None: return 0
    (L, ML) = f(v.left)
    (R, MR) = f(v.right)

    v.f = max(0, v.val, v.val+L, v.val+R)
    M = max(ML, MR, v.f)
    return (v.f, M)

# dwa przedzialy mozna skleic jesli dotykaja sie (ale nie zachodza na siebie). Prosze podac algorytm, ktory oblicza dlugosc najdluzszego
# przedzialu jaki mozna osiagnac przez sklejanie k przedzialow

# tworzymy mapowanie
# f(i,j) = minimalna liczba przedzialow ktore trzeba skleic zeby powstal
# przedzial od punktu i do pkt j
# f(i,j) = min po k {f(i,k)+f(k,j)+1}