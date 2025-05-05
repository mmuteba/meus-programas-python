

print('-' *20)
print('Loja Super Baratao')
print('-' *20)
preçoTotal = mais = menor = count =  0
barato = ' '
while True:
    nomeP = str(input('Informe o produto: '))
    preço = float(input('Qual é o preço: Kz '))
    preçoTotal += preço
    count += 1
    if preço > 1000:
        mais += 1
    if count == 1 or preço < menor:
        menor = preço
        barato = nomeP
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer adicionar mais produto? ')).strip().upper()
    if resp == 'N':
        break
print('-' *10, end=' ')
print('COMPRA CONCLUIDA', end= ' ')
print('-' *10)
print(f'O total da compra foi de {preçoTotal} Kz')
print(f'Temos {mais} produtos custando mais de 1000 KZ')
print(f'O produto mais barato foi {barato} e custou {menor} Kz')