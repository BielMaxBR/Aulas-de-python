import pygame
pygame.mixer.pre_init(48300, -16, 1, 51200)
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('big_hero.mp3')
pygame.mixer.music.play()
input()
