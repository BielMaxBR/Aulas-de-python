# coloque o destino da música entre os parênteses
def tocar(diretorio):
    musica = r'{}'.format(str(diretorio))
    import pygame
    pygame.mixer.pre_init(48300, -16, 1, 51200)
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play()



# caso a música esteja rápida use esse


def ntocar(diretorio):
    musica = r'{}'.format(str(diretorio))
    import pygame
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play()



'''agora, com input para fim de comando'''


def rtocar(diretorio):
    musica = r'{}'.format(str(diretorio))
    import pygame
    pygame.mixer.pre_init(48300, -16, 1, 51200)
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play()
    input()


def rntocar(diretorio):
    musica = r'{}'.format(str(diretorio))
    import pygame
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play()
    input()



