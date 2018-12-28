from time import sleep
nome = str(input('qual o seu nome?: '))
NOME = nome.upper()
Nome = 'SILVA' in NOME
nomeVC = nome.split()
print('seu nome é: {}.'.format(nomeVC[0]))
sleep(1.5)
print('vou ver se tem "Silva" no seu nome.')
sleep(2)
if Nome:
    print('Sim! tem Silva no seu nome.')
else:
    print('não. não tem Silva no seu nome.')
