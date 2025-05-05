print('=' *30)
print('{:^30}'.format('CAIXA ELETRONICO'))
print('=' *30)
valor = int(input('Quanto valor voce quer sacar? Kz'))
total = valor
ced = 50
totced = 0
while True:
    if ced >= 50:
        total -= ced
        totced += 1
    else:
        print(f'Total de {totced} de cedulas de {ced} Kz')
    if ced == 50:
        ced = 20
    elif ced == 20:
        ced = 10
    elif ced == 10:
        ced = 1
    totced = 0
    if ced == 0:
        break
print('Volte sempre.Tenha um bom dia!')