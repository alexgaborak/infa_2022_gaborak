import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((255, 255, 255))
#rect(screen, (255, 0, 255), (100, 100, 200, 200))
#rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
#polygon(screen, (255, 255, 0), [(100,100), (200,50),
                               #(300,100), (100,100)])
#polygon(screen, (0, 0, 255), [(100,100), (200,50),
                             #  (300,100), (100,100)], 5)
circle(screen, (0, 255, 0), (200, 200), 100)

circle(screen, (255, 0, 0), (160, 180), 15)
circle(screen, (255, 0, 0), (240, 180), 15)

circle(screen, (0, 0, 0), (160, 180), 8)
circle(screen, (0, 0, 0), (240, 180), 5)
#circle(screen, (255, 255, 255), (200, 175), 50, 5)
line(screen, (0, 0, 0), (150, 250), (250, 250), 15)

line(screen, (0, 0, 0), (100, 100), (180, 180), 15)
line(screen, (0, 0, 0), (300, 110), (220, 170), 15)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
