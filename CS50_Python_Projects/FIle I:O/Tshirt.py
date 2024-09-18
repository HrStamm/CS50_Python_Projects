# Sætter en png af en t-shirt over et ønsket billede

import sys
from PIL import Image, ImageOps
import os 

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python script.py input.csv output.csv")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    valid_extensions = (".jpg", ".png", ".jpeg")

    if not input_file.lower().endswith(valid_extensions): 
        sys.exit(f"The {input_file} is not in the correct file-format, try again")
    if not output_file.lower().endswith(valid_extensions):
        sys.exit(f"The {output_file} is not in the correct file-format, try again")

    # bruger en funktion fra os.path library hvor at [1] tager alt efter punktummet i min input- og output fil
    # dvs. at den gemmer filens format og tjekker at de er overens længere nede
    input_extension = os.path.splitext(input_file)[1]
    output_extension = os.path.splitext(output_file)[1]
    
    if input_extension != output_extension:
        sys.exit(f"{input_file} and {output_file} don't have the same filetype")

    try:
        # opens the shirt image and the input image and defines it to a variable
        shirt = Image.open("shirt.png")
        input_image = Image.open(input_file)
        # rezises billedet så det passer til størrelsen på shirt.png
        input_image = ImageOps.fit(input_image, shirt.size)
        # sætter shirt billedet oven på inputbilledet
        input_image.paste(shirt, (0, 0), shirt)
        # gemmer det i det pågældende directory
        input_image.save(output_file)
        print(f"image saved as {output_file}")
        
      
    except FileNotFoundError:
        sys.exit(f"File {input_file} not found, try again")
    except PermissionError:
        sys.exit(f"Python dosen't have permission to read {input_file}")
    except Exception as e:
        sys.exit(f"An error occurred: {e}")
    
if __name__ == "__main__":
    main()
