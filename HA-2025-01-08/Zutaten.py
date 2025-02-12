# 1.1 UML Klassendiagramm

class Zutat():
    def __init__(self, name, kalorien_pro_100g, zubereitungszeit):
        self.name = name
        self.kalorien_pro_100g = int(kalorien_pro_100g)
        self.zubereitungszeit = int(zubereitungszeit)

# 1.2 Overkill UML Klassendiagramm mit Methoden

class Rezept():
    def __init__(self, name, beschreibung, zubereitungszeit):
        self.name = name
        self.beschreibung = beschreibung
        self.zutatenliste = {}
        self.zubereitungszeit = zubereitungszeit

    def zutat_hinzufügen(self, zutat, menge):
        self.zutatenliste[zutat] = menge
    def kalorien(self):
        kalorien_counter=0
        for zutat in self.zutatenliste:
            kalorien_counter += zutat.kalorien_pro_100g
        print (f"Die Gesamtkalorien betragen: {kalorien_counter} kcal")
    
    def kochzeit(self):
        kochzeit = 0
        for zutat in self.zutatenliste:
            if zutat.zubereitungszeit > kochzeit:
                kochzeit = zutat.zubereitungszeit
        print (f"Die Kochzeit beträgt {kochzeit} Minuten.")
    
    def rezept_anzeigen(self):
        print(f"Rezept: {self.name}")
        print("Zutaten:")
        for zutat, menge in self.zutatenliste.items():
            print (f"- {zutat.name}: {menge}")
        print(f"\nBeschreibung des Rezepts: {self.beschreibung}")


# 1.3 Beispielrezept

milch = Zutat("Milch", 50, 5)
eier = Zutat("Eier", 150, 0)
mehl = Zutat("Mehl", 300, 10)
zucker = Zutat("Zucker", 400, 6)

pfannkuchen = Rezept("Pfannkuchen", "Super leckere und fluffige Pfannkuchen.")
pfannkuchen.zutat_hinzufügen(milch, "250ml")
pfannkuchen.zutat_hinzufügen(eier, "2 Stück")
pfannkuchen.zutat_hinzufügen(mehl, "150g")
pfannkuchen.zutat_hinzufügen(zucker, "50g")

pfannkuchen.rezept_anzeigen()

pfannkuchen.kalorien()

pfannkuchen.kochzeit()