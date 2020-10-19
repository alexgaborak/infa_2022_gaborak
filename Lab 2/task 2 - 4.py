import turtle as t

def circ(r):
    N = 200
    pi = 3.1415926
    for i in range(N):
        t.forward(2 * pi * r / N)
        t.left(180 - 180 * (N - 2) / N)


r = 100
t.penup()
t.forward(r)
t.left(90)
t.pendown()
circ(r)