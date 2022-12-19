import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 2
screen = pygame.display.set_mode((800, 800))

# Цвета
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

x = 0  # чтобы не вылетала ошибка при клике до появления первого шарика
y = 0
r = 0


def new_ball():
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
    :return: (x, y), r
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
