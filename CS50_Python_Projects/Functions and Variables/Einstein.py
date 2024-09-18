# kode for at beregne E = m*c^2 når du kender massen

def main():
    # først skal vi selv skrive massen ind som en integer:
    m = int(input("What is the mass? "))

    # pow er pythons imbyggede funktion for opløftet i en eksponent, den defineres:
    c2 = pow(300000000,2)
    
    # Dette er formlen vi skal bruge:
    E = m*c2

    print(E)


main()

