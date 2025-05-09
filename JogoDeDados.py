from random import randint
from operator import itemgetter
from time import sleep

jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
ranking = list()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f' {k} tirou {v} no dado.')
    sleep(1)
print('*' *30)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('  === RANKING DOS JOGADORES ===')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)