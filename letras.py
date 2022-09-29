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
  
    


def letra_o(rows):
    
    if rows < 3:
        rows = 3        
    
    for i in range(rows):
        if i == 0 or i == rows - 1:
            print("*" * rows)
        else:
            print("*" + " " * (rows - 2) + "*")     
        
    return



def letra_i(rows):
    
    if rows < 3:
        rows = 3      
    
    for i in range(rows):
        if i == 0 or i == rows - 1:
            print("*" * rows)
        else:
            print(" " * (rows//2) + "*" + " " * (rows//2))     
        
    return



def letra_x(rows):
    
    if rows % 2 == 0:
        rows = rows + 1
    if rows < 3:
        rows = 3
    
    for i in range(rows):
        if i < rows//2:
            print(" " * i, "*", " " * (rows - (2 * i + 3)), "*")
        elif i == int(rows/2):
            print(" " * (rows//2), "*")
        elif i > rows//2:
            print(" " * (rows - i - 1), "*", " " * (2 * i - (rows + 1)), "*")
    
    return

def letra_x2(n):
    
    if n % 2 == 0:
        n += 1
    
    text, aux1, aux2 = "", 0, n-1
    
    for i in range(0, n):
        for j in range(0, n):
            if j == aux1 or j == aux2:
                text += "*"
            else:
                text += " "
        text += "\n"
        aux1 += 1
        aux2 -= 1
    
    print(text)


    
