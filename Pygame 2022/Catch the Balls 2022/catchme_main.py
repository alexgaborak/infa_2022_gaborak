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
    (x, y) - случайные координаты центра кругов
    color - случайный цвет из COLORS
    """
    global x, y, r
    x = randint(100, 700)
    y = randint(100, 700)
    r = randint(50, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def click(our_event):
    """
    Пока что эта функция выводит нам в консоль координаты и радиус шарика
    :param our_event: pygame event
    :return (x, y), r:
    """
    print(x, y, r)


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
            click(event)
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
