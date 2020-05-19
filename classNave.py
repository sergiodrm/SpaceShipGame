import pygame
from classBala import Bala
from classCorazon import Corazon


class Nave:
    def __init__(self, screen, pos, dim, vel=(3, 3), framesPerBullet=5):
        # Inicializacion de posicion y velocidad de la nave
        self.x, self.y = pos
        self.velX, self.velY = vel
        self.vidas = 3
        self.spriteCorazones = [
            Corazon((0, pygame.display.get_surface().get_height() - 10), (10, 10)),
            Corazon((15, pygame.display.get_surface().get_height() - 10), (10, 10)),
            Corazon((30, pygame.display.get_surface().get_height() - 10), (10, 10))
        ]

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

    def colision(self, pos, vel=0):
        # Se especifica si la posicion dada esta o no dentro del triangulo principal de la nave
        if self.y < pos[1] < self.tr1[1][1]:

            if self.x < pos[0] <= self.x + self.width / 2:
                # Eq recta
                y = ((self.tr1[1][1] - self.tr1[0][1]) / (self.tr1[1][0] - self.tr1[0][0])) * \
                    (pos[0] - self.tr1[0][0]) + self.tr1[0][1]
            elif self.x + self.width / 2 < pos[0] < self.x + self.width:
                y = ((self.tr1[2][1] - self.tr1[0][1]) / (self.tr1[2][0] - self.tr1[0][0])) * \
                    (pos[0] - self.tr1[0][0]) + self.tr1[0][1]

            else:
                return False

            if y > self.tr1[1][1]:  # Nave enemiga

                if self.tr1[1][1] < pos[1] < y or pos[1] > y > pos[1] + vel:
                    return True
                return False
            else:

                if y < pos[1] < self.tr1[1][1] or pos[1] < y < pos[1] + vel:
                    return True
                return False
        else:
            return False

    def __str__(self):
        cadena = "Posicion: [" + str(self.x) + ", " + str(self.y) + "]"
        return cadena
