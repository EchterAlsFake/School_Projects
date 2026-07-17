import math
from fractions import Fraction

radius = float(input("Bitte geben Sie den Radius ein -->:"))

def errechne_volumen(radius: float) -> float:
    fraction = Fraction(4, 3)
    ergebnis = fraction * math.pi * math.pow(radius, 3)
    return round(ergebnis)

def errechne_oberfläche(radius: float) -> float:
    ergebnis = 4 * math.pi * math.pow(radius, 3)
    return round(ergebnis)

volumen = errechne_volumen(radius)
oberfläche = errechne_oberfläche(radius)

print(f"""
Volumen: {volumen}
Oberfläche: {oberfläche}
""")