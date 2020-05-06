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
        if nave.x < self.x < nave.x + nave.width and nave.y < self.y < nave.y + self.height:
            if nave.x < self.x <= nave.x + nave.width / 2:
                y = ((nave.tr1[1][1]-nave.tr1[0][1]) / (nave.tr1[1][0]-nave.tr1[0][0])) * \
                    (self.x - nave.tr1[0][0]) + nave.tr1[0][1]
            elif nave.x + nave.width / 2 < self.x < nave.x + nave.width:
                y = ((nave.tr1[2][1] - nave.tr1[0][1]) / (nave.tr1[2][0] - nave.tr1[0][0])) * \
                    (self.x - nave.tr1[0][0]) + nave.tr1[0][1]

            if y > nave.tr1[1][1]:  # Nave enemiga
                if nave.tr1[1][1] < self.y < y or self.y <= nave.tr1[1][1] < self.y - self.vel:
                    return True
                return False
            else:
                if y < self.y < nave.tr1[1][1] or self.y + self.vel > nave.tr1[1][1] or self.y - self.vel < nave.tr1[1][1]:
                    return True
                return False
        return False
