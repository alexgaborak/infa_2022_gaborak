import turtle as t



def star(number):
    for i in range(number):
        side = 150
        alpha = 180 * (number - 1) / number
        t.forward(side)
        t.left(alpha)


# Первая звезда
t.left(180)
star(5)

# Переходим в удобное место
t.penup()
t.goto(200, 50)
t.pendown()

# Нужный поворот и вторая звезда (чтобы биссектриса верхнего луча была вертикальной, как на сайте)
beta = 90 * 6 / 11
t.left(beta)
star(11)