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

q1_sum = []
q2_sum = []
q3_sum = []
q4_sum = []

for k,v in ventas.items():
      
    if k == "Enero" or k == "Febrero" or k == "Marzo":
        q1_sum.append(ventas[k])
    elif k == "Abril" or k == "Mayo" or k == "Junio":
        q2_sum.append(ventas[k])
    elif k == "Julio" or k == "Agosto" or k == "Septiembre":
        q3_sum.append(ventas[k])
    else:
        q4_sum.append(ventas[k])
        
quarters_aux = ["Q1", "Q2", "Q3", "Q4"]
sum_aux = [q1_sum, q2_sum, q3_sum, q4_sum]

quarters = dict(zip(quarters_aux, sum_aux))

print(quarters)