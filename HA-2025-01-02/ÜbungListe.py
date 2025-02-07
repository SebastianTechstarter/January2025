# Übungen für Listen
## Erstelle ein Python-Skript, das eine Liste von Zahlen enthält
## 1) Die Summe aller Zahlen berechnen
## 2) Nur die ungeraden Zahlen ausgibt
## 3) Die größte Zahl in der Liste findet.


example_list = [7, 12, 11, 15]
# 1
summe=sum(example_list)

print (summe)

# 2
def ungerade(example_list):
    for num in example_list:
        if num % 2 == 1:
        
            print (num)

ungerade(example_list)

# 3
biggest=max(example_list)

print (biggest)

for zahl in example_list:
    if zahl > biggest:
        biggest = zahl

print (biggest)