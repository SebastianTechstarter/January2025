# Implementiere den Algorithmus aus Aufgabe 2 in Python. Das Programm sollte: 
# 1. Zwei Zahlen als Eingabe akzeptieren. 
# 2. Die Summe aller ungeraden Zahlen im Bereich berechnen. 
# 3. Die Summe und die Anzahl der ungeraden Zahlen ausgeben.

print ("Dieses Programm zählt die ungeraden Zahlen in einem Intervall und errechnet deren Summe")
print ("")
a= int(input ("Gib die Anfangszahl an: "))
e= int(input ("Gib die Endzahl an: "))

start = min(a, e)
ende = max(a, e)

ungerade=[zahl for zahl in range(start, ende +1)if zahl % 2 !=0]
summe = sum(ungerade)
anzahl=len(ungerade)

print ("")
print (f"Summe der ungeraden Zahlen: {summe}")
print (f"Anzahl der ungeraden Zahlen: {anzahl}")
print ("")