import turtle

turtle.shape('turtle')
n = 18
length = 100
for i in range(n):
     turtle.forward(length)
     turtle.stamp()
     turtle.backward(length)
     turtle.right(360 / n)