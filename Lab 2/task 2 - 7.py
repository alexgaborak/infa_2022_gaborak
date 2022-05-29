import turtle
from math import pi, sin, cos

turtle.shape('turtle')
turtle.speed(0)
turtle.left(90)
angle = 360 / 240
for i in range(100000):
    a = i / 120 * pi
    dx = 2 * a * cos(a)
    dy = 2 * a * sin(a)
    turtle.left(angle)
    turtle.goto(dx, dy)