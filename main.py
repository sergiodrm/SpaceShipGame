import pygame
from classNave import Nave
from classEnemigo import Enemigo
import time


# Inicializar pantalla
pygame.init()

# Configurar pantalla
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
bg = 25, 25, 25
screen.fill(bg)

# Inicializacion de nave del jugador
nave = Nave(screen, (width/2-25, height-75), (30, 50))

# Inicializacion de naves enemigas
enemigo = Enemigo(screen, (50, 50), (25, 25))

running = True
while running:
    time.sleep(0.1)
    screen.fill(bg)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        nave.move(pygame.K_UP)
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        nave.move(pygame.K_LEFT)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        nave.move(pygame.K_RIGHT)
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        nave.move(pygame.K_DOWN)
    if keys[pygame.K_ESCAPE]:
        running = False
    mouseClick = pygame.mouse.get_pressed()
    if mouseClick[0] == 1 or keys[pygame.K_SPACE]:
        nave.shot()
    nave.draw()
    enemigo.draw()
    pygame.display.flip()

print("Saliendo...")
pygame.quit()
