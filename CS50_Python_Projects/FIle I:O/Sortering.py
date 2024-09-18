# Sortering af CSV filer i rigtig rækkefølge
# Virker således:
# the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
# the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.

import csv
import sys

def main():
    # Definere filerne plus sørger for at debugge:
    if len(sys.argv) != 3:
        sys.exit("Usage: python script.py input.csv output.csv")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not input_file.endswith(".csv"):
        print(f"{input_file} is not a .cvs file, try again")

    # læser filen plus printer den i en ny csv fil
    try:
        students = []
        with open(input_file, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # setting the maxsplit parameter to 1, will return a list with 2 elements!
                # fjener kommaet imellem first og last name
                last_name, first_name = row["name"].replace(",", "").split(maxsplit=1)
                students.append({"LastName": last_name, "FirstName": first_name, "House": row["house"]})
        
        with open(output_file, "w", newline='') as file2:
            writer = csv.DictWriter(file2, fieldnames=["FirstName", "LastName", "House"])
            # laver en header med de valgte fieldnames i csv filen, det vil sige der nu i toppen af filen vil stå:
            # FirstName, LastName, House
            writer.writeheader()

            # bruger listen students for tidligere som er blevet fyldt ud med dataene fra input_file tidligere
            # det printes så linje for linje i output_filen, men hvori navnet deles op i for- og efternavn
            for student in students:
                writer.writerow(student)

    # sørger for exceptions (Error handling)
    except FileNotFoundError:
        sys.exit(f"File {sys.argv[1]} not found, try again")
    except PermissionError:
        sys.exit(f"Python dosen't have permission to read {sys.argv[1]}")
    # generelle exceptions i tilfælde andre errors skulle forekomme
    except Exception as e:
        sys.exit(f"An error occurred: {e}")
    
if __name__ == "__main__":
    main()
