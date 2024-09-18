# Fuel Gauge

# Eksekverer koden
def main():
    try:
        fraction = input("Input: ") 
        X, Y = convert(fraction)
        percentage = gauge(X, Y)
        print(percentage)
    except ValueError:
           print("Error, please try again")
    except ZeroDivisionError:
        print("Cannot divide by zero")
               
# Converter fraktionen "X/Y" og retunerer den
def convert(fraction):
    x, y = fraction.split("/", 2)
    X = float(x)
    Y = float(y)
    return X, Y

# Laver fraktionen om til procent og retunerer
def gauge(X, Y):
    percentage = X/Y * 100
    if percentage <= 1:
        return "Empty"
    elif percentage >= 99:
        return "Full"
    else: 
        return f"{round(percentage)}%"

if __name__ == "__main__":
    main()