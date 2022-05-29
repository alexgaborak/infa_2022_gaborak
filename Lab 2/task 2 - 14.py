import turtle


def star(number_of_sides):
    for i in range(number_of_sides):
        side_length = 150
        star_angle = 180 * (number_of_sides - 1) / number_of_sides
        turtle.forward(side_length)
        turtle.left(star_angle)


# Первая звезда
turtle.left(180)
star(5)

# Переходим в удобное место
turtle.penup()
turtle.goto(200, 50)
turtle.pendown()

# Нужный поворот и вторая звезда (чтобы биссектриса верхнего луча была вертикальной, как на сайте)
beta = 90 * 6 / 11
turtle.left(beta)
star(11)
