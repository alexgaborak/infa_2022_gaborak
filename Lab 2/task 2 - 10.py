import turtle as t
import math as m

t.speed(0)

def circle(radius, direction):
    n = 100
    if direction == 'left':
        for i in range(n):
            t.forward(2 * m.pi * radius / n)
            t.left(360 / n)
    if direction == 'right':
        for i in range(n):
            t.forward(2 * m.pi * radius / n)
            t.right(360 / n)


R = 40
t.right(60)

for i in range(3):
    t.left(60)
    for dir in 'left', 'right':
        circle(R, dir)

