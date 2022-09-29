import sys

saldo = 0
opcion = 0

if len(int(sys.argv[1])) == 1:
    
    saldo = 0

else:
    
    saldo = int(sys.argv[1])
    
print("----Bienvenid@ al Banco de Talca. Ingresa una opción:----\n1. Consultar saldo\n2. Hacer depósito\n3. Realizar giro\n4. Salir")
    
opcion = int(input("Opción:\n"))

def mostrar_saldo(saldo = 0):
    
    print("Tu saldo es de {saldo} pesos.\n")
    
def depositar(saldo, cantidad):
    
    cantidad = int(input("Ingresa la cantidad que deseas depositar:\n"))
            
    saldo = saldo + cantidad
    
    print(f"Tu nuevo saldo es {cantidad} pesos.")
        
    return saldo

def girar(saldo, cantidad):
    
   cantidad = int(input("Ingresa la cantidad que deseas girar:\n"))
        
   if saldo < cantidad:
            
       print(f"No puedes realizar este giro, tu saldo es de {saldo}, ingresa otro monto:\n")
       saldo = int(input("Ingresa otro monto:\n"))
             
   else:
            
       saldo = saldo - cantidad
       print(f"Giro realizado, tu nuevo saldo es de {saldo}.")
       
       return saldo
               
while opcion < 4:
      
    print("La opción escrita es incorrecta, ingresa una opción del menú")
        
    opcion = int(input("Opción:\n"))   
    
    if opcion == 1: #definición de saldo
          
        mostrar_saldo()
        
    elif opcion == 2:

        depositar()        

    elif opcion == 3:
        
        girar()
        
    elif opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4:

    elif opcion == 4: #salir, opción 4
        
        print("Hasta luego!")
        break

