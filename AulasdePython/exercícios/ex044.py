print('========== Lojas Asiáticas ==========')
preco = int(input('diga seu preço R$: '))
print('''Formas de pagamento:
-[1] a vista no dinheiro/cheque
-[2] a vista no cartão
-[3] 2x no cartão
-[4] 3x ou mais no cartão
''')
Forma = int(input('escolha aqui: '))
if Forma == 1:
    total = preco - (preco * 10 / 100)
    print('sua compra vale R${:.2f} vai custar R${:.2f}'.format(preco, total))

elif Forma == 2:
    total = preco - (preco * 5 / 100)
    print('sua compra vale R${:.2f} vai custar R${:.2f}'.format(preco, total))

elif Forma == 3:
    total = preco
    parcela = total / 2
    print('sua compra será parcelada em 2x de {:.2f} sem juros'.format(parcela))
    print('sua compra vale R${:.2f} vai custar R${:.2f}'.format(preco, total))

elif Forma == 4:
    total = preco + (preco * 20 / 100)
    tp = int(input('quantas parcelas? '))
    parcela = total / tp
    print('sua compra será parcelada em {}x de {:.2f} com juros'.format(tp, parcela))
    print('sua compra vale R${:.2f} vai custar R${:.2f}'.format(preco, total))

else:
    print('essa opção não existe.')
