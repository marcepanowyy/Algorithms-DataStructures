# Dostajac na wejsciu string zlozony z liter a-z zwrocic najdluzszy jego fragment
# ktory jest palindromem

# Palindrom to ciag znakow, ktory wyglada tak samo czytany zarowno od lewej, jak i od prawej
# strony np. abba xyzyx

# f(i,j) = True, jezeli ciag od i do j jest palindromem
# f(i,j) = f(i-1, j+1) | a[i] = a[j]
# f(i, i+1) = a[i] == a[i+1]
# f(0,0) = True
# sprawdzamy czy istnieja palindromy dwuelementowe