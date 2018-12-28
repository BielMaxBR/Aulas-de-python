loop = False
while not loop:
    nota_1 = float(input('primeira nota: '))
    nota_2 = float(input('segunda nota: '))
    media = (nota_1 + nota_2) / 2
    print('sua media foi de {}'.format(media))
    if nota_2 < 10.0 and nota_1 < 10.0:
        if media >= 7.0:
            print('você passou!')
        elif 6.9 >= media >= 5.0:
            print('você ficou em recuperação')
        elif media <= 4.9:
            print('você reprovou.')
        loop = True
    elif (nota_2 > 10.0 or nota_1 > 10.0) or (nota_2 > 10.0 and nota_1 > 10.0):
        print('\033[1;31mquer ter uma nota maior do que pode Hein.\033[m')

