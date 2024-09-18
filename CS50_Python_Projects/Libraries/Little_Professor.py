# LITTLE PROFESSOR GAME

# Libraries: 
import random 

# Main Code:
def main():
    # konstanter:
    correct_answers = 0
    questions_asked = 0
    # laver user defined functions om til en konstant jeg kan bruge i main()
    level = get_level()

    while questions_asked < 10:
        x, y = generate_integer(level)
        # tre forsøg til at svare spørgsmålet rigtigt
        for attempt in range(3):
            try: 
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    print("Correct")
                    correct_answers = correct_answers + 1
                    break
                else:
                    print(f"incorrect. Try again")
            except ValueError:
                pass
        else:
            print(f"incorrect. The correct answer is {x + y}.")
        
        # laver plus en således at useren får 10 spørgsmål i alt
        questions_asked = questions_asked + 1

    print(f"Congratulations! you got {correct_answers} out of 10 questions correctly.")
    
# går useren til at vælge level og returner det til main()
def get_level():
    print("please pick a difficulty level between 1-3")
    while True:
        try:
            n = int(input("Level: "))
            if 1 <= n <= 3:
                return n
        except ValueError:
            pass

# genererer tallene i regnestykket ud fra hvilket level useren vælger og sender x,y tilbage til main()
def generate_integer(level):
    if level == 1:
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        return x, y 
    elif level == 2:
        x = random.randint(1, 25)
        y = random.randint(1, 25) 
        return x, y 
    else:
        x = random.randint(1, 50)
        y = random.randint(1, 50) 
        return x, y 


if __name__ == "__main__":
    main()