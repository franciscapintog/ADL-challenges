import sys

g = float(sys.argv[1])
r = float(sys.argv[2])
Ue = round((2*g*r*1000)**0.5, 2)

print(f"La velocidad de escape del planeta es {Ue} m/s")