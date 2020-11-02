import turtle as t
from math import pi, sin

# Забыл в прошлых задачах написать, что используется math, а не numpy, т.к. у меня на компьютере
# почему-то не запускается программа двойным кликом (win 10) при использовании numpy

def polygon(radius, number):
    alpha = 360 / number
    beta = 90 * (number + 2) / number
    t.left(beta)
    side = 2 * radius * sin(pi / number)
    for i in range(number):
        t.forward(side)
        t.left(alpha)
    t.right(beta)

r_0 = 25

for i in range(3, 13):
    t.penup()
    t.forward(r_0)
    t.pendown()
    polygon(r_0 * (i - 2), i)