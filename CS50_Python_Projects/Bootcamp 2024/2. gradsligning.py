import math

a,b,c = map(int,input("giv os a,b.c i en andengradsligning: ").split())

b2 = b*b

d = b2-(4*a*c)

if d>0:
    x1 = (-b+math.sqrt(d))/2*a
    x2 = (-b-math.sqrt(d))/2*a
    print(f"de to løsninger er {x1} og {x2}")
elif d==0:
    x = -b/2*a
    print(f"løsningen er {x}")
elif d<0:
    print("ingen løsning")
    
