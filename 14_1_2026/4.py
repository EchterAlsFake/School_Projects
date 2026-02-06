def collatz(zahl):
    idx = 0

    while True:
        idx += 1

        if zahl % 2 == 0:
            zahl = zahl / 2

        else:
            zahl = 3 * zahl + 1

        print(f"Zahl: {zahl}, Index: {idx}")

        if zahl == 1:
            break

    return idx

print(f"Simulation...")

versuche = []

for i in range(1, 100):
    x = collatz(i)
    print(f"Für: {i} hat es: {x} Versuche gebraucht?")

    versuche.append(x)

versuche.sort()
print(versuche)
# 97


