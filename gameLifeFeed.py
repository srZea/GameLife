import pygame
import numpy as np
from pygame.locals import *
import sys
#import os

sizeDisplay = (400, 400)
pygame.init()

# display size, clock tracking, draw bg
clock = pygame.time.Clock()
screen = pygame.display.set_mode((sizeDisplay))
bg = (255, 255, 255)
screen.fill(bg)

pygame.display.set_caption('Game life of Conway')
# cells distribution and size
cellX, cellY = 30, 30
cellSizeW = 400 / cellX
cellSizeH = 400 / cellY
# bones cells
state = np.zeros((cellX, cellY))


running = True
while running:
   # tick clocl 60 fps
    clock.tick(60)

    screen.blit(screen, (0, 0))
    # draw grid
    for y in range(0, cellX):
        for x in range(0, cellY):
#esquina superior izquierda (x-1,y-1),arriba(x,y-1),superior derecha(x+1,y-1)
#izquierda (x-1,y),derecha (x+1,y)
#esquina inferior derecha (x-1,y+1), abajo (x,y+1), inferior izquierda(x+1,y+1)

            neatherNeigh = state[(x-1) % cellX, (y-1) % cellY] +\
                           state[(x) % cellX, (y-1) % cellY] +\
                           state[(x+1) % cellX, (y-1) % cellY] +\
                           state[(x-1) % cellX, (y) % cellY] +\
                           state[(x+1) % cellX, (y) % cellY] +\
                           state[(x-1)% cellX,(y+1)%cellY]+\
                           state[(x)%cellX,(y+1)%cellY]+\
                           state[(x+1)%cellX,(y+1)%cellY]

            points = [
                (x * cellSizeW, y * cellSizeH),
                ((x+1) * cellSizeW, y * cellSizeH),
                ((x+1) * cellSizeW, (y+1) * cellSizeH),
                (x * cellSizeW, (y+1) * cellSizeH)
            ]
            pygame.draw.polygon(screen, (25, 25, 25), points, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    pygame.display.update()

pygame.quit()
