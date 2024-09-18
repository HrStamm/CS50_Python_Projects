

print()

etage = int(input("vælg etage: "))

æg = 2
gæt = 0
foreløbigt_gæt = 0

while æg>0:
    if æg == 2:
        foreløbigt_gæt = foreløbigt_gæt + 10
        print(f"computeren gættede på {foreløbigt_gæt}")
        if etage <= foreløbigt_gæt:
            æg = æg-1
            print("computeren gættede forkert og mistede et æg")
            foreløbigt_gæt = foreløbigt_gæt - 10
            gæt = gæt + 1
        else:
            print("Etagen er for lav, computeren mistede ikke et æg")
            gæt = gæt + 1

    if æg == 1:
        foreløbigt_gæt = foreløbigt_gæt + 1
        print(f"computeren gættede på {foreløbigt_gæt}")
        if etage <= foreløbigt_gæt:
            æg = æg-1
            print(f"computeren gættede på {foreløbigt_gæt}, det var rigtigt")
            gæt = gæt + 1
            print(f"\ncomputeren brugte {gæt} antal gæt")
        else:
            print("Etagen er for lav, computeren mistede ikke et æg")
            gæt = gæt + 1

            
                
 

   
