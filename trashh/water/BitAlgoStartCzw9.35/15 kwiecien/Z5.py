# czarodziej pascal ma n stosow porcelanowych talerzy, przy czym kazdy stos zawiera dokladnie k talerzy.
# pascal wystawia dzis wieczorem kolacje dla P gosci i jedzenie bedzie serwowane na tych wlasnie talerzach.
# kazdy talerz ma pewne piekno okreslone liczba calkowita. Pomoz czarodziejowi wybrac dokladnie P talerzy
# tak aby one mialy one maksymalne mozliwe piekno, Ale uwaga: stos to stos wiec jesli chcesz zebrac jakis talerz
# to musisz tez zebrac wszystkie nad nim
# NIE PRZEKLADAMY TALERZY ZE STOSU NA STOS!!!

# g(t, i) = suma gornych i talerzy stosu t
# f(t,i) ---> t - stosy od 0 do t wlacznie, i - liczba talerzy = maksymalne piekno
# przy wzieciu i talerzy ze stosu od 0 do t wlacznie
# f(t,i) = max{f(t-1, x) + g(t, i-x)}, 0<=x<=i, x <= k

# max z 9 stosow + piekna talerzy z 10 stosu
















