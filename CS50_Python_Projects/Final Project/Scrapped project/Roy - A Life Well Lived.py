# Roy: A Life Well Lived

import textwrap

def main():
    main_menu()

def main_menu():
    print('\nHello, and welcome to "Roy: A Life Well Lived"')
    print("In this game you take on the role of Roy, where you have to guide him trough a life full of decisions")
    print("This includes things such as work, investments and purchases which help spice up Roys life\n")
    print("Please choose an option:")
    print("A - Work")
    print("B - Investments")
    print("C - Shop")
    print("D - Check balance")
    print("E - Exit\n")

    while True:
        choice = input("Choice: ").upper().strip()

        if choice == "A":
            work()
        elif choice == "B":
            investing()
        elif choice == "C":
            shop()
        elif choice == "D":
            check_balance()
        elif choice == "E":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

def work():
    print("work")

def investing():
    print("invest")

def shop():
    print("\nWelcome to the shop")
    print("Please choose a shop-option:")
    print("A - Houses")
    print("B - Cars")
    print("C - Back\n")

    shop_choice = input("Choice: ").upper().strip()
    if shop_choice == "A":
        houses()
    elif shop_choice == "B":
       cars()
    elif shop_choice == "C":
        main_menu()
    

def check_balance():
    print("check balance")

def houses():
    ...
def cars():
    print("Welcome to the car shop, whoch car would you like to buy?")
    print("A - Toyota AE86")
    print("B - ")
    print("C - Back to the shop-option\n")

    car_choice = input("Choice: ").upper().strip()
    if car_choice == "A":
        toyota = f"""
         ______
        /|_||_\`.__
        (   _    _ _\\
        =`-(_)--(_)-' 
        """
        
        print(toyota)
        print("\nCongrats, you just bought yourself a brand new Toyota AE86\n")
    elif car_choice == "B":
        Ferrari = textwrap.dedent(f"""          
           
            _.-="_-         _
            _.-="   _-          | ||"""""""---._______     __..
        ___.=""""-.______-,,,,,,,,,,,,`-''----" """""       """""  __'
        __.--""     __        ,'                   o \\           __        [__|
        __-""=======.--""  ""--.=================================.--""  ""--.=======:
        ]       [w] : /        \\ : |========================|    : /        \\ :  [w] :
        V___________:|          |: |========================|    :|          |:   _-"
        V__________: \\        / :_|=======================/_____: \\        / :__-"
        -----------'  "-____-"  `-------------------------------'  "-____-"

        """)
        
        print(Ferrari)

    elif car_choice == "C":
        print("exiting car menu")
        shop()

if __name__ == "__main__":
    main()


