# Старая версия игры на уродском tk
from random import randrange as rnd, choice
from math import pi, cos, sin
import tkinter as tk
import math
import time
import sys

g = 1

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
surface = tk.Canvas(root, bg='white')
surface.focus_set()
surface.pack(fill=tk.BOTH, expand=1)
k = 0.4


class Ball:
    """Класс шарика"""
    def __init__(self, x, y):
        """
        Конструктор класса Ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        vx, vy - проекции скорости
        a - ускорение
        hits - попадание
        """
        self.x = x
        self.y = y
        self.r = 15
        self.vx = 0
        self.vy = 0
        self.a = g
        self.hits = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = surface.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )

    def set_coord(self):
        """
        Целевой квадрат
        :return: canv.coords
        """
        surface.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """
        Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки.
        То есть, обновляет значения self.x и self.y с учетом скоростей
        self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.vy -= self.a
        self.x += self.vx
        self.y -= self.vy
        self.check_walls()
        self.set_coord()

    def check_walls(self):
        """
        Проверяет, не ударилась ли пушка об стену
        """
        if self.x >= 800 - self.r:
            self.vx = -k * self.vx
            self.x -= self.r
            self.hits += 1

        elif self.x <= self.r:
            self.vx = -k * self.vx
            self.x += self.r
            self.hits += 1

        if self.y >= 600 - self.r:
            self.vy = - self.vy
            self.y -= self.r
            self.hits += 1
        elif self.y <= self.r:
            self.vy = -k * self.vy
            self.y += self.r
            self.hits += 1

    def hit_it(self, obj):
        """
        Проверка попадания
        :param obj:
        :return: bool
        """
        if ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** 0.5 \
                <= obj.r + self.r:
            obj.v = 0
            obj.x = -100
            obj.y = -100
            return True
        else:
            return False


class Gun:
    """Класс пушки"""
    def __init__(self):
        """
        Конструктор класса Gun
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.f2_power = 10
        self.f2_on = 0
        self.angle = 1
        self.v_y = 5
        self.x = 50
        self.y = 300
        self.id = surface.create_line(self.x, self.y,
                                      self.x + 30, self.y - 30, width=7)

    def fire2_start(self, event):
        """
        Начало выстрела
        :param event:
        :return: f2_on = 1
        """
        self.f2_on = 1

    def fire2_end(self, event):
        """
        Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча
        vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(
            self.x + max(self.f2_power, 20) * math.cos(self.angle),
            self.y + max(self.f2_power, 20) * math.sin(self.angle)
        )
        if event.x != new_ball.x:
            self.angle = math.atan(
                (event.y - new_ball.y) /
                (event.x - new_ball.x)
            )
        else:
            self.angle = pi / 2
        new_ball.vx = self.f2_power * math.cos(self.angle) / 5
        new_ball.vy = - self.f2_power * math.sin(self.angle) / 5
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def move_up(self, event):
        """
        Двигай вверх
        :param event:
        :return: y-v_y
        """
        self.y -= self.v_y

    def move_down(self, event):
        """
        Двигай вниз
        :param event:
        :return: y+v_y
        """
        self.y += self.v_y

    def targeting(self, event):
        """
        Прицеливание. Зависит от положения мыши.
        """
        if event and event.x != self.x:
            self.angle = math.atan(
                (event.y - self.y) /
                (event.x - self.x)
            )
        elif event and event.x == self.x:
            self.angle = pi / 2
        if self.f2_on:
            surface.itemconfig(self.id, fill='orange')
        else:
            try:
                surface.itemconfig(self.id, fill='black')
            except sys.exit(1):
                sys.exit(1)
        surface.coords(self.id, self.x, self.y,
                       self.x + max(self.f2_power, 20) *
                       math.cos(self.angle),
                       self.y + max(self.f2_power, 20) *
                       math.sin(self.angle)
                       )

    def power_up(self):
        """
        Изменение силы выстрела

        :return:
        """
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            surface.itemconfig(self.id, fill='orange')
        else:
            surface.itemconfig(self.id, fill='black')


class Target:
    """Класс целей"""
    def __init__(self):
        """
        Конструктор класса Target
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.points = 0
        self.live = 1
        self.id = surface.create_oval(0, 0, 0, 0)
        self.id_points = surface.create_text(30, 30, text=self.points, font='28')
        """ Инициализация новой цели. """
        self.x = rnd(600, 780)
        self.y = rnd(300, 550)
        self.r = rnd(2, 50)
        self.angle = rnd(-314, 314) / 100
        self.v = rnd(1, 5)
        self.vx = self.v * cos(self.angle)
        self.vy = self.v * sin(self.angle)
        self.color = 'red'

    def new_target(self):
        """
        Фигачит новую цель
        """
        self.x = rnd(600, 780)
        self.y = rnd(300, 550)
        self.r = rnd(2, 50)
        surface.coords(self.id, self.x - self.r, self.y - self.r,
                       self.x + self.r, self.y + self.r)
        surface.itemconfig(self.id, fill=self.color)

    def hit(self, points=1):
        """
        Попадание шарика в цель.
        """
        surface.coords(self.id, -10, -10, -10, -10)
        self.points += points
        surface.itemconfig(self.id_points, text=self.points)

    def set_coord(self):
        """Лень остальное документировать, там всё и так очев"""
        surface.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def check_walls(self):
        """Допишите и киньте PR, если хотите, потомкам на будущее"""
        if self.x >= 800 - self.r:
            self.vx = - self.vx
        elif self.x <= self.r:
            self.vx = - self.vx

        if self.y >= 600 - self.r:
            self.vy = - self.vy
        elif self.y <= self.r:
            self.vy = - self.vy

    def move(self):
        """Допишите и киньте PR, если хотите, потомкам на будущее"""
        self.x += self.vx
        self.y -= self.vy
        self.check_walls()
        self.set_coord()


target_1 = Target()
target_2 = Target()
screen1 = surface.create_text(400, 300, text='', font='28')
gun_1 = Gun()
bullet = 0
balls = []


def new_game(event=''):
    """О, пошла жара (игра)"""
    global Gun, target_1, screen1, balls, bullet
    target_1.new_target()
    target_2.new_target()
    surface.bind('<Button-1>', gun_1.fire2_start)
    surface.bind('<ButtonRelease-1>', gun_1.fire2_end)
    surface.bind('<Motion>', gun_1.targeting)
    surface.bind('<Up>', gun_1.move_up)
    surface.bind('<Down>', gun_1.move_down)

    target_1.live = 1
    target_2.live = 1
    aim = 0
    while target_1.live == 1 or target_2.live == 1:
        """Допишите и киньте PR, если хотите, потомкам на будущее - тут стоило бы =)"""
        if target_1.live or balls or target_2.live:
            target_2.move()
            target_1.move()
            for ball in balls:
                ball.move()
                if ball.hit_it(target_1) and target_1.live:
                    ball.hits = 20
                    target_1.live = 0
                    aim += 1
                    if aim == 2:
                        surface.itemconfig(
                            screen1, text='Все противники уничтожены! '
                                          '\n  Потрачено: ' + str(bullet) + ' выстрелов'
                        )
                        bullet = 0
                        surface.bind('<Button-1>', '')
                        surface.bind('<ButtonRelease-1>', '')
                        target_1.hit()
                        target_2.hit()

                if ball.hit_it(target_2) and target_2.live:
                    ball.hits = 20
                    target_2.live = 0
                    aim += 1
                    if aim == 2:
                        surface.itemconfig(
                            screen1, text='Все противники уничтожены!'
                                          ' \n  Потрачено: ' + str(bullet) + ' выстрелов'
                        )
                        bullet = 0
                        surface.bind('<Button-1>', '')
                        surface.bind('<ButtonRelease-1>', '')
                        target_1.hit()
                        target_2.hit()

                if ball.hits >= 10:
                    surface.delete(ball.id)
                    balls.remove(ball)

            surface.update()
            time.sleep(0.03)
            gun_1.targeting(event)
            gun_1.power_up()

    time.sleep(3)
    surface.itemconfig(screen1, text='')

    for ball in balls:
        surface.delete(ball.id)
        balls.remove(ball)

    root.after(750, new_game)


try:
    new_game()
except sys.exit(1):
    sys.exit(1)

tk.mainloop()
