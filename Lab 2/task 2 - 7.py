import turtle as t
from math import pi, sin, cos

t.shape('turtle')
t.left(90)
angle = 360 / 240
for i in range(100000):
    a = i / 120 * pi
    dx = 2 * a * cos(a)
    dy = 2 * a * sin(a)
    t.left(angle)
    t.goto(dx, dy)