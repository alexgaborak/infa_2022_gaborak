import turtle

def circle(radius):
    number_of_sides = 200
    pi = 3.1415926
    for i in range(number_of_sides):
        turtle.forward(2 * pi * radius / number_of_sides)
        turtle.left(180 - 180 * (number_of_sides - 2) / number_of_sides)


radius_value = 100

turtle.speed(0)
turtle.penup()
turtle.forward(radius_value)
turtle.left(90)
turtle.pendown()
circle(radius_value)