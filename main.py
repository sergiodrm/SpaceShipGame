import pygame
import numpy as np
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

# Variables de texto y raton
fuente = pygame.font.Font(None, 20)
mouseX, mouseY = 0, 0


# Inicializacion de nave del jugador
velJX, velJY = 5, 5
widthJ, heightJ = 30, 50
framesPerBullet = 10
nave = Nave(
    screen,
    (width / 2 - 25, height - 75),
    (widthJ, heightJ), (velJX, velJY),
    framesPerBullet
)

# Inicializacion de naves enemigas
enemigos = []
id, enemyWidth, enemyHeight, velEnemyMax = 1, 25, 25, 1
frames_per_enemy, counterEnemy = 200, 0
running, paused = True, False
while running:
    time.sleep(0.03333)

    screen.fill(bg)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Movimientos del jugador

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

    # Generar enemigos
    if counterEnemy == 0:
        generarEnemigo = np.random.rand()
        if generarEnemigo > 0.75:
            vel = np.floor((np.random.rand() * velEnemyMax)) + 1
            enemigos.append(
                Enemigo(screen, id, (np.floor(np.random.rand() * width), 0), (enemyWidth, enemyHeight), vel)
            )
            id += 1
            counterEnemy += 1
    else:
        if counterEnemy == frames_per_enemy:
            counterEnemy = 0
        else:
            counterEnemy += 1

    # Mover enemigos
    for i in reversed(range(0, len(enemigos))):
        remove = False
        enemigos[i].draw()
        # Comprobar colisiones con nave del jugador

        #if nave.colision(enemigos[i].tr1[0]) or nave.colision(enemigos[i].tr1[1]) or nave.colision(enemigos[i].tr1[2]):
        #    print("Colision con nave! id: " + str(enemigos[i].id))
        # Comprobar colisiones con las balas

        # Colisiones de las balas del jugador con los enemigos
        if nave.colision(enemigos[i].balas):
            nave.vidas -= 1
            if nave.vidas == 0:
                print("Game Over!")
                running = False

        if enemigos[i].colision(nave.balas):
            enemigos.pop(i)
        else:
            enemigos[i].move()
            if np.random.rand() < enemigos[i].shotProb:
                enemigos[i].shot()

    nave.draw()

    pygame.display.flip()

print("Saliendo...")
pygame.quit()
