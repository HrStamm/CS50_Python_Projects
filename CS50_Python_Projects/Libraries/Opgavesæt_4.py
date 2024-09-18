#Libraries:
import json
import sys
import requests
import emoji 
import inflect
import random

# en Itunes søgemaskine til at søge sange
def søge_maskine():
    if len(sys.argv) != 2:
        sys.exit()

    response = requests.get(
        "https://itunes.apple.com/search?entity=song&term=" + sys.argv[1])
    o = response.json()
    for result in o["results"]:
        print(result["trackName"])

# Laver emojis
def emojizer():
    hejmeddig = input(emoji.emojize(input("input: ")))
    print(hejmeddig)

#Siger hej hej til en liste af personer med korrekt grammatur
def Adieu():
    p = inflect.engine()

    navne_liste = []
    while True:
        try:
            navn = input("Navn: ")
            navne_liste.append(navn)
        except EOFError:
            navne_liste = p.join((navne_liste))
            print("\nAdieu, adieu, to", navne_liste)
            break

# Gæt et nummer leg!
def Number_Game():
    while True:
        try:
            level = int(input("level: "))
            if 0 < level:
                random_number = random.randint(1, level)
                while True: 
                    try: 
                        guess = int(input("Guess: "))
                        if guess > random_number:
                            print("Too Large!")
                        elif guess < random_number:
                            print("Too Small")
                        else:
                            print("Just right")
                            break
                    except ValueError:
                        print("Please enter a number")
            break
        except ValueError:
            print("Please enter a number")

if __name__ == "__main__":
    Number_Game()



