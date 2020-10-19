import turtle as t

def square(side):
    for i in range(4):
        t.forward(side)
        t.left(90)

step = 10
for i in range(step, 11 * step, step):
    square(i)
    t.right(135)
    t.penup()
    t.forward(step / (2 ** 0.5))
    t.left(135)
    t.pendown()