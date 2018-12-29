peso = float(input("qual o seu peso:"))
altura = float(input("qual a sua altura:"))
imc = peso / (altura ** 2)
"""
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
"""
print('o seu imc é {:.1f}'.format(imc))
if imc < 18.5:
    print("você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print('você está no peso ideal.')
elif 25 <= imc < 30:
    print('você está sobrepeso ideal.')
elif 30 <= imc < 40:
    print("você está com obesidade.")
elif 40 <= imc:
    print("vish! você está na obesidade mórbida.")
