import turtle
import math as m

turtle.speed(0)

def circle(radius, direction):
    n = 100
    if direction == 'left':
        for i in range(n):
            turtle.forward(2 * m.pi * radius / n)
            turtle.left(360 / n)
    if direction == 'right':
        for i in range(n):
            turtle.forward(2 * m.pi * radius / n)
            turtle.right(360 / n)


R = 40
turtle.right(60)

for i in range(3):
    turtle.left(60)
    for dir in 'left', 'right':
        circle(R, dir)

