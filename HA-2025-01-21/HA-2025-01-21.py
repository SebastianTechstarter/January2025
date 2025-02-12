# 1. Erstelle eine Flask-App mit mindestens drei GET-Endpunkten.
# 2. Die GET-Anfragen sollen unterschiedliche Funktionen ausführen:
# ○ Route 1: /brand/<id>?type=<type>&condition=<condition>
# ■ Beispiel: http://localhost:6060/brand/10?type=clothes&condition=new ■ Ausgabe: "Brand-ID: 10, Type: clothes, Condition: new"
# ○ Route 2: /product/<product_id>
# ■ Beispiel: http://localhost:6060/product/123
# ■ Ausgabe: "Product-ID: 123"
# ○ Route 3: /search
# ■ Beispiel: http://localhost:6060/search?query=shoes
# ■ Ausgabe: "Searching for: shoes"
# 3. Bonus: Implementiere eine Validierung der Parameter (z. B. id muss eine Zahl sein).
# 4. Teste die Routen mit Postman oder deinem Browser.

from flask import Flask, request

app = Flask(__name__)


@app.route("/brand/<id>", methods=["GET"])
def get_brand_by_id(id):
    clothes = request.args.get("clothes")
    condition = request.args.get("condition")
    return (
        f"Welcome to {id} store. The type is {clothes} and the condition is {condition}"
    )


@app.route("/product/<product_id>", methods=["GET"])
def product_id(product_id):
    # Eingabe muss eine Zahl sein
    if product_id.isnumeric():
        return f"Product-ID: {product_id}"
    else:
        return f"Unfortunately {product_id} is not listed."


@app.route("/search/<query>", methods=["GET"])
def search(query):
    return f"Searching for: {query}"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
