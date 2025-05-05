import math
ang = int(input('Digite um angulo: '))
seno = math.sin(math.radians(ang))
coseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print('O angulo de {} tem o Seno de {:.2f} \n O angulo de {} tem o Cos de {:.2f} \n O angulo de {} tem a tangente de {:.2f}'.format(ang, seno, ang, coseno, ang, tangente))