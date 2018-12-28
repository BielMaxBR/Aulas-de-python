from datetime import date
data = date.today().year
ano = int(input("""qual o ano que você quer analizar?
digite 0 para analizar o ano atual: """))

if ano == 0:
    Bano = data % 4
    Cano = data % 100
    Qano = data % 400

    if Bano == 0 and Cano != 0 or Qano == 0:
        print('o ano {} é bissexto'.format(data))
    else:
        print('o ano {} não é bissexto'.format(data))
else:
    Bano = ano % 4
    Cano = ano % 100
    Qano = ano % 400

    if Bano == 0 and Cano != 0 or Qano == 0:
        print('o ano {} é bissexto'.format(ano))
    else:
        print('o ano {} não é bissexto'.format(ano))
