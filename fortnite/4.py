def check_winkel(winkel: int) -> bool:
    if winkel in range(0, 360):
        return True

    else:
        return False


def start():
    winkel = int(input("Bitte gib einen Winkel ein -->:"))


    while True:
        if check_winkel(winkel):
            return winkel


        print(f"Winkel: {winkel} ist nicht korrekt, wird angepasst")
        if winkel < 0:
            winkel += 360

        elif winkel > 360:
            winkel -= 360

print(start())
