zahl_1 = int(input("Please enter first number -->:"))
zahl_2 = int(input("Please enter second number -->:"))

x = zahl_1
y = zahl_2

while True:
    r = x % y
    print(fr"R: {r}")
    x = y
    print(f"X: {x}")
    y = r
    print(f"Y: {y}")
    if r == 0:
        break

print(x)
