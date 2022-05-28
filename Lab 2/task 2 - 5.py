import turtle

def square(side):
    for i in range(4):
        turtle.forward(side)
        turtle.left(90)

step = 10
for i in range(step, 11 * step, step):
    square(i)
    turtle.right(135)
    turtle.penup()
    turtle.forward(step / (2 ** 0.5))
    turtle.left(135)
    turtle.pendown()