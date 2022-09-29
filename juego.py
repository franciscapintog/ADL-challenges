import sys
import random

usuario = sys.argv[1]

if usuario == str("piedra") or usuario == str("papel") or usuario == str("tijera"):

    for i in range(1):
        
        computador = random.randint(1,3)
           
        if computador == 1:
            
            print("Computador juega piedra.")
                
        elif computador == 2:
                
            print("Computador juega papel.")
                
        else:
                
            print("Computador juega tijera.")
            
        if (computador == 1 and usuario == str("piedra")) or (computador == 2 and usuario == str("papel")) or (computador == 3 and usuario == str("tijera")):
        
            print("Empate.")
            
        elif (computador == 1 and usuario == str("papel")) or (computador == 2 and usuario == str("tijera")) or (computador == 3 and usuario == str("piedra")):
        
            print("Ganaste.")
            
        else:
            
            print("Perdiste.")
            
else:
    
    print("Argumento inválido: Debe ser 'piedra', 'papel' o 'tijera'.")