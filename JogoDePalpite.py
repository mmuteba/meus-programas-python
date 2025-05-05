from random import randint
comuputador = randint(0, 10)
print('Sou computador... acabei de pensar em um número entre 1 e 10.')
print('Será que voce consegue acertar que número foi pensado? ')
acertou = False
palpites = 0
while not acertou:
    palpites += 1
    jogador = int(input('Qual é o seu palpite? '))
    if jogador == comuputador:
        acertou = True
    else:
        if jogador > comuputador:
            print('Menos.... Tente novamente')
        else:
            print('Mais... Tente novamente!')
print(f'Voce acertou o número pensado pelo seu computador foi {jogador}, com {palpites} tentativas! Parabéns..')
