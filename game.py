#!/usr/bin/env python3

import sys
import time
import pygame
import random

from pygame.locals import *
from math import sin, cos, pi

pygame.init()


orange = (255, 127, 0)
black = (0, 0, 0)
red = (255, 0, 0)


def move(N):
    alpha = pi*N*0.001
    R = 30
    hof = 320
    vof = 550
    left_up = R * cos(2*pi/3 + alpha) + hof, R * sin(2*pi/3 + alpha) + vof
    right_up = R * cos(pi/3 + alpha) + hof, R * sin(pi/3 + alpha) + vof
    left_down = R * cos(4*pi/3 + alpha) + hof, R * sin(4*pi/3 + alpha) + vof
    right_down = R * cos(5*pi/3 + alpha) + hof, R * sin(5*pi/3 + alpha) + vof
    return left_up, right_up, left_down, right_down

def move_bullet(N):
    alpha = pi*N*0.001
    H = cos(alpha)*0.8, -sin(alpha)*0.8
    return H


screen = pygame.display.set_mode((640, 600))


n = 0
t1, t2, t3, t4 = move(n)

list_of_bullets = []
list_of_bobbles = []
delta = 0
start = 0
pygame.draw.polygon(screen, (orange), [t1, t2, t4, t3])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # ПОВОРАЧИВАЕМ ПУШЕЧКУ
    keys = pygame.key.get_pressed()
    backend = pygame.draw.rect(screen, black, ((0, 0), (640, 600)))
    if keys[pygame.K_LEFT]:
        # if n > -1000:
        n -= 1
    if keys[pygame.K_RIGHT]:
        # if n < 0:
        n += 1
    t1, t2, t3, t4 = move(n)

    # СОЗДАЕМ ПУЛЬКИ
    if keys[pygame.K_SPACE]:
        tau = time.clock()
        if tau - delta >= 0.3:
            b1, b2 = move_bullet(n)
            list_of_bullets.append([320, 550, b1, b2])
            delta = tau
    now = time.clock()

    # СОЗДАЕМ ПУЗЫКИКИ
    if now - start >= 1:
        start = now
        r = int(random.randrange(15, 40))
        x = random.randrange(r, 600-r)
        speed = random.randrange(1, 10)
        Yspeed = random.randrange(1, 10)
        list_of_bobbles.append([x, 40, speed/100, Yspeed/100, r])

    # ПЕРЕРИСОВЫВАЕМ ПУЛЬКИ )))
    if len(list_of_bullets) >= 20:
        list_of_bullets = list_of_bullets[-20:]
    for i in range(len(list_of_bullets)):
        el = list_of_bullets[i]
        if el != [0]:
            pygame.draw.circle(screen, orange, (int(el[0]+el[2]), int(el[1]+el[3])), 5)
            list_of_bullets[i][0], list_of_bullets[i][1] = el[0]+el[2], el[1]+el[3]


    # ПЕРЕРИСОВЫВАЕМ ПУЗЫРИКИ)))
    if len(list_of_bobbles) >= 20:
        list_of_bobbles = list_of_bobbles[-20:]
    for i in range(len(list_of_bobbles)):
        el = list_of_bobbles[i]
        if el != [0]:
            if el[0]+el[2] > 640-el[4] or el[0]+el[2] < el[4]:
                list_of_bobbles[i][2] = -list_of_bobbles[i][2]
            pygame.draw.circle(screen, red, (int(el[0]+el[2]), int(el[1]+el[3])), el[4])
            list_of_bobbles[i][0], list_of_bobbles[i][1] = el[0]+el[2], el[1]+el[3]
            # print(list_of_bobbles[0], (int(el[0]+el[2]), int(el[1]+el[3])))

    # ДЕЛАЕМ КОЛЛИЗИИ )))
    for i in range(len(list_of_bobbles)):
        for j in range(len(list_of_bullets)):
            bobble = list_of_bobbles[i]
            bullet = list_of_bullets[j]
            if bullet != [0] and bobble != [0]:
                xis = abs(bobble[0]-bullet[0])
                yis = abs(bobble[1]-bullet[1])
                if xis**2 + yis**2 < (5+bobble[4])**2:
                    list_of_bullets[j], list_of_bobbles[i] = [0], [0]

    pygame.draw.polygon(screen, orange, [t1, t2, t4, t3])

    pygame.display.update()
