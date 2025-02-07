# Aufgabe 1
# Schreibe ein Programm, das die Häufigkeit eines Buchstabens in einem Text zählt.

print ("\n Willkommen, hier können wir die Anzahl einzelner Buchstaben in einem beliebigen Text bestimmen.\n")

content = input("Gib einen Text ein: ").lower()
letter = input ("Welcher Buchstabe soll gezählt werden? ").lower()


counter =0
while True:

    if counter in range(1):
        print (f"Der Buchstabe {letter} kommt " + str(content.count(letter)) + " mal vor.")
        counter = counter + 1
    else:
        break

print ("")