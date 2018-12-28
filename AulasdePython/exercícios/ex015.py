dias = int(input('quantos dias você ficou com o carro? '))
km = float(input('quantos quilômetros você andou? '))
s = ((dias*60)+km*0.15)
print('você deve R${}.'.format(s))
