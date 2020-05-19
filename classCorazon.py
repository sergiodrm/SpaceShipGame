import pygame
import funciones as fcn


class Corazon(pygame.sprite.Sprite):

    def __init__(self, pos, dim):
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = pos
        self.pos = pos
        self.dim = dim
        self.image = fcn.loadImage("corazon.png", "Imagenes")
        self.image = pygame.transform.scale(self.image, dim)
        self.rect = (pos, dim)
