casa = float(input('Valor da casa R$:'))
salario = float(input('Salário do comprador:'))
anos = int(input('Quantos anos de financiamento?:'))
prestacao = casa / (anos * 12)
salario_30 = salario / 100 * 30
print("""pra pagar uma casa de R${:.2f} em {} anos
a prestação será de R${:.2f}""".format(casa, anos, prestacao))

if prestacao <+ salario_30:
    print('seu empréstimo é menor que 30% do salário')
    print('Seu empréstimo foi aceito!')
elif prestacao > salario_30:
    print('seu empréstimo é maior que 30% do salário')
    print('Seu empréstimo foi Negado.')
