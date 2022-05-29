# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import turtle
from random import *
turtle.speed(0)

for i in range(10000):
    #r = randint(-100, 100)
    x = turtle.xcor()
    y = turtle.ycor()
    turtle.goto(x + randint(-30, 30), y + randint(-30, 30))
    i += 1
