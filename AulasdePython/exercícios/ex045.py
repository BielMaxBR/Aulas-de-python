from random import randint
from time import sleep
print('===== preda papeu e tisora =====')
item = ('preda', 'papeu', 'tisora')
comp = randint(0, 2)
print('''
Suas opções:
[0] preda
[1] papeu
[2] tisora''')
player = int(input('Qual é a sua jogada? '))
sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!')
print('-=' * 11)
print('o computador jogou {}'.format(item[comp]))
print('você jogou {}'.format(item[player]))
print('-=' * 11)
if comp == 0: #team preda
    if player == 0:
        print('empate')
    elif player == 1:
        print('você ganhou')
    elif player == 2:
        print('o computador ganhou')
    else:
        print('isso N vale espertinho')

elif comp == 1: #teampapeu
    if player == 0:
        print('o computador ganhou')
    elif player == 1:
        print('empate')
    elif player == 2:
        print('você ganhou')
    else:
        print('isso N vale espertinho')

elif comp == 2: #teamtisora
    if player == 0:
        print('você ganhou')
    elif player == 1:
        print('o computador ganhou')
    elif player == 2:
        print('empate')
    else:
        print('isso N vale espertinho')
