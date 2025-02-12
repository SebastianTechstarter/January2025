# Schreibt ein Python-Programm, das den User nach einem Ort fragt. 
# Nutzt wie am Vormittag einen API-call an wttr.in,
#  um einen JSON-string über die aktuellen Wetterinfos 
# des gegebenen Orts zu erhalten. 
# Bereitet die Infos für den User auf, 
# indem ihr die Temperatur, gefühlte Temparatur und
#  den area_name (Das ist der Ort der Wetterstation,
#  auf die sich wttr.in bezieht) auf der Konsole ausgebt.

import requests

location = input("Which city do you want to look at? ").capitalize()

response = requests.get(f"https://wttr.in/{location}?format=j1")
daten = response.json()
# jetzt sind die json daten in der Variable "daten" gespeichert

# print(daten)
# print(daten["current_condition"][0]["temp_C"])

temperatur = daten["current_condition"][0]["temp_C"]
feeling = daten["current_condition"][0]["FeelsLikeC"]
station = daten["nearest_area"][0]["areaName"][0]["value"]

print(f"The temperature in {location} is {temperatur} °C and feels like {feeling} °C")
print(f"Our weather station stands in {station}")