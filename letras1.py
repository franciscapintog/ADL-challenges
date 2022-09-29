import string

def gen(len):
    
    alf = string.ascii_lowercase
    alf2 = ""
    if len < 1:
        len = 1
    elif len > 26:
        len = 26
    
    for i in range(len):
        alf2 += alf[i]
    
    print(alf2)
    return 
  
b = int(input("Ingresa un número entre 1 y 26:\n"))

gen(b)

    
