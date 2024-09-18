import random

x = random.randint(1,100)

print("Velkommen til mit spil!\nDu skal gætte et tal mellem 0 og 100\nDu har 7 gæt i alt\n")

antal_gæt = 7

while antal_gæt>0:
    gæt = int(input("Skriv dit gæt:\n"))
    if gæt == x:
        print("Tilykke du har vundet")
        break
    elif gæt > x:
        print(f"{gæt} er større end tallet")
        antal_gæt = antal_gæt-1
        print(f"Du har nu {antal_gæt} tilbage")
    elif gæt < x:
        print(f"{gæt} er mindre end tallet")
        antal_gæt = antal_gæt-1
        print(f"Du har nu {antal_gæt} tilbage")

if antal_gæt == 0:
    print("Du har brugt for mange gæt")
        
 

 
