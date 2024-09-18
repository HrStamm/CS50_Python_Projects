# tre forskelige metoder at lave loops:
def loops():
    # while loop (f.eks. print meow 3 gange)
    i = 0
    while i < 3:
        print("meow")
        i += 1

    # for loop (samme eksempel) 
    # man bruger _ for at vise at det er varibel der ikke skal bruges senere
    for _ in range(3):
        print("meow")

    # multiplikation i funktionen (samme eksempel)
    # \n betyder ny linje, så det hele ikke printes i samme linje
    print("meow\n" * 3, end="")

def okayokay():
    # bliv ved med at have et input til useren giver et korrekt input (dette tilfælde en int)
    # her vælger useren hvor mange gange den skal meowe, men tvinger useren til at vælge et positivt tal
    while True:
        n = int(input("What is n? "))
        if n > 0:
            break
    
    for _ in range(n):
        print("meow")

def rangliste():
    # man kan lave en rangliste af forskellige ting, f.eks.:
    students = ["Hermione", "Harry", "Ron"]

    for i in range(len(students)):
        print(i+1, students[i])

