import pygame
from pygame.draw import *
from random import randint
from catchme_config import *

pygame.init()
screen = pygame.display.set_mode((800, 800))


def new_ball():
    # Надо бы, по-хорошему, класс для этого сделать
    # сделаю, если останется время
    """
    Рисует "шарики" - круги случайного радиуса r
    (x_0, y_0) - случайные координаты центра кругов
    color - случайный цвет из COLORS
    """
    global x_0, y_0, r
    x_0 = randint(100, 700)
    y_0 = randint(100, 700)
    r = randint(50, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x_0, y_0), r)


def other_ball():  # idk понадобится или нет
    """

    :return:
    """
    pass


def third_figure():  # idk понадобится или нет (мб спец тим мишеней тоже круглыми сделаю)
    """

    :return:
    """
    pass


def check_click():
    """
    Проверяем попадание по шарику (надо доделать)
    :param : pygame event
    :return Bool:
    """
    print(x_0, y_0, r)
    coord = pygame.mouse.get_pos()
    x = coord[0]
    y = coord[1]
    return (x - x_0)**2 + (y - y_0)**2 <= r**2


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


def score():
    """
    Счёт
    :return :
    """
    pass


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
            print('Click!')
            zzz = check_click()
            print(f" ", zzz)
    new_ball()
    new_ball()  # Пока что для этого не срабатывает check_click
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
