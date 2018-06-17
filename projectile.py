#!/usr/bin/env python3

import pygame

from math import sin, cos, pi

class Projectile(object):
    def __init__(self, screen, N, color=(255, 127, 0), R=30):
        alpha = pi*N*0.002
        hof = 320
        vof = 550
        self.R = 4
        self.color = color
        self.screen = screen
        self.vx = cos(3*pi/2 + alpha)
        self.vy = sin(3*pi/2 + alpha)
        self.x = R * self.vx + hof
        self.y = R * self.vy + vof
        self.destroyed = False

    def move(self):
        self.x += self.vx
        self.y += self.vy
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.R)

    def state(self):
        return 0 <= self.x <= 640 and 0 <= self.y <= 600 and not self.destroyed
