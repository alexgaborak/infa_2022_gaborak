import turtle
from math import pi

turtle.speed(0)
turtle.left(90)

def half_of_circle(radius):
    number_of_sides = 100
    for j in range(number_of_sides // 2):
        turtle.forward(2 * pi * radius / number_of_sides)
        turtle.right(360 / number_of_sides)


# coord = 0
# turtle.goto(coord, coord)
radius_1 = 40
radius_2 = 5

for i in range(20):
    if i % 2 == 0:
        half_of_circle(radius_1)
        x = (i + 2) * radius_1 - i * radius_2
        turtle.goto(x, 0)            # Приходится делать так, иначе пружинка "поднимается" под небольшим углом
    else:
        half_of_circle(radius_2)
        x = (i + 1) * (radius_1 - radius_2)
        turtle.goto(x, 0)

# Пружинка поднимается тем меньше, чем точнее рисуется окружность (при возрастании перменной "n").
# Чтобы этого избежать можно было также использовать встроенную в "черепаху" функцию рисования окружности,
# но задание, как я понял, этого не подразумевает.
