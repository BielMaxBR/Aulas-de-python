print('analizador de valores. saberei qual dos valores é maior e qual é menor')
v1 = int(input('fale o primeiro valor: '))
v2 = int(input('fale o segundo número: '))
v3 = int(input('fale o terceiro número: '))
'''maiores'''
if v1 > v2 and v1 > v3:
    print('o primeiro valor é o maior e')
if v2 > v1 and v2 > v3:
    print('o segundo valor é o maior e')
if v3 > v1 and v3 > v2:
    print('o terceiro valor é o maior e')
'''menores'''
if v1 < v2 and v1 < v3:
    print('o primeiro valor é o menor')
if v2 < v1 and v2 < v3:
    print('o segundo valor é o menor')
if v3 < v1 and v3 < v2:
    print('o terceiro valor é o menor')
