import pygame
from pygame.locals import *
tela = pygame.display.set_mode((200, 100))
continua = True
clock = pygame.time.Clock()
pygame.init()
while continua:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            continua = False
    tela.fill((255, 255, 255))
    pygame.display.flip()
