
# just setting up my twttr
# en bot der tager din string, fjerner alle vokalerne og printer dem:
def main():
    input_string = input("noget: ")
    result = shorten(input_string)
    print(result)
    

def shorten(word):
    vowels = ["a", "e", "y", "u", "i", "o", "A", "E", "Y", "U", "I", "O"]
    result = "".join([charachter for charachter in word if charachter not in vowels])
    return result

if __name__ == "__main__":
    main()