import turtle as t
from math import pi

t.speed(0)

def circle(radius):
    n = 100
    for i in range(n):
        t.forward(2 * pi * radius / n)
        t.right(360 / n)


def half_of_circle(radius):
    n = 200
    for i in range(n // 2):
        t.forward(2 * pi * radius / n)
        t.right(360 / n)
                    # Морда
t.penup()
t.goto(0, 80)
t.pendown()

t.color('black', 'yellow')
t.begin_fill()
circle(80)
t.end_fill()

                    # Левый глаз
t.penup()
t.goto(-40, 40)
t.pendown()

t.color('black', 'blue')
t.begin_fill()
circle(10)
t.end_fill()

                    # Правый глаз
t.penup()
t.goto(40, 40)
t.pendown()

t.color('black', 'blue')
t.begin_fill()
circle(10)
t.end_fill()

                    # Нос
t.color('black')
t.penup()
t.goto(0, 20)
t.pendown()
t.right(90)
t.width(8)
t.forward(30)

                    # Рот
t.penup()
t.goto(60, 0)
t.pendown()

t.color('red')
t.width(10)
half_of_circle(60)
