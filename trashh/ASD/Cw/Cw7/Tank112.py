# Czołg jedzie z punktu A do punktu B. Spalanie czołgu to dokładnie jeden litr paliwa na jeden kilometr
# trasy. W baku mieści się dokładnie L litrów paliwa. Trasa z A do B to prosta, na której znajdują się
# stacje benzynowe (na pozycjach będących liczbami naturalnymi; A jest na pozycji 0). Proszę podać
# algorytmy dla następujących przypadków:

#     1) Wyznaczamy stacje na których tankujemy tak, żeby łączna liczba tankowań była minimalna.

#     2) Wyznaczamy stacje tak, żeby koszt przejazdu był minimalny (w tym wypadku każda stacja ma
#        dodatkowo cenę za litr paliwa). Na każdej stacji możemy tankować dowolną ilość paliwa.

#     3) j.w., ale jeśli na stacji tankujemy, to musimy zatankować do pełna.


# 1

# jakis zachlan
# tankujemy zawsze na ostatniej stacji do ktorej mozemy dojechac na zasiegu L

def tank_fueling1(distance, fuel_tank, stops):
    refills = 0
    current_refill = 0
    limit = fuel_tank
    while limit < distance:
        if current_refill >= len(stops) or stops[current_refill] > limit:
            return False
        while current_refill < len(stops) - 1 and stops[current_refill + 1] <= limit:
            current_refill += 1
        refills += 1
        limit = stops[current_refill] + fuel_tank
        current_refill += 1
    return refills


distance1 = 21
fuel_tank1 = 5
stops1 = [2, 3, 5, 8, 11, 13, 17]
# print(tank_fueling1(distance, fuel_tank, stops))


#     2) Wyznaczamy stacje tak, żeby koszt przejazdu był minimalny (w tym wypadku każda stacja ma
#        dodatkowo cenę za litr paliwa). Na każdej stacji możemy tankować dowolną ilość paliwa.


from math import inf

def tank_fueling2(distance, fuel_tank, stops, prices):
    if fuel_tank < stops[0]:
        return False
    T = [-1] * (distance + 1)
    for i in range(len(T)):
        for j in range(len(stops)):
            if stops[j] > i:
                break
            if stops[j] == i:
                T[i] = prices[j]
    total_cost = 0
    for i in range(1, distance + 1 - fuel_tank):
        min_cost = inf
        for j in range(i, i + fuel_tank):
            if T[j] != -1:
                min_cost = min(min_cost, T[j])
        total_cost += min_cost
    return total_cost


# 3)


def tank_fueling3(distance, fuel_tank, stops, prices):
    F = [0] * len(stops)
    F[0] = prices[0] * stops[0]
    for i in range(1, len(stops)):
        j = i - 1
        minimum = F[j] + (stops[i] - stops[j]) * prices[i]
        while j >= 0 and fuel_tank >= stops[i] - stops[j]:
            minimum = min(minimum, F[j] + (stops[i] - stops[j]) * prices[i])
            j -= 1
        if j == -1 and fuel_tank >= stops[i]:
            minimum = min(minimum, prices[i] * stops[i])
        F[i] = minimum
    result = F[len(stops) - 1]
    for i in range(len(stops)):
        if distance - stops[i] <= fuel_tank:
            result = min(F[i], result)
    return result


stops = [1, 9, 15, 16, 17, 27, 28]
prices = [1, 100, 10, 15, 1, 30, 30]
distance = 30
fuel = 14
print(tank_fueling2(distance, fuel, stops, prices))
print(tank_fueling3(distance, fuel, stops, prices))