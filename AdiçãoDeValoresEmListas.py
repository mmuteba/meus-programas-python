num = []
print('=*' *20)
while True:
    n = (int(input('Digite um numero: ')))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso....')
    else:
        print('Valor duplicado! Nao vou adicionar....')
    res = str(input('Quer continuar? [S/N] ')).strip().upper()
    if res in 'SN':
        if res == 'N':
            break
num.sort()
print(f'Os valores digitados foram {num}')