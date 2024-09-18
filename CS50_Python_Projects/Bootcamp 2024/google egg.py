import random

x = random.randint(1,100)
kylling_chance = random.randint(1,100)

print("Du skal smide to æg ud fra en vilkårlig etage mellem 1 og 100\nhvis den valgte etage er højere end den etage som spillet har valgt, mister du ægget\n")

æg = 2
gæt = 0

while æg>0:
    valgt_etage = int(input("Hvilken etage dropper du fra?\n"))
    if valgt_etage >= x:
        print("Etagen var for høj, du har mistet et æg")
        æg = æg - 1
        gæt = gæt + 1 
        print(f"Du har {æg} antal æg tilbage\n")
        kylling_chance = random.randint(1,100)
        if kylling_chance <= 10:
            print("Hov, dit æg blev til en kylling... den lagde et æg mere, du har nu endnu et æg")
            æg = æg + 1
            print(f"Du har nu {æg} antal æg tilbage\n")
    else:
        print("dit æg overlevede")
        print(f"Du har {æg} antal æg tilbage\n")
        gæt = gæt + 1 

if æg == 0:
    svar_etage = int(input("Hvilken etage tror du svaret er? "))
    if svar_etage == x:
        print("Det er rigtigt!")
        print(f"Du gættede det på {gæt} gæt") 
    else:
        print(f"Det er forkert, det rigtige svar er {x}'ne etage")
        
    
                      
    
