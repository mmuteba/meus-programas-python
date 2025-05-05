from random import randint
comput = randint(1, 5)
jogador = int(input('Que valor entre 1 e 5 voce acha que o computador pensou?  '))
print('-=-=' *10)
print('Processando....')
print('-=-=' *10)
if comput == jogador:
    print('Voce venceu...')
else:
    print('O computador pensou em {} e nao em {} ' . format(comput, jogador))