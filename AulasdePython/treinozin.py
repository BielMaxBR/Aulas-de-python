# todos os teste de coisas que eu aprendo ficam aqui
from PIL import ImageGrab
import time

try:
    import pyautogui
except Exception as err:
    print('erro no módulo:{}'.format(err))

x = None
y = None

def Coletor_de_tela():
    tela = ImageGrab.grab()
    return tela


def Detector_de_inimigo(Tela):
    #if x in range(310, 338):
    #    if y in range(463, 340):
    color = Tela.getpixel((338, 463))
    if color == (83, 83, 83):
        return True


def pule():
    pyautogui.press('up')


try:
    print('espere 3 segundos...')
    time.sleep(3)
    while True:
        try:
            screen = Coletor_de_tela()
            if Detector_de_inimigo(screen) is True:
                print('pulou')
                pule()

        except Exception as err:
            print('deu ruim', err)
            break

except KeyboardInterrupt:
    print('Encerrado')
