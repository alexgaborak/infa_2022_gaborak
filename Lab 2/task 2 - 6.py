import turtle as t

t.shape('turtle')
n = 18
length = 100
for i in range(n):
     t.forward(length)
     t.stamp()
     t.backward(length)
     t.right(360 / n)