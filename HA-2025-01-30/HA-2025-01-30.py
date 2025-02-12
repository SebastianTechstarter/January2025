def begruessung(name):  # Klammern um "name" vergessen
    print(
        "Hallo, " + name
    )  # Variablen werden nicht groß geschrieben, print nicht eingerückt


def addiere_zahlen(a, b):  # Doppelpunkt vergessen
    ergebnis = a + b
    return ergebnis  # "n" in "ergebnis" vergessen


def subtrahiere_zahlen(a, b):
    return int(
        a - b
    )  # "c" nicht definiert, durch "b" ersetzt, Ergebnis muss eine Zahl sein und kein Text


def main():  # Doppelpunkt vergessen
    zahl1 = int(
        input("Gib eine Zahl ein: ")
    )  # Zahlen müssen für Python als Zahl erkennbar sein
    zahl2 = int(input("Gib eine weitere Zahl ein: "))

    summe = addiere_zahlen(zahl1, zahl2)
    print(f"Die Summe ist: {summe}")  # "f" und die geschweiften Klammern vergessen

    differenz = subtrahiere_zahlen(zahl1, zahl2)
    print(f"Die Differenz ist: {differenz}")

    begruessung("Max")


if __name__ == "__main__":  # Zweites "=" vergessen
    main()
