from datetime import date
atual = date.today().year
nascimento = int(input('diga o ano de nascimento do atleta:'))
idade = atual - nascimento
if nascimento < atual:
    if idade <= 9:
        print('seu atleta é MIRIM.')
    elif idade <= 14:
        print('seu atleta é INFANTIL.')
    elif idade <= 19:
        print('seu atleta é JUNIOR.')
    elif idade <= 25:
        print('seu atleta é SÊNIOR.')
    else:
        print('seu atleta é MASTER.')
elif nascimento > atual:
    print('você não pode competir, nem nasceu ainda!')
elif nascimento == atual:
    print('você acabou de nascer, por isso não pode competir.')
