import turtle
import math
import random

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(1)

colors = ["red", "blue", "lime", "yellow",
          "cyan", "magenta", "orange", "pink"]

for i in range(120):
    t.penup()
    t.goto(0, 0)
    angle = math.pi * 2 / 120

    x = 16 * (math.sin(angle * i) ** 3)

    y = (13 * math.cos(angle * i)
         - 5 * math.cos(2 * angle * i)
         - 2 * math.cos(3 * angle * i)
         - math.cos(4 * angle * i)) * 15

    c = random.choice(colors)
    t.color(c)

    t.pendown()
    t.goto(x, y)

    for _ in range(8):
        t.forward(6)
        t.backward(6)
        t.right(45)

turtle.done()