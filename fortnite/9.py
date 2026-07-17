lied = "Drei Chinesem mit dem Kontrabass".lower()
selbstlaute = ["a", "e", "i", "o", "u"]


for i in range(5):
    fertig_gebautes_lied = []

    for char in lied:
        if char in selbstlaute:
            fertig_gebautes_lied.append(selbstlaute[i])

        else:
            fertig_gebautes_lied.append(char)

    print(f"Zeile: {i} ->: {"".join(fertig_gebautes_lied)}")

