import turtle
import math
import random

# Screen
screen = turtle.Screen()
screen.setup(900, 700)
screen.bgcolor("#100D24")
screen.title("Brahim & Yamna ❤️")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Draw a heart
def draw_heart(x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.color(color)
    t.begin_fill()

    for i in range(200):
        angle = 2 * math.pi * i / 200

        hx = 16 * math.sin(angle)**3
        hy = (13 * math.cos(angle)
              - 5 * math.cos(2 * angle)
              - 2 * math.cos(3 * angle)
              - math.cos(4 * angle))

        t.goto(x + hx * size, y + hy * size)

    t.end_fill()
    t.penup()

# Decorative stars
colors = ["#FFD700", "#FF69B4", "#FFFFFF",
          "#DA70D6", "#87CEFA"]

for i in range(65):
    x = random.randint(-420, 420)
    y = random.randint(-300, 300)

    t.goto(x, y)
    t.dot(random.randint(2, 5),
          random.choice(colors))

# Main title
t.goto(0, 270)
t.color("#FFD700")
t.write("A SPECIAL GIFT",
        align="center",
        font=("Georgia", 25, "bold"))

t.goto(0, 225)
t.color("#FFFFFF")
t.write("For my lovely parents",
        align="center",
        font=("Georgia", 17, "italic"))

# Main heart
draw_heart(0, 20, 8, "#FF2E78")

# Small heart inside
draw_heart(0, 25, 2.2, "#FFB6D5")

# Parents' names
t.goto(0, -190)
t.color("#FFD700")
t.write("BRAHIM  &  YAMNA",
        align="center",
        font=("Georgia", 29, "bold"))

t.goto(0, -235)
t.color("#FFB6D5")
t.write("My parents, my greatest blessing",
        align="center",
        font=("Georgia", 16, "italic"))

# Bottom decoration
t.goto(0, -285)
t.color("#FFFFFF")
t.write("LOVE YOU FOREVER  ♥",
        align="center",
        font=("Georgia", 16, "bold"))

# Keep window open
turtle.done()