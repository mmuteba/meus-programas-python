from random import randint
print('=-' *20)
print('VAMOS JOGAR')
print('=-' *20)
v = 0
while True:
    jog = int(input('Digite um valor: '))
    pc = randint(0,10)
    total = jog + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar: [P/I]')).strip().upper()
    print(f'Voce jogou {jog}, o computador jogou {pc}, dando um total de {total}', end=' ')
    print('Deu Par' if total % 2 == 0 else 'Deu Impar')
    if tipo == 'P':
        if  total % 2 == 0:
            print('Voce venceu!')
            v += 1
        else:
            print('Voce perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce venceu!')
            v += 1
        else:
            print('Voce perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Voce venceu {v} vezes.')