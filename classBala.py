import pygame

class Bala:
    def __init__(self, screen, pos, dim=(1, 5), vel=8, color=(200, 200, 0)):
        self.x, self.y = pos
        self.width, self.height = dim
        self.vel = vel
        self.screen = screen
        self.color = color

    def draw(self):
        poly = [[self.x, self.y], [self.x + self.width, self.y],
                [self.x + self.width, self.y + self.height], [self.x, self.y + self.height]]
        pygame.draw.polygon(self.screen, self.color, poly, 0)

    def move(self):
        self.y += self.vel

    def colision(self, nave):
        if nave.x < self.x < nave.x + nave.width:
            if nave.y < self.y < nave.y + nave.height:
                y = ((nave.tr1[1][1]-nave.tr1[0][1]) / (nave.tr1[1][0]-nave.tr1[0][0])) * \
                    (self.x - nave.tr1[0][0]) + nave.tr1[0][1]
                if not nave.id == 0:
                    if self.y - y <= 0:
                        return True
                else:
                    if y - self.y <= 0:
                        return True
        return False
