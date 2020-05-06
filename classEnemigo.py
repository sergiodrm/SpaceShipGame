import pygame
from classNave import Bala, Nave


class Enemigo(Nave):
    def __init__(self, screen, id, pos, dim, velY):
        Nave.__init__(self, screen, pos, dim)
        self.velY = velY
        self.id = id

    def draw(self):
        self.tr1 = [[self.x + self.width / 2, self.y + self.height],
                    [self.x, self.y + self.height / 3],
                    [self.x + self.width, self.y + self.height / 3]]
        pygame.draw.polygon(self.screen, (10, 120, 100), self.tr1, 0)

        self.mot1 = [[self.x + self.width / 3, self.y],
                     [self.x + self.width / 3 + 2, self.y + self.height / 6],
                     [self.x + self.width / 3 - 2, self.y + self.height / 6]]
        self.mot2 = [[self.x + self.width * 2 / 3, self.y],
                     [self.x + self.width * 2 / 3 + 2, self.y + self.height / 6],
                     [self.x + self.width * 2 / 3 - 2, self.y + self.height / 6]]
        pygame.draw.polygon(self.screen, (150, 100, 10), self.mot1, 0)
        pygame.draw.polygon(self.screen, (150, 100, 10), self.mot2, 0)

        if not self.frame == 0:
            if not self.frame == self.frame_per_bullet:
                self.frame += 1
            else:
                self.frame = 0

    def move(self):
        self.y += self.velY

    def shot(self):
        if self.frame == 0:
            self.balas.append(Bala(self.screen, self.tr1[0], color=(200, 0, 0)))
            self.frame += 1
