from math import hypot
oposto = float(input('qual o tamanho do cateto oposto?: '))
adjacente = float(input('qual o tamanho do cateto adjacente?: '))
hipo = hypot(oposto, adjacente)
print('a hipotenuza é {:.3f}.'.format(hipo))
