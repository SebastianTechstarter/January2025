# Python Dictionary 
# 10 Wörter Gemüse und Obst

ger_eng = {
    "Apfel": "apple",
    "Banane": "banana",
    "Erdbeere": "strawberry",
    "Gurke": "cucumber",
    "Ananas": "pineapple",
    "Zitrone": "lemon",
    "Orange": "orange",
    "Kirsche": "cherry",
    "Tomate": "tomato",
    "Aubergine": "eggplant"
    }

my_input = input ("Welches Wort soll übersetzt werden? ").strip().capitalize()

if my_input in ger_eng:
    trans_input = ger_eng[my_input]
    print (f"Die Übersetzung von {my_input} lautet: {trans_input}")
else:
    print (f"Das Wort {my_input} befindet sich nicht im Wörterbuch")

# my_dict = {"apfel": "Apple", "wörterbuch": "dictionary"}
# my_userinput = input("Gib ein deutsches Wort ein: ")
# if my_userinput in my_dict:
#     print(f"Die Übersetzung zu {my_userinput} ist {my_dict[my_userinput]}")
# else:
#     actual_translation = input(
#         "Das Wort gibt es noch nicht, gib die engl. Übersetzung ein: "
#     )
#     my_dict[my_userinput] = actual_translation
#     print(f"Die Übersetzung zu {my_userinput} ist {my_dict[my_userinput]}")