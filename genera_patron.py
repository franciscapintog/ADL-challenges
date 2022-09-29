import sys
a = ""
n = abs(int(sys.argv[1]))

for i in range (1,n+1):
    a += str(i) + "\n"
    if i == n:
        break
    for j in range (1, i+1):
        a += str(j)

print(a)