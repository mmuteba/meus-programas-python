from random import  randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
comput = randint(0, 2)
print('''Suas opcoes:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada?  '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POO!!')

print('=-' *15)
print('O jogador jogou {}  '.format(itens[jogador]))
print('O computador jogou  {} ' .format(itens[comput]))
print('=-' *15)

if comput == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('O JOGADOR VENCE')
    elif jogador == 2:
        print('O COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif comput == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('O JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif comput == 2:
    if jogador == 0:
        print('O JOGADOR VENCE')
    elif jogador == 1:
        print('O COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')

