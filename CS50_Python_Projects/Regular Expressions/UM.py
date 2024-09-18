# Regular, um, Expressions

import re

def main():
    print(count(input("Text: ")))

# tester hvor mange gange ordet "um" bliver brugt i inputtet 
def count(s):
    pattern = r"\bum\b"
    tekst = re.findall(pattern, s, re.IGNORECASE)
    # tæller antallet af ums
    antal_um = len(tekst)
    if tekst:
        return f'The total number of "ums" in your text is {antal_um}'
    else:
        return f'The total number of "ums" in your text is 0'

if __name__ == "__main__":
    main()

