from math import sin, cos, tan, radians
angulo = float(input('me dê um ângulo: '))
seno = sin(radians(angulo))
coseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('o seno é {} o coseno é {} e a tangente é {}'.format(seno, coseno, tangente))
