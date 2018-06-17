import pygame

from random import randrange, random
from math import sin, cos, pi

class Bubble(object):
    def __init__(self, screen):
        self.screen = screen
        self.color = (255,0,0)
        self.x = randrange(40, 560)
        self.y = 40
        self.R = randrange(10, 40)
        alpha = random() * pi
        beta = 10 / self.R
        self.vx = cos(2 * alpha) * beta * .8
        self.vy = sin(alpha) * beta * .8
        self.destroyed = False

    def move(self):
        if self.x > 640 - self.R or self.x < self.R:
            self.vx = -self.vx
        self.y += self.vy
        self.x += self.vx
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.R)


    def collision(self, bullet):
        x1 = self.x
        y1 = self.y

        x2 = bullet.x
        y2 = bullet.y

        R = self.R
        r = bullet.R

        if (R + r)**2 >= (x1 - x2)**2 + (y1 - y2)**2:
            self.destroyed = True
            bullet.destroyed = True

    def state(self):
        return 0 <= self.y <= 600 and not self.destroyed
