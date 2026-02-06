# Zahlenraten

from random import randint
from math import log2

print(log2(1000000000))


zahl = randint(1, 100)

while True:
    tipp = int(input(f"Gib einen Tipp ein -->:"))

    if tipp == zahl:
        print(f"Korrekt!")
        break

    elif tipp > zahl:
        print(f"Nein, die Zahl ist kleiner")

    elif tipp < zahl:
        print(f"Nein, die Zahl ist größer")






