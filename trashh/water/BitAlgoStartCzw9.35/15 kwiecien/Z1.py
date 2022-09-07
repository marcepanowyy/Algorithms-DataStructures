# mamy dany ciag napisow (slow) S = [s1, ..., sn] oraz pewien napis t. Wiadomo ze t mozna zapisac jako zlaczenie pewnej
# ilosci napisow z S (z powtorzeniami). Na przyklad dla S = [s1, s2, s3, s4, s5] gdzie s1 = ab, s2 = abab, s3 = ba, s4 = bab
# s5 = b, napis t = ababbab mozna zapisac miedzy innymi jakos s2s4 lub jako s1s1s3s5. Taki wybor konkretnych si nazywamy
# reprezentacja. Przez szerokosc reprezentacji rozumiemy dlugosc najkrotszego si nalezacego do reprezentacji- dla s2s4 szerokosc
# to 3, a dla s1s1s3s5 szerokosc to 1. Zaimplementuj algorytm, ktory majac na wejsciu S oraz t znajdzie max szerokosc reprezentacji t
# tzn najkrotszy napis w jej reprezentacji jest najdluzszy. Oszacuj czas dzaialania algorytmu

# majac napis t, oraz slowo s1 ktore przedstawia t, szerokoscia w tym przypadku bylalby dlugosc slowa t

# F(i,j) - maksymalna szerokosc reprezentacji od i do j
# F(i,j) = -1, dla i >= j
#        = -1, dla gdy nie istnieje reprezentacja od i do j
#        = maksymalna szerokosc od i do j w pozostalych przypadkach

# F(i,j) = max{min{F(i, k)+F(k, j)+1, F(i,j)}} i<k<j   NIE JESTEM PEWNY XD
#              po k