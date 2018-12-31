vT = 0
cont = 0
for c in range(1, 7):
    v = int(input('digite o valor número {}: '.format(c)))
    if v % 2 == 0:
        vT += v
        cont += 1
print('você falou {} números PARES e a soma foi {}'.format(cont, vT))

