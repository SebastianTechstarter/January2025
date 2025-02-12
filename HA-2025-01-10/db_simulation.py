user_database = [
    {"id": 1, "email": "max@mustermann.de", "password": "12345!"},
    {"id": 2, "email": "anna@mustermann.de", "password": "12345?"},
]


def login(email, password):
    logged_in_user = None
    for user in user_database:
        if email == user["email"]:
            print("Der Nutzer existiert")
            if password == user["password"]:
                print("Der Nutzer hat das richtige Password eingegeben")
                logged_in_user = {
                    "id": user["id"],
                    "email": user["email"],
                }
            else:
                print("Der Nutzer existiert aber das Passwort ist falsch")
            break

    if logged_in_user != None:
        print("Der Nutzer konnte erfolgreich eingeloggt werden")
        return logged_in_user
    else:
        print("Der Nutzer konnte nicht erfolgreich eingeloggt werden")
        return None


email_input = input("Email: ")
password_input = input("Passwort: ")

user = login(email_input, password_input)

print(f"Unser Benutzer: {user}")