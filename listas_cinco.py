auto1 = ["Mazda RX4", 21.0, 6, False, 4]
auto2 = ["Merc 240D", 24.4, 4, False, 2]
auto3 = ["Merc 280", 19.2, 6, True, 4]
auto4 = ["Valiant", 18.1, 6, True, 1]
auto5 = ["Merc 450SL", 17.3, 8, False, 3]
auto6 = ["Toyota Corolla", 33.9, 4, False, 1]
 
autos = [auto1, auto2, auto3, auto4, auto5, auto6]
prom2 = 22.316

a = list(filter(lambda x : x[1] > prom2, autos))

print(a)