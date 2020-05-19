
import os
import pygame
import sys


def loadImage(file, path, alpha=False):
    fullpath = os.path.join(path, file)
    try:
        image = pygame.image.load(fullpath)
    except:
        print("Error al cargar la imagen: " + fullpath)
        sys.exit(1)

    if alpha:
        image = image.convert_alpha()
    else:
        image = image.convert()
    return image