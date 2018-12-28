n3: bool = False
# se n3 for falso ele para
while not n3:
    # primeiro número
    n1 = input('primeiro número: ')
    # segundo número
    n2 = input('segundo número: ')
    #(um ou outro) ou (um e outro)
    if (n1.isalpha() or n2.isalpha()) or (n1.isalpha() and n2.isalpha()):
        print('isso não tá certo')
        # n3 fica True e então repete
        n3 = True
    elif n1 > n2:
        print('o primeiro número é o maior.')
    elif n2 > n1:
        print('o segundo número é o maior')
    elif n1 == n2:
        print('eles são iguais')
