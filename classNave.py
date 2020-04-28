import pygame
from classBala import Bala


class Nave:
    def __init__(self, screen, pos, dim):
        # Inicializacion de posicion y velocidad de la nave
        self.x, self.y = pos[0], pos[1]
        self.velX, self.velY = 5, 5
        # Dimensiones de la nave
        self.width, self.height = dim[0], dim[1]
        # Objeto ventana para dibujar
        self.screen = screen
        # Crear array de balas
        self.balas = []
        # Frame entre disparos
        self.frame_per_bullet = 5
        self.frame = 0

    def draw(self):
        # Motores
        mot1 = [[self.x + self.width / 3 - 2, self.y + self.height * 5 / 6],
                [self.x + self.width / 3, self.y + self.height],
                [self.x + self.width / 3 + 2, self.y + self.height * 5 / 6]]
        mot2 = [[self.x + self.width * 2 / 3 - 2, self.y + self.height * 5 / 6],
                [self.x + self.width * 2 / 3, self.y + self.height],
                [self.x + self.width * 2 / 3 + 2, self.y + self.height * 5 / 6]]
        pygame.draw.polygon(self.screen, (150, 100, 15), mot1, 0)
        pygame.draw.polygon(self.screen, (150, 100, 15), mot2, 0)

        # Canyones
        x, y = 7, 5
        ca1 = [[self.x + self.width / 2 - x, self.y],
               [self.x + self.width / 2 - x, self.y + self.height / 4 + y]]
        ca2 = [[self.x + self.width / 2 + x, self.y],
               [self.x + self.width / 2 + x, self.y + self.height / 4 + y]]
        pygame.draw.polygon(self.screen, (150, 20, 100), ca1, 2)
        pygame.draw.polygon(self.screen, (150, 20, 100), ca2, 2)

        # Triangulo 1:
        tr1 = [[self.x + self.width / 2, self.y],
               [self.x, self.y + self.height * 5 / 6],
               [self.x + self.width, self.y + self.height * 5 / 6]]
        pygame.draw.polygon(self.screen, (128, 128, 125), tr1, 2)

        # Triangulo 2:
        tr2 = [[self.x + self.width / 3, self.y + self.height / 2],
               [self.x + self.width * 2 / 3, self.y + self.height / 2],
               [self.x + self.width / 2, self.y + self.height * 5 / 6]]
        #pygame.draw.polygon(self.screen, (15, 75, 15), tr2, 0)

        for b in reversed(range(0, len(self.balas))):
            if self.balas[b].y + self.balas[b].height < 0:
                self.balas.pop(b)
            else:
                self.balas[b].draw()
                self.balas[b].move()

        # Como la nave se dibuja en cada frame, se hace la cuenta de los disparos cada x frame en este metodo
        if not self.frame == 0:
            if self.frame == self.frame_per_bullet:
                self.frame = 0
            else:
                self.frame += 1

    def move(self, dir):
        if dir == pygame.K_UP:
            self.y -= self.velY
        elif dir == pygame.K_RIGHT:
            self.x += self.velX
        elif dir == pygame.K_LEFT:
            self.x -= self.velX
        elif dir == pygame.K_DOWN:
            self.y += self.velY

    def shot(self):
        if self.frame == 0:
            self.balas.append(Bala(self.screen, (self.x + self.width / 2 + 7, self.y), (1, 5)))
            self.balas.append(Bala(self.screen, (self.x + self.width / 2 - 7, self.y), (1, 5)))
            self.frame += 1

    def __str__(self):
        cadena = "Posicion: [" + str(self.x) + ", " + str(self.y) + "]"
        return cadena