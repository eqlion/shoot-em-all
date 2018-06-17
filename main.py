#!/usr/bin/env python3

import sys
import pygame

from gun import Gun
from projectile import Projectile
from bubble import Bubble

from time import clock as clc
from math import sin, cos, pi

from pygame.locals import *

pygame.init()

orange = (255, 127, 0)
black = (0, 0, 0)
red = (255, 0, 0)
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((640, 600))
g = Gun(screen)

g.rotate(0)
n = 0
projectiles = []
bubbles = []
now = clc()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    pygame.draw.rect(screen, black, ((0, 0), (640, 600)))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if n > -250:
            n -= 1

    if keys[pygame.K_RIGHT]:
        if n < 250:
            n += 1

    if keys[pygame.K_SPACE] and clc() - now > 0.3:
        projectiles.append(Projectile(screen, n))
        now = clc()

    for bubble in bubbles:
        bubble.move()
        for bullet in projectiles:
            bubble.collision(bullet)
    bubbles = list(filter(lambda x: x.state(), bubbles))

    while len(bubbles) < 10:
        bubbles.append(Bubble(screen))

    for bullet in projectiles:
        bullet.move()
    projectiles = list(filter(lambda x: x.state(), projectiles))

    g.rotate(n)

    pygame.display.update()
    clock.tick(500)
