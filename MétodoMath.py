import math
CO = float(input('Digite o valor do cateto Oposto: '))
CA = float(input('Digite o valor do cateto adjacente: '))
Hi = math.hypot(CO,CA)
print('O valor da hipotenusa e {:.2f} ' .format(Hi))