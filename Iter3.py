import sys

ventas = {
"Enero": 15000,
"Febrero": 22000,
"Marzo": 12000,
"Abril": 17000,
"Mayo": 81000,
"Junio": 13000,
"Julio": 21000,
"Agosto": 41200,
"Septiembre": 25000,
"Octubre": 21500,
"Noviembre": 91000,
"Diciembre": 21000,
}

def filter_dict(diccionario):
    
    ventas_us = int(sys.argv[1])
    ventas_us_dict = {}
    
    for k,v in diccionario.items():
        if ventas_us < diccionario[k]:
            ventas_us_dict[k] = v
        else:
            pass
        
    if len(ventas_us_dict) == 0:
        print("No hay ventas superiores al valor ingresado, por favor ingresa una cifra mayor.")
    
    return ventas_us_dict

print(filter_dict(ventas))