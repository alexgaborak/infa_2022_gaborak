import turtle
from math import pi

turtle.speed(0)


def circle(radius):
    number_of_sides = 100
    for i in range(number_of_sides):
        turtle.forward(2 * pi * radius / number_of_sides)
        turtle.right(360 / number_of_sides)


def half_of_circle(radius):
    number_of_sides = 200
    for i in range(number_of_sides // 2):
        turtle.forward(2 * pi * radius / number_of_sides)
        turtle.right(360 / number_of_sides)


# Морда

turtle.penup()
turtle.goto(0, 80)
turtle.pendown()

turtle.color('black', 'yellow')
turtle.begin_fill()
circle(80)
turtle.end_fill()

# Левый глаз

turtle.penup()
turtle.goto(-40, 40)
turtle.pendown()

turtle.color('black', 'blue')
turtle.begin_fill()
circle(10)
turtle.end_fill()

# Правый глаз

turtle.penup()
turtle.goto(40, 40)
turtle.pendown()

turtle.color('black', 'blue')
turtle.begin_fill()
circle(10)
turtle.end_fill()

# Нос

turtle.color('black')
turtle.penup()
turtle.goto(0, 20)
turtle.pendown()
turtle.right(90)
turtle.width(8)
turtle.forward(30)

# Рот

turtle.penup()
turtle.goto(60, 0)
turtle.pendown()

turtle.color('red')
turtle.width(10)
half_of_circle(60)
