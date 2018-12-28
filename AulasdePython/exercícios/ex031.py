viagem = float(input('quantos quilômetros você voará?: '))
if viagem > 200:
    print("""você pagará R${:.2f} pela viagem.
por causa do desconto por viagens mais longas que 200Km""".format(float(viagem*0.45)))
else:
    print('você pagará R${:.2f} pela viagem'.format(float(viagem * 0.50)))
