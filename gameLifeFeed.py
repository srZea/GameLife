import pygame
import numpy as np
from pygame.locals import *
import sys
import os

size = (400, 400)
pygame.init() 

clock = pygame.time.Clock()

screen = pygame.display.set_mode((size))
bg = (255,255, 255)
screen.fill(bg)

pygame.display.set_caption('Game life of Conway')
cellX,cellY = 30, 30
cellSizeW = 400/ cellX
cellSizeH = 400/ cellY

running = True
while running :

    clock.tick(60)

    screen.blit(screen,(0, 0))

    for x in range(0,cellY):
        for y in range(0, cellX):
            points = [
                (x * cellSizeW, y * cellSizeH),
                ((x+1) * cellSizeW, y * cellSizeH),
                ((x+1) * cellSizeW, (y+1) * cellSizeH),
                ( x *  cellSizeW, (y+1) * cellSizeH)
            ]
            pygame.draw.polygon(screen,(25,25,25),points,1)

    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get() : 
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
    
    pygame.display.update()

pygame.quit()
