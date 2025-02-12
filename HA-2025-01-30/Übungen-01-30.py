# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user
# Odd or even

num = int(input("Welche zahl soll überprüft werden? "))

if num % 2 == 0:
    print("Die Zahl ist gerade")

else:
    print("Die Zahl ist ungerade")

###


# Exercise 20 (and Solution)
# Write a function that takes an ordered list of numbers
# (a list where the elements are in order from smallest to largest)
#  and another number. The function decides whether or not the given
#  number is inside the list and returns (then prints) an appropriate boolean.
def crawl_elements():
    for suche in liste:
        if suche == liste:
            return True

    return False


if __name__ == "__main__":
    liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    suche = int(input("Nach welcher Zahl suchen wir? "))

crawl_elements()
