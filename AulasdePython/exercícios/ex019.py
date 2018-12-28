al1 = str(input('qual o primeiro aluno?: '))
al2 = str(input('qual o segundo aluno?: '))
al3 = str(input('qual o terceiro aluno?: '))
al4 = str(input('qual o quarto aluno?: '))
from random import choice
alunos = [al1, al2, al3, al4]
ales = choice(alunos)
print('o aluno escolhido foi {}'.format(ales))
