# En kode der validerer om useren input af en IPV4 adresse er rigtig eller ej

import re 

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # det skal åbenbart splittes op med store tal fordi ellers virker det ik, den kan kun 0-9
    # 0-9 for single-digit numbers.
    # 10-99 for two-digit numbers.
    # 100-199, 200-249, 250-255 for three-digit numbers.
    regex = r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])"
    if re.search(f"^{regex}\\.{regex}\\.{regex}\\.{regex}$", ip):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
