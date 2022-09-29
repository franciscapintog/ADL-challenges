import time

#se crea variable cuenta regresiva, cr

cr = int(input("Ingresa un número para iniciar la cuenta regresiva:\n"))

print(f"Iteración {cr}...")
time.sleep(1)

while cr > 0:
        
        if cr > 1:
            cr -= 1
            print(f"Iteración {cr}...")
            time.sleep(1)