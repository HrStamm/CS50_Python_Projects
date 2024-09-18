# kode der laver CSV filer om til tabeller (overskuelighed for brugeren)

import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) != 2:
        sys.exit("Too few command line arguments! ")
    
    if not sys.argv[1].endswith(".csv"):
        print(f"{sys.argv[1]} is not a .cvs file, try again")
    
    try: 
        # laver en tom liste som jeg kan adde til
        liste = []
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            for row in reader:
                liste.append(row)

        # tjekker om listen er tom, og printer hvis den ikke er
        if liste: 
            print(tabulate(liste[1:], headers=liste[0], tablefmt="grid"))
        else:
            print("The file is empty")

    except FileNotFoundError:
        sys.exit(f"File {sys.argv[1]} not found, try again")
    except PermissionError:
        sys.exit(f"Python dosen't have permission to read {sys.argv[1]}")
    
if __name__ == "__main__":
    main()