import sys

a = ""
b = 0
n = abs(int(sys.argv[1]))

for i in range (1,n,2):
    
    if i % 2 != 0: #loop impar
        b += i + 1
        if i != n - 2:
            print(f"{i+1} + ", end="")
        else:
            print(f"{i + 1}")
    elif i % 2 == 0: #loop par
        b += i
        if i != n - 1:
            print(f"{i} + ", end="")
        else:
            print(f"{i}")
    
print(b)