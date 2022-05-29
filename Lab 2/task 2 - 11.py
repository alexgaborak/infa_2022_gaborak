import turtle
from math import pi

turtle.speed(0)

def circle(radius, direction):
    number_of_sides = 50
    if direction == 'left':
        for i in range(number_of_sides):
            turtle.forward(2 * pi * radius / number_of_sides)
            turtle.left(360 / number_of_sides)
    if direction == 'right':
        for i in range(number_of_sides):
            turtle.forward(2 * pi * radius / number_of_sides)
            turtle.right(360 / number_of_sides)


turtle.left(90)

for rad in range(40, 230, 8):
    for dir in 'left', 'right':
        circle(rad, dir)