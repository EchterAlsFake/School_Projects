text = input(f"Bitte gib einen Text ein -->:")
text = text.lower()

selbstlaute = ["a", "e", "i", "o", "u"]
selbstlaute_anzahl = 0


for char in text:
    if char in selbstlaute:
        selbstlaute_anzahl += 1

print(f"Hat: {selbstlaute_anzahl} an Selbstlauten")