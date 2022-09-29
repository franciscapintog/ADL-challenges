import sys

n = abs(int(sys.argv[1]))
m = n + 1

for i in range (m):
    
    if m % 2 != 0:
        m -= 2
        print(m)
        
    else:
        m -= 1
        print(m)
        
    if m == 1 or m == 0:
        break