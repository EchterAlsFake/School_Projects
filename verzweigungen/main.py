# I already know this of course, cuz BRO I've been writing software for 5 years now xD
# If statements (ez as fuck)

# Task 1:

def task_1():
    import random
    zahl = random.randint(0, 10)
    while True:
        guess = int(input(f"Errate die Zahl -->:"))

        if guess == zahl:
            print(f"Korrekt :)")
            break

        elif guess > zahl:
            print(f"Ein bisschen mehr...")

        elif guess < zahl:
            print(f"Ein bisschen weniger...")

def task_2():
    # Dog age 1 = 14 in human
    # Dog age 2 = 22 in humans
    # After that each year = 5 in human
    dog_age = int(input(f"Gib das Alter deines Hundes ein -->:"))
    ergebnis = 0

    if dog_age >= 1:
        ergebnis += 14
        dog_age -= 1

    if dog_age >= 2:
        ergebnis += 8
        dog_age -= 1

    ergebnis += dog_age * 5
    print(f"Ihr Hund ist: {ergebnis} Jahre alt.")


def task_3():
    jahr = int(input(f"Bitte gib das Jahr ein -->:"))

    if jahr % 4 == 0:
        print(f"Erste Bedingung...")

        if jahr // 100 == 0 and jahr // 400 == 0:
            print(f"Ja, ist ein Schaltjahr")

        elif jahr // 100 == 0:
            print(f"Nein, es ist kein Schaltjahr")

        else:
            print(f"Ja, ist ein Schaltjahr")

    else:
        print(f"Nein, ist kein Schaltjahr")


def task_4():
    einkommen = int(input(f"Bitte gib dein Jahreseinkommen ein -->:"))

    if einkommen <= 8004:
        print(f"Du musst keine Steuern zahlen :)")
        return

    elif 8005 <= einkommen <= 13469:
        y = (einkommen - 8004) / 10000
        ergebnis = (912.17 * y+ 1400) * y
        einkommen = einkommen - ergebnis
        print(f"Du musst: {round(ergebnis)} Steuern zahlen")


s







def main():
    option = input(f"""
Aufgabe:
1)
2)
3)
4)
----->:
""")
    if option == "1":
        task_1()

    elif option == "2":
        task_2()

    elif option == "3":
        task_3()

    elif option == "4":
        task_4()

if __name__ == "__main__":
    main()










