# Lines of code
# et program der fortæller hvor mange linjer kode en fil er

import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Input should be: python3 Lines_of_code filename.py")
    
    if not sys.argv[1].endswith(".py"):
        sys.exit("Can only be a Python file (.py)")

    try: 
        with open(sys.argv[1], "r") as file:
            lines_in_code = 0
            for line in file:
                stripped_line = line.strip()
                if stripped_line and not stripped_line.startswith("#"):
                    lines_in_code += 1

    except FileNotFoundError:
        sys.exit(f"File {sys.argv[1]} not found, please try again")
    except PermissionError:
        sys.exit(f"Python dosen't have permission to read {sys.argv[1]}")

    print(f" The total lines of code excluding comments and blank lines is: {lines_in_code}")
  

if __name__ == "__main__":
    main()
