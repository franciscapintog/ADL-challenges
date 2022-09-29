import sys
a = ""
b = 0
n = abs(int(sys.argv[1]))
m = n + 1

for i in range (1,n,2):
    
    if i % 2 != 0:
        b += i + 1
    elif i % 2 == 0:
        b += i
    
print(a)
print(b)