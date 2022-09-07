# Ćwiczenia 10: Ciąg dalszy najkrótszych ścieżek oraz zadania różne
#
# Zadania obowiązkowe
#
# Zadanie 1. (malejące krawędzie, c.d.) Dany jest graf G = (V, E), gdzie każda krawędź ma wagę
# ze zbioru {1, . . . , ∣E∣} (wagi krawędzi są parami różne). Proszę zaproponować algorytm, który dla danych
# wierzchołków x i y oblicza ścieżkę o najmniejszej sumie wag, która prowadzi z x do y po krawędziach o
# malejących wagach (jeśli ścieżki nie ma to zwracamy ∞).
#
# Zadanie 2. (domknięcie przechodnie) Proszę zaimplementować algorytm obliczający domknięcie prze-
# chodnie grafu reprezentowanego w postaci macierzowej (domknięcie przechodnie grafu G, to graf nad tym
# samym zbiorem wierzchołków, który dla każdych dwóch wierzchołków u i v ma krawędź z u do v wtedy i
# tylko wtedy, gdy w G istnieje ścieżka z u do v.
#
# Zadania standardowe

# Zadanie 1. (SAT-2CNF) Dana jest formuła logiczna w postaci 2CNF. To znaczy, że formuła jest
# koniunkcją klauzuli, gdzie każda klauzula to alternatywa dwóch literałów, a każdy literał to zmienna lub jej
# negacja. Przykładem formuły w postaci 2CNF nad zmiennymi x,y,z jest:
# (x ∨ y) ∧ (x ∨ z) ∧ (z ∨ y).
# Proszę podać algorytm, który w czasie wielomianowym stwierdza, czy istnieje wartościowanie spełniające formułę.

# Zadanie 2. (wyścigi) Król Bitocji postanowił zorganizować serię wyścigów samochodowych. Wyścigi
# mają się odbywać po trasach zamkniętych, składających się z odcinków autostrady łączących miasta Bitocji.
# Król chce, żeby każde miasto było zaangażowane w dokładnie jeden wyścig. W tym celu należy sprawdzić,
# czy da się wynająć odpowiednie odcinki autostad. Należy jednak pamiętać o następujących ograniczeniach:
# 1. w Bitocji wszystkie autostrady są jednokierunkowe,
# 2. z każdego miasta wychodzą co najwyżej dwa odcinki autostrady, którymi można dojechać do innych
# miast,
# 3. do każdego miasta dochodzą co najwyżej dwa odcinki autostrady, którymi można przyjechać z innych
# miast,
# Proszę zaproponować algorytm, który mając na wejściu opis sieci autostrad Bitocji sprawdza czy da się
# zorganizować serię wyścigów tak, żeby przez każde miasto przebiegała trasa dokładnie jednego.
# Utrudnienie: Każdy odcinek autostrady ma przedział dopuszczalnych cen i należy wybrać wspólną cenę
# dla wszystkich wynajętych odcinków.


# Zadanie 3. (wymiana walut) Dana jest tabela kursów walut. Dla każdych dwóch walut x oraz y wpis
# K[x][y] oznacza ile trzeba zapłacić waluty x żeby otrzymać jednostkę waluty y. Proszę zaproponować al-
# gorytm, który sprawdza czy istnieje taka waluta z, że za jednostkę z można uzyskać więcej niż jednostkę z
# przez serię wymian walut.


# Zadanie 4. (szachuję) Algocja leży na wielkiej pustyni i składa się z miast oraz oaz połączonych drogami.
# Każde miasto jest otoczone murem i ma tylko dwie bramy—północną i południową. Z każdej bramy prowadzi
# dokładnie jedna droga do jednej oazy (ale do danej oazy może dochodzić dowolnie wiele dróg; oazy mogą też
# być połączone drogami między sobą). Prawo Algocji wymaga, że jeśli ktoś wjechał do miasta jedną bramą,
# to musi go opuścić drugą. Szach Algocji postanowił wysłać gońca, który w każdym mieście kraju odczyta
# zakaz formułowania zadań “o szachownicy” (obraza majestatu). Szach chce, żeby goniec odwiedził każde
# miasto dokładnie raz (ale nie ma ograniczeń na to ile razy odwiedzi każdą z oaz). Goniec wyjeżdża ze stolicji
# Algocji, miasta x, i po odwiedzeniu wszystkich miast ma do niej wrócić. Proszę przedstawić algorytm, który
# stwierdza czy odpowiednia trasa gońca istnieje


# Zadanie 5. (autostrady) W pewnym państwie, w którym znajduje się N miast, postanowiono połączyć
# wszystkie miasta siecią autostrad, tak aby możliwe było dotarcie autostradą do każdego miasta. Ponieważ
# kontynent, na którym leży państwo jest płaski położenie każdego z miast opisują dwie liczby x, y, a odległość
# w linii prostej pomiędzy miastami liczona w kilometrach wyraża się wzorem len =
# sqrt((x1 − x2)^2 + (y1 − y2)^2).
# Z uwagi na oszczędności materiałów autostrada łączy dwa miasta w linii prostej.
# Ponieważ zbliżają się wybory prezydenta, wszystkie autostrady zaczęto budować równocześnie i jako cel
# postanowiono zminimalizować czas pomiędzy otwarciem pierwszej i ostatniej autostrady. Czas budowy auto-
# strady wyrażony w dniach wynosi ⌈len⌉ (sufit z długości autostrady wyrażonej w km). Proszę zaproponować
# algorytm wyznaczający minimalną liczbę dni dzielącą otwarcie pierwszej i ostatniej autostrady.

# Zadanie 6. (najlepszy korzeń) Dany jest acykliczny, spójny nieskierowany, ważony graf T (czyli T jest
# tak naprawdę ważonym drzewem). Proszę wskazać algorytm, który znajduje taki wierzchołek T, z którego
# odległość do najdalszego wierzchołka jest minimalna.