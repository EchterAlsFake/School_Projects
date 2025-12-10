"""
Dieses Programm rechnet den Geldbetrag mit Mehrwertsteuer in einen Netteobetrag ohne Mehrwertsteuer.
"""


betrag = input(f"Gib den Betrag mit Mehrwertsteuer ein -->:")

netto = float(betrag) * 0.19


print(f"Die Mehrwertsteuer beträgt -->: {netto}")
print(f"Der Betrag ohne Mehrwertsteuer beträgt: {float(betrag) - netto}")