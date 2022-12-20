import pygame
from pygame.draw import *
from random import randint
from catchme_config import *

pygame.init()
screen = pygame.display.set_mode((800, 800))

# Шрифт
FONT = pygame.font.SysFont('couriernew', 30, bold=True)

score = 0

def new_ball():
    # Надо бы, по-хорошему, класс для этого сделать
    # сделаю, если останется время
    """
    Рисует "шарики" - круги случайного радиуса r_0
    (x_0, y_0) - случайные координаты центра кругов
    color - случайный цвет из COLORS
    """
    global x_0, y_0, r_0
    x_0 = randint(100, 700)
    y_0 = randint(100, 700)
    r_0 = randint(50, 100)
    color_0 = COLORS[randint(0, 5)]
    circle(screen, color_0, (x_0, y_0), r_0)


def other_ball():  # idk понадобится или нет
    """
    Рисует "шарики" - круги случайного радиуса r_1
    (x_1, y_1) - случайные координаты центра кругов
    color - случайный цвет из COLORS
    """
    global x_1, y_1, r_1
    x_1 = randint(100, 700)
    y_1 = randint(100, 700)
    r_1 = randint(50, 100)
    color_1 = COLORS[randint(0, 5)]
    circle(screen, color_1, (x_1, y_1), r_1)


def third_figure():  # пока третий шарик
    """
    Рисует "шарики" - круги случайного радиуса r_1
    (x_1, y_1) - случайные координаты центра кругов
    color - случайный цвет из COLORS
    """
    global x_2, y_2, r_2
    x_2 = randint(100, 700)
    y_2 = randint(100, 700)
    r_2 = randint(50, 100)
    color_2 = COLORS[randint(0, 5)]
    circle(screen, color_2, (x_2, y_2), r_2)


def check_click():
    """
    Проверяем попадание по шарику (надо доделать)
    :param : pygame event
    :return Bool:
    """

    coord = pygame.mouse.get_pos()
    x = coord[0]
    y = coord[1]
    hit0 = (x - x_0) ** 2 + (y - y_0) ** 2 <= r_0 ** 2
    hit1 = (x - x_1) ** 2 + (y - y_1) ** 2 <= r_1 ** 2
    #hit2 = (x - x_2) ** 2 + (y - y_2) ** 2 <= r_2 ** 2

    return hit0 or hit1 #or hit2


def move():
    """
    Движение
    :return:
    """
    pass


def reflection():
    """
    Отражение от стен.
    :return :
    """
    pass


def current_score():
    """
    Выводит на экран текущий счёт
    """
    global score
    score += check_click()
    score_text = FONT.render('Your score:' + str(score), True, (0, 255, 0))
    screen.blit(score_text, (10, 50))

def best_players():
    """
    Лучшие игроки (не уверен, что успею доделать)
    :return:
    """
    pass


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    """
    mainloop
    """
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_click()
            print(f'', check_click())
    current_score()

    new_ball()
    other_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
