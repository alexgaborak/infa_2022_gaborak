import turtle
from math import pi, sin

# Забыл в прошлых задачах написать, что используется math, а не numpy, т.к. у меня на компьютере
# почему-то не запускается программа двойным кликом (win 10) при использовании numpy

turtle.speed(0)

def polygon(radius, number_of_sides):
    alpha = 360 / number_of_sides
    beta = 90 * (number_of_sides + 2) / number_of_sides
    turtle.left(beta)
    side = 2 * radius * sin(pi / number_of_sides)
    for i in range(number_of_sides):
        turtle.forward(side)
        turtle.left(alpha)
    turtle.right(beta)

r_0 = 25

for i in range(3, 13):
    turtle.penup()
    turtle.forward(r_0)
    turtle.pendown()
    polygon(r_0 * (i - 2), i)