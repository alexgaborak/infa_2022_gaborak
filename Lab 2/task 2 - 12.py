import turtle as t
from math import pi

t.speed(0)
t.left(90)

def half_of_circle(radius):
    n = 100
    for i in range(n // 2):
        t.forward(2 * pi * radius / n)
        t.right(360 / n)

# coord = 0
# t.goto(coord, coord)

r_1 = 40
r_2 = 5
for i in range(20):
    if i % 2 == 0:
        half_of_circle(r_1)
        x = (i + 2) * r_1 - i * r_2
        t.goto(x, 0)            # Приходится делать так, иначе пружинка "поднимается" под небольшим углом
    else:
        half_of_circle(r_2)
        x = (i + 1) * (r_1 - r_2)
        t.goto(x, 0)

# Пружинка поднимается тем меньше, чем точнее рисуется окружность (при возрастании перменной "n").
# Чтобы этого избежать можно было также использовать встроенную в "черепаху" функцию рисования окружности,
# но задание, как я понял, этого не подразумевает.