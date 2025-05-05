print('-' *20)
print('Cadastramento de pessoas')
print('-' *20)
maior = totH = qmulher = 0
f'''
while True:
    idade = int(input('Informe a idade: '))
    if idade >= 18:
        maior += 1
    sexo = str(input('Informe o sexo: [M/F] ')).strip().upper()
    if sexo == 'M':
        totH += 1
    elif sexo == 'F':
        if idade < 20:
            qmulher += 1
    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()
    if pergunta == 'N':
        break
print(f'Ao todo sao {maior} pessoas maiores de idade, '
      f'foram cadastrados {totH} homens e '
      f'{qmulher} mulheres abaixo dos 20 anos!')
'''
while True:
    idade = int(input('Informe a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo: [M/F]  ')).strip().upper()
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20 :
        qmulher += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ?  [S/N] ')).strip().upper()
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos {maior}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {qmulher} mulheres com menos de 20 anos!')