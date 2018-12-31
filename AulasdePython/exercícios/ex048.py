total = 0
valores = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        total = total + c
        valores += 1
print('a soma de todos os {} valores é {}'.format(valores, total))
