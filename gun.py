#!/usr/bin/env python3

import pygame

from math import sin, cos, pi

class Gun(object):
    def __init__(self, screen, color=(255, 127, 0), hof=320, vof=550):
        self.color = color
        self.screen = screen

        # Moving the origin of coordinates to (hof;vof)
        self.hof = hof
        self.vof = vof

        # R = Half of the polygon's diagonal
        self.R = 30

        self.l_u = 0
        self.r_u = 0
        self.l_d = 0
        self.r_d = 0

    def render(self):
        pygame.draw.polygon(self.screen, self.color, [self.l_u, self.r_u, self.r_d, self.l_d])

    def rotate(self, N):
        alpha = pi*N*0.002
        self.l_u = self.R * cos(2*pi/3 + alpha) + self.hof, self.R * sin(2*pi/3 + alpha) + self.vof
        self.r_u = self.R * cos(pi/3 + alpha) + self.hof, self.R * sin(pi/3 + alpha) + self.vof
        self.l_d = self.R * cos(4*pi/3 + alpha) + self.hof, self.R * sin(4*pi/3 + alpha) + self.vof
        self.r_d = self.R * cos(5*pi/3 + alpha) + self.hof, self.R * sin(5*pi/3 + alpha) + self.vof
        self.render()

if __name__ == '__main__':
    pass
