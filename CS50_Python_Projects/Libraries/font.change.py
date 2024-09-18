# lav en font changer
import sys
import random
from pyfiglet import Figlet

def font_change():
    figlet = Figlet()

    commands = ["-f", "--font"]
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        tekst = input("input: ")
        ny_font = random.choice(fonts)
        figlet.setFont(font = ny_font)
        print(figlet.renderText(tekst))
    
    if len(sys.argv) == 3 and sys.argv[2] in fonts and sys.argv[1] in commands:
        tekst = input("input: ")
        ny_font = sys.argv[2]
        figlet.setFont(font = ny_font)
        print(figlet.renderText(tekst))
        
    else:
        sys.exit("Error Message")

if __name__ == "__main__":    
    font_change() 
    
    
    

 


