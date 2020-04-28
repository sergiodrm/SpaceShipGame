import pygame
from classNave import Bala, Nave

class Enemigo(Nave):
    def __init__(self, screen, pos, dim, velX):
        Nave.__init__(self, screen, pos, dim)
        self.velX = velX

    def draw(self):
        tr1 = [[self.x, self.y + self.height / 3],
               [self.x + self.width, self.y + self.height / 3],
               [self.x + self.width / 2, self.y + self.height]]
        pygame.draw.polygon(self.screen, (150, 100, 100), tr1, 1)

        mot1 = [[self.x + self.width / 3, self.y],
                [self.x + self.width / 3 + 2, self.y + self.height / 6],
                [self.x + self.width / 3 - 2, self.y + self.height / 6]]
        mot2 = [[self.x + self.width * 2 / 3, self.y],
                [self.x + self.width * 2 / 3 + 2, self.y + self.height / 6],
                [self.x + self.width * 2 / 3 - 2, self.y + self.height / 6]]
        pygame.draw.polygon(self.screen, (150, 100, 10), mot1, 0)
        pygame.draw.polygon(self.screen, (150, 100, 10), mot2, 0)

    def move(self):
        pass
