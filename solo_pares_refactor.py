import sys

n = abs(int(sys.argv[1]))
m = n + 1

for i in range (m):
    
    if m % 2 != 0:
        m -= 1
        print(m)
        
    else:
        m -= 2
        print(m)
        
    if m == 2 or m == 1:
        break