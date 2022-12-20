import pygame
from pygame.draw import *
from random import randint
from catchme_config import *

pygame.init()
screen = pygame.display.set_mode((800, 800))

# Шрифт
FONT = pygame.font.SysFont('couriernew', 30, bold=True)

score = 0


def new_ball_0():
    # Надо бы, по-хорошему, класс для этого сделать
    # сделаю, если останется время
    """
    Рисует "шарики" - круги случайного радиуса r_0
    (x_0, y_0) - случайные координаты центра кругов
    (vx0, vy0) - проекции скоростей
    color_0 - случайный цвет из COLORS
    """
    global x_0, y_0, r_0, vx0, vy0, color_0
    x_0 = randint(MIN_X_OF_CENTRE, MAX_X_OF_CENTRE)
    y_0 = randint(MIN_Y_OF_CENTRE, MAX_Y_OF_CENTRE)
    r_0 = randint(MIN_RADIUS, MAX_RADIUS)
    vx0 = random_speed()
    vy0 = random_speed()
    color_0 = COLORS[randint(0, 5)]


def move_target_0():
    """
    Движение и перерисовка первого шарика.
    :return none:
    """
    global x_0, y_0
    x_0 += vx0
    y_0 += vy0
    circle(screen, color_0, (x_0, y_0), r_0)


def new_ball_1():  # idk понадобится или нет
    """
    Рисует "шарики" - круги случайного радиуса r_1
    (x_1, y_1) - случайные координаты центра кругов
    (vx1, vy1) - проекции скоростей
    color_1 - случайный цвет из COLORS
    """
    global x_1, y_1, r_1, vx1, vy1, color_1
    x_1 = randint(MIN_X_OF_CENTRE, MAX_X_OF_CENTRE)
    y_1 = randint(MIN_Y_OF_CENTRE, MAX_Y_OF_CENTRE)
    r_1 = randint(MIN_RADIUS, MAX_RADIUS)
    vx1 = random_speed()
    vy1 = random_speed()
    color_1 = COLORS[randint(0, 5)]


def move_target_1():
    """
    Движение и перерисовка 2-го шарика.
    :return:
    """
    global x_1, y_1
    x_1 += vx1
    y_1 += vy1
    circle(screen, color_1, (x_1, y_1), r_1)


def new_special_figure():  # пока третий шарик
    """
    Рисует "шарики" - круги случайного радиуса r_1
    (x_2, y_2) - случайные координаты центра кругов
    (vx2, vy2) - проекции скоростей
    color_2 - случайный цвет из COLORS
    """
    global x_2, y_2, r_2, vx2, vy2, color_2
    x_2 = randint(MIN_X_OF_CENTRE, MAX_X_OF_CENTRE)
    y_2 = randint(MIN_Y_OF_CENTRE, MAX_Y_OF_CENTRE)
    r_2 = randint(MIN_RADIUS/10, MAX_RADIUS/4)
    vx2 = random_speed()
    vy2 = random_speed()
    color_2 = COLORS[randint(0, 5)]


def move_special_target():
    """
    Движение и перерисовка 3-го шарика.
    :return:
    """
    global x_2, y_2
    x_2 += vx2
    y_2 += vy2
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
    hit2 = (x - x_2) ** 2 + (y - y_2) ** 2 <= r_2 ** 2

    return hit0 or hit1 or hit2


def random_speed():
    """
    Генерит рандомную проекцию скорости
    """
    return randint(-MAX_SPEED, MAX_SPEED)


def reflection(v):
    """
    Случайное отражение от стен. (меняет проекцию скорости на рандомную другого знака)
    :return :
    """
    if v > 0:
        return randint(-MAX_SPEED, 0)
    elif v < 0:
        return randint(0, MAX_SPEED)


def current_score():
    """
    Выводит на экран текущий счёт
    """
    global score
    score += check_click()


def best_players():
    """
    Все сыгравшие игроки записываются в файл (не уверен, что успею доделать)
    :return:
    """
    print("Your name:")
    player_name = input()
    file = open("players.txt", "a")
    file.write(player_name + " - " + str(score) + "\n")
    file.close()


def initial_set():
    new_ball_0()
    new_ball_1()
    new_special_figure()


initial_set()
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
            current_score()
            print(f'', check_click())
            if check_click():
                initial_set()

    move_target_0()
    move_target_1()
    move_special_target()
    score_text = FONT.render('Your score:' + str(score), True, (0, 255, 0))
    screen.blit(score_text, (10, 50))
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()

# best_players()
