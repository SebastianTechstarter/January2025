from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hier findet Ihr die Startseite."

# Zusatzaufgabe
# 1. Route 1: /greet/<name> 
# ○ Diese Route soll eine personalisierte Begrüßung zurückgeben. ○ Beispiel: 
# ■ Aufruf: http://127.0.0.1:5000/greet/Max 

@app.route("/greet/<name>")
def greet(name):
    return (f"Hallo {name}, willkommen auf meiner Flask-API!")

# Zusatz Ende

@app.route("/about")
def about():
    return "Mein Name ist Sebastian Rehberg und ich bin gerade dabei, n/ mich für die IT-Branche weiterzubilden."

@app.route("/projekt")
def projekt():
    return "Aktuell arbeite ich, genau wie meine Mitstreiter, an einer einfachen Flask-API für Anfänger. Bisher macht es Spaß. ;-)"

@app.route("/news")
def news():
    return "Man kann sich mit so vielen Bereichen beschäftigen. n/ Seit einer Woche habe ich bspw. einen neuen 3D-Drucker, der genutzt werden möchte n/ und ich habe vor, in naher Zukunft mittels Raspberry Pi den Druckprozess zu automatisieren."

@app.route("/feedback")
def feedback():
    return "Wir freuen uns immer über Feedback. Schreibe uns gern unter feedback@example.com oder unter sebastianrehberg.rehberg@tn.techstarter.de"

@app.route("/support")
def support():
    return "Erfahrene Programmierer würden hier Kontaktdaten für den Support anbieten. n/ Eine naheligende E-Mail dafür wäre support@example.com"

if __name__ == "__main__":
    app.run(port=5000)