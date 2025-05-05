while True:
    number = int(input('Digite um valor, para saber a sua tabuada: '))
    if number < 0:
        break
    print('-' *20)
    print('-' *20)
    for c in range(1, 11):
        print(f'{number} x {c} = {number*c}')
    print('-' * 20)
    print('-' * 20)
print('PROGRAMA FINALIZADO......')