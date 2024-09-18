# Lav en fuel tank der omregner til procent når du skriver hvor fyldt tanken er i formatet X/Y:
def Fuel_Tank():
    Fuel = get_fuel_in_percent("Fraction: ")
    print(Fuel)

# Funtkionen herunder får et input som en brøk og sender brøken i procent tilbage til min main function

def get_fuel_in_percent(integer):
        while True:
            try:
                Tank = input(integer)
                x, y = Tank.split("/", 2)
                # laves til floats (et tal computeren kan bruge)
                X = float(x)
                Y = float(y)
                # omregnes til procent
                Percentage = X/Y * 100
                # returner enten ordene empty eller fuld til main funktionen
                # hvs ikke de er nogen af delene, sendes procenten tilbage til main funtkionen i stedet
                # (sker på sidste linje)
                if Percentage <= 1:
                     return "Empty"
                elif Percentage >= 99:
                     return "Full"
            except ValueError:
                pass 
            except ZeroDivisionError:
                pass
            else:
                return Percentage
                           


# Lav en kode hvor brugeren kan placere ordre i restauranten "Felipe’s Taqueria"
def Felipes():
    print("Welcome to Felipes Taqueria, what can i get you?")
    bestilling = get_order("Item: ")
    print("Thank you for for your ordering at Felipes Tanqureia")

def get_order(string):
    # Definerer menuen og sætter totalen lig 0:
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    total = 0
    # Laver et loop hvori den tjekker om userens input findes i listen, 
    # hvis den gør gemmes prisen af varen under "price"
    while True:
        try: 
            order = input(string)
            if order in menu:
                price = menu[order]
    # Dernæst omdefineres totalen til den forrige total plus prisen, hvorefter det printes
    # Dette sker igen og igen til useren er færdig med at bestille, og loopet stopper når CTR D trykkes
    # Herefter sendes den endelige total tilbage til main function
                total = total + price
                print("Total: ", end="")
                print(total, "$", sep="")
        except EOFError:
            return total

# Lav en indkøbsliste i alfabetisk rækkefølge ud fra diverse input   
def Grocery():

    liste = {}

    while True:
        try:
            vare = input("").upper()
            if vare in liste:
                liste[vare] = liste[vare] + 1
            else:
                liste[vare] = 1
        except EOFError:
            print("\n" * 5)
            for _ in sorted(liste):
                print(liste[_], _,) 
            print("\n" * 5)
            break 


# input er i formatet 9/8/1636 eller September 8, 1636, hvori outputte skal være i formatet: YYYY-MM-DD
def Dato():
    måneder = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
    }
    while True:
        try:
            # For at kunne splitte ud fra flere seperators replacer jeg de to andre ønskede seperators med " "
            Month, Day, Year = input("date: ").capitalize().replace(", ", " ").replace("/", " ").split(" ", 3)
            # Laver Day til integer for at formatere den til to cifre (dvs. for at få 0 foran)
            Day = int(Day)
            if 1 > Day > 31:
                print("There cannot be more than 31 days in a month")
                break
            # hvis månederne skrives skal de udskiftes med månedsnummeret, hvorefter det skrives i ønsket format
            if Month in måneder:
                # f"{n:02}" sætter et nul foran månedsdatoerne hvis det kun er et ciffer 
                print(Year, f"{måneder[Month]:02}", f"{Day:02}", sep="-")
                break
            # month laves til integer ligesom days for at få to cifre + for at tjekke at der ikke er mere end 12 måneder
            Month = int(Month)
            if 1 > Month > 12:
                print("There is only between 1-12 months")
                break
            # hvis ikke måneden findes i min liste over måneder printes tallene bare:
            else:
                print(Year, f"{Month:02}", f"{Day:02}", sep="-")
                break
        except ValueError:
            pass
            
    

