import pygame
import numpy as np
from classBala import Bala
from classCorazon import Corazon


pos2str = lambda x, y: "X: " + str(x) + " Y: " + str(y)


class Nave:
    def __init__(self, screen, pos, dim, vel=(3, 3), framesPerBullet=5, id=0):
        # Inicializacion de posicion y velocidad de la nave
        self.x, self.y = pos
        self.velX, self.velY = vel
        self.vidas = 3
        self.spriteCorazones = [
            Corazon((0, pygame.display.get_surface().get_height() - 20), (20, 20)),
            Corazon((20, pygame.display.get_surface().get_height() - 20), (20, 20)),
            Corazon((40, pygame.display.get_surface().get_height() - 20), (20, 20))
        ]
        self.id = id
        # Dimensiones de la nave
        self.width, self.height = dim
        # Objeto ventana para dibujar
        self.screen = screen
        # Crear array de balas
        self.balas = []
        # Frame entre disparos
        self.frame_per_bullet = framesPerBullet
        self.frame = 0

        # Inicializar variables de forma
        self.mot1, self.mot2 = [], []
        self.ca1, self.ca2 = [], []
        self.tr1 = []

    def draw(self):
        # Definir forma del dibujo de la nave
        self.mot1 = [[self.x + self.width / 3 - 2, self.y + self.height * 5 / 6],
                     [self.x + self.width / 3, self.y + self.height],
                     [self.x + self.width / 3 + 2, self.y + self.height * 5 / 6]]
        self.mot2 = [[self.x + self.width * 2 / 3 - 2, self.y + self.height * 5 / 6],
                     [self.x + self.width * 2 / 3, self.y + self.height],
                     [self.x + self.width * 2 / 3 + 2, self.y + self.height * 5 / 6]]

        # Cannones
        x, y = 7, 5
        self.ca1 = [[self.x + self.width / 2 - x, self.y],
                    [self.x + self.width / 2 - x, self.y + self.height / 4 + y]]
        self.ca2 = [[self.x + self.width / 2 + x, self.y],
                    [self.x + self.width / 2 + x, self.y + self.height / 4 + y]]
        # Triangulo 1:
        self.tr1 = [[self.x + self.width / 2, self.y],
                    [self.x, self.y + self.height * 5 / 6],
                    [self.x + self.width, self.y + self.height * 5 / 6]]

        pygame.draw.polygon(self.screen, (150, 100, 15), self.mot1, 0)
        pygame.draw.polygon(self.screen, (150, 100, 15), self.mot2, 0)
        pygame.draw.polygon(self.screen, (150, 20, 100), self.ca1, 2)
        pygame.draw.polygon(self.screen, (150, 20, 100), self.ca2, 2)
        pygame.draw.polygon(self.screen, (128, 128, 125), self.tr1, 0)

        for i in range(len(self.spriteCorazones)):
            self.screen.blit(self.spriteCorazones[i].image, self.spriteCorazones[i].rect)
        fuente = pygame.font.Font(None, 15)
        self.screen.blit(
            fuente.render(
                pos2str(self.tr1[0][0], self.tr1[0][1]), 1, (255, 255, 255)
            ),
            (15, 5)
        )

        # Como la nave se dibuja en cada frame, se hace la cuenta de los disparos cada x frame en este metodo
        if not self.frame == 0:
            if self.frame == self.frame_per_bullet:
                self.frame = 0
            else:
                self.frame += 1

        self.moveBullets()

    def move(self, dir):
        if dir == pygame.K_UP and self.y >= 0:
            self.y -= self.velY
        elif dir == pygame.K_RIGHT and self.x + self.width <= pygame.display.get_surface().get_width():
            self.x += self.velX
        elif dir == pygame.K_LEFT and self.x >= 0:
            self.x -= self.velX
        elif dir == pygame.K_DOWN and self.y + self.height <= pygame.display.get_surface().get_height():
            self.y += self.velY

    def shot(self):
        if self.frame == 0:
            self.balas.append(Bala(self.screen, (self.ca1[0][0], self.y), (1, 5), vel=-8))
            self.balas.append(Bala(self.screen, (self.ca2[0][0], self.y), (1, 5), vel=-8))
            self.frame += 1

    def moveBullets(self):
        for b in reversed(range(0, len(self.balas))):
            if self.balas[b].y + self.balas[b].height < 0:
                self.balas.pop(b)
            else:
                self.balas[b].draw()
                self.balas[b].move()

    def colision(self, balas):
        for i in reversed(range(len(balas))):
            if self.x < balas[i].x < self.x + self.width:
                if self.y < balas[i].y < self.y + self.height:
                    m = (self.tr1[1][1] - self.tr1[0][1]) / (self.tr1[1][0] - self.tr1[0][0])
                    y = m * (balas[i].x - self.tr1[0][0]) + self.tr1[0][1]
                    if np.sign(m) * (balas[i].y - y) <= 0:
                        balas.pop(i)
                        return True
        return False

    def __str__(self):
        cadena = "Posicion: [" + str(self.x) + ", " + str(self.y) + "]"
        return cadena
