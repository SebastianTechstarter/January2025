# Aufgabe 1:

class Haustier:
    def __init__(self, name, species, age, favorite_food, energy_level):
        self.name = name
        self.species = species
        self.age = age
        self.favorite_food = favorite_food
        self.energy_level = energy_level

# Aufgabe 2:

    def get_description(self):
        return(f"{self.name} ist ein(e) {self.species} und ist {self.age} Jahre alt.")
        
    def play(self, duration):
        energy_loss = duration * 5
        if self.energy_level - energy_loss >= 0:
            self.energy_level -= energy_loss    
        else:
            self.energy_level = 0
            print(f"Du hast {duration} Minuten mit Deinem Haustier gespielt. {self.name} ist jetzt müde und braucht eine Pause.")
        
        return(f"Du hast {duration} Minuten mit Deinem Haustier gespielt. Der Energielevel liegt nun bei {self.energy_level} %")
    
    def feed(self, food):
        if food == self.favorite_food:
            energy_gain = 30
            print(f"Dein Haustier {self.name} wurde mit seinem Lieblingsessen {self.favorite_food} gefüttert.")
        else:
            energy_gain = 10
        if self.energy_level + energy_gain > 100:
            self.energy_level = 100
        else:
            self.energy_level += energy_gain
        return (f"{self.name} wurde gefüttert und hat jetzt {self.energy_level} % Energie")
    
    # Bonus 1:
    def sleep(self, hours):
        energy_gain = hours * 10
        if self.energy_level + energy_gain > 100:
            self.energy_level = 100
            print(f"{self.name} hat genug geschlafen und ist jetzt voller Energie!")
        else:
            self.energy_level += energy_gain
            print(f"{self.name} hat geschlafen und fühlt sich erholt.")
        return f"{self.name} hat jetzt {self.energy_level} Energie."

# Aufgabe 3:
# Haustier-Objekt
first_pet = Haustier("Mimi", "Katze", 3, "Fisch", 100)

# Bonus 2:
second_pet = Haustier("Moritz", "Katze", 12, "Schinken", 85)

# Aufgabe 4:
# Klasse testen
print(first_pet.get_description())
print(first_pet.play(21))
print(first_pet.feed("Fisch"))
print(first_pet.feed("Anderes"))
print(first_pet.sleep(2))

# Bonustier:
print(second_pet.get_description())
print(second_pet.play(10))
print(second_pet.feed("Schinken"))
print(second_pet.feed("Salami"))
print(second_pet.sleep(8))