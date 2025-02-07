# Loop zum Füllen einer Liste

gerichte = []

for _ in range(3):
    user_input=input ("Welches Essen möchtest Du hinzufügen? ")
    gerichte.append(user_input)
    print (f"Meine aktuelle Liste: {gerichte}")

# die Liste wird nach und nach abgearbeitet und ausgegeben
for ge in gerichte:
    print(f"Mein Lieblingsgericht: {ge}")


# Wochentage abfragen (Essensplan)

weekdays = ["Montag", "Dienstag", "Mittwoch"]
food = []
for w in weekdays:
    for _ in range(2):
        food_input = input(f"Was möchtest du am {w} essen?")
        food.append(food_input)
print(f"Der Essensplan für die gesamte Woche sieht wie folgt aus: {food}")