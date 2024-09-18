def main():
    #divider med 100 for at få det i procent
    dollars = float(input("How much was the meal? ").replace("$", " "))
    percent = float(input("What percentage would you like to tip? ").replace("%", " "))/100


    tip = dollars*percent
    print(tip)

    total = tip + dollars

    response = input("Do you wanna know how much that is in total? ")
    if response.lower() == "yes":
        print(total)
    elif response.lower() == "no":
        print("alright thats fair")
    else:
        print("invalid reponse, please enter yes or no")
    
    
    
main()
