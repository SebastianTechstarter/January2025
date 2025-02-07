# Implementiere einen Algorithmus, der als Git-Befehle-Wörterbuch genutzt werden
# soll. Also zum Beispiel soll der Nutzer pull eingeben und dazu soll eine Beschreibung
# zu dem pull Befehl ausgegeben werden.

gitcom = {
    "git init": "Erstellt ein neues Git-Repository im aktuellen Verzeichnis.",
    "git clone": "Klonen eines bestehenden Repositories aus einem Remote-Repository.",
    "git pull": "Holt die neuesten Änderungen vom Remote-Repository und integriert sie in das lokale Repository.",
    "git push": "Überträgt die lokalen Commits auf das Remote-Repository.",
    "git commit": "Speichert Änderungen in der lokalen Git-Datenbank.",
    "git status": "Zeigt den aktuellen Status der Arbeitskopie und des Staging-Bereichs an.",
    "git branch": "Zeigt die aktuellen Branches an oder erstellt einen neuen Branch.",
    "git merge": "Merge den angegebenen Branch in den aktuellen Branch.",
    "git log": "Zeigt die Commit-Historie des Repositories an.",
    "git diff": "Zeigt die Unterschiede zwischen den Dateien oder Commits an.",
    "git checkout": "Wechselt zu einem anderen Branch oder einer bestimmten Commit-Version.",
    "git reset": "Setzt den aktuellen Branch auf einen früheren Zustand zurück.",
    "git rm": "Entfernt eine Datei aus dem Git-Index und optional auch aus dem Arbeitsverzeichnis.",
    }

my_input = input ("Welcher Begriff ist noch unklar?  ").strip().lower()
print ("")

if my_input in gitcom:
    description = gitcom[my_input]
    print (f"{my_input}: {description}")
    print ("")
else:
    print (f"Das Wort {my_input} befindet sich nicht im Verzeichnis")
    print ("")