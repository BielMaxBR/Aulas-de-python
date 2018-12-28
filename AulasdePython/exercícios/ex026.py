frase = str(input('escreva uma frase: ')).strip()
FRASE = frase.upper()
A_frase = FRASE.count('A')
print('a letra "A" aparece {} vezes '.format(A_frase))
Ffrase = FRASE.find('A') + 1
print('ela aparece primeiro no dígito número {} '.format(Ffrase))
Ufrase = FRASE.rfind('A') + 1
print('ela aperece pela última vez no dígito número {}'.format(Ufrase))
