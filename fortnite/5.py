import random

feld = []

for i in range(100):
    zahl = random.randint(5, 10)
    feld.append(zahl)

print(feld)
vertauschen = input(f"Soll das Feld vertauscht werden? [Ja/Nein]")

if vertauschen == "Ja":
    feld.reverse()

print(f"Feld vertauscht: \n {feld}")
