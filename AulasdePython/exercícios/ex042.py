v1 = float(input('primeiro segmento: '))
v2 = float(input('segundo segmento: '))
v3 = float(input('terceiro segmento: '))

if v1 + v2 > v3 and v3 + v1 > v2 and v3 + v2 > v1:
    print('dá pra fazer um triângulo :)')
    if v1 == v2 == v3:
        print('seu triângulo é Equilátero')
    elif v1 == v2 or v1 == v3 or v2 == v3:
        print('seu triângulo é Isóceles')
    else:
        print('seu triângulo é Escaleno')
else:
    print('não dá pra fazer um triângulo :(')


