# Aufgabe 2
# Schreibe ein Programm, das: 
# 1. Den Benutzer auffordert, 5 Zahlen einzugeben. 
# 2. Mit einer Schleife die Summe und den Durchschnitt der Zahlen berechnet. 3. Die Ergebnisse ausgibt. 

counting = int(input("Wieviele Zahlen möchtest Du verrechnen?"))
numbers = []

for _ in range(counting):
    user_input = input ("Welche Zahl soll hinzugefügt werden? ")
    converted_input = float(user_input)
    numbers.append(converted_input)
    print (f"Meine aktuelle Liste: {numbers}")
    print ("")


summe = sum(numbers)
average = float(summe / counting)
print ("")
print (f"Die Summe der eingegebenen Zahlen lautet {summe}")
print (f"Und der Durchschnitt der Zahlen ist {average}")
print ("")