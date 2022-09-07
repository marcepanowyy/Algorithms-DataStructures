# L - pojemnosc baku czolgu (litry)
# si - odleglosc stacji od punktu 0 (km)
# czolg spala 1l/1km
# pi - cena za litr na kazdej stacji
#
# 3 niezalezne problemy
# a) obliczyc minimalna liczbe tankowan, zeby dotrzec do punktu t (czol startuje z pelnym bakiem)
# b) obliczyc minimalny koszt dotarcia do punktu t
# b1) na kazdej stacji mozna tankowac tyle ile sie chce
# b2) jesli tankujemy to do pelna

# a) tankujemy zawsze na ostatniej stacji do ktorej mozemy dojechac majac L pojemnosci w baku (zawsze tankujemy do pelna)
# b) f(i) = minimlmy koszt dotarcia na ity kilometr
# f(k) = 0 dla k <= L
# f(x) = f(x-1) + minimum po r(k-l, k-1) z P(r)


# pokrycie przedzialami jednostkowymi. Dany jest zbior punktow {x1, x2,...,xn} na prostej.
# prosze podac algorytm ktory znajduje minimalna liczbe przedzialow jednostkowych domknietych
# potrzebnych do pokrycia wszystkich punktow z X. Przyklad: Jesli X={0.25,0.5,1.6} to potrzeba
# dwoch przedzialow np. [0.2, 1.2] oraz [1.4, 2.4]

# kolejny przedzial rozpoczyna sie na najblizszym punkcie poprzedniego konca przedzialu ktory nie zostal
# w nim uwzgledniony

def do_the_magic(T):
    T.sort()
    n, i = len(T), 0
    output = []
    while i < n:
        start = T[i]
        stop = start + 1
        i += 1
        while i < n and T[i] <= stop:
            i += 1
        output += [(start, stop)]
    return output

# T = [0.5, 0.25, 1.6]
# print(do_the_magic(T))

# Mamy dany zbior zadan T={t1,...,tn}. Kaze zadanie ti dodatkowo posiada
# a) termin wykonania d(ti) (liczba naturalna) oraz b) zysk g(t) za wykonaie w
# terminie (liczba naturalna). Wykonanie kazdeog zadania trwa jednostkę czasu
# Jesli zadanie ti zostanie wykonane przed przekroczeniem swojego terminu d(ti)
# to dostajemy za nie nagrode g(ti) (pierwsze wybrane zadanie jest wykonywane w chwili 0,
# drugie wybrane w chwili 1, trzecie w chwili 2 itd)
# Prosze podac algorytm, ktory znajdzie podzbior zdan, ktore mozna wykonac w terminie i
# ktory prowadzi do maksymalnego zysku. Prosze uzasadnic poprawnosc algorytmu

# wybieramy zadanie o najwieksyzm zysku i umieszczamy najdalej jak to jest mozliwe
# d = [5,4,4,3,1,2]
# g = [8,7,5,4,4,2]

# na piatym miejscu umieszczamy zadanie pod indeksem 0 na czwartym zadanie pod indeksem 1 itp


# ladownai eprzyczepy. Mamy przyczepe o pojemnosci K kg
# oraz zbior ladunkow o wagach w1, ..., wn. Waga kazdego z ladunkow jest potega dwojki
# czyli na przyklad dla siedmiu ladumkow wagi moga wynosic 2, 2, 4, 8, 1, 8, 16
# a pojemnosc przyczepy K = 27. Prosze podac algorytm zachlanny i uzasadnic jego poprawnosc
# kotry wybiera ladunki tak ze przyczepa jest mozliwie maksymalnie zapelniona
# ale bez przekraczania pojemnosc i jednoczesnie uzylismy mozliwie jak najmniej ladunkow
# ale jesli sie da np zaladowac przyczepe do pelna uzywajac 100 ladunkow albo zaladowac do pojemnosc
# K-1 uzywajac jednego ladunku to lepsze jest to pierwsze rozwiazanie

# wybieramy najciezszy przedmiot ktory jestesmy w stanie wsadzic
# 


# Wieze. Grupa m dzieci bawi sie w ukladanie mozliwie jak najwiekszej wiezy. Kaze dziecko ma klocki
# roznej wysokosci. Pierwsze dziecko ma klocki o wysokosciach w1^1,..., wn^1, drugie dziecko
# o wysokosciach w1^2, ..., wn^2 itd. Dzieci wlasnie poszly zjesc deser zanim uloza swoje wieze, ale
# jedno dziecko zostalo. Ma teraz jedyna okazje zeby podebrac kilka klockow innym dzieciom tak
# zeby jego wieza byla najwyzsza. Prosze podac mozliwie najszybszy algorytm rozwiazujacy ten problem
# ktory zabiera minimalna ilosc klockow (Prosze zworcic uwage, ze liczby wj^i moga byc bardzo duze)

# suma odleglosci. Dana jest posortowana tablica A zawierajaca n liczb i celem jest wyznaczenie liczby x takiej ze wartosc
# SUMA od i=0 do n-1 z | A[i] -x| jest minimalna. Prosze zaproponowac algorytm i uzasadnic jego poprawnosc
# oraz oceniz zlozonosc obliczeniowa



