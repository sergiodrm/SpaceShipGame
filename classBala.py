import pygame

class Bala:
    def __init__(self, screen, pos, dim, vel=8):
        self.x, self.y = pos[0], pos[1]
        self.width, self.height = dim[0], dim[1]
        self.vel = vel
        self.screen = screen

    def draw(self):
        poly = [[self.x, self.y], [self.x + self.width, self.y],
                [self.x + self.width, self.y + self.height], [self.x, self.y + self.height]]
        pygame.draw.polygon(self.screen, (200, 200, 0), poly, 0)

    def move(self):
        self.y -= self.vel
