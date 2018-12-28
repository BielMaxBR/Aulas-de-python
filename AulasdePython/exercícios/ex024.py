from sys import exit
from time import sleep
while True:
    txt = str(input('qual a sua cidade natal?: ')).strip()
    print('vamos ver se sua cidade tem "santo" no começo')
    sleep(3)
    cidade = bool(txt[:5].upper() == 'SANTO')
    if cidade:
        print('tem Santo no começo do nome.')
    else:
        print('não tem Santo no começo do nome.')
    if txt == 'parar':
        exit()
