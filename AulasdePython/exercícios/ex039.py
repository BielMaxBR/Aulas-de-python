# um ou outro ou um e outro e ou outro e ou outro outro ou um e outro e ou ou e oU! youtru um ou outro ou um e ou outro e ou outro outro ou outro ou um e outro e ou outro e ou outro outro ou tro tro tro tro tro tro tro tro tro tro tro tro tro tro tro tro tro ouo ou ou ou ou e ou ou ou e chega eu vou me despedir desse emprego de pete repete eram dois cachorros. pete morreu quem ficou? repete.)) pete repete eram dois cachorros. pete morreu quem ficou? repete
import datetime
ano3 = False

anos = input('quando você nasceu? ')
ano_atual: int = datetime.date.today().year
idade = ano_atual - int(anos)
print('Quem nasceu em {} tem {} anos em {}'.format(anos, idade, ano_atual))
if idade > 18:
    devia = int(anos) + 18
    atraso = devia - ano_atual
    print('está atrasado {} anos'.format(atraso))
    print('deveria ter se alistado em {}'.format(devia))
if idade < 18:
    falta = 18 - idade
    ainda = ano_atual + falta
    print('faltam {} anos para se alistar'.format(falta))
    print('você se alistará em {}'.format(ainda))
if idade == 18:
    print('tem que se alistar AGORA!')
