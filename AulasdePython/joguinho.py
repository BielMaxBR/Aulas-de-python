import pygame

"""a musica"""
pygame.mixer.pre_init(48300, -16, 1, 512)
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('big_hero.mp3')
pygame.mixer.music.play()
"""a tela"""
pygame.display.init()
pygame.display.set_mode([600, 480])
"""fim"""
input()
