# Dana jest tablica 2n liczb rzeczywistych. Zaproponuj algorytm, ktory podzieli te liczby na n par w taki sposob,
# ze podzial bedzie mial najmniejsza maksymalna sume liczb w parze. Przykladowo dla liczb (1, 3, 5, 9) mozemy miec
# podzialy ((1,3)(5,9),((1,5),(3,9)) oraz ((1,9),(3,5)). SUmy par dla podzialow to (4,14), (6,12) oraz (10,8), w zwiazku
# z tym maksymalne sumy to 14, 12 oraz 10. Wynika z tego , ze ostatni podzial ma najmniejsza maksymalna sume


# algorytm zachlanny (TRZEBA UDOWODNIC POPRAWNOSC)
# 1) posortuj
# 2) dzielimy pierwszy z ostatnim potem drugi z przedostatnim itp.