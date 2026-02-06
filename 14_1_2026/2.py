from random import randint

number = 0
index = 0

while number != 6:
    index += 1
    number = randint(1, 6)

print(f"Es hat: {index} Versuche gebraucht!")
