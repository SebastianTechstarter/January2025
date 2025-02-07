# Aufgabe 3
# Erstelle ein Muster mit einer verschachtelten Schleife. 

counting = int(input("Wie viele Zeilen sollen erstellt werden? "))

sternchen = 0
for _ in range(counting):
    sternchen = sternchen + 1
    print ("*" * sternchen)