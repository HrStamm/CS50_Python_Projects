import math

x1,y1 = map(int,input("punkt 1:").split(","))
x2,y2 = map(int,input("punkt 2:").split(","))

# punkterne i anden:
punkt1 = (x2-x1)*(x2-x1)
punkt2 = (y2-y1)*(y2-y1)

Afstand = math.sqrt(punkt1+punkt2)

print(f"Afstanden er {Afstand}")
