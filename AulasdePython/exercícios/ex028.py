from random import randint
comp = randint(0, 5)
print('-_' * 23)
print('adivinhe um número que eu pensei entre 0 e 5')
print('-_' * 23)
player = int(input('em que número eu pensei?: '))
if player == comp:
    print('parabéns era {} mesmo!'.format(comp))
else:
    print('HAHA! você errou! era {}'.format(comp))
