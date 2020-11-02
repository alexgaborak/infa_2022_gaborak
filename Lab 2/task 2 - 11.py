import turtle as t
from math import pi

t.speed(0)


def circle(radius, direction):
    n = 50
    if direction == 'left':
        for i in range(n):
            t.forward(2 * pi * radius / n)
            t.left(360 / n)
    if direction == 'right':
        for i in range(n):
            t.forward(2 * pi * radius / n)
            t.right(360 / n)


t.left(90)

for rad in range(40, 230, 8):
    for dir in 'left', 'right':
        circle(rad, dir)