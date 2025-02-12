
class Auto():
    # Eigenschaften
    def __init__(self, name, motor, reichweite, kilometerzahl):
        self.name = name
        self.motor = motor
        self.reichweite = float(reichweite)
        self.kilometerzahl = float(kilometerzahl)
    
    # Methoden
    def fahren (self, km):
        if self.reichweite >= km:
            self.kilometerzahl += km
            self.reichweite -= km
        else:
            print("Reichweite nicht ausreichend!")

    def tanken (self, km):
        self.reichweite += km

my_car = Auto("VW Caddy", "Diesel", 200, 0)
my_car.fahren(30)

print(my_car.reichweite)
my_car.tanken(200)
print(my_car.reichweite)

class E_Auto(Auto):
    def __init__(self, name, kilometerzahl):
        super().__init__(name, "Elektro", kilometerzahl)
        self.akkuladung = 100