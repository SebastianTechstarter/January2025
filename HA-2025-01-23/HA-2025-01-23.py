# Übungen auf https://www.practicepython.org/

# Exercise 3 (and Solution)
# Take a list, say for example this one:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

num = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []

for n in num:
    if n <= 5:
        new_list.append(n)

print(new_list)

# Ende Aufgabe 3

# Exercise 4 (and Solution)
# Create a program that asks the user for a number and
# then prints out a list of all the divisors of that number.

number = int(input("Welche Zahl soll überprüft werden? "))
list_range = list(range(1, number + 1))
teiler = []

for div in list_range:
    if number % div == 0:
        teiler.append(div)

print(teiler)
# Ende Aufgabe 4

# Exercise 11 (and Solution)
# Ask the user for a number and determine whether the number is prime or not.

number = int(input("Welche Zahl soll überprüft werden? "))
list_range = list(range(2, number))
teiler = []

for div in list_range:
    if number % div == 0:
        teiler.append(div)

if len(teiler) == 0:
    print("Deine eingegebene Zahl ist eine Primzahl")
else:
    print("Deine eingegebene Zahl ist keine Primzahl")

# Ende Aufgabe 11
