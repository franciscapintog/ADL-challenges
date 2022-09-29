import sys

a = ""
password = (sys.argv[1])
p = password.lower()
b = "abcdefghijklmnopqrstuvwxyz"
c = 0

for i in p:
    for j in b:
        c += 1
        if i == j:
            print(f"{i}", end="")
            break
            
print(f"\n{c} intentos.")