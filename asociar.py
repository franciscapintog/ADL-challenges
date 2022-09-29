from functools import reduce

velocidad = [4, 4, 7, 7, 8, 9, 10, 10, 10, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 15, 15, 15, 16, 16, 17, 17, 17, 18, 18, 18, 18, 19, 19, 19, 20, 20, 20, 20, 20, 22, 23, 24, 24, 24, 24, 25]
distancia = [2, 10, 4, 22, 16, 10, 18, 26, 34, 17, 28, 14, 20, 24, 28, 26, 34, 34, 46, 26, 36, 60, 80, 20, 26, 54, 32, 40, 32, 40, 50, 42, 56, 76, 84, 36, 46, 68, 32, 48, 52, 56, 64, 66, 54, 70, 92, 93, 120, 85]
 
vd = list(zip(velocidad, distancia))

def promedio (lista):

    vd_sum = 0
    vd_prom = 0
    n = len(vd)

    vd_sum = list(reduce(lambda x,y : (x[0] + y[0], x[1] + y[1]), lista))
    vd_prom = list(map(lambda x : x/n, vd_sum))
    return list(vd_prom)

print("1. Los promedios de velocidad y distancia son, respectivamente: ", promedio(vd))

vel_bp = 0
vel_bp_dist_sp = 0
vel_sp = 0
vel_sp_dist_bp = 0

for x in vd:
    if x[0] < promedio(vd)[0]:
        vel_bp += 1
        if x[1] > promedio(vd)[1]:
          vel_bp_dist_sp += 1
    elif x[0] > promedio(vd)[0]:
        vel_sp += 1
        if x[1] < promedio(vd)[1]:
          vel_sp_dist_bp += 1

print("2. La cantidad de veces que la velocidad es menor al promedio es", vel_bp)
print("3. La cantidad de veces que la velocidad es menor al promedio y la distancia está sobre su promedio es", vel_bp_dist_sp)
print("4. La cantidad de veces que la velocidad está sobre el promedio es", vel_sp)
print("5. La cantidad de veces que la velocidad es mayor al promedio y la distancia está bajo su promedio es", vel_sp_dist_bp)