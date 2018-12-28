vel = float(input('qual a velocidade do seu carro?: ').strip())
multa = (vel - 80) * 7.00
if vel > 80:
    print('PARABÉNS!! você foi MULTADO. passou dos 80Km')
    print('a multa será de R${:.2f}'.format(float(multa)))
else:
    print('ok.')
