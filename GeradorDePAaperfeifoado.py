print('Gerador de PA')
print('-=' *10)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao da PA: '))
termos = primeiro
count = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while count <= total:
        print(f'{termos} -> ', end='')
        count += 1
        termos += razao
    print('Pausa')
    mais = int(input('Mais quantos? '))
print(f'A PA foi finalizada com {total} termos')