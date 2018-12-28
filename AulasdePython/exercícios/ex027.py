from time import sleep
nome = str(input("Digite seu nome completo: "))
Nom = nome.split()
print('muito prazer em te conhecer')
sleep(1)
print('seu primeiro nome é {}'.format(Nom[0]))
print('seu último nome é {}'.format(Nom[-1]))
sleep(3)
print('juntando fica {} {}'.format(Nom[0], Nom[-1]))
