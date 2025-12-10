import time
import random
import turtle
from hue_shift import return_color

tx = turtle.Screen()
t = turtle.Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)



t.speed(100)
t.pensize(2)
t.pencolor(random_color())

x = -480
y = 400

q = 480
w = 400


def back_one():
    global x, y
    t.pencolor(random_color())

    t.penup()
    t.goto(x, y)
    t.pendown()

    y -= 10
    t.goto(480,  y)


def back_two():
    global q, w
    t.pencolor(random_color())

    t.penup()
    t.goto(q, w)
    t.pendown()

    w -= 15
    t.goto(-q, w)

def back_three():
    global q, w
    t.pencolor(random_color())

    t.penup()
    t.goto(q, -w)
    t.pendown()

    w -= 15
    print(f"Going to: {q}, {-w}")
    t.goto(q, -w)



# Links -> Rechts
t.penup()
t.goto(-480, y)
t.pendown()
t.goto(480, y)

# Rechts -> Links

for i in range(50):
    back_one()


# Links -> Rechts
t.pencolor(random_color())
t.penup()
t.goto(q, w)
t.pendown()
t.goto(q, w)


for i in range(50):
    back_two()


t.pencolor(random_color())
t.penup()
t.goto(q, -w)
t.pendown()
t.goto(q, -w)


for i in range(50):
    back_three()

tx.exitonclick()






