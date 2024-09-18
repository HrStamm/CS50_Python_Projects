# Lav en generator der fortælller om din nummerplade er valid eller ej ud fra nogle kriterier  

# kriterier:
# “All vanity plates must start with at least two letters.”
# “vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “No periods, spaces, or punctuation marks are allowed.”
# "Numbers cannot be used in the middle of a plate"
# "The first number used cannot be a ‘0’

# har lavet alle kriterine om til userdefined functions for overskuelighed

def main():
    while True:
        plate = input("Plate: ").upper()
        if is_valid(plate):
            print("Valid")
            break
        else:
            print("Invalid")

def is_valid(s):
    if beggining(s) and length(s) and punctuation(s) and check_first_zero(s) and middle_numbers(s):
        return True 
    else:
        return False
        
def beggining(s):
    if s[0:2].isalpha():
        return True
    else:
        return False

def length(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False

def punctuation(s):
    if not s.isalpha() or s.isdigit():
        return False
    else:
        return True

def check_first_zero(s):
    if s.startswith("0"):
        return False
    else:
        return True


def middle_numbers(s):
    isFirstTry = True
    isNum = False
    for w in s:
        if not w.isalpha():
            if isFirstTry:
                isNum = True
                isFirstTry = False
    if isNum and s[-1].isalpha():
        return False
    else:
        return True

if __name__ == "__main__":
    main()